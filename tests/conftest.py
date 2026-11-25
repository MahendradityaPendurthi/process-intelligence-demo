import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from process_intel import normalization  # noqa: E402

EMPLOYEES = pd.DataFrame({
    "employee_id": ["E1", "M1", "L1", "H1"],
    "employee_name": ["Exec", "Inch", "Lead", "Hod"],
    "department": ["Finance"] * 4,
    "role": ["Executor", "Incharge", "Lead", "HOD"],
    "reporting_to": ["M1", "L1", "H1", None],
    "active_status": ["Active"] * 4,
})

AUDIT_COLUMNS = ["event_id", "ticket_id", "employee_id", "action", "timestamp", "stage",
                 "previous_status", "new_status", "change_type", "details"]


def raw_events(rows, ticket_id="T1"):
    """rows: (action, 'HH:MM', employee, stage[, change_type, details])"""
    out = []
    for i, r in enumerate(rows, start=1):
        action, hhmm, emp, stage, *rest = r
        change_type, details = (rest + [None, None])[:2]
        out.append({"event_id": f"EV{i:03d}", "ticket_id": ticket_id, "employee_id": emp, "action": action,
                    "timestamp": f"2026-08-01 {hhmm}:00", "stage": stage, "previous_status": None,
                    "new_status": action, "change_type": change_type, "details": details})
    return pd.DataFrame(out, columns=AUDIT_COLUMNS)


def normalized(rows, ticket_id="T1"):
    ev, _ = normalization.normalize_events(raw_events(rows, ticket_id), EMPLOYEES)
    return ev


@pytest.fixture
def employees():
    return EMPLOYEES.copy()
