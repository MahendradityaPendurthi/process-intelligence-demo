"""Process map: how tickets actually move between steps, built from the normalised audit log.

Each ticket becomes a sequence of plain-language steps ("Submitted", "On hold", "Approved by Incharge", ...).
Repeated steps in a row (several edits) are merged into one. Arrows carry the number of tickets that take
them and the time from entering one step to entering the next. The map is drawn as Graphviz DOT text,
which Streamlit renders without extra packages.
"""
from __future__ import annotations

import pandas as pd

START, END = "Start", "Done"
EVENT_COLS = ["ticket_id", "event_type", "stage", "timestamp", "raw_change_type"]

# sequential blue ramp (light -> dark) from the validated palette, for arrow wait time
RAMP = ["#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
HIGHLIGHT = "#eb6834"          # slowest step
NODE_FILL, NODE_LINE, INK, SURFACE = "#f0efec", "#52514e", "#0b0b0b", "#fcfcfb"


def step_label(event_type: str, stage, change_type) -> str:
    stage = stage if isinstance(stage, str) and stage else ""
    if event_type == "APPROVED":
        return f"Approved by {stage}" if stage else "Approved"
    if event_type == "REJECTED":
        return f"Sent back by {stage}" if stage else "Sent back"
    if event_type == "UPDATED":
        return "Fixing after rejection" if change_type == "correction" else "Working on it"
    return {"CREATED": "Created", "ASSIGNED": "Assigned", "SUBMITTED": "Submitted", "DEPENDENCY_WAIT": "On hold",
            "RESUBMITTED": "Resubmitted", "REASSIGNED": "Reassigned", "ESCALATED": "Escalated",
            "REOPENED": "Reopened", "CLOSED": "Closed", "CANCELLED": "Cancelled"}.get(
        event_type, str(event_type).replace("_", " ").capitalize())


def ticket_steps(events: pd.DataFrame) -> pd.DataFrame:
    """One row per (ticket, step) with the time the ticket entered the step; repeats in a row merged."""
    e = events[EVENT_COLS].copy()
    e["timestamp"] = pd.to_datetime(e.timestamp)
    e = e.sort_values(["ticket_id", "timestamp"], kind="stable")
    e["step"] = [step_label(t, s, c) for t, s, c in zip(e.event_type, e.stage, e.raw_change_type)]
    same = (e.step == e.groupby("ticket_id").step.shift()) & (e.ticket_id == e.ticket_id.shift())
    return e[~same][["ticket_id", "step", "timestamp"]].reset_index(drop=True)


def transitions(steps: pd.DataFrame) -> pd.DataFrame:
    """Arrows between consecutive steps, plus Start -> first step and last step -> Done."""
    s = steps.copy()
    s["next_step"] = s.groupby("ticket_id").step.shift(-1)
    s["next_time"] = s.groupby("ticket_id").timestamp.shift(-1)
    s["hours"] = (s.next_time - s.timestamp).dt.total_seconds() / 3600
    firsts = s.groupby("ticket_id").head(1).assign(next_step=lambda d: d.step, step=START, hours=0.0)
    s["next_step"] = s.next_step.fillna(END)
    s.loc[s.next_step == END, "hours"] = 0.0
    return pd.concat([firsts[["ticket_id", "step", "next_step", "hours"]],
                      s[["ticket_id", "step", "next_step", "hours"]]], ignore_index=True)


def edges(tr: pd.DataFrame) -> pd.DataFrame:
    n_tickets = tr.ticket_id.nunique()
    g = tr.groupby(["step", "next_step"])
    out = g.agg(moves=("ticket_id", "size"), tickets=("ticket_id", "nunique"), median_h=("hours", "median"),
                p90_h=("hours", lambda h: h.quantile(0.9)), total_h=("hours", "sum")).reset_index()
    out["share"] = out.tickets / max(n_tickets, 1)
    return out.sort_values("moves", ascending=False).reset_index(drop=True)


def paths(steps: pd.DataFrame, durations: pd.Series | None = None, top: int = 10) -> pd.DataFrame:
    """Most common complete paths (step sequences), with share of tickets and typical total time."""
    p = steps.groupby("ticket_id").step.agg(" → ".join).rename("path").reset_index()
    if durations is not None:
        p = p.merge(durations.rename("duration_h"), left_on="ticket_id", right_index=True, how="left")
    else:
        p["duration_h"] = float("nan")
    out = p.groupby("path").agg(tickets=("ticket_id", "size"), median_duration_h=("duration_h", "median"))
    out["share"] = out.tickets / len(p)
    return out.sort_values("tickets", ascending=False).head(top).reset_index()


def slowest(e: pd.DataFrame, min_share: float = 0.05) -> pd.Series | None:
    """The arrow with the most total waiting time among arrows used by at least min_share of tickets."""
    cand = e[(e.share >= min_share) & ~e.step.eq(START) & ~e.next_step.eq(END)]
    return None if cand.empty else cand.loc[cand.total_h.idxmax()]


def _hours(h: float) -> str:
    return f"{round(h * 60)} min" if h < 1 else f"{h:.1f} h"


def to_dot(e: pd.DataFrame, min_share: float = 0.02) -> str:
    """Graphviz DOT for the arrows used by at least min_share of tickets."""
    shown = e[e.share >= min_share]
    if shown.empty:
        return "digraph { }"
    slow = slowest(e)
    timed = shown[~shown.step.eq(START) & ~shown.next_step.eq(END)].median_h
    hi = max(float(timed.max()) if len(timed) else 1.0, 1e-9)
    max_t = shown.tickets.max()
    nodes = sorted(set(shown.step) | set(shown.next_step))
    lines = ["digraph process {", f'  graph [rankdir=TB, bgcolor="{SURFACE}", pad=0.3, nodesep=0.6, ranksep=0.45, '
             f'fontname="Helvetica"];',
             f'  node [shape=box, style="rounded,filled", fillcolor="{NODE_FILL}", color="{NODE_LINE}", '
             f'fontcolor="{INK}", fontname="Helvetica", fontsize=14, penwidth=1.2, margin="0.15,0.08"];',
             f'  edge [fontname="Helvetica", fontsize=12, fontcolor="{INK}", arrowsize=0.8];']
    for n in nodes:
        if n in (START, END):
            lines.append(f'  "{n}" [shape=circle, fixedsize=true, width=0.7, fillcolor="{NODE_LINE}", '
                         f'fontcolor="{SURFACE}", fontsize=12];')
        else:
            lines.append(f'  "{n}" [label="{n.replace(" by ", "\\nby ").replace(" after ", "\\nafter ")}"];')
    for r in shown.itertuples():
        width = 0.8 + 5 * r.tickets / max_t
        is_slow = slow is not None and r.step == slow.step and r.next_step == slow.next_step
        if r.step == START or r.next_step == END:
            color, label = NODE_LINE, f"{r.tickets:,}"
        else:
            color = HIGHLIGHT if is_slow else RAMP[min(len(RAMP) - 1, int(r.median_h / hi * (len(RAMP) - 1) + 0.5))]
            label = f"{r.tickets:,} · {_hours(r.median_h)}" + ("\\nslowest step" if is_slow else "")
        lines.append(f'  "{r.step}" -> "{r.next_step}" [penwidth={width:.2f}, color="{color}", label="{label}"'
                     + (', style=dashed' if r.share < 0.1 else "") + "];")
    lines.append("}")
    return "\n".join(lines)


def summary(e: pd.DataFrame, top_paths: pd.DataFrame, steps: pd.DataFrame, typical_h: float | None) -> list[str]:
    n_tickets = steps.ticket_id.nunique()
    pts = []
    if len(top_paths):
        p = top_paths.iloc[0]
        pts.append(f"**{p.share:.0%}** of the {n_tickets:,} tickets follow the most common path: {p.path}.")
        k = min(5, len(top_paths))
        pts.append(f"The {k} most common paths cover **{top_paths.share.head(k).sum():.0%}** of tickets.")
    slow = slowest(e)
    if slow is not None:
        total = e[~e.step.eq(START) & ~e.next_step.eq(END)].total_h.sum()
        pts.append(f"**Slowest step:** from “{slow.step}” to “{slow.next_step}”, typically "
                   f"**{_hours(slow.median_h)}** ({slow.share:.0%} of tickets). It accounts for "
                   f"**{slow.total_h / total:.0%}** of all the time tickets spend in the process.")
    def share_with(cond) -> float:
        return steps[cond].ticket_id.nunique() / max(n_tickets, 1)

    back = share_with(steps.step.str.startswith("Sent back"))
    if back:
        pts.append(f"**{back:.0%}** of tickets were sent back at least once and went round the "
                   "“Fixing after rejection → Resubmitted” loop.")
    hold = share_with(steps.step.eq("On hold"))
    if hold:
        pts.append(f"**{hold:.0%}** of tickets were put on hold after submission.")
    if typical_h is not None:
        pts.append(f"A typical ticket takes **{_hours(typical_h)}** from creation to the final approval.")
    return pts
