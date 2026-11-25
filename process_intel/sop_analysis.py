"""Stage 4 (SOP part): compare SOP expectations with what the logs show.

    attach_sop_priors()   per-ticket SOP band (C7) and component expectations
    task_type_analysis()  SOP vs actual per task type          -> sop_time_complexity.csv
    effort_coverage()     task type x month, aggregated only     -> sop_effort_coverage.csv
    cs_rank_correlation() Spearman rho of CS vs observed median elapsed time

Only comparisons allowed by schema §7.3 are made. SOP effort is never compared
with an individual ticket's or employee's hold time.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import config, sop

PRIOR_COLUMNS = {
    "e_elapsed_h": "sop_expected_elapsed_h", "p10_h": "sop_p10_h", "p90_h": "sop_p90_h",
    "e_effort_exec_h": "sop_effort_exec_h", "exp_queue_h": "sop_exp_queue_h",
    "exp_first_decision_h": "sop_exp_first_decision_h", "exp_lead_decision_h": "sop_exp_lead_decision_h",
    "required_approvals": "sop_required_approvals", "required_stages": "sop_required_stages",
    "estimate_flags": "sop_estimate_flags",
}


def attach_sop_priors(f: pd.DataFrame, sops: dict[str, dict], wip_hold: pd.Series) -> pd.DataFrame:
    f = f.copy()
    f["sop_id"] = f.task_type.map({t: d["sop_id"] for t, d in sops.items()})
    f["sop_version"] = f.task_type.map({t: d["version"] for t, d in sops.items()})
    priors = [sop.ticket_prior(sops, r.task_type, r.approval_count, r.dependency_count) or {}
              for r in f.itertuples(index=False)]
    p = pd.DataFrame(priors, index=f.index).rename(columns=PRIOR_COLUMNS)
    for col in PRIOR_COLUMNS.values():
        f[col] = p[col] if col in p else np.nan
    f["sop_elapsed_ratio"] = (f.total_duration_h / f.sop_expected_elapsed_h).round(4)
    f["sop_band"] = np.select(
        [f.sop_expected_elapsed_h.isna() | f.total_duration_h.isna(),
         f.total_duration_h < f.sop_p10_h, f.total_duration_h > f.sop_p90_h],
        ["n/a", "below_p10", "above_p90"], default="within")
    f["executor_hold_wip_adj_h"] = f.ticket_id.map(wip_hold).fillna(0.0)
    return f


def effort_coverage(f: pd.DataFrame) -> pd.DataFrame:
    """Schema §8. Rows with n below the minimum are kept and flagged, never dropped."""
    done = f[f.total_duration_h.notna() & f.sop_effort_exec_h.notna()]
    g = done.groupby(["task_type", "sop_id", "completed_month"])
    out = g.agg(n=("ticket_id", "size"), median_wip_adj_hold_h=("executor_hold_wip_adj_h", "median"),
                median_raw_hold_h=("processing_time_est_h", "median"),
                sop_effort_exec_h=("sop_effort_exec_h", "first")).reset_index()
    ok = out.n >= config.EFFORT_COVERAGE_MIN_N
    out["effort_coverage"] = np.where(ok, out.sop_effort_exec_h / out.median_wip_adj_hold_h.replace(0, np.nan), np.nan)
    out["coverage_flag"] = np.select(
        [~ok, out.effort_coverage > config.EFFORT_COVERAGE_HIGH, out.effort_coverage < config.EFFORT_COVERAGE_LOW],
        ["insufficient_n", "standard_exceeds_hold", "low_coverage"], default="plausible")
    return out.round(4)


def task_type_analysis(f: pd.DataFrame, params: pd.DataFrame, coverage: pd.DataFrame) -> pd.DataFrame:
    done = f[f.total_duration_h.notna()]
    rows = []
    for p in params.itertuples(index=False):
        g = done[done.task_type == p.task_type]
        if g.empty:
            continue
        lead = g.decision_wait_lead_h[g.decision_wait_lead_h > 0]
        cov = coverage[(coverage.task_type == p.task_type) & (coverage.coverage_flag != "insufficient_n")]
        flags = cov.coverage_flag.value_counts()
        rej = (g.rejection_count > 0).mean()
        rows.append({
            "task_type": p.task_type, "sop_id": p.sop_id, "cs": p.cs, "complexity_derived": p.complexity_derived,
            "complexity_declared": p.complexity_declared, "complexity_match": p.complexity_match, "tickets": len(g),
            "observed_median_h": g.total_duration_h.median(), "observed_p90_h": g.total_duration_h.quantile(0.9),
            "sop_expected_elapsed_h": p.e_elapsed_h, "sop_p10_h": p.p10_h, "sop_p90_h": p.p90_h,
            "median_actual_to_sop": g.total_duration_h.median() / p.e_elapsed_h,
            "share_below_p10": (g.sop_band == "below_p10").mean(),
            "share_within": (g.sop_band == "within").mean(),
            "share_above_p90": (g.sop_band == "above_p90").mean(),
            "actual_median_queue_h": g.queue_time_h.median(), "sop_exp_queue_h": p.exp_queue_h,
            "actual_median_first_decision_h": g.pre_decision_wait_h.median(),
            "sop_exp_first_decision_h": p.exp_first_decision_h,
            "actual_median_lead_decision_h": lead.median() if len(lead) else 0.0,
            "sop_exp_lead_decision_h": p.exp_lead_decision_h,
            "sop_exp_hod_decision_h": p.exp_hod_decision_h,
            "median_wip_adj_hold_h": g.executor_hold_wip_adj_h.median(), "sop_effort_exec_h": p.e_effort_exec_h,
            "effort_coverage_overall": p.e_effort_exec_h / g.executor_hold_wip_adj_h.median()
            if g.executor_hold_wip_adj_h.median() > 0 else np.nan,
            "coverage_months_flagged": "; ".join(f"{k}:{v}" for k, v in flags.items()),
            "observed_rejection_rate": rej, "sop_expected_rejection_rate": p.expected_rejection_rate,
            "rejection_vs_sop": rej / p.expected_rejection_rate if p.expected_rejection_rate else np.nan,
            "quality_targets_source": p.quality_targets_source,
            "sop_estimate_flags": p.estimate_flags,
        })
    return pd.DataFrame(rows).round(4)


def cs_rank_correlation(table: pd.DataFrame) -> float:
    """Spearman rho between CS and observed median elapsed time (average ranks for ties)."""
    if len(table) < 3:
        return float("nan")
    return float(table.cs.rank().corr(table.observed_median_h.rank()))
