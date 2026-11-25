"""Stage 5: employee- and team-level metrics over weekly, monthly and overall windows.

Raw ticket count is reported but never used alone: `expected_effort_h` (sum of
each ticket's baseline median duration) is the complexity-weighted workload.
"""
from __future__ import annotations

import pandas as pd

PERIODS = {"week": "completed_week", "month": "completed_month", "overall": None}


def _mix(s: pd.Series) -> str:
    vc = s.value_counts()
    return "; ".join(f"{k}:{v}" for k, v in vc.items())


def _agg(g: pd.DataFrame) -> pd.Series:
    return pd.Series({
        "tickets_completed": len(g),
        "expected_effort_h": g.expected_duration_h.sum(),
        "simple_tickets": (g.complexity == "Simple").sum(),
        "medium_tickets": (g.complexity == "Medium").sum(),
        "complex_tickets": (g.complexity == "Complex").sum(),
        "complex_share": (g.complexity == "Complex").mean(),
        "task_mix": _mix(g.task_type),
        "avg_duration_h": g.total_duration_h.mean(),
        "median_duration_h": g.total_duration_h.median(),
        "median_duration_ratio": g.duration_ratio.median(),
        "median_processing_ratio": g.processing_ratio.median(),
        "avg_processing_est_h": g.processing_time_est_h.mean(),
        "avg_waiting_h": g.waiting_time_h.mean(),
        "avg_approval_wait_h": g.approval_waiting_time_h.mean(),
        "rejection_rate": (g.rejection_count > 0).mean(),
        "rework_rate": (g.rework_cycles > 0).mean(),
        "rework_time_share": g.rework_time_h.sum() / max(g.total_duration_h.sum(), 1e-9),
        "sla_compliance": g.sla_met.astype(float).mean(),
        "tickets_above_threshold": int(g.get("duration_flag", pd.Series(False, index=g.index)).sum()),
    })


def employee_metrics(features: pd.DataFrame, employees: pd.DataFrame) -> pd.DataFrame:
    done = features[features.total_duration_h.notna()]
    frames = []
    for ptype, col in PERIODS.items():
        keys = ["assigned_employee_id"] + ([col] if col else [])
        m = done.groupby(keys).apply(_agg).reset_index()
        m["period_type"] = ptype
        m["period"] = m[col] if col else "ALL"
        if col:
            m = m.drop(columns=col)
        frames.append(m)
    out = pd.concat(frames, ignore_index=True).rename(columns={"assigned_employee_id": "employee_id"})
    out = out.merge(employees[["employee_id", "department", "role", "reporting_to"]], on="employee_id", how="left")
    out = out.sort_values(["employee_id", "period_type", "period"])
    out["processing_ratio_trend"] = out.groupby(["employee_id", "period_type"]).median_processing_ratio.diff()
    front = ["employee_id", "department", "role", "reporting_to", "period_type", "period"]
    return out[front + [c for c in out.columns if c not in front]].round(4).reset_index(drop=True)


def team_metrics(features: pd.DataFrame) -> pd.DataFrame:
    done = features[features.total_duration_h.notna()]
    frames = []
    for ptype, col in PERIODS.items():
        keys = ["department"] + ([col] if col else [])
        g = done.groupby(keys)
        m = g.apply(_agg).reset_index()
        extra = g.agg(
            active_executors=("assigned_employee_id", "nunique"),
            median_pre_decision_wait_h=("pre_decision_wait_h", "median"),
            median_lead_wait_h=("decision_wait_lead_h", lambda s: s[s > 0].median() if (s > 0).any() else 0.0),
            total_hours=("total_duration_h", "sum"),
            processing_hours=("processing_time_est_h", "sum"),
            approval_wait_hours=("approval_waiting_time_h", "sum"),
            dependency_wait_hours=("dependency_waiting_time_h", "sum"),
            queue_hours=("queue_time_h", "sum"),
        ).reset_index()
        m = m.merge(extra, on=keys)
        m["decision_wait_share"] = (m.approval_wait_hours + m.dependency_wait_hours) / m.total_hours
        m["processing_share"] = m.processing_hours / m.total_hours
        m["period_type"] = ptype
        m["period"] = m[col] if col else "ALL"
        if col:
            m = m.drop(columns=col)
        frames.append(m)
    out = pd.concat(frames, ignore_index=True)
    front = ["department", "period_type", "period"]
    return out[front + [c for c in out.columns if c not in front]].round(4)
