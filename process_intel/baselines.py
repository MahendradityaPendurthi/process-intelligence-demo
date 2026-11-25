"""Stage 6: contextual historical baselines.

Two levels, most specific first:
    L2 = task_type + complexity + priority   (used when n >= MIN_BASELINE_N)
    L1 = task_type + complexity              (fallback)
Robust statistics (median, percentiles, MAD) are used throughout.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import config

LEVELS = [
    ("L2", ["task_type", "complexity", "priority"]),
    ("L1", ["task_type", "complexity"]),
]

COMPONENTS = {
    "processing_time_est_h": "median_processing_est_h",
    "executor_processing_h": "median_executor_processing_h",
    "queue_time_h": "median_queue_h",
    "approval_waiting_time_h": "median_approval_wait_h",
    "dependency_waiting_time_h": "median_dependency_wait_h",
    "rework_time_h": "median_rework_h",
}


def _mad(s: pd.Series) -> float:
    return float((s - s.median()).abs().median())


def _stats(g: pd.DataFrame) -> pd.Series:
    d = g.total_duration_h
    out = {
        "n": len(g),
        "median_duration_h": d.median(),
        "p25_duration_h": d.quantile(0.25),
        "p75_duration_h": d.quantile(0.75),
        "p90_duration_h": d.quantile(0.90),
        "mad_duration_h": _mad(d),
        **{name: g[col].median() for col, name in COMPONENTS.items()},
        "mean_rework_h": g.rework_time_h.mean(),
        "median_waiting_h": g.waiting_time_h.median(),
        "rejection_rate": (g.rejection_count > 0).mean(),
        "rework_rate": (g.rework_cycles > 0).mean(),
        "sla_rate": g.sla_met.astype(float).mean(),
    }
    return pd.Series(out)


def build_baselines(features: pd.DataFrame) -> pd.DataFrame:
    done = features[features.total_duration_h.notna()]
    period = f"{done.completed_at.min():%Y-%m-%d}..{done.completed_at.max():%Y-%m-%d}"
    frames = []
    for level, keys in LEVELS:
        b = done.groupby(keys).apply(_stats).reset_index()
        b["baseline_level"] = level
        b["group_keys"] = "+".join(keys)
        for k in ["task_type", "complexity", "priority"]:
            if k not in b:
                b[k] = "ALL"
        b["sufficient_n"] = b.n >= config.MIN_BASELINE_N
        frames.append(b)
    out = pd.concat(frames, ignore_index=True)
    out["baseline_id"] = (config.BASELINE_VERSION + ":" + out.baseline_level + ":" + out.task_type + ":"
                          + out.complexity + ":" + out.priority)
    out["baseline_version"] = config.BASELINE_VERSION
    out["data_period"] = period
    out["n"] = out.n.astype(int)
    front = ["baseline_id", "baseline_version", "baseline_level", "group_keys", "task_type", "complexity",
             "priority", "n", "sufficient_n", "data_period"]
    return out[front + [c for c in out.columns if c not in front]].round(4)


def attach_baselines(features: pd.DataFrame, baselines: pd.DataFrame) -> pd.DataFrame:
    """Give every ticket its most specific sufficient baseline and the ratios against it."""
    f = features.copy()
    usable = baselines[baselines.sufficient_n]
    l2 = usable[usable.baseline_level == "L2"].set_index(["task_type", "complexity", "priority"])
    l1 = usable[usable.baseline_level == "L1"].set_index(["task_type", "complexity"])

    def pick(row):
        k2 = (row.task_type, row.complexity, row.priority)
        if k2 in l2.index:
            return l2.loc[k2]
        k1 = (row.task_type, row.complexity)
        if k1 in l1.index:
            return l1.loc[k1]
        return None

    picked = [pick(r) for r in f.itertuples(index=False)]
    cols = ["baseline_id", "median_duration_h", "p75_duration_h", "p90_duration_h", *COMPONENTS.values()]
    rows = [p[cols] if p is not None else pd.Series({c: np.nan for c in cols}) for p in picked]
    b = pd.DataFrame(rows).reset_index(drop=True)
    b.columns = ["baseline_id", "expected_duration_h", "baseline_p75_h", "baseline_p90_h",
                 *[f"expected_{c.removeprefix('median_')}" for c in COMPONENTS.values()]]
    f = pd.concat([f.reset_index(drop=True), b], axis=1)
    f["duration_ratio"] = (f.total_duration_h / f.expected_duration_h).round(4)
    # Executor processing outside rework, vs the same task-type baseline (rework is tracked separately).
    f["processing_ratio"] = (f.executor_processing_h / f.expected_executor_processing_h.replace(0, np.nan)).round(4)
    f["above_p90"] = f.total_duration_h > f.baseline_p90_h
    return f


def build_stage_baselines(features: pd.DataFrame) -> pd.DataFrame:
    """Org-wide decision-wait baselines per approver stage and declared dependency count."""
    done = features[features.total_duration_h.notna()]
    rows = []
    for stage, col in [("Incharge", "pre_decision_wait_h"), ("Lead", "decision_wait_lead_h")]:
        sub = done[done[col] > 0] if stage != "Incharge" else done
        for dep, g in sub.groupby("dependency_count"):
            rows.append({"stage": stage, "dependency_count": int(dep), "n": len(g),
                         "median_wait_h": g[col].median(), "p90_wait_h": g[col].quantile(0.9)})
    return pd.DataFrame(rows).round(4)
