"""Stage 6: attach reasons to every deviation.

Statistical detectors (deviations.py) already rank causes against historical baselines.
This stage adds the SOP view:
  - links rejections to the SOP step that detects them and the control that would prevent them;
  - explains each SOP nonconformance (logging gap, routing rule, hold instead of rejection, ...);
  - decomposes SOP time-band deviations into components vs SOP expectations;
  - states which SOP clause each finding refers to.
Adds columns: sop_id, sop_reference, preventable_by, reason_source.
Candidate causes are hypotheses ranked by evidence, never verdicts.
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

from . import sop as sop_mod


def _r(x, nd=2):
    return None if x is None or pd.isna(x) else round(float(x), nd)


def _conf(share: float) -> str:
    return "high" if share >= 0.6 else ("medium" if share >= 0.4 else "low")


class _Ctx:
    def __init__(self, f, conf, sops, events):
        self.f = f.set_index("ticket_id", drop=False)
        self.conf = conf.set_index("ticket_id", drop=False)
        self.sops = sops
        self.triggers = sop_mod.rework_trigger_map(sops)
        self.logged_stages = set(events.loc[events.event_type == "APPROVED", "stage"])
        self.n_tickets = len(f)

    def tickets(self, ids: str) -> pd.DataFrame:
        ids = [t for t in str(ids or "").split("|") if t and t in self.f.index]
        return self.f.loc[ids]

    def control(self, task_type, reason):
        return self.triggers.get((task_type, str(reason).strip().lower()))


# --------------------------------------------------------------------------- SOP-derived rows

def _nonconformance(row, ctx: _Ctx) -> dict:
    ev = json.loads(row.evidence)
    ttype, check, value = ev["task_type"], ev["check"], ev["result"]
    d = ctx.sops[ttype]
    h = ctx.tickets(row.source_ticket_ids)
    matrix = {m["stage"]: m["condition"] for m in d["approval_matrix"]}

    if check == "c1_approvals" and value == "fewer":
        c = ctx.conf.loc[h.index]
        missing = sorted({s for req, obs in zip(c.required_approval_stages, c.observed_approval_stages)
                          for s in req.split(">") if s and s not in obs.split(">")})
        never = [s for s in missing if s not in ctx.logged_stages]
        causes = [{"cause": f"Platform never logs {s} approvals (0 {s} approval events in all {ctx.n_tickets} tickets)",
                   "classification": "platform_logging"} for s in never]
        causes += [{"cause": f"Required {s} approval skipped", "classification": "process"}
                   for s in missing if s not in never]
        return dict(classification="platform_logging" if never else "process", candidate_causes=causes,
                    confidence="high" if never else "medium",
                    sop_reference="; ".join(f"{d['sop_id']} approval_matrix: {s} ({matrix.get(s)})" for s in missing),
                    recommended_investigation=f"Confirm with the platform team whether {', '.join(missing)} approval "
                                              "happens outside the system or is skipped (see data-quality finding DQ057).")
    if check == "c1_approvals" and value == "more":
        conds = {s: c for s, c in matrix.items() if c != "always"}
        causes = [{"cause": f"{s} approval logged on every ticket although the SOP requires it only when '{c}'",
                   "classification": "process"} for s, c in conds.items()]
        causes.append({"cause": "Routing condition cannot be verified: its drivers are not in the export",
                       "classification": "data_gap"})
        return dict(classification="process", candidate_causes=causes, confidence="medium",
                    sop_reference="; ".join(f"{d['sop_id']} approval_matrix: {s} ({c})" for s, c in conds.items()),
                    recommended_investigation="Check whether these tickets are routed for approval by default. Either "
                                              "configure the SOP condition on the platform or update the SOP.")
    if check == "c3_dependency_wait":
        dw = h.dependency_waiting_time_h.median()
        pre, exp = h.pre_decision_wait_h.median(), h.sop_exp_first_decision_h.median()
        causes = [
            {"cause": "Ticket put on hold where the SOP requires rejection for missing information",
             "classification": "process"},
            {"cause": f"Reviewer queue time logged as DependencyWait (median hold {dw:.2f}h; first-decision wait "
                      f"{pre:.2f}h vs SOP {exp:.2f}h)", "classification": "process"},
        ]
        # Two competing hypotheses the log cannot separate -> low confidence.
        return dict(classification="process", candidate_causes=causes, confidence="low",
                    sop_reference=f"{d['sop_id']} dependency_count: 0; procedure: 'This SOP has no external dependency'",
                    recommended_investigation="Ask Incharges and executors why these tickets are put on hold. If it is "
                                              "queue time, stop logging it as DependencyWait; if information is "
                                              "missing, reject with 'Required document missing'.")
    if check == "c6_rejection_reasons":
        return dict(classification="process", candidate_causes=[{"cause": f"Rejection reason not in {d['sop_id']} "
                    "rework_triggers", "classification": "process"}], confidence="high",
                    sop_reference=f"{d['sop_id']} rework_triggers",
                    recommended_investigation="Add the reason to the SOP or correct the platform reason code.")
    return dict(classification="process", candidate_causes=[{"cause": f"Audit path differs from {d['sop_id']} ({value})",
                "classification": "process"}], confidence="medium", sop_reference=f"{d['sop_id']} steps",
                recommended_investigation="Review the affected tickets' audit trails against the SOP procedure.")


def _components(h: pd.DataFrame) -> dict[str, tuple[float, float]]:
    lead = h.decision_wait_lead_h[h.decision_wait_lead_h > 0]
    return {
        "intake queue": (h.queue_time_h.median(), h.sop_exp_queue_h.median()),
        "first-decision wait (incl. DependencyWait)": (h.pre_decision_wait_h.median(), h.sop_exp_first_decision_h.median()),
        "Lead decision wait": (lead.median() if len(lead) else 0.0, h.sop_exp_lead_decision_h.median()),
        "executor hold, WIP-adjusted (upper bound on effort)": (h.executor_hold_wip_adj_h.median(), h.sop_effort_exec_h.median()),
    }


def _elapsed_band(row, ctx: _Ctx) -> dict:
    ev = json.loads(row.evidence)
    d = ctx.sops[ev["task_type"]]
    h = ctx.tickets(row.source_ticket_ids)
    above = row.deviation_type.endswith("ABOVE_STANDARD")
    comps = _components(h)
    gaps = {k: a - e for k, (a, e) in comps.items()}
    relevant = {k: g for k, g in gaps.items() if (g > 0 if above else g < 0)}
    total = sum(abs(g) for g in relevant.values()) or 1e-9
    ranked = sorted(relevant.items(), key=lambda kv: abs(kv[1]), reverse=True)
    causes = [{"cause": f"{k}: actual {comps[k][0]:.2f}h vs SOP {comps[k][1]:.2f}h ({g:+.2f}h)",
               "component": k, "share_of_gap": _r(abs(g) / total)} for k, g in ranked]
    undeclared = int(h.dependency_wait_undeclared.sum())
    if above and undeclared:
        causes.append({"cause": f"{undeclared} of {len(h)} tickets carry a DependencyWait the SOP does not allow",
                       "component": "context", "share_of_gap": None})
    evidence = {**ev, "component_medians_actual_vs_sop_h": {k: [_r(a), _r(e)] for k, (a, e) in comps.items()},
                "tickets_in_tail": len(h), "note": "executor hold is compared in aggregate only (schema §7.3)"}
    share = causes[0]["share_of_gap"] if causes and causes[0]["share_of_gap"] is not None else 0
    if above:
        rec = ("Investigate the dominant component. Waits point to the approval queue or holds; executor hold "
               "points to work content.")
        cls = "process"
    else:
        rec = ("SOP time standards look high for this task type. Review them with the SOP owner; recalibrate only "
               "as a new SOP version fitted on an earlier period (schema §3.1).")
        cls = "sop_standard"
    return dict(classification=cls, candidate_causes=causes, confidence=_conf(share), evidence=json.dumps(evidence),
                sop_reference=f"{d['sop_id']} v{d['version']} §7.1 E_elapsed band", recommended_investigation=rec)


def _effort_standard(row, ctx: _Ctx) -> dict:
    ev = json.loads(row.evidence)
    d = next(x for x in ctx.sops.values() if x["sop_id"] == row.sop_id)
    if ev["flag"] == "standard_exceeds_hold":
        causes = [{"cause": f"SOP executor effort standard too high ({d['standard_time_source']})", "classification": "sop_standard"},
                  {"cause": "Work done outside the ticket window (before Created or after Submitted)", "classification": "process"}]
    else:
        causes = [{"cause": "Holding time includes much non-SOP time (waiting on others, multitasking, idle)", "classification": "process"},
                  {"cause": "SOP executor effort standard too low", "classification": "sop_standard"}]
    return dict(classification="sop_standard", candidate_causes=causes, confidence="low",
                sop_reference=f"{d['sop_id']} v{d['version']} work-step effort_min (schema §8)",
                recommended_investigation="Review the standard with the SOP owner or run a short time study. Do not edit "
                                          "standard times to match the data (schema §3.1).")


def _rework(row, ctx: _Ctx) -> dict:
    ev = json.loads(row.evidence)
    d = next(x for x in ctx.sops.values() if x["sop_id"] == row.sop_id)
    total = sum(ev["reasons"].values()) or 1
    causes = []
    for reason, n in ev["reasons"].items():
        t = ctx.control(d["task_type"], reason) or {}
        causes.append({"cause": f"{reason} ({n})", "detected_at": t.get("detected_at"),
                       "preventable_by": t.get("preventable_by"), "share": _r(n / total)})
    top = causes[0]
    return dict(classification="rework", candidate_causes=causes,
                confidence="low" if d["quality_targets_source"] == "unconfirmed" else "medium",
                dominant_cause=f"{top['cause']}: preventable by {top['preventable_by']}",
                preventable_by="|".join(c["preventable_by"] for c in causes[:2] if c["preventable_by"]),
                sop_reference=f"{d['sop_id']} rework_triggers; expected_first_pass_yield {d['expected_first_pass_yield']}",
                recommended_investigation=f"Strengthen the upstream control '{top['preventable_by']}' and re-measure the "
                                          "first-pass yield.")


# --------------------------------------------------------------------------- statistical rows

def _ticket(row, ctx: _Ctx) -> dict:
    if row.entity_id not in ctx.f.index:
        return {}
    t, c = ctx.f.loc[row.entity_id], ctx.conf.loc[row.entity_id] if row.entity_id in ctx.conf.index else None
    ev = json.loads(row.evidence)
    ev["sop_comparison"] = {
        "sop_id": t.sop_id, "sop_band": t.sop_band, "sop_expected_elapsed_h": _r(t.sop_expected_elapsed_h),
        "sop_p10_p90_h": [_r(t.sop_p10_h), _r(t.sop_p90_h)],
        "first_decision_wait_actual_vs_sop_h": [_r(t.pre_decision_wait_h), _r(t.sop_exp_first_decision_h)],
        "conformance_fitness": None if c is None else c.fitness,
    }
    out = {"evidence": json.dumps(ev), "sop_reference": f"{t.sop_id} band {t.sop_band}"}
    if c is not None and c.preventable_by and row.classification == "rework":
        out["preventable_by"] = c.preventable_by
        out["dominant_cause"] = f"{row.dominant_cause}; preventable by {c.preventable_by}"
        out["sop_reference"] += f"; rework_trigger {c.rework_trigger_codes}"
    if c is not None and c.c3_dependency_wait == "undeclared" and "DependencyWait" in row.dominant_cause:
        out["sop_reference"] += f"; C3 undeclared dependency wait ({t.sop_id} declares none)"
    return out


def _rejection(row, ctx: _Ctx) -> dict:
    h = ctx.tickets(row.source_ticket_ids)
    controls = {}
    for t in h.itertuples():
        for reason in str(t.rejection_reasons).split("|"):
            tr = ctx.control(t.task_type, reason)
            if tr:
                controls[tr["preventable_by"]] = controls.get(tr["preventable_by"], 0) + 1
    top = sorted(controls.items(), key=lambda kv: kv[1], reverse=True)
    return {"preventable_by": "|".join(k for k, _ in top[:2]),
            "sop_reference": "rework_triggers of " + ", ".join(sorted(set(h.sop_id.dropna()))),
            "recommended_investigation": row.recommended_investigation
            + (f" Most relevant SOP controls: {', '.join(f'{k} ({v})' for k, v in top[:2])}." if top else "")}


def _bottleneck(row, ctx: _Ctx) -> dict:
    ev = json.loads(row.evidence)
    dept, dep = row.department, ev["dependency_count"]
    h = ctx.f[(ctx.f.department == dept) & (ctx.f.dependency_count == dep) & ctx.f.total_duration_h.notna()]
    exp = h.sop_exp_first_decision_h.median()
    obs = h.pre_decision_wait_h.median()
    ev["sop_first_decision_expected_h"] = _r(exp)
    ev["observed_vs_sop"] = _r(obs / exp) if exp else None
    note = (f"Relative to the SOP standard ({exp:.2f}h) the observed wait ({obs:.2f}h) is "
            + ("higher" if obs > exp else "lower") + "; the bottleneck is "
            + ("against both the SOP and other departments." if obs > exp else "relative to other departments only."))
    causes = json.loads(row.candidate_causes) + [{"cause": note, "classification": "context"}]
    return {"evidence": json.dumps(ev), "candidate_causes": json.dumps(causes),
            "sop_reference": ", ".join(sorted(set(h.sop_id.dropna()))) + " first approval queue_wait_h + review effort + dependencies"}


def _mismatch(row, ctx: _Ctx) -> dict:
    ev = json.loads(row.evidence)
    causes = [{"cause": f"Structural mismatch: {m}", "classification": "sop_mismatch"}
              for m in str(ev.get("structural_mismatches", "")).split("; ") if m and m != "none"]
    if ev.get("closest_sop_by_time") != ev.get("sop_id"):
        causes.append({"cause": f"Time scale matches {ev['closest_sop_by_time']} better", "classification": "sop_mismatch"})
    for note in str(ev.get("notes", "")).split(" | "):
        if note:
            causes.append({"cause": note, "classification": "context"})
    if not causes:
        causes = [{"cause": "Correspondence below threshold", "classification": "sop_mismatch"}]
    excluded = ev.get("verdict") == "does_not_correspond"
    return dict(classification="sop_mismatch", candidate_causes=causes, confidence="high" if excluded else "medium",
                sop_reference=f"{ev.get('sop_id')} task_type mapping (schema §9.2)",
                recommended_investigation=("Confirm which SOP governs this task type (or whether the task_type label "
                                           "mixes processes). The SOP was excluded from all comparisons."
                                           if excluded else "Review the mismatching tickets; SOP comparisons for this "
                                           "task type are reported with caution."))


HANDLERS_SOP = {"SOP_LOG_MISMATCH": _mismatch, "SOP_NONCONFORMANCE": _nonconformance, "SOP_ELAPSED_ABOVE_STANDARD": _elapsed_band,
                "SOP_ELAPSED_BELOW_STANDARD": _elapsed_band, "SOP_EFFORT_STANDARD": _effort_standard,
                "REWORK_ABOVE_SOP_EXPECTATION": _rework}
HANDLERS_STAT = {"TICKET_DURATION": _ticket, "ELEVATED_REJECTION_RATE": _rejection,
                 "APPROVAL_STAGE_BOTTLENECK": _bottleneck}
STAT_NOTES = {
    "PERSISTENT_UNEXPLAINED_PROCESSING_INCREASE": "n/a: SOP effort is never compared per employee (schema §8)",
    "PERSISTENT_PROCESSING_INCREASE_WITH_CONTEXT": "n/a: SOP effort is never compared per employee (schema §8)",
    "SLA_DETERIORATION": "SOP sla_hours (High 6 / Medium 12 / Low 24)",
    "SLA_DROP": "SOP sla_hours (High 6 / Medium 12 / Low 24)",
    "APPROVAL_WAIT_INCREASE": "SOP approval_matrix and approval-step queue_wait_h",
    "REWORK_INCREASE": "SOP rework_triggers (reason -> preventing step)",
}


def attach_reasons(devs: pd.DataFrame, f: pd.DataFrame, conf: pd.DataFrame, sops: dict, events: pd.DataFrame) -> pd.DataFrame:
    ctx = _Ctx(f, conf, sops, events)
    out = devs.copy()
    for col in ["sop_id", "sop_reference", "preventable_by", "reason_source"]:
        if col not in out:
            out[col] = ""
    out = out.astype({c: object for c in ["sop_id", "sop_reference", "preventable_by", "dominant_cause",
                                          "candidate_causes", "confidence", "classification", "evidence",
                                          "recommended_investigation"]})
    for i, row in out.iterrows():
        if row.deviation_type in HANDLERS_SOP:
            res = HANDLERS_SOP[row.deviation_type](row, ctx)
            causes = res.pop("candidate_causes")
            res.setdefault("dominant_cause", causes[0]["cause"] if causes else "undetermined")
            res["candidate_causes"] = json.dumps(causes)
            res["reason_source"] = "sop"
        elif row.deviation_type in HANDLERS_STAT:
            res = HANDLERS_STAT[row.deviation_type](row, ctx)
            res["reason_source"] = "baseline+sop"
        else:
            res = {"sop_reference": STAT_NOTES.get(row.deviation_type, ""), "reason_source": "baseline"}
        for k, v in res.items():
            out.at[i, k] = v
    out["sop_id"] = out.sop_id.replace("", np.nan)
    return out
