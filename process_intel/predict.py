"""Time prediction: P50 / P90 duration and SLA-miss risk for a ticket, at the moment it is created.

Only facts known at creation are used:
    the ticket       task type, department, priority, complexity, SLA hours, SOP expectations
    the clock        hour of day, weekday, hours left in the working day
    the load now     open tickets in the department, open tickets of the assignee (a count: the
                     assignee's identity is NOT a feature, so the model learns no per-person speed)
    recent history   median duration / approval wait / late rate of tickets that FINISHED in the
                     14 days before this one was created (captures slowdowns as they happen)

Models: gradient-boosted trees (scikit-learn HistGradientBoosting), quantile loss on log hours for
P50 and P90, a classifier for SLA miss. Evaluation is walk-forward: each test month is predicted by a
model trained only on tickets completed before that month started.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor
from sklearn.metrics import brier_score_loss, roc_auc_score

CATEGORICAL = ["task_type", "department", "priority", "complexity"]
NUMERIC = ["sla_hours", "sop_expected_elapsed_h", "sop_p90_h", "sop_required_approvals", "dependency_count",
           "created_hour", "created_weekday", "hours_left_in_day", "dept_open", "assignee_open",
           "tt_recent_median_h", "tt_recent_n", "dept_recent_appr_wait_h", "dept_recent_late_rate"]
FEATURES = CATEGORICAL + NUMERIC
RECENT_DAYS = 14
DAY_END_HOUR = 18
QUANTILES = {"p50": 0.5, "p90": 0.9}
PARAMS = {"max_iter": 300, "learning_rate": 0.05, "max_leaf_nodes": 15, "min_samples_leaf": 20,
          "l2_regularization": 1.0, "random_state": 0}
# late tickets are rare (~5%): a smaller, more regularised classifier gives honest probabilities
RISK_PARAMS = {**PARAMS, "max_iter": 150, "min_samples_leaf": 60, "max_leaf_nodes": 7}
CALIBRATION_DAYS = 60        # P90 is shifted so that 90% of the most recent 60 days of training tickets fit


# ------------------------------------------------------------------ features
def _open_at(created: np.ndarray, completed: np.ndarray, at: np.ndarray) -> np.ndarray:
    """Tickets created before `at` and not yet completed at `at` (both known at time `at`)."""
    c, d = np.sort(created), np.sort(completed)
    return np.searchsorted(c, at, side="left") - np.searchsorted(d, at, side="right")


def _recent(at: np.ndarray, done: np.ndarray, values: np.ndarray, fn, days=RECENT_DAYS) -> tuple:
    """fn(values of tickets completed in [at - days, at)) for each `at`; NaN when none."""
    order = np.argsort(done)
    done, values = done[order], values[order]
    lo = np.searchsorted(done, at - np.timedelta64(days, "D"), side="left")
    hi = np.searchsorted(done, at, side="left")
    out = np.array([fn(values[a:b]) if b > a else np.nan for a, b in zip(lo, hi)], dtype=float)
    return out, (hi - lo).astype(float)


def build_features(f: pd.DataFrame) -> pd.DataFrame:
    """One row per closed ticket: creation-time features + targets (duration_h, late)."""
    x = f[f.is_closed & f.total_duration_h.notna()].copy()
    x["created_at"] = pd.to_datetime(x.created_at)
    x["completed_at"] = pd.to_datetime(x.completed_at)
    x["duration_h"] = x.total_duration_h
    x["late"] = (~x.sla_met.astype(bool)).astype(int)
    x["created_hour"] = x.created_at.dt.hour + x.created_at.dt.minute / 60
    x["created_weekday"] = x.created_at.dt.weekday
    x["hours_left_in_day"] = (DAY_END_HOUR - x.created_hour).clip(lower=0)
    x["dept_open"] = 0.0
    x["assignee_open"] = 0.0
    for col, key in (("dept_open", "department"), ("assignee_open", "assigned_employee_id")):
        for _, g in x.groupby(key):
            x.loc[g.index, col] = _open_at(g.created_at.values, g.completed_at.values, g.created_at.values)
    for tt, g in x.groupby("task_type"):
        med, n = _recent(g.created_at.values, g.completed_at.values, g.duration_h.values, np.median)
        x.loc[g.index, "tt_recent_median_h"], x.loc[g.index, "tt_recent_n"] = med, n
    for _, g in x.groupby("department"):
        w, _n = _recent(g.created_at.values, g.completed_at.values, g.approval_waiting_time_h.values, np.median)
        late, _n = _recent(g.created_at.values, g.completed_at.values, g.late.values, np.mean)
        x.loc[g.index, "dept_recent_appr_wait_h"], x.loc[g.index, "dept_recent_late_rate"] = w, late
    for c in CATEGORICAL:
        x[c] = x[c].astype("category")
    x["month"] = x.created_at.dt.to_period("M").astype(str)
    return x.sort_values("created_at").reset_index(drop=True)


# ------------------------------------------------------------------ models
def _fit_models(train: pd.DataFrame) -> dict:
    X, y = train[FEATURES], np.log1p(train.duration_h)
    models = {k: HistGradientBoostingRegressor(loss="quantile", quantile=q, categorical_features="from_dtype",
                                               **PARAMS).fit(X, y) for k, q in QUANTILES.items()}
    models["late"] = HistGradientBoostingClassifier(categorical_features="from_dtype", **RISK_PARAMS).fit(
        X, train.late)
    models["p90_shift"] = 0.0
    return models


def fit(train: pd.DataFrame) -> dict:
    """Fit the models; calibrate P90 on the most recent tickets (conformalised quantile regression).

    A model fitted without the last CALIBRATION_DAYS predicts those tickets; the log-scale shift that makes
    90% of them fall under P90 is then applied to the model refitted on all training tickets.
    """
    cut = train.completed_at.max() - pd.Timedelta(days=CALIBRATION_DAYS)
    early, recent = train[train.completed_at < cut], train[train.created_at >= cut]
    shift = 0.0
    if len(early) >= 200 and len(recent) >= 50:
        m = _fit_models(early)
        resid = np.log1p(recent.duration_h) - m["p90"].predict(recent[FEATURES])
        shift = float(np.quantile(resid, QUANTILES["p90"]))
    models = _fit_models(train)
    models["p90_shift"] = shift
    return models


def predict(models: dict, x: pd.DataFrame) -> pd.DataFrame:
    X = x[FEATURES]
    p50 = np.expm1(models["p50"].predict(X))
    p90 = np.maximum(np.expm1(models["p90"].predict(X) + models["p90_shift"]), p50)
    return pd.DataFrame({"pred_p50_h": p50, "pred_p90_h": p90,
                         "pred_late_prob": models["late"].predict_proba(X)[:, 1]}, index=x.index)


def baselines(train: pd.DataFrame, test: pd.DataFrame) -> pd.DataFrame:
    """Segment (task type x priority) median / P90 / late rate from the training months; SOP estimates."""
    seg = (train.groupby(["task_type", "priority"], observed=True)
           .agg(seg_p50_h=("duration_h", "median"), seg_p90_h=("duration_h", lambda s: s.quantile(0.9)),
                seg_late_rate=("late", "mean")).reset_index())
    b = test[["task_type", "priority"]].merge(seg, on=["task_type", "priority"], how="left")
    b.index = test.index
    b["sop_p50_h"], b["sop_p90_h"] = test.sop_expected_elapsed_h, test.sop_p90_h
    return b.drop(columns=["task_type", "priority"])


def walk_forward(x: pd.DataFrame, test_months: list[str]) -> pd.DataFrame:
    out = []
    for m in test_months:
        start = pd.Period(m, "M").start_time
        train = x[x.completed_at < start]
        test = x[x.month == m]
        if test.empty or len(train) < 200:
            continue
        p = predict(fit(train), test).join(baselines(train, test))
        out.append(test[["ticket_id", "month", "task_type", "department", "priority", "sla_hours", "duration_h",
                         "late"]].join(p).assign(train_tickets=len(train)))
    return pd.concat(out, ignore_index=True)


# ------------------------------------------------------------------ evaluation
def _pinball(y, q, tau):
    d = y - q
    return float(np.mean(np.maximum(tau * d, (tau - 1) * d)))


def duration_metrics(p: pd.DataFrame, p50: str, p90: str) -> dict:
    y = p.duration_h
    return {"p50_mae_h": round(float((y - p[p50]).abs().mean()), 3),
            "p50_median_abs_pct_err": round(float(((y - p[p50]).abs() / y).median()), 3),
            "p90_coverage": round(float((y <= p[p90]).mean()), 3),
            "p90_pinball": round(_pinball(y, p[p90], 0.9), 3),
            "p50_pinball": round(_pinball(y, p[p50], 0.5), 3)}


def risk_metrics(p: pd.DataFrame, col: str) -> dict:
    y, s = p.late, p[col].fillna(p[col].mean())
    k = max(1, int(round(0.1 * len(p))))
    top = s.sort_values(ascending=False).index[:k]
    out = {"late_share": round(float(y.mean()), 3), "brier": round(float(brier_score_loss(y, s)), 4),
           "top10pct_precision": round(float(y.loc[top].mean()), 3),
           "top10pct_recall": round(float(y.loc[top].sum() / max(y.sum(), 1)), 3)}
    out["auc"] = round(float(roc_auc_score(y, s)), 3) if y.nunique() == 2 else None
    return out


def calibration(p: pd.DataFrame, col="pred_late_prob", bins=(0, .05, .1, .2, .4, 1.0001)) -> pd.DataFrame:
    b = pd.cut(p[col], bins, right=False)
    return (p.groupby(b, observed=True).agg(tickets=("late", "size"), mean_predicted=(col, "mean"),
                                            observed_late=("late", "mean")).round(3).reset_index()
            .rename(columns={col: "risk_band"}))


def evaluate(p: pd.DataFrame) -> dict:
    res = {"tickets": len(p), "months": sorted(p.month.unique())}
    res["duration"] = {"model": duration_metrics(p, "pred_p50_h", "pred_p90_h"),
                       "segment_baseline": duration_metrics(p.dropna(subset=["seg_p50_h"]), "seg_p50_h", "seg_p90_h"),
                       "sop_estimate": duration_metrics(p.dropna(subset=["sop_p50_h"]), "sop_p50_h", "sop_p90_h")}
    res["sla_risk"] = {"model": risk_metrics(p, "pred_late_prob"),
                       "segment_baseline": risk_metrics(p, "seg_late_rate")}
    res["by_month"] = {m: {"tickets": len(g), **duration_metrics(g, "pred_p50_h", "pred_p90_h"),
                           "seg_p90_coverage": duration_metrics(g.dropna(subset=["seg_p50_h"]), "seg_p50_h",
                                                                "seg_p90_h")["p90_coverage"],
                           "late_share": round(float(g.late.mean()), 3),
                           "auc": risk_metrics(g, "pred_late_prob")["auc"]}
                       for m, g in p.groupby("month")}
    return res


def feature_importance(models: dict, x: pd.DataFrame, n_repeats: int = 5) -> pd.DataFrame:
    """Permutation importance on the P50 model (which inputs move the prediction), for the model card."""
    from sklearn.inspection import permutation_importance
    X, y = x[FEATURES], np.log1p(x.duration_h)
    r = permutation_importance(models["p50"], X, y, n_repeats=n_repeats, random_state=0,
                               scoring="neg_mean_absolute_error")
    return (pd.DataFrame({"feature": FEATURES, "importance": r.importances_mean})
            .sort_values("importance", ascending=False).round(4))
