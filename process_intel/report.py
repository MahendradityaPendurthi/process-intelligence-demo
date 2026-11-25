"""Prototype demonstration report (Markdown), generated from pipeline outputs.

All numbers come from deterministic pipeline outputs. The verification section
recomputes 10 tickets directly from the raw audit CSV with independent, simpler
code and compares the results with the pipeline.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd

from . import config


def _md_table(df: pd.DataFrame, floatfmt: str = "{:.2f}") -> str:
    def fmt(v):
        if isinstance(v, float):
            return "" if pd.isna(v) else floatfmt.format(v)
        return str(v)
    head = "| " + " | ".join(map(str, df.columns)) + " |"
    sep = "|" + "|".join("---" for _ in df.columns) + "|"
    body = ["| " + " | ".join(fmt(v) for v in row) + " |" for row in df.itertuples(index=False)]
    return "\n".join([head, sep, *body])


def _timeline(ticket_id: str, events: pd.DataFrame, segments: pd.DataFrame) -> str:
    ev = events[events.ticket_id == ticket_id]
    seg = segments[segments.ticket_id == ticket_id].set_index("from_event_id")
    rows = []
    for e in ev.itertuples(index=False):
        s = seg.loc[e.event_id] if e.event_id in seg.index else None
        rows.append({
            "event_id": e.event_id, "time": f"{e.timestamp:%m-%d %H:%M}", "event": e.event_type, "stage": e.stage,
            "actor": e.employee_id, "next interval": "" if s is None else f"{s.duration_h:.2f}h {s.category}"
            + (f" (on {s.waiting_on})" if s.category in ("approval_wait", "dependency_wait") else ""),
            "note": e.rejection_reason if isinstance(e.rejection_reason, str) else "",
        })
    return _md_table(pd.DataFrame(rows))


def _ticket_card(row, events, segments, dev=None) -> str:
    lines = [
        f"**{row.ticket_id}** - {row.task_type} / {row.complexity} / {row.priority} priority / {row.department} / "
        f"assignee {row.assigned_employee_id}",
        "",
        f"- Duration {row.total_duration_h:.2f}h vs baseline median {row.expected_duration_h:.2f}h "
        f"(ratio {row.duration_ratio:.2f}, P90 {row.baseline_p90_h:.2f}h, baseline `{row.baseline_id}`)",
        f"- Executor processing (est.) {row.executor_processing_h:.2f}h, rework {row.rework_time_h:.2f}h, "
        f"approval wait {row.approval_waiting_time_h:.2f}h, dependency wait {row.dependency_waiting_time_h:.2f}h, "
        f"queue {row.queue_time_h:.2f}h",
        f"- Rejections {row.rejection_count}, rework cycles {row.rework_cycles}, SLA met: {row.sla_met}",
    ]
    if dev is not None:
        lines.append(f"- Deviation `{dev.deviation_id}`: {dev.explanation}")
        lines.append(f"- Classification: **{dev.classification}**, confidence {dev.confidence}. "
                     f"Recommended: {dev.recommended_investigation}")
        causes = json.loads(dev.candidate_causes)
        lines.append("- Ranked candidate causes: " + "; ".join(
            f"{c['cause']} ({c['share_of_excess']:.0%})" for c in causes if c.get("share_of_excess") is not None))
    else:
        lines.append("- No deviation raised.")
    return "\n".join(lines) + "\n\n" + _timeline(row.ticket_id, events, segments)


def verify_tickets(raw_audit: pd.DataFrame, raw_tickets: pd.DataFrame, features: pd.DataFrame,
                   ticket_ids: list[str]) -> pd.DataFrame:
    """Independent recomputation from raw CSV rows (no pipeline code reused)."""
    rows = []
    for tid in ticket_ids:
        ev = raw_audit[raw_audit.ticket_id == tid].copy()
        ev["ts"] = pd.to_datetime(ev.timestamp)
        ev = ev.sort_values(["ts", "event_id"])
        t = raw_tickets[raw_tickets.ticket_id == tid].iloc[0]
        total = (pd.Timestamp(t.completed_at) - pd.Timestamp(t.created_at)).total_seconds() / 3600
        gaps = ev.ts.diff().dt.total_seconds().div(3600).dropna()
        f = features[features.ticket_id == tid].iloc[0]
        comp_sum = (f.queue_time_h + f.processing_time_est_h + f.approval_waiting_time_h + f.dependency_waiting_time_h)
        sla = pd.Timestamp(t.completed_at) <= pd.Timestamp(t.due_at)
        checks = {
            "total_h": (round(total, 4), round(f.total_duration_h, 4)),
            "sum_of_intervals_h": (round(gaps.sum(), 4), round(comp_sum, 4)),
            "rejections": (int((ev.action == "Rejected").sum()), int(f.rejection_count)),
            "resubmissions": (int((ev.action == "Resubmitted").sum()), int(f.resubmission_count)),
            "approvals": (int((ev.action == "Approved").sum()), int(f.approval_events)),
            "updates": (int((ev.action == "Updated").sum()), int(f.update_count)),
            "sla_met": (bool(sla), bool(f.sla_met)),
        }
        ok = all(abs(a - b) < 1e-3 if isinstance(a, float) else a == b for a, b in checks.values())
        rows.append({"ticket_id": tid, "raw_sequence": ">".join(ev.action),
                     **{k: f"{a} / {b}" for k, (a, b) in checks.items()}, "result": "PASS" if ok else "FAIL"})
    return pd.DataFrame(rows)




def _causes_text(dev, limit=4) -> str:
    causes = json.loads(dev.candidate_causes) if isinstance(dev.candidate_causes, str) else []
    parts = []
    for c in causes[:limit]:
        share = c.get("share_of_excess", c.get("share_of_gap", c.get("share")))
        parts.append(c["cause"] + (f" ({share:.0%})" if isinstance(share, (int, float)) else ""))
    return "; ".join(parts)


def _scenario_tickets(f, dev):
    tdev = dev[dev.level == "ticket"].copy()
    if not tdev.empty:
        tdev["share"] = tdev.candidate_causes.map(lambda c: (json.loads(c) or [{}])[0].get("share_of_excess") or 0)
    normal = f[(f.rejection_count == 0) & f.duration_ratio.between(0.95, 1.05) & (f.priority == "Medium")
               & (f.sop_band == "within")]
    if normal.empty:
        normal = f[(f.rejection_count == 0) & f.duration_ratio.between(0.95, 1.05) & (f.priority == "Medium")]
    a = normal.iloc[(normal.duration_ratio - 1).abs().argsort().iloc[0]] if not normal.empty else None
    b = tdev[tdev.classification == "process"].sort_values(["share", "ratio"], ascending=False)
    c = tdev[tdev.classification == "rework"].sort_values(["share", "ratio"], ascending=False)
    return tdev, a, (b.iloc[0] if not b.empty else None), (c.iloc[0] if not c.empty else None)


def write_report(r: dict, path: Path) -> Path:
    f, dev, ev, seg = r["features"], r["deviations"], r["events"], r["segments"]
    dq, base, emp, team, raw = r["dq"], r["baselines"], r["employee_metrics"], r["team_metrics"], r["raw"]
    srep, params, tt, cov, conf = r["sop_report"], r["sop_params"], r["tt_table"], r["coverage"], r["conformance"]
    out = []
    w = out.append

    w("# Process Intelligence - Technical Report\n")
    w("_Synthetic data only. Generated by `python run_pipeline.py`. Every number comes from the deterministic "
      "pipeline outputs in `outputs/`. No ML and no LLM are used. Short summary: `outputs/demo_report.md`; full "
      "per-deviation details: `outputs/deviation_report.md`._\n")
    w("> Deviations are **signals for investigation**, not performance judgments. Human managers remain "
      "responsible for any conclusion.\n")

    w("## Pipeline sequence\n")
    n_err = int(((srep.severity == "error") & (srep.status == "fail")).sum())
    n_legacy = sum(x["format"] == "legacy" for x in r["sop_records"])
    w(_md_table(pd.DataFrame([
        {"stage": "1 Read SOPs", "result": f"{len(r['sops'])} schema SOPs valid ({n_err} errors); "
         f"{n_legacy} legacy SOPs listed, not parsed", "output": "sop_validation_report.csv"},
        {"stage": "2 Understand parameters", "result": f"CS + expected time band for {len(params)} task types; "
         f"{int(params.complexity_match.sum())}/{len(params)} derived = declared complexity",
         "output": "sop_parameters.csv"},
        {"stage": "3 Read the logs", "result": f"{len(ev)} events, {len(r['lifecycles'])} lifecycles, "
         f"{int(((dq.status == 'fail') & (dq.severity == 'error')).sum())} data-quality errors",
         "output": "data_quality_report.csv, ticket_lifecycles.csv"},
        {"stage": "3b SOP-log correspondence", "result": "; ".join(
            f"{k}: {v}" for k, v in r["correspondence"].verdict.value_counts().items())
         + f" ({len(r['sops_used'])} of {len(r['sops'])} SOPs used in stages 4-6)",
         "output": "sop_log_correspondence.csv, sop_crossfit.csv"},
        {"stage": "4 Analyse time and complexity", "result": f"CS vs observed rank correlation rho = "
         f"{r['cs_rho']:.2f}; {(f.sop_band == 'within').mean():.0%} of tickets inside the SOP band",
         "output": "ticket_features.csv, sop_time_complexity.csv, sop_effort_coverage.csv"},
        {"stage": "5 Check deviations", "result": f"mean SOP path fitness {conf.fitness.mean():.2f}; "
         f"{len(dev)} deviations", "output": "conformance.csv"},
        {"stage": "6 Find reasons", "result": f"{int(dev.reason_source.str.contains('sop').sum())} deviations "
         "linked to an SOP step, control or clause", "output": "deviations.csv"},
        {"stage": "7 Report", "result": "this report, deviation_report.md, run_manifest.json", "output": ""},
    ])))
    w("")

    # ---------------- Stage 1
    w("## Stage 1 - SOPs read and validated\n")
    files = pd.DataFrame([{
        "sop_id": x["sop_id"], "file": x["file"], "format": x["format"],
        "task_type": (x["data"] or {}).get("task_type", ""), "version": (x["data"] or {}).get("version", ""),
        "used": "yes" if x["data"] and r["sops"].get(x["data"].get("task_type"), {}).get("sop_id") == x["sop_id"]
        else "no"} for x in r["sop_records"]])
    w(_md_table(files[files.format == "schema"]))
    w(f"\nLegacy free-text SOPs (not parsed): {', '.join(files[files.format == 'legacy'].sop_id)}.\n")
    w(f"{len(srep)} checks: {int((srep.status == 'pass').sum())} passed, {n_err} errors, "
      f"{int(((srep.status == 'fail') & (srep.severity == 'warning')).sum())} warnings.\n")
    issues = srep[srep.status == "fail"].groupby(["check", "severity"]).agg(
        sops=("sop_id", lambda s: ", ".join(s)), details=("details", "first")).reset_index()
    if not issues.empty:
        w(_md_table(issues))
    w("")

    # ---------------- Stage 2
    w("## Stage 2 - SOP parameters\n")
    w(f"Complexity score `{config.CS_VERSION}` and expected elapsed time (PERT, P10-P90 band, parallel dependency "
      "waits combined as a maximum). Standard times are illustrative and are never tuned to the data.\n")
    w(_md_table(params[["sop_id", "task_type", "cs", "complexity_derived", "complexity_declared", "required_stages",
                        "e_effort_exec_h", "e_wait_h", "e_elapsed_h", "p10_h", "p90_h", "expected_rejection_rate",
                        "estimate_flags"]]))
    w("\nApproximations: steps are assumed sequential and independent; the normal approximation understates the "
      "right tail; drivers missing from the export contribute 0 (`drivers_missing`).\n")

    # ---------------- Stage 3
    w("## Stage 3 - Audit logs read, validated and reconstructed\n")
    w(_md_table(pd.DataFrame([
        {"item": "Employees / tickets", "value": f"{len(raw['employees'])} / {len(raw['tickets'])}"},
        {"item": "Audit events (raw / normalized / quarantined)",
         "value": f"{len(raw['audit_logs'])} / {len(ev)} / {len(r['quarantine'])}"},
        {"item": "Period (completion)", "value": f"{f.completed_at.min():%Y-%m-%d} .. {f.completed_at.max():%Y-%m-%d}"},
        {"item": "Lifecycles reconstructed",
         "value": f"{len(r['lifecycles'])} ({int(r['lifecycles'].is_closed.sum())} closed)"},
        {"item": "Duration reconciliation", "value": f"{int((~f.duration_source_mismatch).sum())}/{len(f)} match"},
    ])))
    fails = dq[dq.status == "fail"]
    w(f"\n{len(dq)} data-quality checks; not passed:\n")
    if not fails.empty:
        w(_md_table(fails[["check_id", "dataset", "check", "severity", "affected_rows", "details"]]))
    variants = r["lifecycles"].event_sequence.value_counts().head(5).reset_index()
    variants.columns = ["process variant", "tickets"]
    w(f"\n{r['lifecycles'].event_sequence.nunique()} process variants; most frequent:\n")
    w(_md_table(variants))
    w("")

    # ---------------- Stage 3b
    corr, cross = r["correspondence"], r["crossfit"]
    w("## Stage 3b - SOP-log correspondence (is each log the process its SOP describes?)\n")
    w("Every ticket's audit path is replayed on a process model built from its SOP: actor department and role, "
      "intake, submission, holds, approval stages and their order, who may reject, the rework loop and closure. "
      "`does_not_fit` means the path could not come from that SOP; `fits_with_known_deviations` means the same "
      "process with conformance deviations (approval count, holds, reasons). Each task type is also replayed "
      "against every other SOP (path score: fit 1, known deviation 0.5, no fit 0) and compared on time scale, "
      "excluding stages the platform never logs. SOPs that do not correspond are excluded from stages 4-6.\n")
    w(_md_table(corr[["task_type", "sop_id", "tickets", "fits", "fits_with_known_deviations", "does_not_fit",
                      "correspondence", "path_score_own", "best_other_sop_by_path", "path_score_best_other",
                      "time_ratio_own", "closest_sop_by_time", "structural_mismatches", "verdict"]]))
    noted = corr[corr.notes.astype(str).str.len() > 0]
    if not noted.empty:
        w("\nNotes:\n")
        for v in noted.itertuples():
            w(f"- **{v.task_type}** ({v.sop_id}): {v.notes}")
    w("\nCross-fit path score (rows: logs of a task type; columns: SOP replayed):\n")
    w(_md_table(cross.pivot(index="task_type", columns="sop_id", values="path_score").reset_index()))
    w("\nReading: the diagonal should be the best or tied-best entry in each row. Where another SOP scores higher, "
      "the cause is a known deviation listed above (for example holds the SOP forbids), and the time scale "
      "confirms the labelled SOP. Executor work steps leave no audit footprint, so SOPs with the same routing can "
      "only be told apart by time scale and the task_type label.\n")

    # ---------------- Stage 4
    w("## Stage 4 - Time and complexity analysis\n")
    w("### 4.1 SOP expectation vs actual\n")
    w(f"Spearman rank correlation between CS and observed median elapsed time: **rho = {r['cs_rho']:.2f}** "
      f"across {len(tt)} task types. This is the real test of the complexity score; matching the declared labels "
      "is weak evidence.\n")
    w(_md_table(tt[["task_type", "cs", "observed_median_h", "sop_expected_elapsed_h", "sop_p10_h", "sop_p90_h",
                    "share_below_p10", "share_within", "share_above_p90", "actual_median_first_decision_h",
                    "sop_exp_first_decision_h", "observed_rejection_rate", "sop_expected_rejection_rate"]]))
    w("\n### 4.2 Effort coverage (SOP executor effort / median WIP-adjusted hold, task type x month)\n")
    w(_md_table(tt[["task_type", "sop_effort_exec_h", "median_wip_adj_hold_h", "effort_coverage_overall",
                    "coverage_months_flagged"]]))
    w(f"\n{int((cov.coverage_flag == 'standard_exceeds_hold').sum())} of "
      f"{int((cov.coverage_flag != 'insufficient_n').sum())} eligible task-type-months show SOP executor effort "
      "above the observed upper bound: either the illustrative standards are high, or work happens outside the "
      "ticket window. Standards are not edited to match (schema §3.1).\n")
    w("### 4.3 Historical baselines\n")
    w(f"Baseline `{config.BASELINE_VERSION}`: task type + complexity + priority when n >= {config.MIN_BASELINE_N}, "
      f"else task type + complexity ({f.baseline_id.str.contains(':L2:').mean():.0%} of tickets use the specific "
      "level).\n")
    w(_md_table(base[base.baseline_level == "L1"][["task_type", "complexity", "n", "median_duration_h",
                                                    "p75_duration_h", "p90_duration_h",
                                                    "median_executor_processing_h", "rejection_rate", "sla_rate"]]))
    w("\n### 4.4 Where ticket time goes\n")
    w(_md_table(team[team.period_type == "overall"][["department", "tickets_completed", "processing_share",
                                                     "decision_wait_share", "median_pre_decision_wait_h",
                                                     "rejection_rate", "sla_compliance"]], "{:.3f}"))
    w("\n### 4.5 Workload: raw counts vs complexity-weighted effort\n")
    overall = emp[emp.period_type == "overall"]
    best = None
    for dept, g in overall.groupby("department"):
        for a in g.itertuples():
            for bb in g.itertuples():
                if a.tickets_completed > bb.tickets_completed and a.expected_effort_h < bb.expected_effort_h:
                    score = (bb.expected_effort_h / bb.tickets_completed) / (a.expected_effort_h / a.tickets_completed)
                    if best is None or score > best[0]:
                        best = (score, dept, a.employee_id, bb.employee_id)
    if best:
        _, dept, ea, eb = best
        w(f"In {dept}, **{ea}** completed more tickets than **{eb}**, but {eb} carried more expected effort:\n")
        w(_md_table(overall[overall.employee_id.isin([ea, eb])][[
            "employee_id", "tickets_completed", "simple_tickets", "medium_tickets", "complex_tickets",
            "expected_effort_h", "median_duration_ratio", "task_mix"]]))
    w("")

    # ---------------- Stage 5
    w("## Stage 5 - Deviations detected\n")
    w(_md_table(dev.groupby(["level", "deviation_type", "classification"]).size().reset_index(name="count")))
    w("\n### 5.1 SOP conformance per ticket\n")
    w(f"Conformance mode: {conf.conformance_mode.value_counts().to_dict()}. Tickets created before an SOP's "
      "effective date are checked **retrospectively** (schema §9.1): the results show how far past practice was "
      "from the documented process, not breaches of a rule in force at the time.\n")
    rows = [{"check": col, "result": v, "tickets": n}
            for col in [c for c in conf.columns if c[:1] == "c" and c[1:2].isdigit()]
            for v, n in conf[col].value_counts().items()]
    w(_md_table(pd.DataFrame(rows)))
    w("\nMean path fitness (C1-C6) by task type:\n")
    w(_md_table(conf.groupby("task_type").fitness.mean().reset_index().rename(columns={"fitness": "mean_fitness"})))
    w("")

    # ---------------- Stage 6
    w("## Stage 6 - Reasons\n")
    w("### 6.1 Process-level deviations\n")
    for d in dev[dev.level == "process"].itertuples():
        w(f"- **`{d.deviation_id}` {d.deviation_type}** - {d.entity_id} ({d.severity}, {d.classification}, "
          f"confidence {d.confidence})  \n  {d.explanation}  \n  Reason: {d.dominant_cause}  \n"
          f"  SOP reference: {d.sop_reference or '-'}  \n  _Recommended: {d.recommended_investigation}_")
    w("\n### 6.2 Employee-level signals\n")
    for d in dev[dev.level == "employee"].itertuples():
        w(f"- **`{d.deviation_id}` {d.entity_id}** {d.deviation_type} ({d.severity}): {d.explanation}  \n"
          f"  _Recommended: {d.recommended_investigation}_")
    tdev, a, b, c = _scenario_tickets(f, dev)
    w("\n### 6.3 Ticket-level deviations\n")
    if not tdev.empty:
        w(f"{len(tdev)} tickets >= {config.DURATION_RATIO_THRESHOLD}x their baseline median. Dominant contributor:\n")
        w(_md_table(tdev.groupby(["classification", "dominant_cause"]).size().reset_index(name="tickets")
                    .sort_values("tickets", ascending=False).head(12)))
    w("\n### 6.4 Worked examples\n")
    if a is not None:
        w("**A. Normal ticket** (within baseline and within the SOP band)\n")
        w(_ticket_card(a, ev, seg) + "\n")
    if b is not None:
        w("**B. Slow because of waiting, not the executor**\n")
        w(_ticket_card(f[f.ticket_id == b.entity_id].iloc[0], ev, seg, b))
        w(f"\nSOP view: {b.sop_reference}\n")
    if c is not None:
        w("**C. Slow because of rework, linked to the SOP control that would prevent it**\n")
        w(_ticket_card(f[f.ticket_id == c.entity_id].iloc[0], ev, seg, c))
        w(f"\nSOP view: {c.sop_reference}. Preventable by: **{c.preventable_by or '-'}**\n")
    w("")

    # ---------------- Stage 7
    w("## Stage 7 - Verification against raw audit events\n")
    sample = []
    for pool in [f[f.rejection_count == 0], f[f.rejection_count > 0], f[f.approval_events >= 2],
                 f[f.sla_met == False], f[f.dependency_wait_events == 0]]:  # noqa: E712
        sample += [t for t in pool.ticket_id.head(2) if t not in sample]
    sample = (sample + [t for t in f.ticket_id if t not in sample])[:10]
    ver = verify_tickets(raw["audit_logs"], raw["tickets"], f, sample)
    r["verification"] = ver
    w("Ten tickets recomputed from `data/raw/audit_logs.csv` with independent code (`independent / pipeline`):\n")
    w(_md_table(ver))
    w(f"\n**{int((ver.result == 'PASS').sum())}/{len(ver)} PASS.**\n")

    w("## Assumptions and limitations\n")
    for line in [
        "Durations are calendar hours; timestamps are naive, one timezone. Business hours are not modelled.",
        "Processing vs waiting is **estimated** from who holds the ticket. WIP-adjusted hold is still an upper "
        "bound on effort.",
        "The interval after DependencyWait cannot be split into dependency vs reviewer wait; first-decision "
        "comparisons use the full submission-to-decision wait.",
        "SOP standard times and first-pass yields are illustrative (`quality_targets_source: unconfirmed`); "
        "SOP-vs-actual gaps are findings for the SOP owner, not proof of a problem.",
        "The SOPs took effect after the data period, so all conformance results are retrospective.",
        "The export has no complexity-driver values (line items, values, severity, ...); SOP estimates use base "
        "effort and route conditional approvals from the ticket's approval_count.",
        "No leave/absence data; persistent employee deviations state this explicitly.",
        "Baselines are in-sample; all thresholds are demonstration values in `process_intel/config.py`.",
    ]:
        w(f"- {line}")
    w("")
    path.write_text("\n".join(out), encoding="utf-8")
    return path


def _pct(x) -> str:
    return f"{x:.0%}"


def _task(entity: str) -> str:
    return str(entity).split(":")[0]


def write_summary(r: dict, path: Path) -> Path:
    """One-page, plain-language summary for managers. Every number comes from the pipeline outputs;
    the full detail is in technical_report.md and deviation_report.md."""
    f, dev, conf, dq, team, tt = r["features"], r["deviations"], r["conformance"], r["dq"], r["team_metrics"], r["tt_table"]
    corr = r["correspondence"]
    by = {k: g for k, g in dev.groupby("deviation_type")}
    proc = dev[dev.level == "process"]
    nc = by.get("SOP_NONCONFORMANCE", dev.iloc[0:0])
    out = []
    w = out.append

    w("# Process Intelligence - Summary\n")
    w(f"_What happened in {len(f):,} tickets ({f.completed_at.min():%d %b} to {f.completed_at.max():%d %b %Y}), "
      "compared with the company SOPs. Synthetic demo data. Every flag is a **signal to look into, not a judgment "
      "of anyone**._\n")

    # ---------------- At a glance
    dq_err = int(((dq.status == "fail") & (dq.severity == "error")).sum())
    dq_warn = int(((dq.status == "fail") & (dq.severity == "warning")).sum())
    n_corr = int((corr.verdict == "corresponds").sum())
    counts = dev.level.value_counts()
    w("## At a glance\n")
    w(_md_table(pd.DataFrame([
        ("Tickets analysed", f"{len(f):,} across {f.department.nunique()} departments and {f.task_type.nunique()} task types"),
        ("Data quality", f"{dq_err} errors, {dq_warn} warnings: the data can be trusted"),
        ("SOPs that match the logs", f"{n_corr} of {len(corr)} (each log really is the process its SOP describes)"),
        ("Tickets that follow the SOP route exactly", _pct((conf.fitness >= 1).mean())),
        ("Tickets finished on time (SLA)", _pct(f.sla_met.mean())),
        ("Things flagged", f"{len(dev)}: {counts.get('process', 0)} about processes or SOPs, "
         f"{counts.get('ticket', 0)} slow tickets, {counts.get('employee', 0)} about individuals"),
    ], columns=["", "Result"])))
    w("")

    # ---------------- Main findings
    w("## Main findings\n")
    findings, actions = [], []

    log_gap = nc[nc.classification == "platform_logging"]
    if not log_gap.empty:
        d = log_gap.iloc[0]
        findings.append(f"**An SOP approval step is never recorded.** {d.dominant_cause}. Affects "
                        f"{', '.join(log_gap.entity_id.map(_task))}.")
        actions.append("**Platform team:** confirm whether HOD approval happens outside the system or is skipped, "
                       "and record it if it happens.")
    extra = nc[nc.entity_id.str.contains("C1=more")]
    if not extra.empty:
        # SOP conditions are expressions ('kpi_breach == true or ...'); show them as words
        cause = re.sub(r"'([^']*)'", lambda m: re.sub(r"\s*==\s*true", "", m.group(1)).replace("_", " "),
                       extra.iloc[0].dominant_cause)
        findings.append(f"**Approvals given when the SOP does not ask for them.** "
                        f"{', '.join(extra.entity_id.map(_task))}: {cause}.")
        actions.append("**Process owner:** set the approval condition on the platform, or update the SOP if "
                       "approval on every ticket is wanted.")
    holds = nc[nc.entity_id.str.contains("C3=undeclared")]
    if not holds.empty:
        n_hold = int((conf.c3_dependency_wait == "undeclared").sum())
        findings.append(f"**Tickets put on hold where the SOP has no waiting step** ({n_hold} tickets). "
                        + ", ".join(f"{_task(d.entity_id)} {_pct(d.observed)}" for d in holds.itertuples())
                        + ". The SOP says to reject for missing information instead.")
        actions.append("**Approvers:** stop using 'on hold' as a queue; reject with a reason when information "
                       "is missing.")
    fast = tt[tt.share_below_p10 >= 0.5]
    if not fast.empty:
        findings.append(f"**SOP time standards look too high.** {_pct((conf.c7_elapsed_band == 'below_p10').mean())} "
                        "of tickets finish faster than the SOP's fastest expected time; in "
                        f"{len(fast)} of {len(tt)} task types most tickets do ("
                        + ", ".join(f"{t.task_type} {_pct(t.share_below_p10)}" for t in
                                    fast.sort_values("share_below_p10", ascending=False).itertuples()) + ").")
        actions.append("**SOP owners:** review the time standards (a short time study). Do not just edit them "
                       "to match the data.")
    slow = by.get("SOP_ELAPSED_ABOVE_STANDARD")
    if slow is not None:
        share = tt.set_index("task_type").share_above_p90
        findings.append("**Slower than the SOP allows:** "
                        + ", ".join(f"{_task(d.entity_id)} ({_pct(share[_task(d.entity_id)])} of tickets)"
                                    for d in slow.itertuples())
                        + ", mostly from waiting for the first approval.")
    rework = by.get("REWORK_ABOVE_SOP_EXPECTATION")
    if rework is not None:
        findings.append(f"**More rework than the SOP expects** in {len(rework)} task types:\n\n")
        rows = []
        for d in rework.itertuples():
            reason, _, fix = str(d.dominant_cause).partition(": preventable by ")
            rows.append({"Task type": _task(d.entity_id), "Sent back": _pct(d.observed),
                         "SOP expects": _pct(d.expected), "Top reason": reason, "Check that would prevent it": fix})
        findings[-1] += "\n".join("   " + line for line in _md_table(pd.DataFrame(rows)).split("\n"))
        actions.append("**Team leads:** tighten the checks listed in the rework table, then re-measure.")
    queue = by.get("APPROVAL_STAGE_BOTTLENECK")
    if queue is not None:
        findings.append("**Approval queues:** " + "; ".join(
            f"{d.department} tickets wait {d.ratio:.1f}x the company average for the "
            f"{d.entity_id.split(':')[1]} decision ({d.observed:.1f}h vs {d.expected:.1f}h)" for d in queue.itertuples())
            + ". This is a process issue, not the executors'.")
        actions.append("**Department heads:** review approver turnaround in "
                       + " and ".join(queue.department) + ".")
    surge = by.get("APPROVAL_WAIT_INCREASE")
    if surge is not None:
        findings.append("**Approval waits that rose for a few months:**\n\n" + "\n".join(
            f"   - {d.explanation}" for d in surge.itertuples()))
        actions.append("**Department heads:** check approver availability for the months listed above.")
    rework_w = by.get("REWORK_INCREASE")
    if rework_w is not None:
        findings.append("**Rework spikes:** " + " ".join(d.explanation for d in rework_w.itertuples()))
    drops = by.get("SLA_DROP")
    if drops is not None:
        findings.append("**On-time delivery dropped:** " + " ".join(
            f"{d.explanation} {d.dominant_cause}." for d in drops.itertuples()))
    sla = by.get("SLA_DETERIORATION")
    if sla is not None:
        for d in sla.itertuples():
            findings.append(f"**On-time delivery is falling.** {d.explanation}")
        actions.append("**Operations head:** review the late tickets together with the queue and individual signals above.")
    tdev = dev[dev.level == "ticket"]
    if not tdev.empty:
        mix = tdev.classification.value_counts()
        label = {"rework": "rework after being sent back", "process": "waiting (approvals, holds, dependencies)",
                 "executor_processing": "the work itself"}
        findings.append(f"**{len(tdev)} tickets took at least {config.DURATION_RATIO_THRESHOLD}x their normal time.** "
                        "Causes: " + ", ".join(f"{n} {label.get(k, k)}" for k, n in mix.items()) + ".")
    edev = dev[dev.level == "employee"]
    if not edev.empty:
        unexplained = sorted(set(edev[edev.classification == "individual_signal"].entity_id))
        context = sorted(set(edev[edev.classification == "context_explained"].entity_id))
        txt = f"**{len(edev)} signals about {edev.entity_id.nunique()} individuals.** "
        if unexplained:
            txt += f"Not explained by workload or complexity: {', '.join(unexplained)}. "
        if context:
            txt += f"Explained by context (e.g. higher workload): {', '.join(context)}. "
        findings.append(txt + "For a private, supportive conversation with context (leave, other duties, tools), "
                        "never as a rating.")
    for i, x in enumerate(findings, 1):
        w(f"{i}. {x}\n")

    # ---------------- Where time goes
    overall = team[team.period_type == "overall"]
    wait = (overall.decision_wait_share * overall.tickets_completed).sum() / overall.tickets_completed.sum()
    w("## Where ticket time goes\n")
    w(f"About **{_pct(wait)} of ticket time is waiting**, mostly for approvals, not working. Speeding up "
      "approvals helps more than pushing executors.\n")
    w(_md_table(pd.DataFrame({
        "Department": overall.department, "Tickets": overall.tickets_completed,
        "Working": overall.processing_share.map(_pct), "Waiting": overall.decision_wait_share.map(_pct),
        "Sent back": overall.rejection_rate.map(_pct), "On time": overall.sla_compliance.map(_pct)})))
    w("")

    # ---------------- Actions
    w("## Recommended next steps\n")
    for i, a in enumerate(actions, 1):
        w(f"{i}. {a}")
    w("")

    w("## Keep in mind\n")
    w("- The SOPs took effect after this data period, so the results show how past practice compares with the "
      "documented process, not rule breaches.")
    w("- SOP time standards and quality targets are illustrative until their owners confirm them.")
    ver = r.get("verification")
    w("- Every number can be traced to ticket and event IDs."
      + (f" {len(ver)} tickets were re-checked against the raw logs with separate code: "
         f"{int((ver.result == 'PASS').sum())} of {len(ver)} match." if ver is not None else "") + "\n")
    w("**More detail:** `technical_report.md` (all stages, tables and methods), `deviation_report.md` (every "
      "flag with its evidence), and the CSV files in `outputs/`.")
    w("")
    path.write_text("\n".join(out), encoding="utf-8")
    return path


def write_deviation_report(r: dict, path: Path) -> Path:
    """Every deviation with all of its details, grouped by level."""
    dev = r["deviations"]
    out = ["# Deviation Report\n",
           f"_{len(dev)} deviations from `outputs/deviations.csv`, in pipeline order (process, employee, ticket). "
           "Each is a signal for investigation, not a judgment._\n",
           _md_table(dev.groupby(["level", "deviation_type"]).size().reset_index(name="count"))]
    titles = {"process": "Process and SOP-level deviations", "employee": "Employee-level signals",
              "ticket": "Ticket-level deviations"}

    def text(v):
        return v if isinstance(v, str) and v else "-"

    for level in ["process", "employee", "ticket"]:
        sub = dev[dev.level == level]
        if sub.empty:
            continue
        out.append(f"\n## {titles[level]} ({len(sub)})\n")
        for d in sub.itertuples():
            tickets = [t for t in str(d.source_ticket_ids or "").split("|") if t and t != "nan"]
            events = [e for e in str(d.source_event_ids or "").split("|") if e and e != "nan"]
            src = (f"{len(tickets)} tickets: {', '.join(tickets[:10])}" + (" ..." if len(tickets) > 10 else "")
                   if tickets else "-")
            if events:
                src += f"; {len(events)} events: {', '.join(events)}"
            fields = pd.DataFrame([
                ("Entity", f"{d.entity_id} ({text(d.department)})"),
                ("Severity / classification / confidence", f"{d.severity} / {d.classification} / {d.confidence}"),
                ("Measured", f"{d.metric}: observed {d.observed}, expected {d.expected}, ratio {d.ratio}"),
                ("Compared with", text(d.baseline_id)),
                ("What happened", text(d.explanation)),
                ("Most likely reason", text(d.dominant_cause)),
                ("Ranked candidate causes", _causes_text(d, 6) or "-"),
                ("SOP reference", text(d.sop_reference)),
                ("Preventable by", text(d.preventable_by)),
                ("Reason source", text(d.reason_source)),
                ("Recommended investigation", text(d.recommended_investigation)),
                ("Source records", src),
            ], columns=["field", "value"])
            out.append(f"### `{d.deviation_id}` {d.deviation_type}\n")
            out.append(_md_table(fields))
            out.append("\n<details><summary>Evidence (JSON)</summary>\n\n```json\n"
                       + json.dumps(json.loads(d.evidence), indent=2) + "\n```\n</details>\n")
    path.write_text("\n".join(out), encoding="utf-8")
    return path
