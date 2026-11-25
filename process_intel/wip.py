"""WIP-adjusted executor hold time (SOP schema §8).

Raw hold time counts a clock hour k times when an executor holds k tickets at once.
Each elementary interval is split equally across the tickets covering it, so the
per-executor total equals the union of their hold intervals.
"""
from __future__ import annotations

import pandas as pd

HOLD_CATEGORIES = ("processing", "rework")


def wip_adjusted_hold(segments: pd.DataFrame, tickets: pd.DataFrame) -> pd.Series:
    """Return executor_hold_wip_adj_h indexed by ticket_id (0 for tickets without hold time)."""
    out = pd.Series(0.0, index=pd.Index(tickets.ticket_id, name="ticket_id"))
    if segments.empty:
        return out
    holder = tickets.set_index("ticket_id").assigned_employee_id
    seg = segments[segments.category.isin(HOLD_CATEGORIES) & (segments.duration_h > 0)].copy()
    # Holder is the ticket's assignee, never the segment actor (a Rejected segment's actor is the reviewer).
    seg["holder"] = seg.ticket_id.map(holder)
    seg = seg.dropna(subset=["holder"])
    for _, g in seg.groupby("holder"):
        starts, ends, tids = g.start.tolist(), g.end.tolist(), g.ticket_id.tolist()
        points = sorted(set(starts) | set(ends))
        for t0, t1 in zip(points, points[1:]):
            covering = [tid for s, e, tid in zip(starts, ends, tids) if s <= t0 and e >= t1]
            if covering:
                share = (t1 - t0).total_seconds() / 3600 / len(covering)
                for tid in covering:
                    out[tid] += share
    return out
