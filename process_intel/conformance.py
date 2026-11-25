"""Stage 5 (SOP part): per-ticket conformance checks C1-C7 (SOP schema §9).

Each ticket's audit path is compared with what its SOP requires for that
ticket's routing. Results before the SOP's effective date are labelled
`retrospective` (schema §9.1).
"""
from __future__ import annotations

import pandas as pd

from . import sop

PASS = {"ok", "none", "expected_exception"}


def _date(x) -> pd.Timestamp:
    return pd.Timestamp(str(x))


def check_ticket(ticket, events: pd.DataFrame, d: dict, prior: dict, triggers: dict) -> dict:
    types = events.event_type.tolist()
    approvals = events[events.event_type == "APPROVED"].stage.tolist()
    required = [s for s in prior["required_stages"].split(">") if s]
    res = {}

    n_obs, n_req = len(approvals), len(required)
    res["c1_approvals"] = "ok" if n_obs == n_req else ("fewer" if n_obs < n_req else "more")

    order = [m["stage"] for m in d["approval_matrix"]]
    idx = [order.index(s) if s in order else None for s in approvals]
    in_order = all(i is not None for i in idx) and idx == sorted(idx)
    res["c2_approval_order"] = "ok" if in_order else "out_of_order"

    has_dw = "DEPENDENCY_WAIT" in types
    if int(ticket.dependency_count) == 0 and has_dw:
        expected = any(x.get("adds_dependency_wait") for x in d.get("exceptions") or [])
        res["c3_dependency_wait"] = "expected_exception" if expected else "undeclared"
    else:
        res["c3_dependency_wait"] = "none"

    missing = [a for a in ("CREATED", "ASSIGNED", "SUBMITTED") if a not in types]
    if not types or types[-1] not in ("APPROVED", "CLOSED"):
        missing.append("final APPROVED")
    res["c4_required_actions"] = "ok" if not missing else "missing:" + ",".join(missing)

    n_rej = types.count("REJECTED")
    exceeded = n_rej > int(d["max_rework_cycles"]) and "ESCALATED" not in types
    res["c5_rework_cycles"] = "exceeded" if exceeded else "ok"

    reasons = events.rejection_reason.dropna().astype(str).str.strip().tolist()
    if not reasons:
        res["c6_rejection_reasons"] = "n/a"
        mapped = []
    else:
        mapped = [triggers.get((ticket.task_type, r.lower())) for r in reasons]
        unmapped = [r for r, m in zip(reasons, mapped) if m is None]
        res["c6_rejection_reasons"] = "ok" if not unmapped else "unmapped:" + ",".join(unmapped)

    res["c7_elapsed_band"] = ticket.sop_band
    evaluated = [v for k, v in res.items() if k != "c7_elapsed_band" and v != "n/a"]
    passed = sum(1 for v in evaluated if v in PASS)
    res["fitness"] = round(passed / len(evaluated), 4) if evaluated else None
    res["required_approval_stages"] = ">".join(required)
    res["observed_approval_stages"] = ">".join(approvals)
    res["rework_trigger_codes"] = "|".join(m["code"] for m in mapped if m)
    res["preventable_by"] = "|".join(m["preventable_by"] for m in mapped if m)
    return res


def check_all(features: pd.DataFrame, events: pd.DataFrame, sops: dict[str, dict]) -> pd.DataFrame:
    triggers = sop.rework_trigger_map(sops)
    by_ticket = dict(tuple(events.groupby("ticket_id")))
    rows = []
    for t in features.itertuples(index=False):
        base = {"ticket_id": t.ticket_id, "task_type": t.task_type, "department": t.department,
                "assigned_employee_id": t.assigned_employee_id, "completed_month": t.completed_month}
        d = sops.get(t.task_type)
        ev = by_ticket.get(t.ticket_id)
        if d is None or ev is None:
            rows.append({**base, "sop_id": None, "conformance_mode": "no_sop" if d is None else "no_events"})
            continue
        prior = sop.ticket_prior(sops, t.task_type, t.approval_count, t.dependency_count)
        mode = "retrospective" if t.created_at < _date(d["effective_date"]) else "in_force"
        rows.append({**base, "sop_id": d["sop_id"], "sop_version": d["version"], "conformance_mode": mode,
                     **check_ticket(t, ev, d, prior, triggers)})
    return pd.DataFrame(rows)


CHECK_COLUMNS = ["c1_approvals", "c2_approval_order", "c3_dependency_wait", "c4_required_actions",
                 "c5_rework_cycles", "c6_rejection_reasons", "c7_elapsed_band"]
