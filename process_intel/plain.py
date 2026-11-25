"""Plain-language wording for findings and planted scenarios (used by the dashboard).

The pipeline's own text is precise but technical ("fail C3 (undeclared)", "WIP-adjusted hold").
These helpers turn a finding row into a short title, a few readable points, the likely cause and what
to do, using the numbers already in the row and its evidence. Nothing is recomputed; when a row does
not have the expected shape the original explanation is shown, cleaned up.
"""
from __future__ import annotations

import json
import re

import pandas as pd

TITLES = {
    "SOP_NONCONFORMANCE": "Not following the SOP",
    "SOP_ELAPSED_BELOW_STANDARD": "Finishes much faster than the SOP says",
    "SOP_ELAPSED_ABOVE_STANDARD": "Takes longer than the SOP says",
    "SOP_EFFORT_STANDARD": "SOP work-time estimate looks too high",
    "REWORK_ABOVE_SOP_EXPECTATION": "More rejections than the SOP target",
    "REWORK_INCREASE": "Rejections suddenly went up",
    "APPROVAL_STAGE_BOTTLENECK": "Slow approval step",
    "APPROVAL_WAIT_INCREASE": "Approval waits went up",
    "SLA_DETERIORATION": "On-time rate falling month after month",
    "SLA_DROP": "On-time rate dropped",
    "ELEVATED_REJECTION_RATE": "More of this person's tickets sent back than colleagues'",
    "PERSISTENT_UNEXPLAINED_PROCESSING_INCREASE": "Work taking longer, no clear reason yet",
    "PERSISTENT_PROCESSING_INCREASE_WITH_CONTEXT": "Work taking longer, with a likely reason",
    "TICKET_DURATION": "Ticket took unusually long",
    "REASON_CODE_MISMATCH": "Wrong rejection reason recorded",
    "LLM_COMMENT_CHECK": "Comment check",
}

CLASSIFICATION = {
    "process": "Process issue", "sop_standard": "SOP standard needs review", "rework": "Rework / quality",
    "executor_processing": "Work took longer", "context_explained": "Individual, explained by context",
    "platform_logging": "Platform not logging a step", "individual_signal": "Individual, worth a conversation",
    "mixed": "Mixed causes", "data_gap": "Missing data",
}

CHECKS = {  # SOP conformance checks: (check letter, result) -> what it means
    ("C1", "more"): "an approval was logged that the SOP does not require here",
    ("C1", "fewer"): "a required approval is missing from the log",
    ("C2", "wrong_order"): "approvals happened in the wrong order",
    ("C3", "undeclared"): "the ticket was put on hold although the SOP lists no outside dependency",
    ("C4", "missing"): "a required step was not done",
    ("C5", "exceeded"): "more rework rounds than the SOP allows",
    ("C6", "unexpected"): "rejected for a reason the SOP does not list",
}

SHORT_CHECKS = {("C1", "more"): "extra approval", ("C1", "fewer"): "missing approval",
                ("C2", "wrong_order"): "approvals out of order", ("C3", "undeclared"): "on hold with no SOP reason",
                ("C4", "missing"): "required step missing", ("C5", "exceeded"): "too many rework rounds",
                ("C6", "unexpected"): "unlisted rejection reason"}

COMPONENTS = {
    "first-decision wait (incl. DependencyWait)": "waiting for the first approval (including holds)",
    "executor hold, WIP-adjusted (upper bound on effort)": "the executor's working time",
    "intake queue": "waiting to be picked up",
    "Lead decision wait": "waiting for the Lead's approval",
    "HOD decision wait": "waiting for the HOD's approval",
}

CONTEXT = {
    "team_wide_trend": "the whole team slowed down at the same time",
    "workload_increase": "they were given many more tickets",
    "complexity_increase": "they were given harder tickets",
    "complexity_shift": "they were given harder tickets",
    "rejection_increase": "more of their tickets were sent back",
    "reassignment": "tickets were reassigned to them part-way",
}

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


# ------------------------------------------------------------------ small formatters
def month(p: str) -> str:
    """'2026-02' -> 'Feb 2026'."""
    try:
        y, m = str(p)[:7].split("-")
        return f"{MONTHS[int(m) - 1]} {y}"
    except (ValueError, IndexError):
        return str(p)


def months(a: str, b: str | None = None) -> str:
    """'2026-02', '2026-03' -> 'Feb–Mar 2026'; across years -> 'Oct 2025 – Sep 2026'."""
    if b is None and ".." in str(a):
        a, b = str(a).split("..", 1)
    if not b or str(a)[:7] == str(b)[:7]:
        return month(a)
    if str(a)[:4] == str(b)[:4]:
        return f"{month(a).split()[0]}–{month(b)}"
    return f"{month(a)} – {month(b)}"


def hours(h) -> str:
    try:
        h = float(h)
    except (TypeError, ValueError):
        return "—"
    if h < 1:
        return f"{round(h * 60)} min"
    return f"{h:.1f} h"


def pct(x) -> str:
    try:
        return f"{float(x):.0%}"
    except (TypeError, ValueError):
        return "—"


def times(x) -> str:
    try:
        return f"{float(x):.1f}×"
    except (TypeError, ValueError):
        return "—"


def possessive(name: str) -> str:
    return f"{name}'" if name.endswith("s") else f"{name}'s"


def _clean(text) -> str:
    if not isinstance(text, str):
        return ""
    t = re.sub(r"\s*\(schema [^)]*\)", "", text).replace("�", "§")
    t = re.sub(r"(\d+\.\d+)h\b", lambda m: hours(m.group(1)), t)
    t = re.sub(r"\b(\d{4}-\d{2})\.\.(\d{4}-\d{2})\b", lambda m: months(m.group(1), m.group(2)), t)
    t = t.replace("logging it as DependencyWait", "logging it as a dependency hold").replace("DependencyWait", "hold")
    t = t.replace("reject with 'Required document missing'", "send it back with the reason “Required document missing”")
    return t.strip()


def _condition(text: str) -> str:
    """"'kpi_breach == true or safety_event == true'" -> "KPI breach or safety event"."""
    def name(m):
        w = m.group(1).replace("_", " ")
        return re.sub(r"\bkpi\b", "KPI", w)
    t = re.sub(r"([a-z_]+)\s*==\s*true", name, text)
    t = re.sub(r"([a-z_]+)\s*==\s*false", lambda m: "no " + m.group(1).replace("_", " "), t)
    t = re.sub(r"([a-z_]+)\s*([<>]=?)\s*([\d.]+)", lambda m: f"{m.group(1).replace('_', ' ')} {m.group(2)} {m.group(3)}", t)
    return t.replace("'", "")


def _evidence(row) -> dict:
    try:
        return json.loads(row.evidence) if isinstance(row.evidence, str) else {}
    except ValueError:
        return {}


def entity(entity_id, deviation_type: str = "") -> str:
    """'Expense Approval:Incharge:2026-02..2026-03' -> 'Expense Approval · Incharge · Feb–Mar 2026'."""
    if not isinstance(entity_id, str):
        return ""
    parts = entity_id.split(":")
    out = []
    for p in parts:
        if re.fullmatch(r"\d{4}-\d{2}\.\.\d{4}-\d{2}", p):
            out.append(months(p))
        elif m := re.fullmatch(r"(C\d)=(\w+)", p):
            out.append(SHORT_CHECKS.get((m.group(1), m.group(2)), "does not match the SOP"))
        elif p == "below_p10":
            out.append("faster than the SOP")
        elif p == "above_p90":
            out.append("slower than the SOP")
        elif p == "effort_coverage":
            out.append("work-time standard")
        elif p == "rework":
            out.append("rejections")
        elif p == "SLA":
            out.append("on-time rate")
        elif m := re.fullmatch(r"deps=(\d+)", p):
            out.append("no outside dependency" if m.group(1) == "0" else f"{m.group(1)} outside dependencies")
        else:
            out.append(p)
    return " · ".join(out)


# ------------------------------------------------------------------ findings
def _sop_nonconformance(r, ev):
    tt = ev.get("task_type", str(r.entity_id).split(":")[0])
    m = re.search(r"(C\d)=(\w+)", str(r.entity_id))
    what = CHECKS.get((m.group(1), m.group(2)), "the log does not match the SOP") if m else "the log does not match the SOP"
    pts = [f"In {ev.get('tickets', '?')} of {ev.get('of', '?')} {tt} tickets ({pct(ev.get('share', r.observed))}), "
           f"{what}."]
    show_approvals = bool(m) and m.group(1) in ("C1", "C2")
    for k, n in (ev.get("required_vs_observed_approvals") or {}).items() if show_approvals else []:
        req, obs = [s.strip() for s in k.split(" vs ")] if " vs " in k else (k, "")
        chain = lambda s: "no approval" if s in ("", "-") else s.replace(">", ", then ")  # noqa: E731
        pts.append(f"SOP requires: {chain(req)} → log shows: {chain(obs)} ({n} tickets).")
    return pts


def _sop_elapsed(r, ev, below: bool):
    tt = ev.get("task_type", str(r.entity_id).split(":")[0])
    pts = [f"A typical {tt} ticket takes {hours(r.observed)}; the SOP expects {hours(r.expected)}.",
           f"{pct(ev.get('share_in_tail'))} of tickets finish {"faster than the SOP's fastest expected time" if below else "slower than the SOP's slowest expected time"}"
           f" (only {pct(ev.get('expected_tail_share', 0.1))} should)."]
    return pts


def _component_cause(cause: str) -> str:
    m = re.match(r"(.+?): actual ([\d.]+)h vs SOP ([\d.]+)h", cause or "")
    if not m:
        return _clean(cause)
    comp = COMPONENTS.get(m.group(1), m.group(1))
    return f"Biggest difference is in {comp}: {hours(m.group(2))} in practice vs {hours(m.group(3))} in the SOP."


def _effort(r, ev):
    tt = str(r.entity_id).split(":")[0]
    n = len(ev.get("months", {}))
    actual = ev.get("sop_effort_exec_h", 0) / r.observed if r.observed else None
    return [f"The SOP says the executor needs about {hours(ev.get('sop_effort_exec_h'))} per {tt} ticket.",
            f"In practice they spend about {hours(actual)}: the SOP figure is {times(r.observed)} the real time"
            + (f", in every one of the last {n} months." if n else ".")]


def _rework_sop(r, ev):
    tt = str(r.entity_id).split(":")[0]
    pts = [f"{ev.get('rejected', '?')} of {ev.get('tickets', '?')} {tt} tickets ({pct(r.observed)}) were sent back at "
           f"least once; the SOP target allows about {pct(r.expected)}."]
    if ev.get("reasons"):
        pts.append("Reasons: " + ", ".join(f"{k} ({v})" for k, v in ev["reasons"].items()) + ".")
    if ev.get("quality_targets_source") == "unconfirmed":
        pts.append("Note: the SOP's quality target has not been confirmed by its owner yet.")
    return pts


def _rework_cause(cause: str) -> str:
    m = re.match(r"(.+?) \((\d+)\): preventable by (.+)", cause or "")
    if m:
        return f"Most common reason: {m.group(1)} ({m.group(2)} tickets). The SOP step “{m.group(3)}” should catch this."
    return _clean(cause)


def _rework_increase(r, ev):
    tt, reason = ev.get("task_type", ""), ev.get("reason")
    win = months(ev.get("window_start", ""), ev.get("window_end"))
    why = f" for “{reason}”" if reason and reason != "any" else ""
    pts = [f"In {win}, {pct(r.observed)} of {tt} tickets were sent back{why}, up from {pct(r.expected)} before."]
    mt = ev.get("monthly_tickets_and_rate") or {}
    if mt:
        pts.append("Month by month: " + ", ".join(f"{month(k)} {pct(v[1])} of {v[0]} tickets" for k, v in mt.items()) + ".")
    pts.append("The jump is far too large to be chance.")
    return pts


def _bottleneck(r, ev):
    dept, stage = (str(r.entity_id).split(":") + ["", ""])[:2]
    pts = [f"{dept} tickets wait {hours(r.observed)} for the {stage}'s decision; {hours(r.expected)} is typical across "
           f"the organisation ({times(r.ratio)} longer)."]
    if ev.get("wait_share_of_ticket_time") is not None:
        pts.append(f"Waiting for this approval is {pct(ev['wait_share_of_ticket_time'])} of the ticket's total time; "
                   f"the actual work takes only {hours(ev.get('median_executor_processing_h'))}.")
    if ev.get("task_types"):
        pts.append("Task types: " + ", ".join(f"{k} ({v})" for k, v in ev["task_types"].items()) + ".")
    return pts


def _wait_increase(r, ev):
    stage, tt = ev.get("stage", ""), ev.get("task_type", "")
    win = months(ev.get("window_start", ""), ev.get("window_end"))
    pts = [f"In {win}, {tt} tickets waited {hours(r.observed)} for the {stage}'s approval, up from "
           f"{hours(r.expected)} in the months before ({times(r.ratio)})."]
    mt = ev.get("monthly_tickets_and_median_wait_h") or {}
    if mt:
        pts.append("Month by month: " + ", ".join(f"{month(k)} {hours(v[1])} ({v[0]} tickets)" for k, v in mt.items()) + ".")
    others = ev.get("same_months_other_task_types") or []
    if others:
        pts.append(f"The same wait also rose in {', '.join(others)} at the same time, so the approver's whole queue "
                   "slowed down, not just this task type.")
    elif ev.get("declared_dependencies"):
        pts.append("This task type waits for outside parties too, so part of the rise may be those parties.")
    return pts


def _sla_drop(r, ev):
    dept = str(r.entity_id).split(":")[0]
    win = months(ev.get("window_start", ""), ev.get("window_end"))
    pts = [f"{dept} finished {pct(r.observed)} of tickets on time in {win}, down from {pct(r.expected)} before."]
    mt = ev.get("monthly_tickets_and_sla") or {}
    if mt:
        pts.append("Month by month: " + ", ".join(f"{month(k)} {pct(v[1])} on time ({v[0]} tickets)"
                                                 for k, v in mt.items()) + ".")
    return pts


def _sla_trend(r, ev):
    dept = str(r.entity_id).split(":")[0]
    m = ev.get("monthly_sla_compliance") or {}
    pts = [f"{possessive(dept)} on-time rate fell {len(m) - 1} months in a row: "
           + " → ".join(f"{month(k)} {pct(v)}" for k, v in m.items()) + "."] if m else []
    if ev.get("late_tickets_last_period") is not None:
        pts.append(f"{ev['late_tickets_last_period']} tickets were late in the last month.")
    pri = ev.get("late_by_priority_all_periods") or {}
    if pri:
        pts.append("Late tickets by priority: " + ", ".join(f"{k} {v}" for k, v in pri.items()) + ".")
    return pts


def _rejection_rate(r, ev):
    pts = [f"{ev.get('rejected_tickets', '?')} of their {ev.get('tickets', '?')} tickets ({pct(r.observed)}) were sent "
           f"back at least once; for colleagues in the department it is {pct(ev.get('peer_rate', r.expected))}."]
    if ev.get("task_mix_of_rejected"):
        pts.append("Sent-back tickets by type: " + ", ".join(f"{k} ({v})" for k, v in ev["task_mix_of_rejected"].items()) + ".")
    return pts


_PERSIST = re.compile(r"has been ([\d.]+)x the task-type baseline for (\d+) consecutive months \(([^)]+)\), up from "
                      r"([\d.]+)x.*?Completed volume moved from ([\d.]+) to ([\d.]+)")


def _persistent(r, ev, context: bool):
    m = _PERSIST.search(str(r.explanation))
    if not m:
        return [_clean(r.explanation)]
    ms = [x.strip() for x in m.group(3).split(",")]
    pts = [f"Their tickets have taken {times(m.group(1))} the usual working time for {m.group(2)} months in a row "
           f"({months(ms[0], ms[-1])}), compared with {times(m.group(4))} before.",
           f"Tickets finished per month: {float(m.group(5)):.0f} before → {float(m.group(6)):.0f} now."]
    if not context:
        pts.append("None of the usual reasons (harder tickets, more work, more rejections, a team-wide slowdown) "
                   "explains it.")
    return pts


def _context_cause(cause: str) -> str:
    m = re.match(r"Context factor: (.+)", cause or "")
    if m:
        reasons = [CONTEXT.get(c.strip(), c.strip().replace("_", " ")) for c in m.group(1).split(",")]
        return "Likely reason: " + "; ".join(reasons) + "."
    if (cause or "").startswith("No available context"):
        return "No known reason found in the data."
    return _clean(cause)


def explain(r) -> dict:
    """A finding row -> {title, subject, points, cause, action, confidence, kind}."""
    ev, t = _evidence(r), r.deviation_type
    cause, action = _clean(r.dominant_cause), _clean(r.recommended_investigation)
    try:
        if t == "SOP_NONCONFORMANCE":
            pts = _sop_nonconformance(r, ev)
            cause = _condition(cause)
            cause = cause if not cause or cause.endswith(".") else cause + "."
            cause = cause.replace("although the SOP requires it only when", "although the SOP asks for it only when")
        elif t in ("SOP_ELAPSED_BELOW_STANDARD", "SOP_ELAPSED_ABOVE_STANDARD"):
            below = t.endswith("BELOW_STANDARD")
            pts, cause = _sop_elapsed(r, ev, below), _component_cause(r.dominant_cause)
            action = ("The SOP's time standards are probably set too high. Review them with the SOP owner and "
                      "publish any change as a new SOP version." if below else
                      "Look at the step named above: long waits point to the approval queue or holds; long working "
                      "time points to the work itself.")
        elif t == "SOP_EFFORT_STANDARD":
            pts = _effort(r, ev)
            too_low = float(r.observed) < 1
            cause = f"The SOP's work-time figure looks too {'low' if too_low else 'high'}" + (
                " (it was an expert estimate, not measured)." if "estimate" in cause else ".")
            action = ("Review the figure with the SOP owner or do a short time study. Do not just change the SOP "
                      "to match the data.")
        elif t == "REWORK_ABOVE_SOP_EXPECTATION":
            pts, cause = _rework_sop(r, ev), _rework_cause(r.dominant_cause)
            m = re.search(r"control '(.+?)'", action)
            if m:
                action = (f"Tighten the SOP step “{m.group(1)}” so these mistakes are caught before review, then "
                          "check again whether fewer tickets are sent back.")
        elif t == "REWORK_INCREASE":
            pts = _rework_increase(r, ev)
            win = months(ev.get("window_start", ""), ev.get("window_end"))
            reason = ev.get("reason")
            cause = (f"Something changed in {win} that leads to “{reason}” mistakes." if reason and reason != "any"
                     else f"Something changed in {win} that leads to more mistakes.")
            action = (f"Read the {ev.get('task_type', '')} rejections from {win} and check the SOP step that should "
                      "prevent them (for example a changed form, code list or rule).")
        elif t == "APPROVAL_STAGE_BOTTLENECK":
            pts = _bottleneck(r, ev)
            dept, stage = (str(r.entity_id).split(":") + ["", ""])[:2]
            cause = f"The {stage} approval queue in {dept}."
            action = (f"Look at how quickly the {dept} {stage} approves tickets and how many are waiting. "
                      "This is about the process, not the person doing the work.")
        elif t == "APPROVAL_WAIT_INCREASE":
            pts = _wait_increase(r, ev)
            stage = ev.get("stage", "")
            win = months(ev.get("window_start", ""), ev.get("window_end"))
            if ev.get("same_months_other_task_types"):
                cause = f"The {stage}'s approval queue slowed down for all the task types they approve."
            elif "dependency" in cause.lower():
                cause = f"Waiting for outside parties before the {stage}'s approval (less certain)."
            else:
                cause = f"The {stage}'s approval queue for {ev.get('task_type', 'this task type')}."
            action = (f"Check the {stage}'s approval queue in {win}: workload, absences, or a change in routing. "
                      "This is about the process, not the person doing the work.")
        elif t == "SLA_DROP":
            pts = _sla_drop(r, ev)
            cause = cause.replace("Late tickets concentrated in", "Most late tickets were")
            action = "Check whether approval waits or ticket volume rose in the same department and months."
        elif t == "SLA_DETERIORATION":
            pts = _sla_trend(r, ev)
            cause = "See the approval-wait and workload findings for the same department."   # never name a person here
            action = "Look at the other findings for this department in the same months; they usually explain the fall."
        elif t == "ELEVATED_REJECTION_RATE":
            pts = _rejection_rate(r, ev)
            cause = cause.replace("Top reason:", "Most common reason:")
            action = re.sub(r"Most relevant SOP controls:.*", "", action).replace(
                "Review rejection reasons; consider checklist or guidance for the top reason.",
                "Go through the rejection reasons together; a checklist or short guidance on the most common one "
                "may help.").strip()
        elif t.startswith("PERSISTENT_"):
            ctx = t.endswith("WITH_CONTEXT")
            pts, cause = _persistent(r, ev, ctx), _context_cause(r.dominant_cause)
            action = ("Check the likely reason first (workload, team-wide changes) before any individual follow-up."
                      if ctx else "A supportive check-in by the manager: leave, other duties, tools or support needs. "
                                  "This is not a performance rating.")
        else:
            pts = [_clean(r.explanation)]
    except (TypeError, ValueError, KeyError, AttributeError, IndexError):
        pts = [_clean(r.explanation)]
    title = TITLES.get(t, t.replace("_", " ").capitalize())
    if t == "SOP_EFFORT_STANDARD" and pd.notna(r.observed) and float(r.observed) < 1:
        title = "SOP work-time estimate looks too low"
    return {"title": title, "subject": entity(r.entity_id, t),
            "points": [p for p in pts if p], "cause": cause, "action": action,
            "confidence": r.confidence if isinstance(r.confidence, str) else "",
            "kind": CLASSIFICATION.get(r.classification, str(r.classification).replace("_", " "))}


# ------------------------------------------------------------------ ticket-level causes
def ticket_cause(cause) -> str:
    if not isinstance(cause, str):
        return ""
    if cause.startswith("Wait after DependencyWait event with no declared dependency"):
        return "On hold with no SOP reason (probably waiting for the reviewer)"
    if m := re.match(r"Approval wait at (\w+) stage", cause):
        return f"Waiting for the {m.group(1)}'s approval"
    if cause.startswith("Cross-team / dependency wait"):
        return "Waiting for another team or outside party"
    if cause.startswith("Extended executor processing"):
        return "The work itself took longer"
    if m := re.match(r"Rework after rejection \((.+?)\); preventable by (.+)", cause):
        return f"Sent back for “{m.group(1)}”; the SOP step “{m.group(2)}” should catch this"
    if m := re.match(r"Rework after rejection \((.+?)\)", cause):
        return f"Sent back for “{m.group(1)}”"
    return _clean(cause)


# ------------------------------------------------------------------ planted scenarios (simulation check)
SCENARIO_TEXT = {
    "SC01": "Finance Incharge became about 3× slower to approve",
    "SC02": "One Finance executor's work slowed down with no workload change",
    "SC03": "One Operations executor slowed down after getting 3× more tickets",
    "SC04": "Control: an HR executor on approved leave (must NOT be flagged)",
    "SC05": "Invoice Verification: many more “Incorrect category” rejections",
    "SC06": "Purchase Requests skipping the Lead approval",
    "SC07": "Vendor Onboarding: legal / compliance screening 3× slower",
    "SC08": "Operations overloaded: more tickets, slower approvals",
    "SC09": "Expense, Leave and Daily Ops tickets put on hold without an SOP reason",
    "SC10": "Vendor Onboarding: HOD approval happens but is never logged",
    "SC11": "Daily Ops reports always approved, although the SOP makes it optional",
    "SC12": "SOP time standards set too high for most task types",
    "SC13": "Wrong rejection reason recorded on 15% of rejections",
    "SC14": "Control: a steady executor (must NOT be flagged)",
}

VERDICT = {"detected": "✅ Found", "missed": "❌ Missed", "control_pass": "✅ Correctly not flagged",
           "control_fail": "❌ Wrongly flagged", "detected_wrong_type": "⚠️ Found, but given the wrong label",
           "out_of_scope": "⚪ Not checked yet"}


def scenario_name(sid: str, fallback: str = "") -> str:
    return SCENARIO_TEXT.get(sid, str(fallback).replace("_", " ").capitalize())


def verdict(v: str) -> str:
    return VERDICT.get(v, str(v).replace("_", " "))


def found_types(s) -> str:
    if not isinstance(s, str) or not s:
        return "—"
    return ", ".join(dict.fromkeys(TITLES.get(t, t.replace("_", " ").lower()) for t in s.split("|")))


def found(s) -> str:
    if not isinstance(s, str) or not s:
        return "—"
    m = re.match(r"(\d+)/(\d+) planted mislabels flagged, precision (\d+)%, recall (\d+)%", s)
    if m:
        caught = "all" if m.group(1) == m.group(2) else m.group(1)
        of = f"all {m.group(2)}" if caught == "all" else f"{caught} of {m.group(2)}"
        return f"Caught {of} wrong reason codes; {m.group(3)}% of its flags were right"
    return "; ".join(entity(e.strip()) for e in s.split(";"))


def window(s) -> str:
    """'2026-02-01..2026-03-31' -> 'Feb–Mar 2026'."""
    if not isinstance(s, str) or ".." not in s:
        return str(s)
    a, b = s.split("..", 1)
    return months(a[:7], b[:7])


def plain_scenarios(ev: pd.DataFrame) -> pd.DataFrame:
    """Same columns, readable content."""
    out = ev.copy()
    out["name"] = [scenario_name(s, n) for s, n in zip(out.scenario, out.name)]
    out["verdict"] = out.verdict.map(verdict)
    out["found_types"] = out.found_types.map(found_types)
    out["found"] = out.found.map(found)
    out["window"] = out.window.map(window)
    return out


# ------------------------------------------------------------------ SOP conformance tab
CHECK_NAMES = {
    "c1_approvals": "Right approvals", "c2_approval_order": "Approvals in order",
    "c3_dependency_wait": "No unplanned holds", "c4_required_actions": "Required steps done",
    "c5_rework_cycles": "Rework rounds within limit", "c6_rejection_reasons": "Rejection reasons listed in SOP",
    "c7_elapsed_band": "Time within SOP range",
}
RESULT_WORDS = {
    "ok": "OK", "more": "extra approval", "fewer": "missing approval", "none": "no hold",
    "undeclared": "hold with no SOP reason", "declared": "planned hold", "within": "within SOP range",
    "above_p90": "slower than SOP range", "below_p10": "faster than SOP range", "wrong_order": "out of order",
    "missing": "step missing", "exceeded": "too many rounds", "unexpected": "reason not in SOP",
}
KNOWN_DEVIATIONS = {
    "hold_not_allowed_by_sop": "holds the SOP does not allow", "approvals_more_than_sop": "extra approvals",
    "approvals_fewer_than_sop": "missing approvals",
}
CORR_VERDICT = {"corresponds": "✅ Matches its SOP", "partial": "⚠️ Partly matches its SOP",
                "does_not_correspond": "❌ Does not match its SOP"}


def check_name(col: str) -> str:
    return CHECK_NAMES.get(col, col.split("_", 1)[-1].replace("_", " ").capitalize())


def result_word(v) -> str:
    return RESULT_WORDS.get(v, str(v).replace("_", " ")) if isinstance(v, str) else "not applicable"


def _deviation_list(text: str) -> str:
    names = [KNOWN_DEVIATIONS.get(x.strip().split(":")[0], x.strip().replace("_", " ")) for x in text.split(";")]
    return " and ".join(n for n in names if n)


def corr_notes(notes) -> str:
    if not isinstance(notes, str) or not notes.strip():
        return "—"
    out = []
    for part in notes.split(" | "):
        part = part.strip()
        if m := re.match(r"audit path cannot distinguish it from (SOP-\d+)", part):
            out.append(f"Its steps look the same as {m.group(1)}; the ticket type and timing tell them apart.")
        elif m := re.match(r"audit path resembles (SOP-\d+) \((.+?)\) more closely.*known deviations: (.+)", part):
            out.append(f"Its steps look more like the {m.group(2)} SOP, but only because of a known problem: "
                       f"{_deviation_list(m.group(3).replace(',', ';'))}.")
        elif m := re.match(r"time comparison excludes SOP stages never logged on the platform: (.+)", part):
            out.append(f"The time comparison leaves out the {m.group(1)} step, which the platform never logs.")
        else:
            out.append(_clean(part))
    return " ".join(out)


def known_deviations(text) -> str:
    if not isinstance(text, str) or not text.strip():
        return "—"
    return ", ".join(f"{KNOWN_DEVIATIONS.get(k.strip(), k.strip().replace('_', ' '))} ({n})"
                     for k, n in (x.split(":") for x in text.split(";") if ":" in x))


# ------------------------------------------------------------------ comment check tab
HOLD_COLUMNS = {"external_dependency": "Waiting for another team", "approver_queue": "Waiting for the approver",
                "missing_info": "Waiting for the requester", "unclear": "Not clear from the comment",
                "holds": "All holds", "sop_has_dependency": "SOP expects outside waits?", "task_type": "Task type"}
CONFIDENCE_WORDS = {"high": "High: the fix comment agrees", "medium": "Medium: no fix comment to confirm",
                    "low": "Low: the fix comment backs the platform"}


# ------------------------------------------------------------------ prediction tab
FEATURE_NAMES = {
    "tt_recent_median_h": "How long this task type took in the last 2 weeks",
    "task_type": "Task type", "assignee_open": "How many open tickets the assignee has",
    "tt_recent_n": "How many of this task type finished in the last 2 weeks",
    "dept_recent_late_rate": "Department's recent late rate", "sop_expected_elapsed_h": "SOP's expected time",
    "dept_recent_appr_wait_h": "Department's recent approval wait", "hours_left_in_day": "Hours left in the working day",
    "created_weekday": "Day of the week", "created_hour": "Time of day", "dept_open": "Open tickets in the department",
    "sla_hours": "SLA hours", "sop_required_approvals": "Number of approvals in the SOP",
    "dependency_count": "Number of outside dependencies", "complexity": "Complexity", "sop_p90_h": "SOP's slow-case time",
    "priority": "Priority", "department": "Department",
}


def feature_name(f: str) -> str:
    return FEATURE_NAMES.get(f, f.replace("_", " ").capitalize())


def risk_band(b) -> str:
    """'[0.05, 0.1)' -> '5–10%'."""
    m = re.match(r"\[([\d.]+),\s*([\d.]+)\)", str(b))
    if not m:
        return str(b)
    lo, hi = float(m.group(1)), min(float(m.group(2)), 1.0)
    return f"{lo:.0%}–{hi:.0%}".replace("%–", "–")
