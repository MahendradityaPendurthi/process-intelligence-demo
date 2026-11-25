"""Stages 1-2: read SOPs, validate them, and derive their parameters.

Implements corporate_sops/SOP_SCHEMA.md v1.2:
    load_sops()        parse YAML front matter (legacy free-text SOPs are listed, not parsed)
    validate_sops()    schema + consistency with task_types.csv  -> sop_validation_report.csv
    complexity_score() derived complexity (CS-v1)
    ticket_prior()     expected effort / elapsed time and P10-P90 band for a ticket's routing
    sop_parameters()   one row per valid SOP                       -> sop_parameters.csv
Standard times are read, never modified (schema §3.1).
"""
from __future__ import annotations

import datetime as dt
import hashlib
import math

import pandas as pd
import yaml

from . import config

REQUIRED_FIELDS = [
    "schema_version", "sop_id", "title", "version", "status", "effective_date", "review_cycle_months",
    "owner_role", "department", "task_type", "complexity_declared", "standard_time_source",
    "standard_time_frozen", "quality_targets_source", "sla_hours", "sop_steps", "approval_count_base",
    "approval_count_max", "approval_matrix", "dependency_count", "dependencies", "complexity_drivers", "steps",
    "rework_triggers", "expected_first_pass_yield", "rework_effort_min", "max_rework_cycles", "exceptions",
]
ENUMS = {
    "status": {"Draft", "Approved", "Retired"},
    "owner_role": {"Executor", "Incharge", "Lead", "HOD"},
    "complexity_declared": set(config.COMPLEXITY_LEVELS),
    "standard_time_source": {"illustrative_expert_estimate", "time_study", "historical_calibration"},
    "quality_targets_source": {"illustrative_expert_estimate", "policy_target", "historical_calibration", "unconfirmed"},
}
STEP_ROLES = {"Executor", "Incharge", "Lead", "HOD", "System", "External"}
STEP_TYPES = {"intake", "work", "approval", "decision", "rework"}
ACTIVE = {"Approved", "Draft"}


# --------------------------------------------------------------------------- stage 1: read

def load_sops(sop_dir=config.SOP_DIR) -> list[dict]:
    """Return one record per SOP file: id, file, sha256, format, parse_error, data, body."""
    records = []
    for path in sorted(sop_dir.glob(config.SOP_FILE_GLOB)):
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        rec = {"file": path.name, "sha256": hashlib.sha256(raw).hexdigest(), "sop_id": path.stem.split("_")[0],
               "format": "legacy", "parse_error": None, "data": None, "body": text}
        if text.startswith("---"):
            rec["format"] = "schema"
            parts = text.split("---", 2)
            if len(parts) < 3:
                rec["parse_error"] = "front matter not closed by a second '---'"
            else:
                try:
                    data = yaml.safe_load(parts[1])
                    if not isinstance(data, dict):
                        raise ValueError("front matter is not a mapping")
                    rec["data"], rec["body"] = data, parts[2]
                    rec["sop_id"] = str(data.get("sop_id", rec["sop_id"]))
                except (yaml.YAMLError, ValueError) as exc:
                    rec["parse_error"] = str(exc).splitlines()[0]
        records.append(rec)
    return records


def _three_point_ok(tp) -> bool:
    if not isinstance(tp, dict) or not {"min", "likely", "max"} <= set(tp):
        return False
    try:
        lo, mid, hi = float(tp["min"]), float(tp["likely"]), float(tp["max"])
    except (TypeError, ValueError):
        return False
    return 0 <= lo <= mid <= hi


def _approval_steps(d: dict) -> dict[str, dict]:
    """First approval step per role."""
    out = {}
    for s in d.get("steps") or []:
        if s.get("type") == "approval":
            out.setdefault(s.get("role"), s)
    return out


def _exec_work_steps(d: dict) -> list[dict]:
    return [s for s in d.get("steps") or [] if s.get("type") == "work" and s.get("role") == "Executor"]


class _Checks:
    def __init__(self):
        self.rows = []

    def add(self, sop_id, check, ok, severity="error", details=""):
        self.rows.append({"sop_id": sop_id, "check": check, "severity": severity,
                          "status": "pass" if ok or severity == "info" else "fail", "details": details})


def validate_sops(records: list[dict], task_types: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, dict]]:
    """Return (validation report, {task_type: sop_data} for valid active SOPs)."""
    c = _Checks()
    tt = task_types.set_index("task_type")
    files = {r["sop_id"] for r in records}
    active_by_type: dict[str, list[str]] = {}

    for r in records:
        sid = r["sop_id"]
        if r["format"] == "legacy":
            c.add(sid, "legacy_free_text_sop", True, "info", "no YAML front matter; listed, not parsed")
            continue
        c.add(sid, "yaml_parses", r["parse_error"] is None, details=r["parse_error"] or "")
        d = r["data"]
        if d is None:
            continue
        missing = [f for f in REQUIRED_FIELDS if f not in d]
        c.add(sid, "required_fields_present", not missing, details=f"missing: {missing}" if missing else "")
        if missing:
            continue
        c.add(sid, "schema_version", str(d["schema_version"]) == config.SOP_SCHEMA_VERSION,
              details=f"found {d['schema_version']}, expected {config.SOP_SCHEMA_VERSION}")
        for field, allowed in ENUMS.items():
            c.add(sid, f"enum:{field}", d[field] in allowed, details=f"{d[field]!r}")
        if d["status"] == "Retired":
            c.add(sid, "status_retired", True, "info", "ignored by the pipeline")
            continue

        steps = d["steps"] or []
        ids = [s.get("step_id") for s in steps]
        c.add(sid, "step_ids_unique", len(ids) == len(set(ids)), details=str(ids))
        bad_steps = [s.get("step_id") for s in steps
                     if s.get("role") not in STEP_ROLES or s.get("type") not in STEP_TYPES
                     or not isinstance(s.get("name"), str)
                     or not _three_point_ok(s.get("effort_min"))
                     or ("queue_wait_h" in s and not _three_point_ok(s["queue_wait_h"]))
                     or any(k in s and not (isinstance(s[k], list) and all(isinstance(x, str) for x in s[k]))
                            for k in ("inputs", "outputs", "audit_actions"))]
        c.add(sid, "steps_well_formed", not bad_steps,
              details="role/type enum, string name, string lists, valid three-point times" +
                      (f"; bad: {bad_steps}" if bad_steps else ""))
        work = _exec_work_steps(d)
        bad_skill = [s["step_id"] for s in work if s.get("skill_level") not in (1, 2, 3)]
        c.add(sid, "work_steps_have_skill_level", not bad_skill, details=str(bad_skill))

        ttype = d["task_type"]
        known = ttype in tt.index
        c.add(sid, "task_type_in_task_types", known, details=ttype)
        if d["status"] in ACTIVE:
            active_by_type.setdefault(ttype, []).append(sid)
        if known:
            row = tt.loc[ttype]
            c.add(sid, "department_matches", d["department"] == row.department, details=f"{d['department']} vs {row.department}")
            c.add(sid, "complexity_declared_matches", d["complexity_declared"] == row.complexity,
                  details=f"{d['complexity_declared']} vs {row.complexity}")
            c.add(sid, "sop_steps_matches_task_types", int(d["sop_steps"]) == int(row.sop_steps),
                  details=f"{d['sop_steps']} vs {row.sop_steps}")
            c.add(sid, "dependency_count_matches_task_types", int(d["dependency_count"]) == int(row.dependency_count),
                  details=f"{d['dependency_count']} vs {row.dependency_count}")
            ac = int(row.approval_count)
            c.add(sid, "task_approval_count_in_range", d["approval_count_base"] <= ac <= d["approval_count_max"],
                  details=f"{ac} in [{d['approval_count_base']}, {d['approval_count_max']}]")
        c.add(sid, "sop_steps_equals_counted_work_steps", int(d["sop_steps"]) == len(work),
              details=f"declared {d['sop_steps']}, counted {len(work)}")

        matrix = d["approval_matrix"] or []
        n_always = sum(1 for m in matrix if m.get("condition") == "always")
        c.add(sid, "approval_base_equals_always_rows", d["approval_count_base"] == n_always,
              details=f"{d['approval_count_base']} vs {n_always}")
        c.add(sid, "approval_max_equals_matrix_length", d["approval_count_max"] == len(matrix),
              details=f"{d['approval_count_max']} vs {len(matrix)}")
        appr = _approval_steps(d)
        no_step = [m.get("stage") for m in matrix if m.get("stage") not in appr]
        c.add(sid, "matrix_stages_have_approval_steps", not no_step, details=str(no_step))

        deps = d["dependencies"] or []
        c.add(sid, "dependencies_listed", len(deps) >= int(d["dependency_count"]),
              details=f"{len(deps)} listed, {d['dependency_count']} declared")
        bad_deps = [x.get("id") for x in deps if x.get("blocking_step") not in ids or not _three_point_ok(x.get("typical_wait_h"))]
        c.add(sid, "dependencies_well_formed", not bad_deps, details=str(bad_deps))
        no_group = [x.get("id") for x in deps if not x.get("parallel_group")]
        c.add(sid, "dependencies_have_parallel_group", not no_group, "warning",
              details=f"treated as sequential: {no_group}" if no_group else "")

        c.add(sid, "sla_hours_match_due_rule", d["sla_hours"] == config.SLA_HOURS, details=str(d["sla_hours"]))
        reasons = [t.get("reason") for t in d["rework_triggers"] or []]
        bad_reasons = [x for x in reasons if x not in config.PLATFORM_REJECTION_REASONS]
        c.add(sid, "rework_reasons_in_platform_vocabulary", not bad_reasons, details=str(bad_reasons))
        appr_ids = {s["step_id"] for s in appr.values()}
        bad_det = [t.get("code") for t in d["rework_triggers"] or [] if t.get("detected_at") not in appr_ids]
        c.add(sid, "rework_detected_at_approval_step", not bad_det, details=str(bad_det))
        c.add(sid, "first_pass_yield_in_range", 0 <= float(d["expected_first_pass_yield"]) <= 1,
              details=str(d["expected_first_pass_yield"]))
        c.add(sid, "rework_effort_three_point", _three_point_ok(d["rework_effort_min"]))
        bad_sup = [s for s in d.get("supersedes") or [] if s not in files]
        c.add(sid, "superseded_sops_exist", not bad_sup, "warning", details=str(bad_sup))
        try:
            frozen_ok = _date(d["standard_time_frozen"]) <= _date(d["effective_date"])
        except (TypeError, ValueError):
            frozen_ok = False
        c.add(sid, "times_frozen_before_effective", frozen_ok, "warning",
              details=f"{d['standard_time_frozen']} <= {d['effective_date']}")
        c.add(sid, "quality_targets_provenance_confirmed", d["quality_targets_source"] != "unconfirmed", "warning",
              details="FPY comparison is weak evidence until provenance is confirmed")
        c.add(sid, "standard_time_source", True, "info", details=d["standard_time_source"])
        c.add(sid, "markdown_body_present", len(r["body"].strip()) > 200, "warning")
        cs = complexity_score(d)
        c.add(sid, "derived_complexity_matches_declared", cs["complexity_derived"] == d["complexity_declared"],
              "warning", details=f"CS {cs['cs']:.2f} -> {cs['complexity_derived']} vs declared {d['complexity_declared']}")

    for ttype, sids in active_by_type.items():
        c.add(",".join(sids), "one_active_sop_per_task_type", len(sids) == 1, details=ttype)
    missing_types = sorted(set(tt.index) - set(active_by_type))
    c.add("ALL", "every_task_type_has_sop", not missing_types, details=str(missing_types))

    report = pd.DataFrame(c.rows)
    report.insert(0, "check_id", [f"SV{i + 1:03d}" for i in range(len(report))])
    failed = set(report[(report.severity == "error") & (report.status == "fail")].sop_id)
    valid = {r["data"]["task_type"]: {**r["data"], "_sha256": r["sha256"], "_file": r["file"]}
             for r in records
             if r["data"] is not None and r["sop_id"] not in failed and r["data"].get("status") in ACTIVE
             and r["data"].get("task_type") in tt.index}
    return report, valid


def _date(x) -> dt.date:
    return x if isinstance(x, dt.date) else dt.date.fromisoformat(str(x))


# --------------------------------------------------------------------------- stage 2: parameters

def pert(tp: dict) -> tuple[float, float]:
    lo, mid, hi = float(tp["min"]), float(tp["likely"]), float(tp["max"])
    return (lo + 4 * mid + hi) / 6, ((hi - lo) / 6) ** 2


def clark_max(m1: float, v1: float, m2: float, v2: float) -> tuple[float, float]:
    """Mean and variance of max(X1, X2) for independent normals (Clark 1961)."""
    theta = math.sqrt(v1 + v2)
    if theta == 0:
        return (m1, v1) if m1 >= m2 else (m2, v2)
    a = (m1 - m2) / theta
    cdf = 0.5 * (1 + math.erf(a / math.sqrt(2)))
    pdf = math.exp(-a * a / 2) / math.sqrt(2 * math.pi)
    mean = m1 * cdf + m2 * (1 - cdf) + theta * pdf
    second = (m1 ** 2 + v1) * cdf + (m2 ** 2 + v2) * (1 - cdf) + (m1 + m2) * theta * pdf
    return mean, max(second - mean ** 2, 0.0)


def complexity_score(d: dict) -> dict:
    w = config.CS_WEIGHTS
    work = _exec_work_steps(d)
    skill = sum(s.get("skill_level", 1) for s in work) / len(work) if work else 1.0
    parts = {
        "steps": w["steps"] * int(d["sop_steps"]),
        "appr_base": w["appr_base"] * int(d["approval_count_base"]),
        "appr_cond": w["appr_cond"] * (int(d["approval_count_max"]) - int(d["approval_count_base"])),
        "dep": w["dep"] * int(d["dependency_count"]),
        "decision": w["decision"] * sum(1 for s in d["steps"] if s.get("type") == "decision"),
        "driver": w["driver"] * sum(1 for x in d.get("complexity_drivers") or [] if x.get("effect") == "effort"),
        "exception": w["exception"] * len(d.get("exceptions") or []),
        "skill": w["skill"] * (skill - 1),
    }
    cs = sum(parts.values())
    lo, hi = config.CS_BANDS
    derived = "Simple" if cs < lo else ("Medium" if cs <= hi else "Complex")
    return {"cs": round(cs, 4), "complexity_derived": derived, **{f"cs_{k}": round(v, 4) for k, v in parts.items()}}


def _prior(d: dict, approval_count: int, dependency_count: int) -> dict:
    """Schema §7.1-7.2 for one routing (approval_count, dependency_count)."""
    flags = set()
    matrix = d["approval_matrix"] or []
    base = int(d["approval_count_base"])
    n_cond = max(0, min(int(approval_count) - base, len(matrix) - base))
    if any(m.get("condition") != "always" for m in matrix):
        flags.add("approval_route_from_ticket")   # no driver values in the export
    required, cond_seen = [], 0
    for m in matrix:
        if m.get("condition") == "always":
            required.append(m["stage"])
        elif cond_seen < n_cond:
            required.append(m["stage"])
            cond_seen += 1
    appr = _approval_steps(d)

    eff_mean = eff_var = 0.0          # minutes, minutes^2 (total effort)
    exec_mean = exec_var = 0.0        # executor effort only
    wait_mean = wait_var = 0.0        # hours, hours^2
    components = {"queue": 0.0}
    stage_comp = {}

    def add_effort(step, executor=False, scale=1.0):
        nonlocal eff_mean, eff_var, exec_mean, exec_var
        m, v = pert(step["effort_min"])
        if "effort_scaling" in step:
            flags.add("drivers_missing")      # driver value unknown -> scaling term 0
        eff_mean += scale * m
        eff_var += scale ** 2 * v
        if executor:
            exec_mean += scale * m
            exec_var += scale ** 2 * v
        return scale * m

    def add_queue(step):
        nonlocal wait_mean, wait_var
        if "queue_wait_h" not in step:
            return 0.0
        m, v = pert(step["queue_wait_h"])
        wait_mean += m
        wait_var += v
        return m

    for s in d["steps"]:
        if s.get("type") == "intake":
            add_effort(s)
            components["queue"] += add_queue(s)
        elif s.get("type") == "work" and s.get("mandatory", True):
            add_effort(s, executor=s.get("role") == "Executor")
            add_queue(s)
    fpy = float(d["expected_first_pass_yield"])
    add_effort({"effort_min": d["rework_effort_min"]}, executor=True, scale=1 - fpy)

    for stage in required:
        step = appr[stage]
        e = add_effort(step) / 60
        q = add_queue(step)
        stage_comp[stage] = e + q

    # Dependencies: first `dependency_count` in list order; same parallel_group -> max (Clark).
    deps = (d["dependencies"] or [])[: int(dependency_count)]
    groups: dict[str, list[tuple[float, float, str]]] = {}
    for x in deps:
        m, v = pert(x["typical_wait_h"])
        groups.setdefault(x.get("parallel_group") or x["id"], []).append((m, v, x["blocking_step"]))
    dep_by_block: dict[str, float] = {}
    for items in groups.values():
        m, v = items[0][0], items[0][1]
        for m2, v2, _ in items[1:]:
            m, v = clark_max(m, v, m2, v2)
        wait_mean += m
        wait_var += v
        dep_by_block[items[0][2]] = dep_by_block.get(items[0][2], 0.0) + m

    step_stage = {s["step_id"]: s.get("role") for s in appr.values()}
    for block, m in dep_by_block.items():
        st = step_stage.get(block)
        if st in stage_comp:
            stage_comp[st] += m

    e_elapsed = eff_mean / 60 + wait_mean
    sd = math.sqrt(eff_var / 3600 + wait_var)
    first = required[0] if required else None
    return {
        "required_approvals": len(required),
        "required_stages": ">".join(required),
        "e_effort_exec_h": exec_mean / 60,
        "e_effort_h": eff_mean / 60,
        "e_wait_h": wait_mean,
        "e_elapsed_h": e_elapsed,
        "sd_h": sd,
        "p10_h": max(0.0, e_elapsed - config.Z_P10_P90 * sd),
        "p90_h": e_elapsed + config.Z_P10_P90 * sd,
        "exp_queue_h": components["queue"],
        "exp_first_decision_h": stage_comp.get(first, 0.0) if first else 0.0,
        "exp_lead_decision_h": stage_comp.get("Lead", 0.0),
        "exp_hod_decision_h": stage_comp.get("HOD", 0.0),
        "estimate_flags": "|".join(sorted(flags)),
    }


_PRIOR_CACHE: dict[tuple, dict] = {}


def ticket_prior(sops: dict[str, dict], task_type: str, approval_count: int, dependency_count: int) -> dict | None:
    """Prior for one ticket routing; cached by SOP content hash so edits invalidate it."""
    if task_type not in sops:
        return None
    key = (sops[task_type]["_sha256"], int(approval_count), int(dependency_count))
    if key not in _PRIOR_CACHE:
        _PRIOR_CACHE[key] = _prior(sops[task_type], int(approval_count), int(dependency_count))
    return _PRIOR_CACHE[key]


def sop_parameters(sops: dict[str, dict], task_types: pd.DataFrame) -> pd.DataFrame:
    """One row per valid SOP, priors computed at the task type's declared routing."""
    rows = []
    tt = task_types.set_index("task_type")
    for ttype, d in sorted(sops.items(), key=lambda kv: kv[1]["sop_id"]):
        row_tt = tt.loc[ttype]
        prior = ticket_prior(sops, ttype, int(row_tt.approval_count), int(row_tt.dependency_count))
        rows.append({
            "sop_id": d["sop_id"], "sop_version": d["version"], "task_type": ttype, "department": d["department"],
            "effective_date": str(d["effective_date"]), "standard_time_source": d["standard_time_source"],
            "quality_targets_source": d["quality_targets_source"], "cs_version": config.CS_VERSION,
            **complexity_score(d), "complexity_declared": d["complexity_declared"],
            "sop_steps": d["sop_steps"], "approval_count_base": d["approval_count_base"],
            "approval_count_max": d["approval_count_max"], "dependency_count": d["dependency_count"],
            "decision_points": sum(1 for s in d["steps"] if s.get("type") == "decision"),
            "expected_first_pass_yield": d["expected_first_pass_yield"],
            "expected_rejection_rate": round(1 - float(d["expected_first_pass_yield"]), 4),
            "max_rework_cycles": d["max_rework_cycles"],
            **{k: (round(v, 4) if isinstance(v, float) else v) for k, v in prior.items()},
            "sha256": d["_sha256"], "file": d["_file"],
        })
    out = pd.DataFrame(rows)
    out["complexity_match"] = out.complexity_derived == out.complexity_declared
    return out


def rework_trigger_map(sops: dict[str, dict]) -> dict[tuple[str, str], dict]:
    """(task_type, lower-cased reason) -> trigger with SOP id."""
    out = {}
    for ttype, d in sops.items():
        for t in d["rework_triggers"] or []:
            out[(ttype, str(t["reason"]).strip().lower())] = {**t, "sop_id": d["sop_id"]}
    return out
