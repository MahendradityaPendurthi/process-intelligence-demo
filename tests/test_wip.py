"""WIP adjustment properties (SOP schema §8)."""
import pandas as pd
import pytest

from process_intel import wip

T0 = pd.Timestamp("2026-08-01 09:00")


def seg(tid, start_h, end_h, category="processing"):
    return {"ticket_id": tid, "category": category, "start": T0 + pd.Timedelta(hours=start_h),
            "end": T0 + pd.Timedelta(hours=end_h), "duration_h": end_h - start_h}


def tickets(mapping):
    return pd.DataFrame({"ticket_id": list(mapping), "assigned_employee_id": list(mapping.values())})


def test_no_overlap_equals_raw_hold():
    s = pd.DataFrame([seg("A", 0, 1), seg("B", 2, 4)])
    out = wip.wip_adjusted_hold(s, tickets({"A": "E1", "B": "E1"}))
    assert out["A"] == pytest.approx(1.0) and out["B"] == pytest.approx(2.0)


def test_overlap_split_equally_and_union_preserved():
    s = pd.DataFrame([seg("A", 0, 2), seg("B", 1, 3)])
    out = wip.wip_adjusted_hold(s, tickets({"A": "E1", "B": "E1"}))
    assert out["A"] == pytest.approx(1.5) and out["B"] == pytest.approx(1.5)
    assert out.sum() == pytest.approx(3.0)                 # union of [0,3)
    assert (out <= pd.Series({"A": 2.0, "B": 2.0})).all()  # never above raw hold


def test_different_executors_do_not_share():
    s = pd.DataFrame([seg("A", 0, 2), seg("B", 0, 2)])
    out = wip.wip_adjusted_hold(s, tickets({"A": "E1", "B": "E2"}))
    assert out["A"] == pytest.approx(2.0) and out["B"] == pytest.approx(2.0)


def test_rework_counts_and_waits_do_not():
    s = pd.DataFrame([seg("A", 0, 1), seg("A", 1, 3, "approval_wait"), seg("A", 3, 4, "rework")])
    out = wip.wip_adjusted_hold(s, tickets({"A": "E1"}))
    assert out["A"] == pytest.approx(2.0)


def test_ticket_without_hold_is_zero():
    out = wip.wip_adjusted_hold(pd.DataFrame([seg("A", 0, 1)]), tickets({"A": "E1", "Z": "E1"}))
    assert out["Z"] == 0.0
