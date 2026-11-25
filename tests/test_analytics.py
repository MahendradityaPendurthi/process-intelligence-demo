"""Features, SLA, baselines and deviation detection on small hand-built datasets."""
import json

import numpy as np
import pandas as pd
import pytest

from process_intel import baselines, deviations, features, ingestion, lifecycle, metrics
from tests.conftest import EMPLOYEES, normalized

BASE_ROWS = [
    ("Created", "09:00", "E1", "Executor"),
    ("Assigned", "09:10", "E1", "Executor"),
    ("Submitted", "10:10", "E1", "Executor"),
    ("Approved", "11:00", "M1", "Incharge"),
]


def ticket_row(tid, created="2026-08-01 09:00:00", completed="2026-08-01 11:00:00", due="2026-08-01 21:00:00",
               task_type="Expense Approval", complexity="Simple", priority="Low", dep=0, emp="E1"):
    return {"ticket_id": tid, "task_type": task_type, "department": "Finance", "assigned_employee_id": emp,
            "priority": priority, "complexity": complexity, "sop_steps": "3", "approval_count": "1",
            "dependency_count": str(dep), "created_at": created, "due_at": due, "completed_at": completed,
            "final_status": "Completed" if completed <= due else "Completed_Late"}


def build(tickets_rows, events):
    lcs, _ = lifecycle.reconstruct_all(events)
    return features.build_ticket_features(pd.DataFrame(tickets_rows), lcs)


def test_duration_and_sla_met():
    f = build([ticket_row("T1")], normalized(BASE_ROWS, "T1"))
    r = f.iloc[0]
    assert r.total_duration_h == pytest.approx(2.0)
    assert r.sla_met == True  # noqa: E712
    assert r.sla_delay_h == 0
    assert not r.duration_source_mismatch


def test_sla_breach_delay():
    f = build([ticket_row("T1", due="2026-08-01 10:30:00")], normalized(BASE_ROWS, "T1"))
    r = f.iloc[0]
    assert r.sla_met == False  # noqa: E712
    assert r.sla_delay_h == pytest.approx(0.5)


def _synthetic_features(n=30, slow_ids=(), slow_extra_h=0.0):
    """n identical tickets of one task type; selected tickets get extra approval wait."""
    rows, evs = [], []
    for i in range(n):
        tid = f"T{i:03d}"
        extra = slow_extra_h if tid in slow_ids else 0.0
        approve = pd.Timestamp("2026-08-01 11:00") + pd.Timedelta(hours=extra)
        rows.append(ticket_row(tid, completed=f"{approve:%Y-%m-%d %H:%M:%S}", due="2026-08-02 09:00:00"))
        evrows = BASE_ROWS[:3] + [("Approved", f"{approve:%H:%M}", "M1", "Incharge")]
        evs.append(normalized(evrows, tid))
    f = build(rows, pd.concat(evs))
    b = baselines.build_baselines(f)
    return baselines.attach_baselines(f, b), b


def test_baseline_uses_robust_median_and_falls_back_to_l1():
    f, b = _synthetic_features(n=30, slow_ids={"T000"}, slow_extra_h=8)
    l1 = b[b.baseline_level == "L1"].iloc[0]
    assert l1.n == 30
    assert l1.median_duration_h == pytest.approx(2.0)   # one outlier does not move the median
    assert l1.mad_duration_h == pytest.approx(0.0)
    assert f.baseline_id.str.contains(":L2:").all()     # 30 >= MIN_BASELINE_N in the single priority group


def test_insufficient_group_falls_back(monkeypatch):
    monkeypatch.setattr("process_intel.config.MIN_BASELINE_N", 50)
    f, b = _synthetic_features(n=30)
    assert f.baseline_id.isna().all()  # neither level has 50 tickets -> no baseline, not a fake one


def test_ticket_deviation_attributes_excess_to_approval_wait():
    f, _ = _synthetic_features(n=30, slow_ids={"T005"}, slow_extra_h=3)
    rows = deviations.ticket_deviations(f)
    assert len(rows) == 1
    d = rows[0]
    assert d["entity_id"] == "T005"
    assert d["ratio"] == pytest.approx(2.5)
    assert d["classification"] == "process"
    assert d["dominant_cause"].startswith("Approval wait at Incharge")
    assert d["confidence"] == "high"
    assert d["source_event_ids"].count("EV") == 4
    ev = json.loads(d["evidence"])
    assert ev["context"]["leave"].startswith("leave/absence data not available")


def test_within_baseline_ticket_not_flagged():
    f, _ = _synthetic_features(n=30)
    assert deviations.ticket_deviations(f) == []


def _employee_frame(ratios_by_month: dict[str, list[float]], emp="E1", dept="Finance", peers_ratio=1.0):
    """Minimal feature frame for the persistence detector."""
    rows = []
    for month, ratios in ratios_by_month.items():
        for i, r in enumerate(ratios):
            rows.append({"ticket_id": f"{emp}-{month}-{i}", "assigned_employee_id": emp, "department": dept,
                         "completed_month": month, "completed_week": month, "processing_ratio": r,
                         "expected_duration_h": 2.0, "rejection_count": 0, "complexity": "Simple",
                         "reassignment_count": 0})
            rows.append({"ticket_id": f"P-{month}-{i}", "assigned_employee_id": "P1", "department": dept,
                         "completed_month": month, "completed_week": month, "processing_ratio": peers_ratio,
                         "expected_duration_h": 2.0, "rejection_count": 0, "complexity": "Simple",
                         "reassignment_count": 0})
    return pd.DataFrame(rows)


def test_persistent_unexplained_decline_detected():
    f = _employee_frame({"2026-06": [1.0] * 6, "2026-07": [1.0] * 6, "2026-08": [1.4] * 6, "2026-09": [1.6] * 6})
    rows = deviations.employee_persistent_deviations(f)
    assert [r["entity_id"] for r in rows] == ["E1"]
    assert rows[0]["deviation_type"] == "PERSISTENT_UNEXPLAINED_PROCESSING_INCREASE"
    assert "Manager review recommended" in rows[0]["recommended_investigation"]
    assert "underperform" not in json.dumps(rows[0]).lower()


def test_single_bad_month_is_not_persistent():
    f = _employee_frame({"2026-06": [1.0] * 6, "2026-07": [1.0] * 6, "2026-08": [1.0] * 6, "2026-09": [1.8] * 6})
    assert deviations.employee_persistent_deviations(f) == []


def test_stable_elevated_level_is_not_a_decline():
    f = _employee_frame({m: [1.4] * 6 for m in ["2026-06", "2026-07", "2026-08", "2026-09"]})
    assert deviations.employee_persistent_deviations(f) == []


def test_team_wide_slowdown_is_context_not_individual():
    f = _employee_frame({"2026-06": [1.0] * 6, "2026-07": [1.0] * 6, "2026-08": [1.4] * 6, "2026-09": [1.6] * 6},
                        peers_ratio=1.0)
    recent = f.completed_month.isin(["2026-08", "2026-09"]) & (f.assigned_employee_id == "P1")
    f.loc[recent, "processing_ratio"] = 1.5
    rows = deviations.employee_persistent_deviations(f)
    assert rows[0]["deviation_type"] == "PERSISTENT_PROCESSING_INCREASE_WITH_CONTEXT"
    assert "team_wide_trend" in rows[0]["explanation"]


def test_validation_flags_orphans_and_duplicates(employees):
    tickets = pd.DataFrame([ticket_row("T1"), ticket_row("T1"), ticket_row("T2", emp="GHOST")])
    from tests.conftest import raw_events
    audit = pd.concat([raw_events(BASE_ROWS, "T1"), raw_events(BASE_ROWS[:1], "T9")], ignore_index=True)
    audit["event_id"] = [f"EV{i}" for i in range(len(audit))]
    task_types = pd.DataFrame([{"task_type": "Expense Approval", "department": "Finance", "complexity": "Simple",
                                "sop_steps": "3", "approval_count": "1", "dependency_count": "0"}])
    dq = ingestion.validate({"employees": employees, "tickets": tickets, "audit_logs": audit,
                             "task_types": task_types}).set_index("check")
    assert dq.loc["unique:ticket_id", "status"] == "fail"
    assert dq.loc["fk:assigned_employee_id->employees", "affected_rows"] == 1
    assert dq.loc["fk:ticket_id->tickets", "affected_rows"] == 1
    assert dq.loc["tickets_without_events", "affected_rows"] == 1  # T2


def test_employee_metrics_use_complexity_weighted_effort():
    f, _ = _synthetic_features(n=30)
    m = metrics.employee_metrics(f, EMPLOYEES)
    overall = m[(m.period_type == "overall")].iloc[0]
    assert overall.tickets_completed == 30
    assert overall.expected_effort_h == pytest.approx(30 * 2.0)
    assert np.isclose(overall.median_duration_ratio, 1.0)
