"""Stages 7-9: deviation detection, context checks and evidence-ranked candidate causes.

All logic is deterministic. Each deviation row carries its evidence (JSON),
ranked candidate causes, a confidence level, a classification that separates
process bottlenecks from individual signals, and the source ticket/event ids.

A deviation is a signal for investigation, never a performance judgment.
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd
from scipy.stats import fisher_exact, mannwhitneyu

from . import config

LEAVE_NOTE = "leave/absence data not available in this dataset"


def _r(x, nd=2):
    return None if x is None or (isinstance(x, float) and np.isnan(x)) else round(float(x), nd)


def _confidence(share: float) -> str:
    if share >= config.DOMINANT_SHARE_HIGH_CONF:
        return "high"
    if share >= config.DOMINANT_SHARE_MED_CONF:
        return "medium"
    return "low"


# --------------------------------------------------------------------------- ticket level

def _ticket_components(row) -> dict[str, tuple[float, float]]:
    """component -> (actual_h, expected_h)."""
    return {
        "queue": (row.queue_time_h, row.expected_queue_h),
        "executor_processing": (row.executor_processing_h, row.expected_executor_processing_h),
        "rework": (row.rework_time_h, row.expected_rework_h),
        "approval_wait": (row.approval_waiting_time_h, row.expected_approval_wait_h),
        "dependency_wait": (row.dependency_waiting_time_h, row.expected_dependency_wait_h),
    }


def _cause_label(component: str, row) -> tuple[str, str]:
    """Return (cause label, classification)."""
    if component == "queue":
        return "Assignment queue delay", "process"
    if component == "approval_wait":
        stage = "Lead" if row.decision_wait_lead_h > row.pre_decision_wait_h else "Incharge"
        return f"Approval wait at {stage} stage", "process"
    if component == "dependency_wait":
        if row.dependency_count == 0:
            return "Wait after DependencyWait event with no declared dependency (likely reviewer queue)", "process"
        return "Cross-team / dependency wait", "process"
    if component == "rework":
        reasons = row.rejection_reasons or "unspecified"
        return f"Rework after rejection ({reasons})", "rework"
    return "Extended executor processing", "executor_processing"


def ticket_deviations(f: pd.DataFrame) -> list[dict]:
    weekly_effort = f.groupby(["assigned_employee_id", "completed_week"]).expected_duration_h.sum()
    typical_week = weekly_effort.groupby(level=0).median()
    rows = []
    flagged = f[f.duration_ratio >= config.DURATION_RATIO_THRESHOLD]
    for row in flagged.itertuples(index=False):
        comps = _ticket_components(row)
        excess = {k: max(0.0, a - (e if not np.isnan(e) else 0.0)) for k, (a, e) in comps.items()}
        total_excess = sum(excess.values()) or 1e-9
        ranked = sorted(excess.items(), key=lambda kv: kv[1], reverse=True)
        causes = []
        for comp, hrs in ranked:
            if hrs <= 0:
                continue
            label, cls = _cause_label(comp, row)
            causes.append({"cause": label, "component": comp, "classification": cls,
                           "excess_h": _r(hrs), "share_of_excess": _r(hrs / total_excess)})
        dominant = causes[0] if causes else {"cause": "undetermined", "classification": "undetermined", "share_of_excess": 0}
        wk = weekly_effort.get((row.assigned_employee_id, row.completed_week), np.nan)
        typ = typical_week.get(row.assigned_employee_id, np.nan)
        evidence = {
            "expected_duration_h": _r(row.expected_duration_h),
            "actual_duration_h": _r(row.total_duration_h),
            "duration_ratio": _r(row.duration_ratio),
            "baseline_p90_h": _r(row.baseline_p90_h),
            "components_actual_vs_expected_h": {k: [_r(a), _r(e)] for k, (a, e) in comps.items()},
            "context": {
                "task_type": row.task_type, "complexity": row.complexity, "priority": row.priority,
                "dependency_count": int(row.dependency_count), "rejection_count": int(row.rejection_count),
                "reassignment_count": int(row.reassignment_count), "escalation_count": int(row.escalation_count),
                "assignee_week_expected_effort_h": _r(wk), "assignee_typical_week_effort_h": _r(typ),
                "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
                "leave": LEAVE_NOTE,
            },
        }
        high_workload = not np.isnan(wk) and not np.isnan(typ) and typ > 0 and wk / typ >= config.CONTEXT_WORKLOAD_INCREASE
        if high_workload:
            causes.append({"cause": "High assignee workload that week", "component": "context",
                           "classification": "workload", "excess_h": None, "share_of_excess": None})
        share = dominant["share_of_excess"] or 0
        cls = dominant["classification"]
        if cls == "process":
            action = "Review the approval/dependency queue for this task type; not an executor issue."
        elif cls == "rework":
            action = "Review rejection reasons and submission checklist for this task type."
        else:
            action = "No individual alert from a single ticket; monitored by the employee-level persistence check."
        rows.append({
            "level": "ticket",
            "entity_id": row.ticket_id,
            "department": row.department,
            "employee_id": row.assigned_employee_id,
            "deviation_type": "TICKET_DURATION",
            "severity": "high" if row.duration_ratio >= config.DURATION_RATIO_HIGH else "medium",
            "metric": "total_duration_h",
            "observed": _r(row.total_duration_h),
            "expected": _r(row.expected_duration_h),
            "ratio": _r(row.duration_ratio),
            "baseline_id": row.baseline_id,
            "classification": cls,
            "dominant_cause": dominant["cause"],
            "confidence": _confidence(share),
            "candidate_causes": json.dumps(causes),
            "evidence": json.dumps(evidence),
            "recommended_investigation": action,
            "source_ticket_ids": row.ticket_id,
            "source_event_ids": row.source_event_ids,
            "explanation": (
                f"{row.task_type} ({row.complexity}, {row.priority}) took {row.total_duration_h:.1f}h vs an expected "
                f"{row.expected_duration_h:.1f}h ({row.duration_ratio:.2f}x). "
                f"{share:.0%} of the extra time is attributed to: {dominant['cause'].lower()}."
            ),
        })
    return rows


# --------------------------------------------------------------------------- time windows

def own_history_windows(g: pd.DataFrame, period_col: str, value_col: str, min_n: int, is_raised,
                        min_run: int, agg: str = "median") -> list[dict]:
    """Find runs of consecutive periods in which a series is raised against its OWN recent normal level.

    Periods are walked in order. Each period's baseline is the `agg` (median, or mean for rates) of the ticket values in the last
    WINDOW_BASELINE_PERIODS *unflagged* periods (so an ongoing problem does not raise its own baseline).
    `is_raised(median, baseline)` decides a flag; periods with fewer than `min_n` tickets, or without
    WINDOW_MIN_HISTORY_PERIODS of history, are never flagged. Returns one dict per run of >= `min_run`
    flagged periods: periods, baseline_periods, baseline, monthly {period: (n, median)}.
    """
    g = g[g[value_col].notna()]
    periods = sorted(g[period_col].unique())
    normal, runs, cur = [], [], None
    stats = g.groupby(period_col)[value_col].agg(["size", agg])
    for p in periods:
        n, med = int(stats.loc[p, "size"]), float(stats.loc[p, agg])
        hist = normal[-config.WINDOW_BASELINE_PERIODS:]
        pool = g.loc[g[period_col].isin(hist), value_col]
        flagged = (n >= min_n and len(hist) >= config.WINDOW_MIN_HISTORY_PERIODS and len(pool) >= min_n
                   and is_raised(med, float(pool.agg(agg))))
        if flagged:
            if cur is None:
                cur = {"periods": [], "baseline_periods": hist, "baseline": float(pool.agg(agg)), "monthly": {}}
            cur["periods"].append(p)
            cur["monthly"][p] = (n, med)
        else:
            if cur is not None:
                runs.append(cur)
                cur = None
            if n >= min_n:      # sparse periods are neither flagged nor used as a baseline
                normal.append(p)
    if cur is not None:
        runs.append(cur)
    return [r for r in runs if len(r["periods"]) >= min_run]


def _window(periods: list[str]) -> str:
    return periods[0] if len(periods) == 1 else f"{periods[0]}..{periods[-1]}"


# --------------------------------------------------------------------------- employee level

def _period_frame(f: pd.DataFrame) -> pd.DataFrame:
    col = "completed_month" if config.PERSIST_PERIOD == "M" else "completed_week"
    return f.assign(period=f[col])


def employee_persistent_deviations(f: pd.DataFrame) -> list[dict]:
    """Executor processing time raised for PERSIST_MIN_PERIODS+ consecutive months, at any point in the data,
    against the employee's OWN earlier level (x PERSIST_SELF_CHANGE) and at least PERSIST_RATIO_THRESHOLD of
    the task-type baseline (so a fast person returning to normal speed is not flagged)."""
    pf = _period_frame(f[f.processing_ratio.notna()])
    rows = []
    for emp, g in pf.groupby("assigned_employee_id"):
        per = g.groupby("period").agg(n=("ticket_id", "size"), ratio=("processing_ratio", "median"))
        # a month with under half the person's usual volume (leave, other duties) is not judged
        min_n = max(config.PERSIST_MIN_TICKETS_PER_PERIOD, config.PERSIST_MIN_VOLUME_SHARE * per.n.median())
        runs = own_history_windows(
            g, "period", "processing_ratio", min_n,
            lambda med, base: med >= config.PERSIST_RATIO_THRESHOLD and med >= base * config.PERSIST_SELF_CHANGE,
            config.PERSIST_MIN_PERIODS)
        for run in runs:
            # the run's tickets must be slower than the baseline months' tickets beyond chance: ~25 people x
            # ~10 possible windows are tested, so a strict (Bonferroni-style) level is used
            run_t = g[g.period.isin(run["periods"])].processing_ratio
            base_t = g[g.period.isin(run["baseline_periods"])].processing_ratio
            p_value = float(mannwhitneyu(run_t, base_t, alternative="greater").pvalue)
            if p_value < config.PERSIST_P_VALUE:
                rows.append(_employee_row(emp, g, pf, per, run, p_value))
    return rows


def _employee_row(emp, g, pf, per, run, p_value: float) -> dict:
    k = len(run["periods"])
    recent_p, earlier_p = run["periods"], run["baseline_periods"]
    rec = per.loc[recent_p]
    g_rec, g_ear = g[g.period.isin(recent_p)], g[g.period.isin(earlier_p)]
    rec_level, ear_level = g_rec.processing_ratio.median(), g_ear.processing_ratio.median()
    self_change = rec_level / ear_level if ear_level else np.inf

    dept = g.department.iloc[0]
    n_rec_periods, n_ear_periods = len(recent_p), max(len(earlier_p), 1)
    effort_rec = g_rec.expected_duration_h.sum() / n_rec_periods
    effort_ear = g_ear.expected_duration_h.sum() / n_ear_periods
    vol_rec, vol_ear = len(g_rec) / n_rec_periods, len(g_ear) / n_ear_periods
    rej_rec, rej_ear = (g_rec.rejection_count > 0).mean(), (g_ear.rejection_count > 0).mean()
    cx_rec, cx_ear = (g_rec.complexity == "Complex").mean(), (g_ear.complexity == "Complex").mean()
    team = pf[(pf.department == dept) & (pf.assigned_employee_id != emp)]
    peer_ratio = team[team.period.isin(recent_p)].processing_ratio.median()
    peer_before = team[team.period.isin(earlier_p)].processing_ratio.median()
    peer_change = peer_ratio / peer_before if peer_before else np.nan

    checks = {
        "complexity_shift": {"recent_complex_share": _r(cx_rec), "earlier_complex_share": _r(cx_ear),
                             "explains": bool(cx_rec - cx_ear >= config.CONTEXT_COMPLEXITY_SHIFT_PTS)},
        "workload_increase": {"recent_effort_h_per_period": _r(effort_rec), "earlier_effort_h_per_period": _r(effort_ear),
                              "explains": bool(effort_ear and effort_rec / effort_ear >= config.CONTEXT_WORKLOAD_INCREASE)},
        # Rework time is excluded from the processing ratio, so rejections cannot explain it;
        # a rise is reported as a co-occurring signal instead.
        "rejection_increase": {"recent_rate": _r(rej_rec), "earlier_rate": _r(rej_ear), "explains": False,
                               "co_occurring_signal": bool(rej_rec - rej_ear >= config.CONTEXT_REJECTION_INCREASE_PTS)},
        # peers slowed down by a similar factor over the same months (v2: was an absolute level check)
        "team_wide_trend": {"peer_recent_processing_ratio": _r(peer_ratio), "peer_earlier_processing_ratio": _r(peer_before),
                            "peer_change": _r(peer_change),
                            "explains": bool(peer_change >= config.PERSIST_SELF_CHANGE)},
        "reassignments": {"recent_reassignments": int(g_rec.reassignment_count.sum()),
                          "explains": bool(g_rec.reassignment_count.sum() > 0)},
        "approval_dependency_wait": {"note": "excluded by design: processing ratio measures executor-held time only",
                                     "explains": False},
        "task_mix": {"note": "controlled: each ticket compared with its own task-type baseline", "explains": False},
        "leave": {"note": LEAVE_NOTE, "explains": None},
    }
    explaining = [k for k, v in checks.items() if v.get("explains")]
    unexplained = not explaining
    causes = ([{"cause": f"Context factor: {k}", "classification": "context"} for k in explaining]
              or [{"cause": "No available context factor explains the change", "classification": "individual_signal"}])
    evidence = {
        "periods": {p: {"tickets": int(per.loc[p, "n"]), "median_processing_ratio": _r(per.loc[p, "ratio"])}
                    for p in per.index},
        "recent_periods": recent_p,
        "window_start": recent_p[0], "window_end": recent_p[-1],
        "baseline_periods": earlier_p,
        "recent_median_processing_ratio": _r(rec_level),
        "own_baseline_median_processing_ratio": _r(ear_level),
        "change_vs_own_history": _r(self_change),
        "mann_whitney_p_value": float(f"{p_value:.2e}"),
        "volume_per_period_recent_vs_earlier": [_r(vol_rec, 1), _r(vol_ear, 1)],
        "context_checks": checks,
    }
    dtype = "PERSISTENT_UNEXPLAINED_PROCESSING_INCREASE" if unexplained else "PERSISTENT_PROCESSING_INCREASE_WITH_CONTEXT"
    return {
        "level": "employee",
        "entity_id": emp,
        "department": dept,
        "employee_id": emp,
        "deviation_type": dtype,
        "severity": "high" if rec.ratio.iloc[-1] >= 1.5 else "medium",
        "metric": "median_processing_ratio",
        "observed": _r(rec_level),
        "expected": 1.0,
        "ratio": _r(rec_level),
        "baseline_id": f"{config.BASELINE_VERSION}:task-type processing baselines",
        "classification": "individual_signal" if unexplained else "context_explained",
        "dominant_cause": causes[0]["cause"],
        "confidence": "medium" if unexplained else "low",
        "candidate_causes": json.dumps(causes),
        "evidence": json.dumps(evidence),
        "recommended_investigation": (
            "Manager review recommended: persistent deviation not explained by complexity, workload, "
            "rejections, reassignment or team-wide trend. Check leave, other duties, tooling or support needs."
            if unexplained else "Review the listed context factors before any individual follow-up."),
        "source_ticket_ids": "|".join(g_rec.ticket_id),
        "source_event_ids": "",
        "explanation": (
            f"Executor processing time on {emp}'s tickets has been {rec_level:.2f}x the task-type baseline for "
            f"{k} consecutive months ({', '.join(recent_p)}), up from {ear_level:.2f}x in the months before "
            f"({self_change:.2f}x change). Completed volume moved from {vol_ear:.1f} to {vol_rec:.1f} tickets/month. "
            + ("Complexity, workload, rejections, reassignment and peer trend do not explain it."
               if unexplained else f"Possible context: {', '.join(explaining)}.")),
    }


def employee_rejection_deviations(f: pd.DataFrame) -> list[dict]:
    rows = []
    done = f[f.total_duration_h.notna()]
    for emp, g in done.groupby("assigned_employee_id"):
        dept = g.department.iloc[0]
        peers = done[(done.department == dept) & (done.assigned_employee_id != emp)]
        rate, peer_rate = (g.rejection_count > 0).mean(), (peers.rejection_count > 0).mean()
        n_rej = int((g.rejection_count > 0).sum())
        if n_rej < config.REJECTION_MIN_COUNT or peer_rate == 0 or rate < config.REJECTION_RATE_MULTIPLIER * peer_rate:
            continue
        reasons = g.rejection_reasons.replace("", np.nan).dropna().str.split("|").explode().value_counts()
        rejected = g[g.rejection_count > 0]
        rows.append({
            "level": "employee", "entity_id": emp, "department": dept, "employee_id": emp,
            "deviation_type": "ELEVATED_REJECTION_RATE", "severity": "medium",
            "metric": "rejection_rate", "observed": _r(rate, 3), "expected": _r(peer_rate, 3),
            "ratio": _r(rate / peer_rate), "baseline_id": f"peer rejection rate ({dept})",
            "classification": "individual_signal", "dominant_cause": f"Top reason: {reasons.index[0]}",
            "confidence": "medium",
            "candidate_causes": json.dumps([{"cause": r, "count": int(c)} for r, c in reasons.items()]),
            "evidence": json.dumps({"tickets": len(g), "rejected_tickets": n_rej, "peer_rate": _r(peer_rate, 3),
                                    "task_mix_of_rejected": rejected.task_type.value_counts().to_dict()}),
            "recommended_investigation": "Review rejection reasons; consider checklist or guidance for the top reason.",
            "source_ticket_ids": "|".join(rejected.ticket_id), "source_event_ids": "",
            "explanation": f"{emp}: {rate:.0%} of tickets were rejected at least once vs {peer_rate:.0%} for department peers.",
        })
    return rows


# --------------------------------------------------------------------------- process level

def process_bottlenecks(f: pd.DataFrame, stage_baselines: pd.DataFrame, team: pd.DataFrame) -> list[dict]:
    """Compare each department's decision wait with the org-wide wait for the same
    approver stage and declared dependency count."""
    done = f[f.total_duration_h.notna()]
    overall_team = team[team.period_type == "overall"].set_index("department")
    rows = []
    for stage, col in [("Incharge", "pre_decision_wait_h"), ("Lead", "decision_wait_lead_h")]:
        sub = done if stage == "Incharge" else done[done[col] > 0]
        for (dept, dep), g in sub.groupby(["department", "dependency_count"]):
            base = stage_baselines[(stage_baselines.stage == stage) & (stage_baselines.dependency_count == dep)]
            if len(g) < config.BOTTLENECK_MIN_N or base.empty:
                continue
            org_med = float(base.median_wait_h.iloc[0])
            dept_med = g[col].median()
            ratio = dept_med / org_med if org_med else np.nan
            if not ratio >= config.BOTTLENECK_RATIO_THRESHOLD:
                continue
            monthly = g.groupby("completed_month")[col].median()
            proc_med = g.executor_processing_h.median()
            wait_share = g[col].sum() / g.total_duration_h.sum()
            top = g.nlargest(20, col)
            evidence = {
                "stage": stage, "dependency_count": int(dep), "tickets": len(g),
                "task_types": g.task_type.value_counts().to_dict(),
                "dept_median_wait_h": _r(dept_med), "org_median_wait_h_same_stratum": _r(org_med),
                "org_p90_wait_h_same_stratum": _r(base.p90_wait_h.iloc[0]),
                "wait_share_of_ticket_time": _r(wait_share, 3),
                "median_executor_processing_h": _r(proc_med),
                "monthly_median_wait_h": {k: _r(v) for k, v in monthly.items()},
                "dept_sla_compliance": _r(overall_team.loc[dept, "sla_compliance"], 3),
                "undeclared_dependency_wait_tickets": int(g.dependency_wait_undeclared.sum()),
                "note": "Incharge decision wait = submission -> first-level decision, including the DependencyWait "
                        "interval (cannot be separated in the audit log).",
            }
            rows.append({
                "level": "process", "entity_id": f"{dept}:{stage}:deps={dep}", "department": dept, "employee_id": "",
                "deviation_type": "APPROVAL_STAGE_BOTTLENECK",
                "severity": "high" if ratio >= config.BOTTLENECK_HIGH else "medium",
                "metric": f"median {stage} decision wait (h)", "observed": _r(dept_med), "expected": _r(org_med),
                "ratio": _r(ratio), "baseline_id": f"{config.BASELINE_VERSION}:stage:{stage}:deps={dep}",
                "classification": "process", "dominant_cause": f"{stage} approval queue ({dept})",
                "confidence": "medium" if len(g) >= 50 else "low",
                "candidate_causes": json.dumps([
                    {"cause": f"{stage} approval capacity/queue in {dept}", "classification": "process"},
                    {"cause": "Unrecorded dependency waits (DependencyWait without declared dependency)",
                     "classification": "process"} if g.dependency_wait_undeclared.any() else
                    {"cause": "Declared dependency waits", "classification": "process"},
                ]),
                "evidence": json.dumps(evidence),
                "recommended_investigation": f"Review {dept} {stage} approval queue and turnaround; this is a process-level "
                                             "signal, not an executor issue.",
                "source_ticket_ids": "|".join(top.ticket_id),
                "source_event_ids": "",
                "explanation": (
                    f"In {dept}, tickets with {dep} declared dependencies wait a median {dept_med:.2f}h for the {stage} "
                    f"decision vs {org_med:.2f}h across the organization ({ratio:.2f}x), while median executor processing is "
                    f"{proc_med:.2f}h. Waiting for this decision is {wait_share:.0%} of ticket time."),
            })
    return rows


def sla_deterioration(f: pd.DataFrame, team: pd.DataFrame, min_periods: int = 3, min_drop: float = 0.05) -> list[dict]:
    monthly = team[team.period_type == "month"].sort_values("period")
    rows = []
    for dept, g in monthly.groupby("department"):
        s = g.set_index("period").sla_compliance
        if len(s) < min_periods + 1:
            continue
        tail = s.iloc[-(min_periods + 1):]
        if not (tail.diff().dropna() < 0).all() or tail.iloc[0] - tail.iloc[-1] < min_drop:
            continue
        last = s.index[-1]
        late = f[(f.department == dept) & (f.completed_month == last) & (f.sla_met == False)]  # noqa: E712
        by_emp = late.assigned_employee_id.value_counts()
        late_all = f[(f.department == dept) & (f.sla_met == False)]  # noqa: E712
        rows.append({
            "level": "process", "entity_id": f"{dept}:SLA", "department": dept, "employee_id": "",
            "deviation_type": "SLA_DETERIORATION", "severity": "medium",
            "metric": "monthly SLA compliance", "observed": _r(tail.iloc[-1], 3), "expected": _r(tail.iloc[0], 3),
            "ratio": _r(tail.iloc[-1] / tail.iloc[0], 3), "baseline_id": f"{dept} SLA compliance {tail.index[0]}",
            "classification": "mixed",
            "dominant_cause": (f"Most late tickets in {last}: {by_emp.index[0]} ({by_emp.iloc[0]} of {len(late)})"
                               if len(by_emp) else "undetermined"),
            "confidence": "low",
            "candidate_causes": json.dumps([{"cause": f"late tickets assigned to {e}", "count": int(c)} for e, c in by_emp.items()]),
            "evidence": json.dumps({"monthly_sla_compliance": {k: _r(v, 3) for k, v in s.items()},
                                    "late_tickets_last_period": len(late),
                                    "late_by_priority_all_periods": late_all.priority.value_counts().to_dict()}),
            "recommended_investigation": "Cross-check with persistent employee-level and bottleneck signals in this department.",
            "source_ticket_ids": "|".join(late.ticket_id), "source_event_ids": "",
            "explanation": f"{dept} SLA compliance fell for {min_periods} consecutive months: "
                           + " -> ".join(f"{v:.1%}" for v in tail) + ".",
        })
    return rows


def approval_wait_increases(f: pd.DataFrame) -> list[dict]:
    """A task type's wait for an approver decision rising for WINDOW_MIN_RUN+ months against its OWN recent level.

    Complements the whole-period cross-department comparison (process_bottlenecks), which misses a problem
    that lasts a few months. The audit log has no "dependency resolved" event, so the Incharge wait includes
    any DependencyWait interval. The cause is therefore decided from the pattern across task types:
      - raised in 2+ task types of the department in the same months -> shared approver queue
      - raised in one task type that declares dependencies           -> dependency wait (or that approver)
      - raised in one task type without dependencies                  -> approver queue for that task type
    """
    done = f[f.total_duration_h.notna()]
    found = []
    for stage, col in [("Incharge", "pre_decision_wait_h"), ("Lead", "decision_wait_lead_h")]:
        sub = done if stage == "Incharge" else done[done[col] > 0]
        for tt, g in sub.groupby("task_type"):
            for run in own_history_windows(
                    g, "completed_month", col, config.WAIT_INCREASE_MIN_N,
                    lambda med, base: med >= base * config.WAIT_INCREASE_RATIO and med - base >= config.WAIT_INCREASE_MIN_H,
                    config.WINDOW_MIN_RUN):
                found.append((stage, col, tt, g, run))

    rows = []
    for stage, col, tt, g, run in found:
        dept = g.department.iloc[0]
        months = set(run["periods"])
        siblings = sorted({t for s2, _, t, g2, r2 in found if s2 == stage and t != tt
                           and g2.department.iloc[0] == dept and months & set(r2["periods"])})
        deps = int(g.dependency_count.max())
        if siblings:
            cause, why = f"{stage} approver queue shared across {dept} task types", (
                f"the same wait rose in {', '.join(siblings)} in the same months")
        elif deps and stage == "Incharge":
            cause, why = f"Dependency wait for {tt} (or its {stage} approver)", (
                "only this task type rose and it declares external dependencies; the log cannot separate the two")
        else:
            cause, why = f"{stage} approver queue for {tt}", "only this task type rose and it has no external dependency"
        gw = g[g.completed_month.isin(run["periods"])]
        med, base = gw[col].median(), run["baseline"]
        window = _window(run["periods"])
        before = g[g.completed_month.isin(run["baseline_periods"])]
        rows.append({
            "level": "process", "entity_id": f"{tt}:{stage}:{window}", "department": dept, "employee_id": "",
            "deviation_type": "APPROVAL_WAIT_INCREASE",
            "severity": "high" if med >= 2 * base else "medium",
            "metric": f"median wait for the {stage} decision (h)",
            "observed": _r(med), "expected": _r(base), "ratio": _r(med / base if base else np.nan),
            "baseline_id": f"{tt} {stage} wait, own previous months {_window(run['baseline_periods'])}",
            "classification": "process", "dominant_cause": cause,
            "confidence": "medium" if siblings or not deps else "low",
            "candidate_causes": json.dumps([
                {"cause": cause, "classification": "process", "why": why},
                {"cause": "Volume increase in the same months", "classification": "context",
                 "tickets_per_month_window": _r(len(gw) / len(run["periods"]), 1),
                 "tickets_per_month_before": _r(len(before) / max(len(run["baseline_periods"]), 1), 1)}]),
            "evidence": json.dumps({
                "stage": stage, "task_type": tt, "window_start": run["periods"][0], "window_end": run["periods"][-1],
                "baseline_periods": run["baseline_periods"], "baseline_median_wait_h": _r(base),
                "monthly_tickets_and_median_wait_h": {p: [n, _r(m)] for p, (n, m) in run["monthly"].items()},
                "declared_dependencies": deps, "same_months_other_task_types": siblings,
                "note": "Incharge wait = submission -> first decision, including any DependencyWait interval."}),
            "recommended_investigation": f"Check {cause.lower()} for {window}; process-level signal, not an executor issue.",
            "source_ticket_ids": "|".join(gw.nlargest(20, col).ticket_id), "source_event_ids": "",
            "explanation": (f"In {window}, {tt} tickets waited a median {med:.2f}h for the {stage} decision vs "
                            f"{base:.2f}h in the months before ({med / base:.1f}x). Likely cause: {cause.lower()} ({why})."),
        })
    return rows


def sla_drops(f: pd.DataFrame) -> list[dict]:
    """A department's monthly SLA compliance WINDOW_MIN_RUN+ months below its own recent level by SLA_DROP_PTS.
    Complements sla_deterioration (which needs consecutive monthly declines ending in the last month)."""
    done = f[f.sla_met.notna()].assign(sla=lambda d: d.sla_met.astype(float))
    rows = []
    for dept, g in done.groupby("department"):
        runs = own_history_windows(g, "completed_month", "sla", config.SLA_DROP_MIN_N,
                                   lambda rate, base: base - rate >= config.SLA_DROP_PTS,
                                   config.WINDOW_MIN_RUN, agg="mean")
        for run in runs:
            gw = g[g.completed_month.isin(run["periods"])]
            rate, base, window = gw.sla.mean(), run["baseline"], _window(run["periods"])
            late = gw[gw.sla == 0]
            by_tt = late.task_type.value_counts()
            rows.append({
                "level": "process", "entity_id": f"{dept}:SLA:{window}", "department": dept, "employee_id": "",
                "deviation_type": "SLA_DROP", "severity": "high" if base - rate >= 2 * config.SLA_DROP_PTS else "medium",
                "metric": "monthly SLA compliance", "observed": _r(rate, 3), "expected": _r(base, 3),
                "ratio": _r(rate / base if base else np.nan, 3),
                "baseline_id": f"{dept} SLA compliance, own previous months {_window(run['baseline_periods'])}",
                "classification": "process", "dominant_cause": f"Late tickets concentrated in {by_tt.index[0]}"
                if len(by_tt) else "undetermined", "confidence": "medium",
                "candidate_causes": json.dumps([{"cause": f"late {t} tickets", "count": int(c)} for t, c in by_tt.items()]),
                "evidence": json.dumps({"window_start": run["periods"][0], "window_end": run["periods"][-1],
                                        "baseline_periods": run["baseline_periods"], "baseline_sla": _r(base, 3),
                                        "monthly_tickets_and_sla": {p: [n, _r(r, 3)] for p, (n, r) in run["monthly"].items()},
                                        "tickets_per_month_window": _r(len(gw) / len(run["periods"]), 1)}),
                "recommended_investigation": "Cross-check with approval-wait and volume signals for the same department "
                                             "and months.",
                "source_ticket_ids": "|".join(late.ticket_id), "source_event_ids": "",
                "explanation": f"{dept} met the SLA on {rate:.0%} of tickets in {window} vs {base:.0%} in the months before.",
            })
    return rows


def rework_increases(f: pd.DataFrame) -> list[dict]:
    """A task type's rejection rate (overall, or for one platform reason) rising for WINDOW_MIN_RUN+ months
    against its OWN recent level: at least REWORK_INCREASE_FACTOR x and REWORK_INCREASE_PTS higher, and
    beyond chance (one-sided Fisher exact test, window vs baseline months, p < REWORK_P_VALUE).
    A reason-level finding is reported in preference to the overall rate for the same months."""
    done = f[f.total_duration_h.notna()].copy()
    done["rej_any"] = (done.rejection_count > 0).astype(float)
    reasons = {r: "rej_" + r.lower().replace(" ", "_") for r in config.PLATFORM_REJECTION_REASONS}
    for r, col in reasons.items():
        done[col] = done.rejection_reasons.fillna("").str.contains(r, regex=False).astype(float)

    def raised(rate, base):
        return rate >= base * config.REWORK_INCREASE_FACTOR and rate - base >= config.REWORK_INCREASE_PTS

    rows = []
    for tt, g in done.groupby("task_type"):
        found = []
        for label, col in [("any reason", "rej_any")] + list(reasons.items()):
            for run in own_history_windows(g, "completed_month", col, config.REWORK_MIN_N, raised,
                                           config.WINDOW_MIN_RUN, agg="mean"):
                w = g[g.completed_month.isin(run["periods"])][col]
                b = g[g.completed_month.isin(run["baseline_periods"])][col]
                p = float(fisher_exact([[w.sum(), len(w) - w.sum()], [b.sum(), len(b) - b.sum()]],
                                       alternative="greater")[1])
                if p < config.REWORK_P_VALUE:
                    found.append((label, col, run, w.mean(), b.mean(), p))
        specific = [x for x in found if x[0] != "any reason"]
        for label, col, run, rate, base, p in found:
            if label == "any reason" and any(set(run["periods"]) & set(s[2]["periods"]) for s in specific):
                continue
            window = _window(run["periods"])
            gw = g[g.completed_month.isin(run["periods"])]
            rejected = gw[gw[col] > 0]
            rows.append({
                "level": "process", "entity_id": f"{tt}:rework:{label}:{window}", "department": gw.department.iloc[0],
                "employee_id": "", "deviation_type": "REWORK_INCREASE",
                "severity": "high" if rate >= 3 * base else "medium",
                "metric": f"share of tickets rejected ({label})", "observed": _r(rate, 3), "expected": _r(base, 3),
                "ratio": _r(rate / base if base else np.nan), "baseline_id":
                    f"{tt} rejection rate, own previous months {_window(run['baseline_periods'])}",
                "classification": "rework",
                "dominant_cause": f"{label} rejections ({tt})" if label != "any reason" else f"Rejections ({tt})",
                "confidence": "medium",
                "candidate_causes": json.dumps([
                    {"cause": f"A check that should prevent '{label}' stopped working in {window}",
                     "classification": "rework"},
                    {"cause": "Change in the reviewer or in how strictly the review is applied", "classification": "process"},
                    {"cause": "Reason codes may be mislabelled; read the reviewers' comments (LLM comment check)",
                     "classification": "data_quality"}]),
                "evidence": json.dumps({"task_type": tt, "reason": label, "window_start": run["periods"][0],
                                        "window_end": run["periods"][-1], "baseline_periods": run["baseline_periods"],
                                        "baseline_rate": _r(base, 3), "fisher_p_value": float(f"{p:.2e}"),
                                        "monthly_tickets_and_rate": {k: [n, _r(v, 3)] for k, (n, v) in run["monthly"].items()},
                                        "window_reason_mix": gw.rejection_reasons.replace("", np.nan).dropna()
                                        .str.split("|").explode().value_counts().to_dict()}),
                "recommended_investigation": f"Review {tt} rejections for {window} and the check that should prevent them.",
                "source_ticket_ids": "|".join(rejected.ticket_id), "source_event_ids": "",
                "explanation": (f"In {window}, {rate:.0%} of {tt} tickets were rejected ({label}) vs {base:.0%} in the "
                                f"months before ({rate / base if base else float('inf'):.1f}x)."),
            })
    return rows


def detect_all(f, stage_baselines, team) -> pd.DataFrame:
    rows = (process_bottlenecks(f, stage_baselines, team) + approval_wait_increases(f) + sla_deterioration(f, team)
            + sla_drops(f) + rework_increases(f) + employee_persistent_deviations(f) + employee_rejection_deviations(f)
            + ticket_deviations(f))
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    out.insert(0, "deviation_id", [f"DEV-{i + 1:04d}" for i in range(len(out))])
    return out
