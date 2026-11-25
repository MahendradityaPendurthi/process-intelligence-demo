"""Stage 4: ticket-level features (ticket attributes + reconstructed lifecycle)."""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import config


def build_ticket_features(tickets: pd.DataFrame, lifecycles: pd.DataFrame) -> pd.DataFrame:
    t = tickets.copy()
    for col in ["created_at", "due_at", "completed_at"]:
        t[col] = pd.to_datetime(t[col], format=config.TIMESTAMP_FORMAT, errors="coerce")
    for col in ["sop_steps", "approval_count", "dependency_count"]:
        t[col] = pd.to_numeric(t[col], errors="coerce").astype("Int64")

    f = t.merge(lifecycles, on="ticket_id", how="left", validate="one_to_one")
    f["has_lifecycle"] = f.event_count.notna()

    is_done = f.final_status.isin(config.COMPLETED_STATUSES) & f.completed_at.notna()
    f["total_duration_h"] = np.where(is_done, (f.completed_at - f.created_at).dt.total_seconds() / 3600, np.nan)
    f["duration_source_mismatch"] = (f.total_duration_h - f.lifecycle_span_h).abs() > 1e-6

    f["queue_time_h"] = f.queue_h
    f["processing_time_est_h"] = f.processing_h + f.rework_h     # executor-held time (estimated)
    f["executor_processing_h"] = f.processing_h                  # executor-held time outside rework cycles
    f["approval_waiting_time_h"] = f.approval_wait_h
    f["dependency_waiting_time_h"] = f.dependency_wait_h
    f["waiting_time_h"] = f.queue_h + f.approval_wait_h + f.dependency_wait_h
    f["rework_time_h"] = f.rework_h
    f["pre_decision_wait_h"] = f.decision_wait_incharge_h  # submission -> first-level decision

    span = f.lifecycle_span_h.replace(0, np.nan)
    f["waiting_ratio"] = (f.waiting_time_h / span).round(4)
    f["rework_ratio"] = (f.rework_h / span).round(4)
    f["ticket_rejection_rate"] = (f.rejection_count / f.submission_count.replace(0, np.nan)).round(4)
    f["dependency_wait_undeclared"] = (f.dependency_wait_events > 0) & (f.dependency_count == 0)

    f["sla_hours"] = (f.due_at - f.created_at).dt.total_seconds() / 3600
    f["sla_met"] = np.where(is_done, f.completed_at <= f.due_at, pd.NA)
    f["sla_delay_h"] = np.where(is_done, ((f.completed_at - f.due_at).dt.total_seconds() / 3600).clip(lower=0), np.nan)

    f["completed_week"] = f.completed_at.dt.to_period("W-SUN").astype(str)
    f["completed_month"] = f.completed_at.dt.to_period("M").astype(str)
    f["metric_quality"] = "processing/waiting split estimated from audit-log state; durations in calendar hours"

    cols = [
        "ticket_id", "task_type", "department", "assigned_employee_id", "priority", "complexity",
        "sop_steps", "approval_count", "dependency_count", "created_at", "due_at", "completed_at", "final_status",
        "completed_week", "completed_month", "total_duration_h", "processing_time_est_h", "executor_processing_h", "waiting_time_h",
        "queue_time_h", "approval_waiting_time_h", "dependency_waiting_time_h", "pre_decision_wait_h",
        "decision_wait_lead_h", "decision_wait_hod_h", "rework_time_h", "waiting_ratio", "rework_ratio",
        "rejection_count", "resubmission_count", "rework_cycles", "update_count", "correction_count",
        "approval_events", "reassignment_count", "escalation_count", "reopen_count", "handoff_count",
        "stage_transition_count", "stages_visited", "dependency_wait_events", "dependency_wait_undeclared",
        "ticket_rejection_rate", "rejection_reasons", "sla_hours", "sla_met", "sla_delay_h", "is_closed",
        "closure_type", "has_lifecycle", "duration_source_mismatch", "anomalies", "metric_quality",
        "source_event_ids",
    ]
    return f[cols]
