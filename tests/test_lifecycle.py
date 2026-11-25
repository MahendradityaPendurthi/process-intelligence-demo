import pytest

from process_intel import lifecycle
from tests.conftest import normalized

HAPPY = [
    ("Created", "09:00", "E1", "Executor"),
    ("Assigned", "09:10", "E1", "Executor"),
    ("Updated", "09:40", "E1", "Executor", "field_change", "normal edit"),
    ("Submitted", "10:10", "E1", "Executor"),
    ("DependencyWait", "10:30", "E1", "Executor", "dependency", "Waiting"),
    ("Approved", "11:30", "M1", "Incharge"),
    ("Approved", "13:00", "L1", "Lead", "final_review"),
]


def rebuild(rows):
    lc, segs = lifecycle.reconstruct_ticket(normalized(rows))
    return lc, segs


def test_happy_path_durations_and_attribution():
    lc, segs = rebuild(HAPPY)
    assert lc["lifecycle_span_h"] == pytest.approx(4.0)
    assert lc["queue_h"] == pytest.approx(10 / 60)
    assert lc["processing_h"] == pytest.approx(1.0)               # 09:10 -> 10:10
    assert lc["approval_wait_h"] == pytest.approx(20 / 60 + 1.5)  # submit->depwait, incharge approve->lead
    assert lc["dependency_wait_h"] == pytest.approx(1.0)
    assert lc["decision_wait_incharge_h"] == pytest.approx(20 / 60 + 1.0)
    assert lc["decision_wait_lead_h"] == pytest.approx(1.5)
    total = sum(lc[f"{c}_h"] for c in lifecycle.CATEGORIES)
    assert total == pytest.approx(lc["lifecycle_span_h"])
    assert lc["rejection_count"] == 0 and lc["rework_cycles"] == 0
    assert lc["approval_events"] == 2
    assert lc["closure_type"] == "final_approval" and lc["is_closed"]
    assert lc["stages_visited"] == "Executor>Incharge>Lead"
    assert lc["stage_transitions"] == "Executor>Incharge|Incharge>Lead"
    assert len(segs) == len(HAPPY) - 1


def test_single_event_ticket():
    lc, segs = rebuild([("Created", "09:00", "E1", "Executor")])
    assert lc["event_count"] == 1 and segs == []
    assert lc["lifecycle_span_h"] == 0
    assert "single_event" in lc["anomalies"] and "not_closed" in lc["anomalies"]


def test_multiple_rejections_and_resubmissions():
    rows = [
        ("Created", "09:00", "E1", "Executor"),
        ("Assigned", "09:05", "E1", "Executor"),
        ("Submitted", "09:30", "E1", "Executor"),
        ("Rejected", "10:00", "M1", "Incharge", "rejection_reason", "Amount mismatch"),
        ("Updated", "10:30", "E1", "Executor", "correction", "Amount mismatch"),
        ("Resubmitted", "10:45", "E1", "Executor"),
        ("Rejected", "11:00", "M1", "Incharge", "rejection_reason", "Wrong quantity"),
        ("Updated", "11:20", "E1", "Executor", "correction", "Wrong quantity"),
        ("Resubmitted", "11:30", "E1", "Executor"),
        ("Approved", "12:00", "M1", "Incharge"),
    ]
    lc, _ = rebuild(rows)
    assert lc["rejection_count"] == 2
    assert lc["resubmission_count"] == 2
    assert lc["rework_cycles"] == 2
    assert lc["correction_count"] == 2
    assert lc["rework_h"] == pytest.approx((45 + 30) / 60)  # 10:00->10:45 and 11:00->11:30
    assert lc["rejection_reasons"] == "Amount mismatch|Wrong quantity"
    assert lc["stage_transitions"].count("Incharge>Executor") == 2


def test_reopened_ticket_resets_closure():
    rows = [
        ("Created", "09:00", "E1", "Executor"),
        ("Assigned", "09:05", "E1", "Executor"),
        ("Submitted", "09:30", "E1", "Executor"),
        ("Approved", "10:00", "M1", "Incharge"),
        ("Closed", "10:05", "M1", "Incharge"),
        ("Reopened", "11:00", "M1", "Incharge"),
        ("Submitted", "11:30", "E1", "Executor"),
        ("Approved", "12:00", "M1", "Incharge"),
    ]
    lc, segs = rebuild(rows)
    assert lc["reopen_count"] == 1
    assert lc["closure_type"] == "final_approval"
    post = [s for s in segs if s["category"] == "post_closure"]
    assert len(post) == 1 and post[0]["duration_h"] == pytest.approx(55 / 60)


def test_reassignment_and_escalation_counted():
    rows = [
        ("Created", "09:00", "E1", "Executor"),
        ("Assigned", "09:05", "E1", "Executor"),
        ("Reassigned", "09:30", "E1", "Executor"),
        ("Submitted", "10:00", "E1", "Executor"),
        ("Escalated", "10:30", "M1", "Incharge"),
        ("Approved", "11:00", "L1", "Lead"),
    ]
    lc, _ = rebuild(rows)
    assert lc["reassignment_count"] == 1 and lc["escalation_count"] == 1
    assert lc["decision_wait_lead_h"] == pytest.approx(1.0)


def test_missing_optional_events_flagged_not_failed():
    lc, _ = rebuild([("Submitted", "10:00", "E1", "Executor"), ("Approved", "11:00", "M1", "Incharge")])
    assert "missing_created_event" in lc["anomalies"]
    assert "missing_assigned_event" in lc["anomalies"]
    assert lc["approval_wait_h"] == pytest.approx(1.0)


def test_reconstruct_all_handles_many_tickets():
    import pandas as pd
    ev = pd.concat([normalized(HAPPY, "T1"), normalized(HAPPY[:3], "T2")])
    lcs, segs = lifecycle.reconstruct_all(ev)
    assert list(lcs.ticket_id) == ["T1", "T2"]
    assert lcs.set_index("ticket_id").loc["T2", "is_closed"] == False  # noqa: E712
