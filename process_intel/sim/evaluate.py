"""Detection evaluation: score a pipeline run on simulated data against the planted scenarios.

For each scenario the verdict is one of
    detected                 an expected deviation type on the right entity, in the right months
    detected_wrong_type      the right entity and months, but a different type than expected
                             (e.g. flagged as unexplained when the context should explain it)
    missed
    control_pass / control_fail   negative controls: the entity must not get an employee-level flag
    out_of_scope             needs a component that does not exist yet (LLM comment check)

False alarms: process- and employee-level statistical findings that match no planted scenario
(by entity or department, and by time window when the finding has one). Ticket-level rows are scored
as a lift: share of the scenario's tickets flagged vs the same task type outside the scenario.
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from .scenarios import SCENARIOS

STATISTICAL = {"APPROVAL_STAGE_BOTTLENECK", "APPROVAL_WAIT_INCREASE", "SLA_DETERIORATION", "SLA_DROP",
               "REWORK_INCREASE",
               "PERSISTENT_UNEXPLAINED_PROCESSING_INCREASE", "PERSISTENT_PROCESSING_INCREASE_WITH_CONTEXT",
               "ELEVATED_REJECTION_RATE"}
EMPLOYEE_TYPES = {"PERSISTENT_UNEXPLAINED_PROCESSING_INCREASE", "PERSISTENT_PROCESSING_INCREASE_WITH_CONTEXT",
                  "ELEVATED_REJECTION_RATE"}
TICKET_LIFT_MIN = 2.0


def _months(start, end) -> set[str]:
    # completed_month lags the activity by up to a month, so the window is extended by one month
    return {str(p) for p in pd.period_range(pd.Period(start, "M"), pd.Period(end, "M") + 1, freq="M")}


def _window(row) -> set[str] | None:
    try:
        ev = json.loads(row.evidence)
    except (TypeError, ValueError):
        return None
    if "window_start" not in ev:
        return None
    return {str(p) for p in pd.period_range(ev["window_start"], ev["window_end"], freq="M")}


def _overlaps(row, months: set[str]) -> bool:
    w = _window(row)
    return w is None or bool(w & months)          # whole-period findings cannot be placed in time


def _in_months(d: pd.DataFrame, months: set[str]) -> pd.DataFrame:
    return d[pd.Series([_overlaps(r, months) for r in d.itertuples()], index=d.index, dtype=bool)]


def _task_types(sc) -> list[str]:
    if sc["task_type"]:
        return [sc["task_type"]]
    if "|" in sc["entity"] or sc["level"] == "process" and sc["department"] is None:
        return sc["entity"].split("|")
    return []


def _candidates(sc, dev: pd.DataFrame) -> pd.DataFrame:
    """Non-ticket findings on this scenario's entity, in its months."""
    months = _months(sc["start"], sc["end"])
    d = dev[dev.level != "ticket"]
    if sc["level"] in ("employee", "control") and sc["entity"].startswith("E"):
        d = d[d.entity_id == sc["entity"]]
    elif tts := _task_types(sc):
        # the task type's own findings, plus department findings whose main cause names the task type
        names_tt = d.dominant_cause.fillna("").apply(lambda c: any(t in c for t in tts))
        d = d[d.entity_id.str.split(":").str[0].isin(tts) | (names_tt & (d.level == "process"))]
    elif sc["department"]:
        d = d[(d.department == sc["department"]) & (d.level != "employee")]   # people are handled separately
        if ":" in sc["entity"]:                       # e.g. Finance:Incharge -> that approver stage only
            stage = sc["entity"].split(":")[1]
            d = d[~d.deviation_type.str.startswith("APPROVAL") | d.entity_id.str.contains(f":{stage}")]
    elif sc["level"] == "sop_standard":
        d = d[d.deviation_type.isin(sc["expected"])]
    return _in_months(d, months)


def _ticket_lift(sc, f: pd.DataFrame, truth: pd.DataFrame) -> float | None:
    """Flag rate on the scenario's tickets / flag rate on comparable tickets outside it."""
    if f is None or "TICKET_DURATION" not in sc["expected"]:
        return None
    t = f.merge(truth[["ticket_id", "scenarios"]], on="ticket_id", how="left")
    t["hit"] = t.scenarios.fillna("").str.split("|").apply(lambda s: sc["id"] in s)
    same = t[t.task_type.isin(t[t.hit].task_type.unique())]
    inside, outside = same[same.hit], same[~same.hit]
    if inside.empty or outside.duration_flag.mean() == 0:
        return None
    return round(float(inside.duration_flag.mean() / outside.duration_flag.mean()), 2)


COMMENT_CHECK_MIN = 0.8          # SC13 counts as detected when precision and recall both reach this


def comment_check_score(out_dir: Path, truth_dir: Path) -> dict | None:
    """SC13: the reason-code mismatches flagged by the comment check vs the planted mislabels."""
    path = out_dir / "reason_code_checks.csv"
    if not path.exists():
        return None
    chk = pd.read_csv(path)
    truth = pd.read_csv(truth_dir / "comments_truth.csv")
    t = chk.merge(truth, on="comment_id", how="left")
    planted = t.true_label != t.platform_reason_code
    flagged = t.status == "mismatch"
    tp = int((planted & flagged).sum())
    prec = tp / max(int(flagged.sum()), 1)
    rec = tp / max(int(planted.sum()), 1)
    hi = flagged & (t.confidence == "high")
    return {"rejections": len(t), "planted": int(planted.sum()), "flagged": int(flagged.sum()), "true_positives": tp,
            "precision": round(prec, 3), "recall": round(rec, 3),
            "high_confidence_flagged": int(hi.sum()),
            "high_confidence_precision": round(int((hi & planted).sum()) / max(int(hi.sum()), 1), 3)}


def evaluate(out_dir: Path, truth_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    dev = pd.read_csv(out_dir / "deviations.csv")
    f = pd.read_csv(out_dir / "ticket_features.csv", usecols=["ticket_id", "task_type", "duration_flag"])
    truth = pd.read_csv(truth_dir / "tickets_truth.csv")

    rows, matched = [], set()
    cc = comment_check_score(out_dir, truth_dir)
    for sc in SCENARIOS:
        cand = _candidates(sc, dev)
        lift = _ticket_lift(sc, f, truth)
        expected = set(sc["expected"]) - {"TICKET_DURATION"}
        if sc["level"] == "control":
            emp = cand[cand.deviation_type.isin(EMPLOYEE_TYPES)]
            verdict = "control_fail" if len(emp) else "control_pass"
            hits = emp
        elif sc["expected"] == ["LLM_COMMENT_CHECK"]:
            hits = cand.iloc[0:0]
            if cc is None:
                verdict = "out_of_scope"                       # run_comment_check.py has not been run
            else:
                ok = cc["precision"] >= COMMENT_CHECK_MIN and cc["recall"] >= COMMENT_CHECK_MIN
                verdict = "detected" if ok else "missed"
                rows.append({"scenario": sc["id"], "name": sc["name"], "level": sc["level"], "entity": sc["entity"],
                             "window": f"{sc['start']}..{sc['end']}", "expected": "LLM_COMMENT_CHECK",
                             "verdict": verdict, "found_types": "REASON_CODE_MISMATCH",
                             "found": f"{cc['true_positives']}/{cc['planted']} planted mislabels flagged, "
                                      f"precision {cc['precision']:.0%}, recall {cc['recall']:.0%}",
                             "coverage": "", "ticket_flag_lift": None})
                continue
        else:
            hits = cand[cand.deviation_type.isin(expected)]
            other = cand[cand.deviation_type.isin(STATISTICAL | {"SOP_NONCONFORMANCE"}) & ~cand.index.isin(hits.index)]
            if len(hits):
                verdict = "detected"
            elif not expected and lift is not None:            # ticket-level only (SC07)
                verdict = "detected" if lift >= TICKET_LIFT_MIN else "missed"
            elif sc["level"] == "employee" and len(other[other.deviation_type.isin(EMPLOYEE_TYPES)]):
                verdict, hits = "detected_wrong_type", other
            else:
                verdict = "missed"
            matched |= set(cand.index)
        tts = _task_types(sc)
        coverage = (f"{hits.entity_id.str.split(':').str[0].nunique()}/{len(tts)} task types"
                    if len(tts) > 1 else "")
        rows.append({"scenario": sc["id"], "name": sc["name"], "level": sc["level"], "entity": sc["entity"],
                     "window": f"{sc['start']}..{sc['end']}", "expected": "|".join(sc["expected"]),
                     "verdict": verdict, "found_types": "|".join(sorted(set(hits.deviation_type))),
                     "found": " ; ".join(hits.entity_id.astype(str).unique()[:4]), "coverage": coverage,
                     "ticket_flag_lift": lift})
    scores = pd.DataFrame(rows)

    stat = dev[dev.deviation_type.isin(STATISTICAL)]
    false_alarms = stat[~stat.index.isin(matched)]
    # employee flags in a department during a department-wide planted event are attributable, but should
    # have been classified as context, not as an individual signal
    for sc in SCENARIOS:
        if sc["level"] == "process" and sc["department"] and sc["task_type"] is None:
            months = _months(sc["start"], sc["end"])
            team = false_alarms[(false_alarms.department == sc["department"]) & false_alarms.level.eq("employee")]
            team = _in_months(team, months)
            false_alarms = false_alarms.drop(team.index)
            team_rows = dev.loc[team.index].assign(attributed_to=sc["id"])
            scores.loc[scores.scenario == sc["id"], "team_member_flags"] = len(team_rows)
            scores.loc[scores.scenario == sc["id"], "team_member_flags_individual"] = int(
                (team_rows.classification == "individual_signal").sum())
    return scores, false_alarms[["deviation_id", "level", "deviation_type", "entity_id", "department",
                                 "classification", "explanation"]]


def summarise(scores: pd.DataFrame, false_alarms: pd.DataFrame) -> dict:
    in_scope = scores[~scores.verdict.isin(["out_of_scope"]) & (scores.level != "control")]
    controls = scores[scores.level == "control"]
    return {
        "scenarios_in_scope": len(in_scope),
        "detected": int((in_scope.verdict == "detected").sum()),
        "detected_wrong_type": int((in_scope.verdict == "detected_wrong_type").sum()),
        "missed": sorted(in_scope[in_scope.verdict == "missed"].scenario),
        "controls_passed": f"{int((controls.verdict == 'control_pass').sum())}/{len(controls)}",
        "out_of_scope": sorted(scores[scores.verdict == "out_of_scope"].scenario),
        "false_alarms": len(false_alarms),
        "false_alarms_by_type": false_alarms.deviation_type.value_counts().to_dict(),
    }
