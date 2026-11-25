import pandas as pd

from process_intel import normalization
from tests.conftest import EMPLOYEES, raw_events


def test_event_type_mapping_and_aliases():
    assert normalization.normalize_event_type("Submitted") == "SUBMITTED"
    assert normalization.normalize_event_type("submitted_for_approval") == "SUBMITTED"
    assert normalization.normalize_event_type("send_back") == "REJECTED"
    assert normalization.normalize_event_type("DependencyWait") == "DEPENDENCY_WAIT"
    assert normalization.normalize_event_type("edit") == "UPDATED"
    assert normalization.normalize_event_type("teleported") == "UNKNOWN"
    assert normalization.normalize_event_type(None) == "UNKNOWN"


def test_raw_value_preserved_and_rejection_reason_extracted():
    raw = raw_events([("Created", "09:00", "E1", "Executor"),
                      ("Rejected", "10:00", "M1", "Incharge", "rejection_reason", "Amount mismatch")])
    ev, q = normalization.normalize_events(raw, EMPLOYEES)
    assert list(ev.raw_event_type) == ["Created", "Rejected"]
    assert list(ev.event_type) == ["CREATED", "REJECTED"]
    assert ev.rejection_reason.iloc[1] == "Amount mismatch"
    assert ev.raw_details.iloc[1] == "Amount mismatch"
    assert q.empty


def test_out_of_order_events_are_sorted_chronologically():
    raw = raw_events([("Submitted", "10:00", "E1", "Executor"), ("Created", "09:00", "E1", "Executor"),
                      ("Assigned", "09:30", "E1", "Executor")])
    ev, _ = normalization.normalize_events(raw, EMPLOYEES)
    assert list(ev.event_type) == ["CREATED", "ASSIGNED", "SUBMITTED"]


def test_timestamp_tie_broken_by_event_id():
    raw = raw_events([("Created", "09:00", "E1", "Executor"), ("Assigned", "09:00", "E1", "Executor")])
    raw = raw.iloc[::-1]
    ev, _ = normalization.normalize_events(raw, EMPLOYEES)
    assert list(ev.event_id) == ["EV001", "EV002"]


def test_duplicate_event_quarantined_not_silently_dropped():
    raw = raw_events([("Created", "09:00", "E1", "Executor"), ("Assigned", "09:10", "E1", "Executor")])
    raw = pd.concat([raw, raw.iloc[[1]]], ignore_index=True)
    ev, q = normalization.normalize_events(raw, EMPLOYEES)
    assert len(ev) == 2
    assert list(q.quarantine_reason) == ["exact_duplicate_event"]


def test_missing_timestamp_quarantined():
    raw = raw_events([("Created", "09:00", "E1", "Executor"), ("Assigned", "09:10", "E1", "Executor")])
    raw.loc[1, "timestamp"] = None
    ev, q = normalization.normalize_events(raw, EMPLOYEES)
    assert len(ev) == 1
    assert q.quarantine_reason.iloc[0] == "missing_or_invalid_timestamp"


def test_missing_employee_kept_and_flagged_unknown():
    raw = raw_events([("Created", "09:00", "GHOST", "Executor")])
    ev, _ = normalization.normalize_events(raw, EMPLOYEES)
    assert len(ev) == 1
    assert ev.department.iloc[0] == "UNKNOWN" and ev.role.iloc[0] == "UNKNOWN"
