"""Stage 2: convert raw audit events to the canonical event schema.

Raw values are preserved alongside normalized ones (raw_event_type, raw_*).
Events that cannot be timed are moved to a quarantine frame with a reason,
never silently dropped.
"""
from __future__ import annotations

import json

import pandas as pd

from . import config

CANONICAL_COLUMNS = [
    "event_id", "ticket_id", "employee_id", "department", "role", "event_type", "raw_event_type",
    "timestamp", "stage", "previous_status", "new_status", "previous_value", "new_value",
    "rejection_reason", "comments", "metadata", "raw_change_type", "raw_details",
]


def normalize_event_type(raw: str | None) -> str:
    if raw is None or (isinstance(raw, float) and pd.isna(raw)):
        return config.UNKNOWN_EVENT_TYPE
    key = str(raw).strip().lower().replace(" ", "").replace("_", "")
    return config.EVENT_TYPE_MAP.get(key, config.UNKNOWN_EVENT_TYPE)


def _status(s: pd.Series) -> pd.Series:
    return s.str.strip().str.upper().str.replace(r"\s+", "_", regex=True)


def normalize_events(audit: pd.DataFrame, employees: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return (normalized_events, quarantined_events)."""
    ev = audit.copy()
    quarantine = []

    dup_mask = ev.duplicated(keep="first")
    if dup_mask.any():
        quarantine.append(ev[dup_mask].assign(quarantine_reason="exact_duplicate_event"))
        ev = ev[~dup_mask]

    out = pd.DataFrame({
        "event_id": ev.event_id,
        "ticket_id": ev.ticket_id,
        "employee_id": ev.employee_id,
        "raw_event_type": ev.action,
        "event_type": ev.action.map(normalize_event_type),
        "timestamp": pd.to_datetime(ev.timestamp, format=config.TIMESTAMP_FORMAT, errors="coerce"),
        "stage": ev.stage.str.strip().str.title().replace({"Hod": "HOD"}),
        "previous_status": _status(ev.previous_status),
        "new_status": _status(ev.new_status),
        # Not provided by this export; kept so the schema is stable for real data.
        "previous_value": pd.NA,
        "new_value": pd.NA,
        "rejection_reason": ev.details.where(ev.change_type.eq("rejection_reason")),
        "comments": ev.details.where(~ev.change_type.eq("rejection_reason")),
        "metadata": ev.change_type.map(lambda c: json.dumps({"change_type": c}) if isinstance(c, str) else "{}"),
        "raw_change_type": ev.change_type,
        "raw_details": ev.details,
    }, index=ev.index)

    emp = employees.set_index("employee_id")
    out["department"] = out.employee_id.map(emp.department).fillna("UNKNOWN")
    out["role"] = out.employee_id.map(emp.role).fillna("UNKNOWN")

    no_ts = out.timestamp.isna()
    if no_ts.any():
        quarantine.append(ev[no_ts].assign(quarantine_reason="missing_or_invalid_timestamp"))
        out = out[~no_ts]

    out = out.sort_values(["ticket_id", "timestamp", "event_id"], kind="mergesort").reset_index(drop=True)
    q = pd.concat(quarantine, ignore_index=True) if quarantine else pd.DataFrame(columns=list(audit.columns) + ["quarantine_reason"])
    return out[CANONICAL_COLUMNS], q
