"""SOP draft checks, review decisions and the review screen (no LLM calls: drafts are built by hand)."""
import json

import pytest

from process_intel import sop
from process_intel.llm import benchmark
from process_intel.llm import sop_review as sr


@pytest.fixture(scope="module")
def sop016():
    return next(r for r in sop.load_sops() if r["sop_id"] == "SOP-016")


def _good_draft(rec):
    d = rec["data"]
    return {"sop_id": "SOP-016", "title": d["title"],
            "steps": [{k: s[k] for k in ("step_id", "name", "role", "type")} for s in d["steps"]],
            "approvals": [{"stage": "Incharge", "condition": "always",
                           "evidence": "The Incharge approves or rejects with a reason code."}],
            "dependencies": [], "rework_reasons": [t["reason"] for t in d["rework_triggers"]],
            "first_pass_yield_target": 0.95}


@pytest.fixture()
def review_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(sr, "REVIEW_DIR", tmp_path)
    return tmp_path


def test_grounded_draft_has_no_errors(sop016):
    issues = sr.check(_good_draft(sop016), sr.source_text(sop016))
    assert not [i for i in issues if i["severity"] == "error"], issues


def test_invented_quote_and_dependency_are_errors(sop016):
    d = _good_draft(sop016)
    d["approvals"].append({"stage": "HOD", "condition": "always", "evidence": "The HOD signs every claim."})
    d["dependencies"] = [{"dep_id": "D1", "provider": "Finance", "item": "budget", "parallel_group": None,
                          "evidence": "Compute the reimbursable amount and submit."}]
    msgs = {i["message"] for i in sr.check(d, sr.source_text(sop016)) if i["severity"] == "error"}
    assert "Quoted evidence is not in the text" in msgs
    assert "The text says there is no external dependency" in msgs


def test_glossary_only_approver_is_flagged(sop016):
    messy = (benchmark.MESSY_DIR / "SOP-016.md").read_text(encoding="utf-8")
    d = _good_draft(sop016)
    d["approvals"] = [{"stage": "Incharge", "condition": "always", "evidence": "The Incharge\nthen approves or rejects"},
                      {"stage": "HOD", "condition": "always",
                       "evidence": "HOD – department head with\ndelegated approval authority."}]
    hod = [i for i in sr.check(d, messy) if i["item"].startswith("HOD")]
    assert any("generic section" in i["message"] for i in hod), hod


def test_quote_naming_another_approver_is_an_error(sop016):
    d = _good_draft(sop016)
    d["approvals"].append({"stage": "Lead", "condition": "always",
                           "evidence": "The Incharge approves or rejects with a reason code."})
    issues = sr.check(d, sr.source_text(sop016))
    assert any(i["item"].startswith("Lead") and i["severity"] == "error" for i in issues)   # quote names no Lead


def test_raci_row_supports_role_in_its_column_header(sop016):
    """Quoting a RACI cell ('A (exceptions only)') supports the Lead named in the column header,
    and the condition in the cell is noticed."""
    d = _good_draft(sop016)
    d["approvals"].append({"stage": "Lead", "condition": "always", "evidence": "A (exceptions only)"})
    lead = [i for i in sr.check(d, sr.source_text(sop016)) if i["item"].startswith("Lead")]
    assert not [i for i in lead if i["severity"] == "error"], lead
    assert any("states a condition" in i["message"] for i in lead)


def test_approval_with_errors_needs_override_and_note(sop016, review_dir):
    d = _good_draft(sop016)
    d["rework_reasons"] = []          # fine
    d["approvals"][0]["evidence"] = "made up"
    with pytest.raises(ValueError, match="open errors"):
        sr.decide("SOP-016", "approved", "Asha", d)
    dec = sr.decide("SOP-016", "approved", "Asha", d, notes="checked with the process owner", override=True)
    assert dec["override_errors"] and (review_dir / "approved" / "SOP-016.json").exists()
    sr.decide("SOP-016", "rejected", "Asha", d, notes="wrong")
    assert not (review_dir / "approved" / "SOP-016.json").exists()
    log = [json.loads(x) for x in (review_dir / "review_log.jsonl").read_text(encoding="utf-8").splitlines()]
    assert [x["status"] for x in log] == ["approved", "rejected"]


def test_reviewer_required_and_stale_detection(sop016, review_dir):
    with pytest.raises(ValueError, match="reviewer"):
        sr.decide("SOP-016", "approved", " ", _good_draft(sop016))
    sr.decide("SOP-016", "approved", "Asha", _good_draft(sop016))
    assert sr.status_of(sop016) == "approved"
    path = review_dir / "decisions" / "SOP-016.json"
    dec = json.loads(path.read_text(encoding="utf-8"))
    dec["source_sha256"] = "0" * 64                        # the SOP text changed since the decision
    path.write_text(json.dumps(dec), encoding="utf-8")
    assert sr.status_of(sop016) == "stale"


def test_review_app_renders_and_approves(sop016, review_dir):
    from streamlit.testing.v1 import AppTest
    sr.save_draft({"sop_id": "SOP-016", "file": sop016["file"], "format": "schema", "model": "test",
                   "source_sha256": "", "drafted_at": "", "seconds": 0, "error": None,
                   "draft": _good_draft(sop016), "checks": [], "comparison": None})
    at = AppTest.from_file("app/sop_review_app.py", default_timeout=60)
    at.run()
    assert not at.exception
    at.sidebar.radio(key="sop").set_value("SOP-016").run()
    at.sidebar.text_input(key="reviewer").set_value("Asha").run()
    next(b for b in at.button if b.key == "ok_SOP-016").click().run()
    assert not at.exception
    assert json.loads((review_dir / "decisions" / "SOP-016.json").read_text(encoding="utf-8"))["status"] == "approved"
