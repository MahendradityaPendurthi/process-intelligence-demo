"""Comment check: the deterministic parts (no LLM calls: labels are set by hand)."""
import pandas as pd

from process_intel.llm import comment_check as cc
from process_intel.sim import evaluate


def _labelled():
    rows = [
        # ticket, context, platform code, text, llm label
        ("T1", "rejection", "Amount mismatch", "qty wrong", "Wrong quantity"),        # mismatch, fix agrees
        ("T1", "correction", "Amount mismatch", "fixed qty", "Wrong quantity"),
        ("T2", "rejection", "Wrong quantity", "count off", "Wrong quantity"),         # agrees
        ("T3", "rejection", "Incorrect category", "receipt missing", "Required document missing"),  # no fix
        ("T4", "rejection", "Amount mismatch", "see mail", "unclear"),
        ("T5", "rejection", "Amount mismatch", "GL wrong", "Incorrect category"),     # fix contradicts the comment
        ("T5", "correction", "Amount mismatch", "amount fixed", "Amount mismatch"),
    ]
    d = pd.DataFrame(rows, columns=["ticket_id", "context", "platform_code", "text", "llm_label"])
    d["comment_id"] = [f"C{i}" for i in range(len(d))]
    for col in ("event_id", "task_type", "department", "stage", "timestamp"):
        d[col] = "x"
    return d


def test_reason_code_check_statuses_and_confidence():
    r = cc.reason_code_checks(_labelled()).set_index("ticket_id")
    assert r.loc["T1", "status"] == "mismatch" and r.loc["T1", "confidence"] == "high"
    assert r.loc["T2", "status"] == "agrees"
    assert r.loc["T3", "status"] == "mismatch" and r.loc["T3", "confidence"] == "medium"
    assert r.loc["T4", "status"] == "unclear"          # no reason in the comment: not a flag
    assert r.loc["T5", "confidence"] == "low"
    assert len(r) == 5                                  # one row per rejection


def test_comment_frame_keeps_only_comments_the_check_reads():
    comments = pd.DataFrame({"comment_id": ["C1", "C2", "C3"], "ticket_id": ["T1"] * 3,
                             "event_id": ["E1", "E2", "E3"], "employee_id": "x", "timestamp": "x",
                             "text": ["qty wrong", "ok", "waiting for bank"]})
    events = pd.DataFrame({"event_id": ["E1", "E2", "E3"], "action": ["Rejected", "Approved", "DependencyWait"],
                           "change_type": ["rejection_reason", None, "dependency"],
                           "details": ["Amount mismatch", None, "Waiting"], "stage": "x"})
    tickets = pd.DataFrame({"ticket_id": ["T1"], "task_type": ["BOQ Review"], "department": ["Projects"]})
    c = cc.comment_frame(comments, events, tickets)
    assert list(c.context) == ["rejection", "hold"]
    assert c.platform_code.iloc[0] == "Amount mismatch" and pd.isna(c.platform_code.iloc[1])


def test_keyword_baseline_and_benchmark_files_are_valid():
    assert cc.keyword_label("Missing GRN, can't approve", "rejection") == "Required document missing"
    for f in cc.MESSY_FILES.values():
        b = pd.read_csv(f)
        assert set(b.context) == {"rejection", "correction", "hold"}
        allowed = {"rejection": cc.REASONS, "correction": cc.REASONS, "hold": cc.HOLD_KINDS}
        assert all(lab in allowed[c] + [cc.UNCLEAR] for c, lab in zip(b.context, b.label))


def test_sc13_scoring_counts_planted_mislabels(tmp_path):
    out, truth = tmp_path / "out", tmp_path / "truth"
    out.mkdir(), truth.mkdir()
    pd.DataFrame({"comment_id": ["C1", "C2", "C3"], "status": ["mismatch", "agrees", "mismatch"],
                  "confidence": ["high", "", "medium"]}).to_csv(out / "reason_code_checks.csv", index=False)
    pd.DataFrame({"comment_id": ["C1", "C2", "C3"], "true_label": ["Wrong quantity", "Amount mismatch",
                                                                   "Amount mismatch"],
                  "platform_reason_code": ["Amount mismatch", "Amount mismatch", "Amount mismatch"]}
                 ).to_csv(truth / "comments_truth.csv", index=False)
    s = evaluate.comment_check_score(out, truth)
    assert (s["planted"], s["flagged"], s["true_positives"]) == (1, 2, 1)
    assert s["recall"] == 1.0 and s["precision"] == 0.5 and s["high_confidence_precision"] == 1.0
    assert evaluate.comment_check_score(tmp_path, truth) is None      # not run -> out of scope
