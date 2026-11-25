"""Run the pipeline end to end, in the fixed stage order of SOP schema §11:

  1 Read SOPs              -> sop_validation_report.csv
  2 Understand parameters  -> sop_parameters.csv
  3 Read the logs          -> data_quality_report.csv, ticket_lifecycles.csv, process_transitions.csv
  3b SOP-log correspondence -> sop_log_correspondence.csv, sop_crossfit.csv (gate: only SOPs whose
                             logs are the process they describe are used in stages 4-6)
  4 Analyse time/complexity-> ticket_features.csv, baselines, metrics, sop_time_complexity.csv, sop_effort_coverage.csv
  5 Check deviations       -> conformance.csv (+ deviation rows)
  6 Find reasons           -> deviations.csv
  7 Report                 -> demo_report.md (one-page summary), technical_report.md, deviation_report.md,
                             run_manifest.json
Each stage uses only the outputs of earlier stages.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import logging
from pathlib import Path

import pandas as pd

from . import (baselines, conformance, config, correspondence, deviations, features, ingestion, lifecycle, metrics,
               normalization, report, root_cause, sop, sop_analysis, sop_deviations, wip)

log = logging.getLogger("process_intel")
LEVEL_ORDER = {"process": 0, "employee": 1, "ticket": 2}
DEVIATION_COLUMNS = [
    "deviation_id", "level", "entity_id", "department", "employee_id", "deviation_type", "severity", "metric",
    "observed", "expected", "ratio", "baseline_id", "sop_id", "classification", "dominant_cause", "confidence",
    "candidate_causes", "evidence", "sop_reference", "preventable_by", "reason_source", "recommended_investigation",
    "source_ticket_ids", "source_event_ids", "explanation",
]


def _show(path: Path) -> str:
    """Project-relative path for logs; absolute when writing outside the project."""
    try:
        return str(path.relative_to(config.ROOT))
    except ValueError:
        return str(path)


def _write(df: pd.DataFrame, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    log.info("wrote %-45s %6d rows", _show(path), len(df))


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(raw_dir=config.RAW_DIR, processed_dir=config.PROCESSED_DIR, output_dir=config.OUTPUT_DIR,
        sop_dir=config.SOP_DIR) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.StreamHandler(), logging.FileHandler(output_dir / "pipeline_run.log", mode="w")],
        force=True,
    )
    raw = ingestion.load_raw(raw_dir)  # read-only; validated in stage 3

    log.info("Stage 1: read + validate SOPs from %s", sop_dir)
    sop_records = sop.load_sops(sop_dir)
    sop_report, sops = sop.validate_sops(sop_records, raw["task_types"])
    _write(sop_report, output_dir / "sop_validation_report.csv")
    log.info("%d SOP files (%d schema, %d legacy); %d valid for %d task types", len(sop_records),
             sum(r["format"] == "schema" for r in sop_records), sum(r["format"] == "legacy" for r in sop_records),
             len(sops), raw["task_types"].task_type.nunique())

    log.info("Stage 2: derive SOP parameters (complexity score, expected time bands)")
    params = sop.sop_parameters(sops, raw["task_types"])
    _write(params, output_dir / "sop_parameters.csv")

    log.info("Stage 3: validate, normalize and reconstruct the audit logs")
    dq = ingestion.validate(raw)
    _write(dq, output_dir / "data_quality_report.csv")
    if not dq[(dq.severity == "error") & (dq.status == "fail")].empty:
        log.warning("data-quality ERROR checks failed; affected records are kept and flagged")
    events, quarantine = normalization.normalize_events(raw["audit_logs"], raw["employees"])
    _write(events, processed_dir / "events_normalized.csv")
    _write(quarantine, processed_dir / "events_quarantined.csv")
    lifecycles, segments = lifecycle.reconstruct_all(events)
    _write(lifecycles, output_dir / "ticket_lifecycles.csv")
    _write(segments, processed_dir / "lifecycle_segments.csv")
    _write(lifecycle.transition_summary(segments, lifecycles), output_dir / "process_transitions.csv")

    log.info("Stage 3b: SOP-log correspondence gate (are the logs the process each SOP describes?)")
    feats = features.build_ticket_features(raw["tickets"], lifecycles)
    corr_tickets, corr, crossfit = correspondence.evaluate(feats, events, sops)
    _write(corr, output_dir / "sop_log_correspondence.csv")
    _write(crossfit, output_dir / "sop_crossfit.csv")
    excluded = set(corr.loc[corr.verdict == "does_not_correspond", "task_type"])
    sops_used = {t: d for t, d in sops.items() if t not in excluded}
    params_used = params[params.task_type.isin(sops_used)]
    log.info("correspondence verdicts: %s; excluded from SOP comparisons: %s",
             corr.verdict.value_counts().to_dict(), sorted(excluded) or "none")

    log.info("Stage 4: analyse time and complexity (baselines, WIP-adjusted hold, SOP vs actual)")
    base = baselines.build_baselines(feats)
    feats = baselines.attach_baselines(feats, base)
    feats["duration_flag"] = feats.duration_ratio >= config.DURATION_RATIO_THRESHOLD
    hold = wip.wip_adjusted_hold(segments, raw["tickets"])
    feats = sop_analysis.attach_sop_priors(feats, sops_used, hold)
    stage_base = baselines.build_stage_baselines(feats)
    coverage = sop_analysis.effort_coverage(feats)
    tt_table = sop_analysis.task_type_analysis(feats, params_used, coverage)
    rho = sop_analysis.cs_rank_correlation(tt_table)
    emp = metrics.employee_metrics(feats, raw["employees"])
    team = metrics.team_metrics(feats)
    for df, name in [(feats, "ticket_features"), (base, "baselines"), (stage_base, "stage_baselines"),
                     (coverage, "sop_effort_coverage"), (tt_table, "sop_time_complexity"),
                     (emp, "employee_metrics"), (team, "team_metrics")]:
        _write(df, output_dir / f"{name}.csv")
    log.info("CS vs observed median elapsed time: Spearman rho = %.3f", rho)

    log.info("Stage 5: check deviations (SOP conformance + statistical)")
    conf = conformance.check_all(feats, events, sops_used)
    conf = conf.merge(corr_tickets[["ticket_id", "correspondence_status", "correspondence_issues"]],
                      on="ticket_id", how="left")
    conf.loc[conf.task_type.isin(excluded), "conformance_mode"] = "sop_excluded_no_correspondence"
    _write(conf, output_dir / "conformance.csv")
    stat = deviations.detect_all(feats, stage_base, team).drop(columns="deviation_id", errors="ignore")
    sop_rows = pd.DataFrame(sop_deviations.log_mismatch(corr, sops)
                            + sop_deviations.detect_all(feats, conf, coverage, params_used, sops_used))
    devs = pd.concat([sop_rows, stat], ignore_index=True)
    devs = devs.sort_values("level", key=lambda s: s.map(LEVEL_ORDER), kind="mergesort").reset_index(drop=True)
    devs.insert(0, "deviation_id", [f"DEV-{i + 1:04d}" for i in range(len(devs))])
    log.info("detected %d deviations: %s", len(devs), devs.deviation_type.value_counts().to_dict())

    log.info("Stage 6: find reasons (baseline cause ranking + SOP steps, controls and clauses)")
    devs = root_cause.attach_reasons(devs, feats, conf, sops, events)[DEVIATION_COLUMNS]
    _write(devs, output_dir / "deviations.csv")

    log.info("Stage 7: reports + run manifest")
    results = dict(raw=raw, dq=dq, events=events, quarantine=quarantine, lifecycles=lifecycles, segments=segments,
                   features=feats, baselines=base, stage_baselines=stage_base, employee_metrics=emp,
                   team_metrics=team, deviations=devs, sop_records=sop_records, sop_report=sop_report, sops=sops,
                   sop_params=params, coverage=coverage, tt_table=tt_table, cs_rho=rho, conformance=conf,
                   correspondence=corr, crossfit=crossfit, sops_used=sops_used)
    for path in (report.write_report(results, output_dir / "technical_report.md"),
                 report.write_summary(results, output_dir / "demo_report.md"),
                 report.write_deviation_report(results, output_dir / "deviation_report.md")):
        log.info("wrote %s", _show(path))
    manifest = {
        "run_at": dt.datetime.now().isoformat(timespec="seconds"),
        "versions": {"baseline": config.BASELINE_VERSION, "complexity_score": config.CS_VERSION,
                     "sop_schema": config.SOP_SCHEMA_VERSION},
        "raw_files_sha256": {p.name: _sha(p) for p in sorted(raw_dir.glob("*.csv"))},
        "sop_files_sha256": {r["file"]: r["sha256"] for r in sop_records},
        "sops_used": {t: {"sop_id": d["sop_id"], "version": d["version"]} for t, d in sorted(sops.items())},
        "row_counts": {"tickets": len(feats), "events": len(events), "quarantined": len(quarantine),
                       "deviations": len(devs)},
        "cs_spearman_rho": round(rho, 4),
        "sop_log_correspondence": {r.task_type: {"sop_id": r.sop_id, "verdict": r.verdict,
                                                 "correspondence": r.correspondence} for r in corr.itertuples()},
        "thresholds": {k: getattr(config, k) for k in dir(config) if k.isupper() and isinstance(
            getattr(config, k), (int, float)) and not isinstance(getattr(config, k), bool)},
    }
    (output_dir / "run_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    log.info("wrote %s", _show(output_dir / "run_manifest.json"))
    return results
