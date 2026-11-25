"""Stage 3: reconstruct ticket lifecycles from normalized events.

Each interval between two consecutive events becomes a *segment* whose category
is decided by the state the ticket entered at the first event:

    CREATED                         -> queue            (awaiting pickup)
    ASSIGNED / REASSIGNED / REOPENED-> processing       (executor holds it)
    UPDATED                         -> processing, or rework if inside a rejection cycle
    REJECTED                        -> rework           (returned for correction)
    SUBMITTED / RESUBMITTED /
    ESCALATED / non-final APPROVED  -> approval_wait    (waiting for a decision)
    DEPENDENCY_WAIT                 -> dependency_wait  (blocked on dependent information)

For waiting segments, `waiting_on` is the stage of the next decision event
(APPROVED / REJECTED), so time is attributed to the approver stage that ended it.

The processing/waiting split is ESTIMATED: audit logs show who holds a ticket,
not whether they are actively working on it.
"""
from __future__ import annotations

import pandas as pd

ROLE_STAGES = ["Incharge", "Lead", "HOD"]
CATEGORIES = ["queue", "processing", "rework", "approval_wait", "dependency_wait"]
DECISION_EVENTS = {"APPROVED", "REJECTED"}
TERMINAL_EVENTS = {"CLOSED", "CANCELLED"}


def _state_after(event_type: str, in_rework: bool, is_last: bool) -> str | None:
    if event_type == "CREATED":
        return "queue"
    if event_type in ("ASSIGNED", "REASSIGNED", "REOPENED"):
        return "processing"
    if event_type == "UPDATED":
        return "rework" if in_rework else "processing"
    if event_type == "REJECTED":
        return "rework"
    if event_type in ("SUBMITTED", "RESUBMITTED", "ESCALATED"):
        return "approval_wait"
    if event_type == "APPROVED":
        return None if is_last else "approval_wait"
    if event_type == "DEPENDENCY_WAIT":
        return "dependency_wait"
    if event_type in TERMINAL_EVENTS:
        return None
    return "unclassified"  # UNKNOWN event types: time is kept but not attributed


def reconstruct_ticket(events: pd.DataFrame) -> tuple[dict, list[dict]]:
    """Reconstruct one ticket. `events` must belong to a single ticket."""
    evs = events.sort_values(["timestamp", "event_id"], kind="mergesort").reset_index(drop=True)
    ticket_id = evs.ticket_id.iloc[0]
    n = len(evs)
    types = evs.event_type.tolist()
    stages = evs.stage.tolist()

    # Index of the next decision event at or after position i (for waiting_on)
    next_decision_stage = [None] * n
    upcoming = None
    for i in range(n - 1, -1, -1):
        next_decision_stage[i] = upcoming
        if types[i] in DECISION_EVENTS:
            upcoming = stages[i]

    segments = []
    in_rework = False
    counts = dict(rejections=0, resubmissions=0, rework_cycles=0, updates=0, corrections=0, approvals=0,
                  reassignments=0, escalations=0, reopens=0, dependency_waits=0, submissions=0)
    open_rejection = False
    closure_event_id, closure_type = None, "open"

    for i, row in evs.iterrows():
        et = row.event_type
        if et == "REJECTED":
            counts["rejections"] += 1
            in_rework = open_rejection = True
        elif et in ("RESUBMITTED", "SUBMITTED"):
            counts["submissions"] += 1
            if et == "RESUBMITTED" or open_rejection:
                counts["resubmissions"] += 1
                if open_rejection:
                    counts["rework_cycles"] += 1
            in_rework = open_rejection = False
        elif et == "UPDATED":
            counts["updates"] += 1
            if in_rework:
                counts["corrections"] += 1
        elif et == "APPROVED":
            counts["approvals"] += 1
        elif et == "REASSIGNED":
            counts["reassignments"] += 1
        elif et == "ESCALATED":
            counts["escalations"] += 1
        elif et == "REOPENED":
            counts["reopens"] += 1
            closure_event_id, closure_type = None, "open"
        elif et == "DEPENDENCY_WAIT":
            counts["dependency_waits"] += 1

        is_last = i == n - 1
        if et in TERMINAL_EVENTS:
            closure_event_id, closure_type = row.event_id, et.lower()
        elif et == "APPROVED" and is_last:
            closure_event_id, closure_type = row.event_id, "final_approval"

        if not is_last:
            nxt = evs.iloc[i + 1]
            category = _state_after(et, in_rework, False) or "post_closure"
            waiting_on = next_decision_stage[i] if category in ("approval_wait", "dependency_wait") else row.stage
            segments.append({
                "ticket_id": ticket_id,
                "seq": i + 1,
                "from_event_id": row.event_id,
                "to_event_id": nxt.event_id,
                "from_event_type": et,
                "to_event_type": nxt.event_type,
                "start": row.timestamp,
                "end": nxt.timestamp,
                "duration_h": (nxt.timestamp - row.timestamp).total_seconds() / 3600,
                "category": category,
                "waiting_on": waiting_on or "Unknown",
                "actor_employee_id": row.employee_id,
            })

    # Stage transitions and handoffs
    transitions = [f"{a}>{b}" for a, b in zip(stages, stages[1:]) if a != b]
    actors = evs.employee_id.tolist()
    handoffs = sum(1 for a, b in zip(actors, actors[1:]) if a != b)
    visited = list(dict.fromkeys(stages))

    seg = pd.DataFrame(segments)
    totals = {c: 0.0 for c in CATEGORIES}
    decision_wait = {s: 0.0 for s in ROLE_STAGES}
    approval_wait_stage = {s: 0.0 for s in ROLE_STAGES}
    unclassified = 0.0
    if not seg.empty:
        by_cat = seg.groupby("category").duration_h.sum()
        for c in CATEGORIES:
            totals[c] = float(by_cat.get(c, 0.0))
        unclassified = float(by_cat.drop(labels=CATEGORIES, errors="ignore").sum())
        waits = seg[seg.category.isin(["approval_wait", "dependency_wait"])]
        for s in ROLE_STAGES:
            decision_wait[s] = float(waits.loc[waits.waiting_on == s, "duration_h"].sum())
            approval_wait_stage[s] = float(waits.loc[(waits.waiting_on == s) & (waits.category == "approval_wait"), "duration_h"].sum())

    first, last = evs.timestamp.iloc[0], evs.timestamp.iloc[-1]
    anomalies = []
    if n == 1:
        anomalies.append("single_event")
    if types[0] != "CREATED":
        anomalies.append("missing_created_event")
    if "ASSIGNED" not in types and "REASSIGNED" not in types:
        anomalies.append("missing_assigned_event")
    if closure_type == "open":
        anomalies.append("not_closed")
    if unclassified > 0:
        anomalies.append("unclassified_time")

    lifecycle = {
        "ticket_id": ticket_id,
        "event_count": n,
        "event_sequence": ">".join(types),
        "stages_visited": ">".join(visited),
        "stage_transitions": "|".join(transitions),
        "stage_transition_count": len(transitions),
        "handoff_count": handoffs,
        "first_event_at": first,
        "last_event_at": last,
        "lifecycle_span_h": (last - first).total_seconds() / 3600,
        "is_closed": closure_type != "open",
        "closure_type": closure_type,
        "closure_event_id": closure_event_id,
        "rejection_count": counts["rejections"],
        "resubmission_count": counts["resubmissions"],
        "rework_cycles": counts["rework_cycles"],
        "submission_count": counts["submissions"],
        "update_count": counts["updates"],
        "correction_count": counts["corrections"],
        "approval_events": counts["approvals"],
        "reassignment_count": counts["reassignments"],
        "escalation_count": counts["escalations"],
        "reopen_count": counts["reopens"],
        "dependency_wait_events": counts["dependency_waits"],
        **{f"{c}_h": v for c, v in totals.items()},
        "unclassified_h": unclassified,
        **{f"decision_wait_{s.lower()}_h": v for s, v in decision_wait.items()},
        **{f"approval_wait_{s.lower()}_h": v for s, v in approval_wait_stage.items()},
        "rejection_reasons": "|".join(evs.rejection_reason.dropna().astype(str)) if "rejection_reason" in evs else "",
        "anomalies": "|".join(anomalies),
        "source_event_ids": "|".join(evs.event_id),
    }
    return lifecycle, segments


def reconstruct_all(events: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    lifecycles, segments = [], []
    for _, grp in events.groupby("ticket_id", sort=True):
        lc, segs = reconstruct_ticket(grp)
        lifecycles.append(lc)
        segments.extend(segs)
    return pd.DataFrame(lifecycles), pd.DataFrame(segments)


def transition_summary(segments: pd.DataFrame, lifecycles: pd.DataFrame) -> pd.DataFrame:
    """Directly-follows graph (event_type -> event_type) with frequency and timing."""
    if segments.empty:
        return pd.DataFrame()
    g = segments.groupby(["from_event_type", "to_event_type"]).duration_h
    out = g.agg(frequency="count", median_h="median", p90_h=lambda s: s.quantile(0.9), total_h="sum").reset_index()
    out["share_of_tickets"] = (segments.groupby(["from_event_type", "to_event_type"]).ticket_id.nunique().values
                               / max(len(lifecycles), 1))
    return out.sort_values("frequency", ascending=False).round(4)
