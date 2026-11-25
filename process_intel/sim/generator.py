"""SOP-driven ticket simulator (v2).

Every ticket is generated from its SOP: executor work steps (three-point times), approval stages and their
response latency, external dependencies (parallel groups wait for the slowest), rework triggers and their
detector stages. Executors and approvers are resources with busy intervals, so queues and workload effects
emerge instead of being painted on. Planted scenarios (scenarios.py) change the generating process for a
known entity and period; their effects are recorded per ticket as ground truth.

Output (same raw format as data/raw, so Phase 1 runs unchanged):
    <out>/raw/{employees,tickets,audit_logs,task_types}.csv
    <out>/extra/{comments,worklogs,absences}.csv          new data Phase 1 does not read yet
    <out>/truth/{scenarios,tickets_truth,comments_truth}.csv   answer key; never read by the pipeline
"""
from __future__ import annotations

import bisect
import datetime as dt
import math
import random
from collections import defaultdict
from pathlib import Path

import pandas as pd

from .. import config, ingestion, sop
from . import text
from .scenarios import SCENARIOS, active

START, END = dt.date(2025, 10, 1), dt.date(2026, 9, 30)
DAILY_RATE = 1.75                       # tickets per task type per weekday
WEEKEND_FACTOR = 0.35
PRIORITY_MIX = {"Low": 0.45, "Medium": 0.40, "High": 0.15}
# Hidden reality: actual executor effort as a share of the SOP standard (SC12), and approver latency factor.
EFFORT_REALITY = {"BOQ Review": 0.45, "Purchase Request": 0.70, "Invoice Verification": 0.60,
                  "Expense Approval": 0.85, "Vendor Onboarding": 0.60, "Daily Operations Report": 0.45,
                  "Incident Review": 0.50, "Leave Approval": 1.10, "Employee Document Verification": 0.55}
LATENCY_REALITY = {"Expense Approval": 1.6, "Leave Approval": 1.6}
HOLD_TYPES = {"Expense Approval": 0.6, "Leave Approval": 0.6, "Daily Operations Report": 0.6}   # SC09
MISLABEL_P = 0.15                                                                                # SC13


def _pert(rng: random.Random, tp: dict, scale: float = 1.0) -> float:
    lo, mode, hi = float(tp["min"]), float(tp["likely"]), float(tp["max"])
    if hi <= lo:
        return lo * scale
    a = 1 + 4 * (mode - lo) / (hi - lo)
    b = 1 + 4 * (hi - mode) / (hi - lo)
    return (lo + rng.betavariate(a, b) * (hi - lo)) * scale


class Resource:
    """A person who does one thing at a time: earliest free slot of a given length after a time."""

    def __init__(self):
        self.starts, self.ends = [], []

    def book(self, after: dt.datetime, hours: float) -> dt.datetime:
        length = dt.timedelta(hours=hours)
        t = after
        i = max(bisect.bisect_left(self.ends, t) - 1, 0)
        while i < len(self.starts):
            if self.ends[i] <= t:
                i += 1
                continue
            if t + length <= self.starts[i]:
                break
            t = max(t, self.ends[i])
            i += 1
        j = bisect.bisect_left(self.starts, t)
        self.starts.insert(j, t)
        self.ends.insert(j, t + length)
        return t


def _absences(rng, employees) -> list[dict]:
    rows = []
    days = (END - START).days
    for e in employees.itertuples():
        if e.role != "Executor":
            continue
        for _ in range(rng.randint(1, 3)):
            s = START + dt.timedelta(days=rng.randrange(days - 10))
            rows.append({"employee_id": e.employee_id, "start_date": s,
                         "end_date": s + dt.timedelta(days=rng.randint(1, 5)),
                         "type": rng.choice(["annual_leave", "annual_leave", "sick_leave"])})
    rows.append({"employee_id": "E1021", "start_date": dt.date(2026, 4, 6), "end_date": dt.date(2026, 4, 24),
                 "type": "annual_leave"})                                                       # SC04
    return rows


def generate(out_dir: Path, seed: int = 2026, sop_dir=config.SOP_DIR, base_raw=config.RAW_DIR) -> dict:
    rng = random.Random(seed)
    base = ingestion.load_raw(base_raw)
    employees, task_types = base["employees"], base["task_types"]
    _, sops = sop.validate_sops(sop.load_sops(sop_dir), task_types)
    tt_meta = task_types.set_index("task_type")
    approver = {(r.department, r.role): r.employee_id for r in employees.itertuples() if r.role != "Executor"}
    execs = {d: g.employee_id.tolist() for d, g in employees[employees.role == "Executor"].groupby("department")}
    speed = {e: math.exp(rng.gauss(0, 0.12)) for es in execs.values() for e in es}
    absences = _absences(rng, employees)
    away = defaultdict(set)
    for a in absences:
        d = a["start_date"]
        while d <= a["end_date"]:
            away[a["employee_id"]].add(d)
            d += dt.timedelta(days=1)
    people = defaultdict(Resource)

    # arrivals
    arrivals = []
    day = START
    while day <= END:
        for tt, d in sops.items():
            rate = DAILY_RATE * (WEEKEND_FACTOR if day.weekday() >= 5 else 1.0)
            if d["department"] == "Operations" and active("SC08", day):
                rate *= 1.8
            n = _poisson(rng, rate)
            for _ in range(n):
                t = dt.datetime.combine(day, dt.time(8)) + dt.timedelta(minutes=rng.randrange(600))
                arrivals.append((t, tt))
        day += dt.timedelta(days=1)
    arrivals.sort()

    tickets, events, comments, ctruth, worklogs, truth = [], [], [], [], [], []
    ev_n = [0]

    def event(tid, emp, action, ts, stage, prev, new, change="", details=""):
        ev_n[0] += 1
        eid = f"EV{ev_n[0]:07d}"
        events.append({"event_id": eid, "ticket_id": tid, "employee_id": emp, "action": action,
                       "timestamp": ts.strftime(config.TIMESTAMP_FORMAT), "stage": stage, "previous_status": prev,
                       "new_status": new, "change_type": change, "details": details})
        return eid

    def comment(tid, eid, emp, ts, body, label, coded=""):
        cid = f"C{len(comments) + 1:07d}"
        comments.append({"comment_id": cid, "ticket_id": tid, "event_id": eid, "employee_id": emp,
                         "timestamp": ts.strftime(config.TIMESTAMP_FORMAT), "text": body})
        ctruth.append({"comment_id": cid, "true_label": label, "platform_reason_code": coded})

    for k, (created, tt) in enumerate(arrivals, 1):
        d, meta, day = sops[tt], tt_meta.loc[tt], created.date()
        dept, tid = d["department"], f"T{k:05d}"
        prio = rng.choices(list(PRIORITY_MIX), weights=PRIORITY_MIX.values())[0]
        steps = {s["step_id"]: s for s in d["steps"]}
        scen = set()

        # assignment (absent executors get nothing; SC03 triples E1015's share)
        pool = [e for e in execs[dept] if day not in away[e]]
        weights = [3.0 if (e == "E1015" and active("SC03", day)) else 1.0 for e in pool]
        ex = rng.choices(pool, weights=weights)[0]
        if ex == "E1015" and active("SC03", day):
            scen.add("SC03")

        # executor work
        size = math.exp(rng.gauss(0, 0.3))
        work_min = sum(_pert(rng, s["effort_min"]) for s in d["steps"]
                       if s["role"] == "Executor" and s["type"] in ("intake", "work"))
        mult = EFFORT_REALITY[tt] * size * speed[ex]
        if ex == "E1003" and active("SC02", day):
            mult *= 1.7
            scen.add("SC02")
        if ex == "E1015" and active("SC03", day):
            mult *= 1.4
        if dept == "Operations" and active("SC08", day):
            mult *= 1.2
            scen.add("SC08")
        work_h = work_min * mult / 60
        assigned = created + dt.timedelta(minutes=rng.randint(2, 8))
        event(tid, ex, "Created", created, "Executor", "", "Created")
        event(tid, ex, "Assigned", assigned, "Executor", "Created", "Assigned")
        start = people[ex].book(assigned + dt.timedelta(minutes=rng.randint(0, 30)), work_h)
        submit = start + dt.timedelta(hours=work_h)
        for _ in range(rng.choices([0, 1, 2], weights=[0.5, 0.38, 0.12])[0]):
            event(tid, ex, "Updated", start + (submit - start) * rng.uniform(0.2, 0.9), "Executor", "Assigned",
                  "Assigned", "field_change", "normal edit")
        event(tid, ex, "Submitted", submit, "Executor", "Assigned", "Submitted")
        worklog_h = work_h

        # approval route for this ticket
        stages = [m["stage"] for m in d["approval_matrix"] if m["stage"] != "HOD"]   # SC10: HOD never logged
        if tt == "Daily Operations Report":
            scen.add("SC11")
        if tt == "Vendor Onboarding":
            scen.add("SC10")
        if tt == "Purchase Request" and active("SC06", day) and rng.random() < 0.45:
            stages = [s for s in stages if s != "Lead"]
            scen.add("SC06")
        detectors = defaultdict(list)
        for t in d["rework_triggers"]:
            role = steps.get(t["detected_at"], {}).get("role")
            if role in stages:
                detectors[role].append(t["reason"])
        p_reject_total = 1 - float(d["expected_first_pass_yield"])
        n_det = sum(len(v) for v in detectors.values()) or 1

        ready, rounds, dep_wait_h, appr_wait_h, rework_h, hold_kind = submit, 0, 0.0, 0.0, 0.0, ""
        # holds before the first review
        if d["dependencies"]:
            hold_t = submit + dt.timedelta(minutes=rng.randint(5, 40))
            eid = event(tid, ex, "DependencyWait", hold_t, "Executor", "Submitted", "Submitted", "dependency",
                        "Waiting for dependent information")
            groups = defaultdict(list)
            for dep in d["dependencies"]:
                w = _pert(rng, dep["typical_wait_h"])
                if tt == "Vendor Onboarding" and dep["id"] == "D2" and active("SC07", day):
                    w *= 3
                    scen.add("SC07")
                groups[dep.get("parallel_group") or dep["id"]].append((w, dep))
            dep_wait_h = sum(max(x[0] for x in g) for g in groups.values())
            slowest = max((x for g in groups.values() for x in g), key=lambda x: x[0])[1]
            comment(tid, eid, ex, hold_t, text.hold(rng, "external_dependency", tt, slowest["provider"].split(" (")[0],
                                                    slowest["item"]), "external_dependency")
            hold_kind = "external_dependency"
            ready = hold_t + dt.timedelta(hours=dep_wait_h)
        elif tt in HOLD_TYPES and rng.random() < HOLD_TYPES[tt]:
            scen.add("SC09")
            hold_t = submit + dt.timedelta(minutes=rng.randint(5, 40))
            eid = event(tid, ex, "DependencyWait", hold_t, "Executor", "Submitted", "Submitted", "dependency",
                        "Waiting for dependent information")
            hold_kind = rng.choices(["approver_queue", "missing_info"], weights=[0.6, 0.4])[0]
            comment(tid, eid, ex, hold_t, text.hold(rng, hold_kind, tt), hold_kind)
            if hold_kind == "missing_info":
                dep_wait_h = rng.uniform(0.5, 3.0)
            ready = hold_t + dt.timedelta(hours=dep_wait_h)

        completed = ready
        while True:
            rejected = False
            for i, stage in enumerate(stages):
                appr = approver[(dept, stage)]
                step = next(s for s in d["steps"] if s["type"] == "approval" and s["role"] == stage)
                lat = _pert(rng, step.get("queue_wait_h") or {"min": 0.1, "likely": 0.5, "max": 2})
                lat *= LATENCY_REALITY.get(tt, 0.7)
                eff = _pert(rng, step["effort_min"]) / 60
                if dept == "Finance" and stage == "Incharge" and active("SC01", day):
                    lat, eff = lat * 3, eff * 2
                    scen.add("SC01")
                if dept == "Operations" and active("SC08", day):
                    lat *= 2.5
                begin = people[appr].book(ready + dt.timedelta(hours=lat), eff)
                decided = begin + dt.timedelta(hours=eff)
                appr_wait_h += (decided - ready).total_seconds() / 3600
                prev = "Submitted" if i == 0 else "Approved"
                reasons = detectors.get(stage, [])
                p = p_reject_total * len(reasons) / n_det * (0.35 if rounds else 1.0)
                weights = [1.0] * len(reasons)
                if tt == "Invoice Verification" and active("SC05", day) and "Incorrect category" in reasons:
                    weights[reasons.index("Incorrect category")] = 5.0
                    p = min(0.6, p * (1 + 4 / len(reasons)))
                if reasons and rounds < int(d["max_rework_cycles"]) and rng.random() < p:
                    reason = rng.choices(reasons, weights=weights)[0]
                    if tt == "Invoice Verification" and active("SC05", day) and reason == "Incorrect category":
                        scen.add("SC05")
                    coded = reason
                    if rng.random() < MISLABEL_P:
                        coded = rng.choice([r for r in config.PLATFORM_REJECTION_REASONS if r != reason])
                        scen.add("SC13")
                    eid = event(tid, appr, "Rejected", decided, stage, prev, "Rejected", "rejection_reason", coded)
                    comment(tid, eid, appr, decided, text.rejection(rng, reason, tt), reason, coded)
                    rw = _pert(rng, d["rework_effort_min"]) * EFFORT_REALITY[tt] * speed[ex] / 60
                    rw_start = people[ex].book(decided + dt.timedelta(minutes=rng.randint(10, 60)), rw)
                    fixed = rw_start + dt.timedelta(hours=rw)
                    rework_h += (fixed - decided).total_seconds() / 3600
                    worklog_h += rw
                    eid = event(tid, ex, "Updated", fixed, "Executor", "Rejected", "Draft", "correction", coded)
                    if rng.random() < 0.7:
                        comment(tid, eid, ex, fixed, text.correction(rng, reason, tt), reason, coded)
                    ready = fixed + dt.timedelta(minutes=rng.randint(5, 15))
                    event(tid, ex, "Resubmitted", ready, "Executor", "Draft", "Submitted")
                    rounds += 1
                    rejected = True
                    break
                eid = event(tid, appr, "Approved", decided, stage, prev, "Approved", "final_review" if i else "")
                if rng.random() < 0.25:
                    comment(tid, eid, appr, decided, text.approve_note(rng, tt), "approval_note")
                ready = completed = decided
            if not rejected:
                break

        due = created + dt.timedelta(hours=config.SLA_HOURS[prio])
        tickets.append({"ticket_id": tid, "task_type": tt, "department": dept, "assigned_employee_id": ex,
                        "priority": prio, "complexity": meta.complexity, "sop_steps": meta.sop_steps,
                        "approval_count": meta.approval_count, "dependency_count": meta.dependency_count,
                        "created_at": created.strftime(config.TIMESTAMP_FORMAT),
                        "due_at": due.strftime(config.TIMESTAMP_FORMAT),
                        "completed_at": completed.strftime(config.TIMESTAMP_FORMAT),
                        "final_status": "Completed" if completed <= due else "Completed_Late"})
        if rng.random() > 0.1:                                       # 10% of tickets have no worklog
            worklogs.append({"ticket_id": tid, "employee_id": ex, "date": day,
                             "minutes": max(5, round(worklog_h * 60 * rng.uniform(0.75, 1.1) / 5) * 5)})
        truth.append({"ticket_id": tid, "scenarios": "|".join(sorted(scen)), "true_exec_work_h": round(work_h, 3),
                      "true_rework_h": round(rework_h, 3), "true_dependency_wait_h": round(dep_wait_h, 3),
                      "true_approval_wait_h": round(appr_wait_h, 3), "hold_kind": hold_kind,
                      "rework_rounds": rounds})

    out = Path(out_dir)
    for sub in ("raw", "extra", "truth"):
        (out / sub).mkdir(parents=True, exist_ok=True)
    # number events in time order, as a platform would; carry the new ids into the comments
    events_df = pd.DataFrame(events).sort_values(["timestamp", "event_id"]).reset_index(drop=True)
    new_id = {old: f"EV{i + 1:07d}" for i, old in enumerate(events_df.event_id)}
    events_df["event_id"] = events_df.event_id.map(new_id)
    for c in comments:
        c["event_id"] = new_id[c["event_id"]]
    files = {
        "raw/employees.csv": employees, "raw/task_types.csv": task_types,
        "raw/tickets.csv": pd.DataFrame(tickets), "raw/audit_logs.csv": events_df,
        "extra/comments.csv": pd.DataFrame(comments), "extra/worklogs.csv": pd.DataFrame(worklogs),
        "extra/absences.csv": pd.DataFrame(absences),
        "truth/scenarios.csv": pd.DataFrame(SCENARIOS).assign(expected=lambda x: x.expected.map("|".join)),
        "truth/tickets_truth.csv": pd.DataFrame(truth), "truth/comments_truth.csv": pd.DataFrame(ctruth),
    }
    for name, df in files.items():
        df.to_csv(out / name, index=False)
    return {name: len(df) for name, df in files.items()}


def _poisson(rng: random.Random, lam: float) -> int:
    n, p, l = 0, 1.0, math.exp(-lam)
    while True:
        p *= rng.random()
        if p <= l:
            return n
        n += 1
