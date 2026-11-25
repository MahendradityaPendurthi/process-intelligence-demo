"""Stage 5 (SOP part): process-level deviations from SOP expectations.

Detection only. Each row carries the measured evidence. Reasons, SOP references
and recommendations are attached in Stage 6 (root_cause.py).

    SOP_NONCONFORMANCE           share of a task type's tickets failing a check C1-C6
    SOP_ELAPSED_ABOVE_STANDARD   too many tickets above the SOP P90
    SOP_ELAPSED_BELOW_STANDARD   too many tickets below the SOP P10
    SOP_EFFORT_STANDARD          effort coverage outside the plausible range in every eligible month
    REWORK_ABOVE_SOP_EXPECTATION observed rejection rate well above 1 - expected FPY
"""
from __future__ import annotations

import json

import pandas as pd

from . import config
from .conformance import CHECK_COLUMNS

NON_FAIL = {"ok", "none", "expected_exception", "n/a", None}


def _r(x, nd=3):
    return None if pd.isna(x) else round(float(x), nd)


def _row(**kw) -> dict:
    base = {"level": "process", "employee_id": "", "classification": "process", "dominant_cause": "",
            "confidence": "", "candidate_causes": "[]", "recommended_investigation": "", "source_event_ids": ""}
    return {**base, **kw}


def nonconformance(conf: pd.DataFrame, sops: dict[str, dict]) -> list[dict]:
    rows = []
    checked = conf[conf.sop_id.notna()]
    for ttype, g in checked.groupby("task_type"):
        d = sops[ttype]
        for col in CHECK_COLUMNS[:-1]:                       # C7 is a time check, handled separately
            vals = g[col].where(~g[col].isin(NON_FAIL))
            for value, h in g[vals.notna()].groupby(col):
                share = len(h) / len(g)
                if len(h) < config.CONFORMANCE_MIN_N or share < config.CONFORMANCE_MIN_SHARE:
                    continue
                check = col.split("_")[0].upper()
                rows.append(_row(
                    entity_id=f"{ttype}:{check}={value}", department=d["department"],
                    deviation_type="SOP_NONCONFORMANCE", severity="high" if share >= 0.5 else "medium",
                    metric=f"share of tickets with {check} = {value}", observed=_r(share), expected=0.0, ratio=None,
                    baseline_id=f"{d['sop_id']} v{d['version']}", sop_id=d["sop_id"],
                    evidence=json.dumps({
                        "task_type": ttype, "check": col, "result": value, "tickets": len(h), "of": len(g),
                        "share": _r(share), "conformance_mode": h.conformance_mode.value_counts().to_dict(),
                        "required_vs_observed_approvals": {
                            f"{req or '-'} vs {obs or '-'}": int(n) for (req, obs), n in
                            h.groupby(["required_approval_stages", "observed_approval_stages"]).size().items()},
                    }),
                    source_ticket_ids="|".join(h.ticket_id),
                    explanation=f"{len(h)} of {len(g)} {ttype} tickets ({share:.0%}) fail {check} ({value}) "
                                f"against {d['sop_id']}.",
                ))
    return rows


def elapsed_band(f: pd.DataFrame, sops: dict[str, dict]) -> list[dict]:
    rows = []
    done = f[f.sop_band != "n/a"]
    for ttype, g in done.groupby("task_type"):
        d = sops[ttype]
        for band, dtype, word in [("above_p90", "SOP_ELAPSED_ABOVE_STANDARD", "above the SOP P90"),
                                  ("below_p10", "SOP_ELAPSED_BELOW_STANDARD", "below the SOP P10")]:
            h = g[g.sop_band == band]
            share = len(h) / len(g)
            if share < config.SOP_BAND_TAIL_SHARE:
                continue
            exp = g.sop_expected_elapsed_h.iloc[0]
            rows.append(_row(
                entity_id=f"{ttype}:{band}", department=d["department"], deviation_type=dtype,
                severity="high" if share >= 0.5 else "medium",
                metric="median elapsed h vs SOP expected", observed=_r(g.total_duration_h.median(), 2),
                expected=_r(exp, 2), ratio=_r(g.total_duration_h.median() / exp, 2),
                baseline_id=f"{d['sop_id']} v{d['version']} E_elapsed", sop_id=d["sop_id"],
                evidence=json.dumps({
                    "task_type": ttype, "tickets": len(g), "share_in_tail": _r(share), "expected_tail_share": 0.10,
                    "sop_band_h": [_r(g.sop_p10_h.iloc[0], 2), _r(exp, 2), _r(g.sop_p90_h.iloc[0], 2)],
                    "observed_p10_p50_p90_h": [_r(g.total_duration_h.quantile(q), 2) for q in (0.1, 0.5, 0.9)],
                }),
                source_ticket_ids="|".join(h.ticket_id),
                explanation=f"{share:.0%} of {ttype} tickets finish {word} (10% expected). Median actual "
                            f"{g.total_duration_h.median():.2f}h vs SOP expected {exp:.2f}h.",
            ))
    return rows


def effort_standard(coverage: pd.DataFrame, sops: dict[str, dict]) -> list[dict]:
    rows = []
    eligible = coverage[coverage.coverage_flag != "insufficient_n"]
    for ttype, g in eligible.groupby("task_type"):
        flags = set(g.coverage_flag)
        if len(flags) != 1 or flags == {"plausible"}:
            continue                                         # only consistent, non-plausible findings
        flag = flags.pop()
        d = sops[ttype]
        cov = g.effort_coverage.median()
        rows.append(_row(
            entity_id=f"{ttype}:effort_coverage", department=d["department"], deviation_type="SOP_EFFORT_STANDARD",
            severity="medium", classification="sop_standard", metric="effort coverage (SOP executor effort / median "
            "WIP-adjusted hold)", observed=_r(cov, 2), expected=1.0, ratio=_r(cov, 2),
            baseline_id=f"{d['sop_id']} v{d['version']} E_effort_exec", sop_id=d["sop_id"],
            evidence=json.dumps({
                "flag": flag, "months": {r.completed_month: {"n": int(r.n), "coverage": _r(r.effort_coverage, 2),
                                                             "median_wip_adj_hold_h": _r(r.median_wip_adj_hold_h, 2)}
                                         for r in g.itertuples()},
                "sop_effort_exec_h": _r(g.sop_effort_exec_h.iloc[0], 2),
                "standard_time_source": d["standard_time_source"],
                "note": "aggregated only (task type x month); never computed per employee",
            }),
            source_ticket_ids="",
            explanation=f"{ttype}: SOP executor effort {g.sop_effort_exec_h.iloc[0]:.2f}h vs median WIP-adjusted "
                        f"hold {g.median_wip_adj_hold_h.median():.2f}h (coverage {cov:.2f}, flag {flag}) in all "
                        f"{len(g)} eligible months.",
        ))
    return rows


def rework_vs_sop(f: pd.DataFrame, params: pd.DataFrame, sops: dict[str, dict]) -> list[dict]:
    rows = []
    done = f[f.total_duration_h.notna()]
    for p in params.itertuples(index=False):
        g = done[done.task_type == p.task_type]
        rej = g[g.rejection_count > 0]
        rate = len(rej) / len(g) if len(g) else 0
        if len(rej) < config.REWORK_SOP_MIN_COUNT or rate < config.REWORK_SOP_MULTIPLIER * p.expected_rejection_rate:
            continue
        d = sops[p.task_type]
        reasons = rej.rejection_reasons.str.split("|").explode().value_counts()
        rows.append(_row(
            entity_id=f"{p.task_type}:rework", department=d["department"],
            deviation_type="REWORK_ABOVE_SOP_EXPECTATION", severity="medium", classification="rework",
            metric="share of tickets rejected at least once", observed=_r(rate), expected=_r(p.expected_rejection_rate),
            ratio=_r(rate / p.expected_rejection_rate, 2), baseline_id=f"{d['sop_id']} v{d['version']} FPY",
            sop_id=d["sop_id"],
            evidence=json.dumps({"tickets": len(g), "rejected": len(rej), "reasons": reasons.to_dict(),
                                 "quality_targets_source": d["quality_targets_source"]}),
            source_ticket_ids="|".join(rej.ticket_id),
            explanation=f"{p.task_type}: {rate:.0%} of tickets rejected at least once vs {p.expected_rejection_rate:.0%} "
                        f"implied by the SOP first-pass yield ({d['quality_targets_source']}).",
        ))
    return rows


def log_mismatch(corr: pd.DataFrame, sops: dict[str, dict]) -> list[dict]:
    """Stage 3b result: SOPs whose task type's logs are not (fully) the process the SOP describes."""
    rows = []
    for v in corr[corr.verdict != "corresponds"].itertuples(index=False):
        d = sops[v.task_type]
        rows.append(_row(
            entity_id=f"{v.task_type}:{v.sop_id}", department=d["department"], deviation_type="SOP_LOG_MISMATCH",
            severity="high" if v.verdict == "does_not_correspond" else "medium", classification="sop_mismatch",
            metric="share of tickets replayable on the SOP process model", observed=_r(v.correspondence),
            expected=config.CORRESPONDENCE_MIN, ratio=None, baseline_id=f"{d['sop_id']} v{d['version']}",
            sop_id=d["sop_id"], evidence=json.dumps(v._asdict(), default=str), source_ticket_ids="",
            explanation=f"{v.task_type} logs vs {v.sop_id}: verdict {v.verdict}; {v.correspondence:.0%} of tickets "
                        f"replay on the SOP model; time ratio {v.time_ratio_own:.2f}; closest SOP by time "
                        f"{v.closest_sop_by_time}." + (" Excluded from SOP comparisons." if v.verdict ==
                                                      "does_not_correspond" else " Used with caution."),
        ))
    return rows


def detect_all(f, conf, coverage, params, sops) -> list[dict]:
    return (nonconformance(conf, sops) + elapsed_band(f, sops) + effort_standard(coverage, sops)
            + rework_vs_sop(f, params, sops))
