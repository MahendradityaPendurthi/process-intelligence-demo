"""Time-windowed detectors (Phase 2): a series compared with its own previous normal months."""
import json

import numpy as np
import pandas as pd

from process_intel import deviations

MONTHS = [f"2026-0{m}" for m in range(1, 10)]


def _series(values_by_month: dict[str, list[float]], col="v"):
    return pd.DataFrame([{"m": m, col: v} for m, vs in values_by_month.items() for v in vs])


def test_window_found_with_own_baseline_and_ends_on_recovery():
    rng = np.random.default_rng(0)
    data = {m: list(rng.normal(1.0, 0.05, 20)) for m in MONTHS}
    data["2026-05"] = list(rng.normal(2.0, 0.05, 20))
    data["2026-06"] = list(rng.normal(2.0, 0.05, 20))
    runs = deviations.own_history_windows(_series(data), "m", "v", 10, lambda med, base: med >= 1.5 * base, 2)
    assert len(runs) == 1
    assert runs[0]["periods"] == ["2026-05", "2026-06"]
    assert abs(runs[0]["baseline"] - 1.0) < 0.05
    assert "2026-05" not in runs[0]["baseline_periods"]


def test_single_month_spike_and_sparse_months_are_not_windows():
    data = {m: [1.0] * 20 for m in MONTHS}
    data["2026-04"] = [3.0] * 20                   # one month only
    data["2026-07"] = [3.0] * 3                    # too few tickets to judge
    data["2026-08"] = [3.0] * 3
    assert deviations.own_history_windows(_series(data), "m", "v", 10, lambda med, base: med >= 1.5 * base, 2) == []


def test_flagged_months_do_not_raise_their_own_baseline():
    data = {m: [1.0] * 20 for m in MONTHS[:3]} | {m: [2.0] * 20 for m in MONTHS[3:]}
    runs = deviations.own_history_windows(_series(data), "m", "v", 10, lambda med, base: med >= 1.5 * base, 2)
    assert runs[0]["periods"] == MONTHS[3:] and runs[0]["baseline"] == 1.0


def _rework_frame(rates: dict[str, tuple[float, float]], n=40, tt="Invoice Verification"):
    """rates: month -> (share rejected for 'Incorrect category', share rejected for 'Amount mismatch')."""
    rows = []
    for m, (cat, amt) in rates.items():
        k_cat, k_amt = round(cat * n), round(amt * n)
        for i in range(n):
            reason = "Incorrect category" if i < k_cat else "Amount mismatch" if i < k_cat + k_amt else ""
            rows.append({"ticket_id": f"{m}-{i}", "task_type": tt, "department": "Finance", "completed_month": m,
                         "total_duration_h": 5.0, "rejection_count": int(bool(reason)), "rejection_reasons": reason})
    return pd.DataFrame(rows)


def test_reason_specific_rework_spike_detected():
    rates = {m: (0.025, 0.05) for m in MONTHS}
    rates["2026-06"] = rates["2026-07"] = (0.30, 0.05)
    rows = deviations.rework_increases(_rework_frame(rates))
    assert [r["entity_id"] for r in rows] == ["Invoice Verification:rework:Incorrect category:2026-06..2026-07"]
    assert json.loads(rows[0]["evidence"])["fisher_p_value"] < 1e-4


def test_stable_rework_not_flagged():
    assert deviations.rework_increases(_rework_frame({m: (0.05, 0.05) for m in MONTHS})) == []


def test_low_volume_month_is_not_judged_for_a_person():
    """A leave month with a handful of slow tickets must not start or extend a signal."""
    rows = []
    for m in MONTHS:
        n, ratio = (2, 2.0) if m in ("2026-05", "2026-06") else (12, 1.0)
        for i in range(n):
            rows.append({"ticket_id": f"{m}-{i}", "assigned_employee_id": "E1", "department": "HR", "completed_month": m,
                         "completed_week": m, "processing_ratio": ratio + 0.01 * i, "expected_duration_h": 2.0,
                         "rejection_count": 0, "complexity": "Simple", "reassignment_count": 0})
    assert deviations.employee_persistent_deviations(pd.DataFrame(rows)) == []
