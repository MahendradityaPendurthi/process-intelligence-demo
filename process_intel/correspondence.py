"""Stage 3b: SOP-log correspondence gate (SOP schema §9.2).

Before any SOP comparison, confirm that each task type's logs are the process its SOP
describes, not a different process that happens to share a label.

Each ticket's audit path is replayed on a process model built from the SOP:
    intake (Created, Assigned)  ->  Updated*  ->  Submitted
    -> review: [DependencyWait] then Approved by the matrix stages in order, or Rejected by a
       stage that the SOP's rework triggers name as detector
    -> rework: Updated* -> Resubmitted -> review
    -> closes on the final approval
Every actor must belong to the SOP's department and hold the role of the step it performs.

Outcomes per ticket:
    fits                         the path matches the SOP model exactly
    fits_with_known_deviations   same process, with conformance deviations only
                                 (approval count C1, undeclared hold C3, unmapped reason C6)
    does_not_fit                 the path cannot be produced by this SOP (wrong department or roles,
                                 approval stages the SOP does not have, wrong order, foreign activities)

Per task type: correspondence = share not `does_not_fit`; path score = fits 1.0, known 0.5, else 0.
Each task type is also cross-fitted against every SOP (path score and time scale). An SOP that
does not correspond is excluded from stages 4-6, so logs are never judged against another process.
"""
from __future__ import annotations

import math

import pandas as pd

from . import config, sop

EXECUTOR_EVENTS = {"CREATED", "ASSIGNED", "UPDATED", "SUBMITTED", "RESUBMITTED", "DEPENDENCY_WAIT"}
KNOWN = {"approvals_fewer_than_sop", "approvals_more_than_sop", "hold_not_allowed_by_sop", "reason_not_in_sop"}


def _model(d: dict, approval_count: int, dependency_count: int, sops_for_prior: dict) -> dict:
    prior = sop.ticket_prior(sops_for_prior, d["task_type"], approval_count, dependency_count)
    steps = {s["step_id"]: s for s in d["steps"]}
    vocab = {a.upper().replace("DEPENDENCYWAIT", "DEPENDENCY_WAIT")
             for s in d["steps"] for a in s.get("audit_actions") or []}
    return {
        "department": d["department"],
        "matrix": [m["stage"] for m in d["approval_matrix"]],
        "required": [s for s in prior["required_stages"].split(">") if s],
        "reject_roles": {steps[t["detected_at"]]["role"] for t in d["rework_triggers"] if t["detected_at"] in steps},
        "hold_allowed": int(d["dependency_count"]) > 0 or any(x.get("adds_dependency_wait") for x in d["exceptions"] or []),
        "reasons": {str(t["reason"]).strip().lower() for t in d["rework_triggers"]},
        "vocab": vocab | ({"DEPENDENCY_WAIT"} if d["dependencies"] else set()),
    }


def replay(events: pd.DataFrame, ticket_department: str, m: dict) -> tuple[str, list[str]]:
    """Replay one ticket's normalized events on an SOP model. Returns (status, issues)."""
    issues: list[str] = []
    fatal = issues.append
    if ticket_department != m["department"]:
        fatal(f"ticket_department_{ticket_department}_not_{m['department']}")
    ev = list(events.itertuples(index=False))
    types = [e.event_type for e in ev]
    if types[:2] != ["CREATED", "ASSIGNED"]:
        fatal("intake_not_created_then_assigned")
    phase, approvals = "work", []
    for e in ev:
        t = e.event_type
        if e.department != m["department"]:
            fatal(f"actor_department_{e.department}")
        if t in EXECUTOR_EVENTS and e.role != "Executor":
            fatal(f"{t.lower()}_by_{e.role}")
        if t not in m["vocab"] and t != "DEPENDENCY_WAIT":
            fatal(f"activity_not_in_sop:{t}")
            continue
        if t in ("CREATED", "ASSIGNED"):
            continue
        if phase == "closed":
            fatal(f"{t.lower()}_after_final_approval")
        elif phase in ("work", "rework"):
            if t == "UPDATED":
                continue
            if (t == "SUBMITTED" and phase == "work") or (t == "RESUBMITTED" and phase == "rework"):
                phase = "review"
            else:
                fatal(f"{t.lower()}_during_{phase}")
        elif phase == "review":
            if t == "DEPENDENCY_WAIT":
                if approvals:
                    fatal("hold_between_approvals")
                elif not m["hold_allowed"]:
                    issues.append("hold_not_allowed_by_sop")
            elif t == "REJECTED":
                if e.stage not in m["reject_roles"]:
                    fatal(f"rejected_by_{e.stage}_not_a_detector")
                reason = str(e.rejection_reason).strip().lower() if isinstance(e.rejection_reason, str) else ""
                if reason and reason not in m["reasons"]:
                    issues.append("reason_not_in_sop")
                phase, approvals = "rework", []
            elif t == "APPROVED":
                known_prev = [a for a in approvals if a in m["matrix"]]
                if e.stage not in m["matrix"]:
                    fatal(f"approval_by_{e.stage}_not_in_sop")
                elif known_prev and m["matrix"].index(e.stage) <= m["matrix"].index(known_prev[-1]):
                    fatal("approval_stages_out_of_order")
                if e.role != e.stage:
                    fatal(f"approval_stage_{e.stage}_by_role_{e.role}")
                approvals.append(e.stage)
            else:
                fatal(f"{t.lower()}_during_review")
    if not types or types[-1] != "APPROVED":
        fatal("not_closed_by_approval")
    if len(approvals) < len(m["required"]):
        issues.append("approvals_fewer_than_sop")
    elif len(approvals) > len(m["required"]):
        issues.append("approvals_more_than_sop")
    issues = list(dict.fromkeys(issues))
    if any(i not in KNOWN for i in issues):
        return "does_not_fit", issues
    return ("fits_with_known_deviations" if issues else "fits"), issues


SCORE = {"fits": 1.0, "fits_with_known_deviations": 0.5, "does_not_fit": 0.0}


def evaluate(features: pd.DataFrame, events: pd.DataFrame, sops: dict[str, dict]):
    """Return (per-ticket results, per-task-type verdicts, cross-fit matrix)."""
    by_ticket = dict(tuple(events.groupby("ticket_id")))
    models: dict[tuple, dict] = {}
    own_rows, cross_rows = [], []
    for t in features.itertuples(index=False):
        ev = by_ticket.get(t.ticket_id)
        if ev is None:
            continue
        for stype, d in sops.items():
            key = (stype, int(t.approval_count), int(t.dependency_count))
            if key not in models:
                models[key] = _model(d, *key[1:], sops)
            status, issues = replay(ev, t.department, models[key])
            cross_rows.append({"task_type": t.task_type, "sop_task_type": stype, "status": status})
            if stype == t.task_type:
                own_rows.append({"ticket_id": t.ticket_id, "task_type": t.task_type,
                                 "correspondence_status": status, "correspondence_issues": "|".join(issues)})
    per_ticket = pd.DataFrame(own_rows)
    cross = pd.DataFrame(cross_rows)
    cross["score"] = cross.status.map(SCORE)

    done = features[features.total_duration_h.notna()]
    observed = done.groupby("task_type").total_duration_h.median()
    # Like with like: completion is logged at the last *recorded* approval, so the time of approval stages the
    # platform never logs (e.g. HOD) is removed from each SOP's expected time before comparing time scales.
    logged = set(events.loc[events.event_type.isin(["APPROVED", "REJECTED"]), "stage"])
    expected, unlogged_by_sop = {}, {}
    for stype, d in sops.items():
        p = sop.ticket_prior(sops, stype, d["approval_count_base"], d["dependency_count"])
        stages = [s for s in p["required_stages"].split(">") if s]
        comp = {s: p["exp_lead_decision_h"] if s == "Lead" else p["exp_hod_decision_h"] if s == "HOD"
                else p["exp_first_decision_h"] if i == 0 else 0.0 for i, s in enumerate(stages)}
        unlogged = [s for s in stages if s not in logged]
        expected[stype] = p["e_elapsed_h"] - sum(comp[s] for s in unlogged)
        unlogged_by_sop[stype] = unlogged
    matrix = cross.groupby(["task_type", "sop_task_type"]).agg(
        path_score=("score", "mean"), share_not_fit=("status", lambda s: (s == "does_not_fit").mean())).reset_index()
    matrix["time_ratio"] = [observed.get(a, math.nan) / expected[b] for a, b in zip(matrix.task_type, matrix.sop_task_type)]
    matrix["time_distance"] = matrix.time_ratio.map(lambda r: abs(math.log(r)) if r and r > 0 else math.inf)
    matrix["sop_id"] = matrix.sop_task_type.map({k: v["sop_id"] for k, v in sops.items()})

    verdicts = []
    lo, hi = config.CORRESPONDENCE_TIME_RANGE
    for ttype, g in per_ticket.groupby("task_type"):
        d = sops[ttype]
        n = len(g)
        counts = g.correspondence_status.value_counts()
        corr = 1 - counts.get("does_not_fit", 0) / n
        mx = matrix[matrix.task_type == ttype].set_index("sop_task_type")
        own = mx.loc[ttype]
        others = mx.drop(index=ttype)
        best_path = others.path_score.idxmax() if len(others) else None
        candidates = mx[mx.path_score >= own.path_score - 1e-9]           # SOPs at least as good by path
        closest_time = candidates.time_distance.idxmin()
        issues = g.correspondence_issues.str.split("|").explode()
        issues = issues[issues != ""].value_counts()
        fatal = issues[[i not in KNOWN for i in issues.index]]
        notes = []
        if best_path and others.loc[best_path, "path_score"] > own.path_score + 1e-9:
            notes.append(f"audit path resembles {sops[best_path]['sop_id']} ({best_path}) more closely "
                         f"(path score {others.loc[best_path, 'path_score']:.2f} vs {own.path_score:.2f}), because of "
                         f"known deviations: {', '.join(issues[[i in KNOWN for i in issues.index]].index)}")
        if closest_time != ttype:
            notes.append(f"time scale is closer to {sops[closest_time]['sop_id']} ({closest_time})")
        if unlogged_by_sop[ttype]:
            notes.append(f"time comparison excludes SOP stages never logged on the platform: "
                         f"{', '.join(unlogged_by_sop[ttype])}")
        ties = [s for s in candidates.index if s != ttype and abs(mx.loc[s, "path_score"] - own.path_score) < 1e-9]
        if ties:
            notes.append(f"audit path cannot distinguish it from {', '.join(sops[s]['sop_id'] for s in ties)}; "
                         "time scale and the task_type label decide")
        in_range = lo <= own.time_ratio <= hi
        identified = closest_time == ttype
        # Another SOP explains the logs at least as well by path AND better by time -> wrong SOP.
        rival = (not identified) and (len(others) > 0) and others.path_score.max() >= own.path_score - 1e-9
        if corr < config.CORRESPONDENCE_PARTIAL or not in_range or rival:
            verdict = "does_not_correspond"
        elif corr >= config.CORRESPONDENCE_MIN and identified:
            verdict = "corresponds"
        else:
            verdict = "partial"
        verdicts.append({
            "task_type": ttype, "sop_id": d["sop_id"], "sop_department": d["department"], "tickets": n,
            "fits": int(counts.get("fits", 0)), "fits_with_known_deviations": int(counts.get("fits_with_known_deviations", 0)),
            "does_not_fit": int(counts.get("does_not_fit", 0)), "correspondence": round(corr, 4),
            "path_score_own": round(own.path_score, 4),
            "best_other_sop_by_path": sops[best_path]["sop_id"] if best_path else None,
            "path_score_best_other": round(others.loc[best_path, "path_score"], 4) if best_path else None,
            "observed_median_h": round(observed.get(ttype, math.nan), 4), "sop_expected_elapsed_h": round(expected[ttype], 4),
            "time_ratio_own": round(own.time_ratio, 4), "closest_sop_by_time": sops[closest_time]["sop_id"],
            "known_deviation_counts": "; ".join(f"{k}:{v}" for k, v in issues.items() if k in KNOWN),
            "structural_mismatches": "; ".join(f"{k}:{v}" for k, v in fatal.items()) or "none",
            "verdict": verdict, "notes": " | ".join(notes),
        })
    return per_ticket, pd.DataFrame(verdicts), matrix.round(4)
