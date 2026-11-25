"""Time prediction: no future information in the features, walk-forward split, sane output."""
import numpy as np
import pandas as pd
import pytest

from process_intel import config, predict


def _features(n=900, seed=0):
    rng = np.random.default_rng(seed)
    created = pd.Timestamp("2026-01-01 09:00") + pd.to_timedelta(np.sort(rng.uniform(0, 180 * 24, n)), unit="h")
    tt = rng.choice(["A", "B", "C"], n)
    dur = np.where(tt == "A", 3, np.where(tt == "B", 6, 10)) * np.exp(rng.normal(0, 0.3, n))
    prio = rng.choice(["High", "Medium", "Low"], n)
    sla = pd.Series(prio).map(config.SLA_HOURS).values
    return pd.DataFrame({
        "ticket_id": [f"T{i}" for i in range(n)], "task_type": tt, "department": np.where(tt == "C", "X", "Y"),
        "assigned_employee_id": rng.choice(["E1", "E2", "E3"], n), "priority": prio, "complexity": "Medium",
        "created_at": created.astype(str), "completed_at": (created + pd.to_timedelta(dur, unit="h")).astype(str),
        "total_duration_h": dur, "is_closed": True, "sla_met": dur <= sla, "sla_hours": sla,
        "approval_waiting_time_h": dur / 3, "sop_expected_elapsed_h": 5.0, "sop_p90_h": 8.0,
        "sop_required_approvals": 2, "dependency_count": 0})


@pytest.fixture(scope="module")
def x():
    return predict.build_features(_features())


def test_recent_history_uses_only_tickets_finished_before_creation(x):
    row = x.iloc[600]
    same = x[(x.task_type == row.task_type) & (x.completed_at < row.created_at)
             & (x.completed_at >= row.created_at - pd.Timedelta(days=predict.RECENT_DAYS))]
    assert row.tt_recent_n == len(same)
    assert row.tt_recent_median_h == pytest.approx(same.duration_h.median())


def test_open_count_is_known_at_creation(x):
    row = x.iloc[500]
    d = x[x.department == row.department]
    expected = ((d.created_at < row.created_at) & (d.completed_at > row.created_at)).sum()
    assert row.dept_open == expected


def test_assignee_identity_is_not_a_feature():
    assert "assigned_employee_id" not in predict.FEATURES


def test_walk_forward_trains_only_on_completed_tickets(x):
    m = sorted(x.month.unique())[-1]
    p = predict.walk_forward(x, [m])
    start = pd.Period(m, "M").start_time
    assert p.train_tickets.iloc[0] == (x.completed_at < start).sum()
    assert set(p.month) == {m}
    assert (p.pred_p90_h >= p.pred_p50_h).all() and p.pred_late_prob.between(0, 1).all()


def test_model_learns_the_task_type_and_evaluation_runs(x):
    months = sorted(x.month.unique())[-2:]
    p = predict.walk_forward(x, months)
    by_tt = p.groupby("task_type", observed=True).pred_p50_h.median()
    assert by_tt["A"] < by_tt["B"] < by_tt["C"]
    res = predict.evaluate(p)
    assert res["duration"]["model"]["p50_median_abs_pct_err"] < 0.35
    assert 0.75 <= res["duration"]["model"]["p90_coverage"] <= 1.0
