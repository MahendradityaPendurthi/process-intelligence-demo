"""Plain-language wording: every finding gets readable text; no pipeline jargon reaches the dashboard."""
import glob

import pandas as pd
import pytest

from process_intel import config, plain

JARGON = ["DependencyWait", "WIP", "p10", "p90", "C1=", "C3=", "..", "first-pass", "�", "schema"]
FILES = glob.glob(str(config.OUTPUT_DIR / "**" / "deviations.csv"), recursive=True)


def test_formatters():
    assert plain.months("2026-02", "2026-03") == "Feb–Mar 2026"
    assert plain.months("2025-10", "2026-09") == "Oct 2025 – Sep 2026"
    assert plain.window("2026-02-01..2026-03-31") == "Feb–Mar 2026"
    assert plain.hours(0.5) == "30 min" and plain.hours(2.26) == "2.3 h"
    assert plain.entity("Expense Approval:Incharge:2026-02..2026-03") == "Expense Approval · Incharge · Feb–Mar 2026"
    assert plain.entity("Purchase Request:C1=fewer") == "Purchase Request · missing approval"
    assert plain.ticket_cause("Approval wait at Lead stage") == "Waiting for the Lead's approval"
    assert plain.found("74/74 planted mislabels flagged, precision 95%, recall 100%").startswith("Caught all 74")
    assert plain.verdict("control_pass") == "✅ Correctly not flagged"


@pytest.mark.skipif(not FILES, reason="no pipeline outputs")
def test_every_finding_reads_plainly():
    dev = pd.concat([pd.read_csv(f) for f in FILES])
    rows = dev[dev.level != "ticket"].drop_duplicates(["deviation_type", "entity_id"])
    for r in rows.itertuples():
        e = plain.explain(r)
        text = " ".join(e["points"] + [e["cause"], e["action"]])
        assert e["title"] and e["points"], r.deviation_type
        assert not [j for j in JARGON if j in text], (r.deviation_type, text)
    # department-level SLA findings never name an individual
    for r in rows[rows.deviation_type == "SLA_DETERIORATION"].itertuples():
        assert "E1" not in plain.explain(r)["cause"]


def test_unexpected_shape_falls_back_to_cleaned_explanation():
    r = pd.DataFrame([{"deviation_type": "SOMETHING_NEW", "entity_id": "X", "evidence": "not json",
                       "explanation": "Took 2.50h (schema §3.1).", "dominant_cause": None,
                       "recommended_investigation": None, "confidence": None, "classification": "process",
                       "observed": 1, "expected": 1, "ratio": 1}]).iloc[0]
    e = plain.explain(r)
    assert e["points"] == ["Took 2.5 h."] and e["kind"] == "Process issue"
