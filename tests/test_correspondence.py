"""Stage 3b: the SOP-log correspondence gate catches logs that are a different process."""
import shutil

import pandas as pd
import pytest

from process_intel import config, correspondence, features, ingestion, lifecycle, normalization, sop
from tests.conftest import normalized


@pytest.fixture(scope="module")
def sops():
    _, valid = sop.validate_sops(sop.load_sops(), ingestion.load_raw()["task_types"])
    return valid


@pytest.fixture(scope="module")
def real():
    raw = ingestion.load_raw()
    ev, _ = normalization.normalize_events(raw["audit_logs"], raw["employees"])
    lc, _ = lifecycle.reconstruct_all(ev)
    return features.build_ticket_features(raw["tickets"], lc), ev


def model(sops, task_type, approvals, deps):
    return correspondence._model(sops[task_type], approvals, deps, sops)


PATH = [("Created", "09:00", "E1", "Executor"), ("Assigned", "09:05", "E1", "Executor"),
        ("Submitted", "10:00", "E1", "Executor"), ("DependencyWait", "10:10", "E1", "Executor"),
        ("Approved", "11:00", "M1", "Incharge")]


def replay(sops, rows, task_type="Invoice Verification", approvals=1, deps=1, dept="Finance"):
    return correspondence.replay(normalized(rows), dept, model(sops, task_type, approvals, deps))


def test_matching_path_fits(sops):
    assert replay(sops, PATH) == ("fits", [])


def test_forbidden_hold_is_known_deviation_not_other_process(sops):
    status, issues = replay(sops, PATH, "Expense Approval", 1, 0)
    assert status == "fits_with_known_deviations" and issues == ["hold_not_allowed_by_sop"]


def test_missing_required_approval_is_known_deviation(sops):
    ev = normalized(PATH + [("Approved", "12:00", "L1", "Lead")]).assign(department="Procurement")
    status, issues = correspondence.replay(ev, "Procurement", model(sops, "Vendor Onboarding", 3, 2))
    assert status == "fits_with_known_deviations" and "approvals_fewer_than_sop" in issues


@pytest.mark.parametrize("rows,dept,expect", [
    (PATH + [("Approved", "12:00", "L1", "Lead")], "Finance", "approval_by_Lead_not_in_sop"),   # stage SOP lacks
    (PATH, "HR", "ticket_department_HR_not_Finance"),                                          # other department
    (PATH[:3] + [("Rejected", "10:30", "L1", "Lead", "rejection_reason", "Amount mismatch")]
     + [("Updated", "10:40", "E1", "Executor"), ("Resubmitted", "10:50", "E1", "Executor"),
        ("Approved", "11:00", "M1", "Incharge")], "Finance", "rejected_by_Lead_not_a_detector"),
    ([PATH[0], PATH[1], ("Approved", "09:30", "M1", "Incharge"), ("Submitted", "10:00", "E1", "Executor")],
     "Finance", "approved_during_work"),                                                      # approved before submit
    ([("Assigned", "09:00", "E1", "Executor"), ("Created", "09:05", "E1", "Executor")] + PATH[2:],
     "Finance", "intake_not_created_then_assigned"),                                          # assigned before created
])
def test_paths_from_another_process_do_not_fit(sops, rows, dept, expect):
    status, issues = replay(sops, rows, dept=dept)
    assert status == "does_not_fit"
    assert any(expect in i for i in issues), issues


def test_actor_in_wrong_role_does_not_fit(sops):
    ev = normalized(PATH)
    ev.loc[ev.event_type == "SUBMITTED", "role"] = "Incharge"
    status, issues = correspondence.replay(ev, "Finance", model(sops, "Invoice Verification", 1, 1))
    assert status == "does_not_fit" and "submitted_by_Incharge" in issues


def test_all_repo_sops_correspond_to_their_logs(sops, real):
    f, ev = real
    _, verdicts, cross = correspondence.evaluate(f, ev, sops)
    assert (verdicts.verdict == "corresponds").all(), verdicts[["task_type", "verdict", "notes"]]
    assert (verdicts.does_not_fit == 0).all()
    # time scale identifies each task type's own SOP, even where the audit path cannot
    assert (verdicts.closest_sop_by_time == verdicts.sop_id).all()
    # logs never fit an SOP of another department
    dept = {t: d["department"] for t, d in sops.items()}
    other = cross[cross.task_type.map(dept) != cross.sop_task_type.map(dept)]
    assert (other.path_score == 0).all()


def test_wrong_sop_is_rejected_by_the_gate(sops, real):
    f, ev = real
    wrong = dict(sops)
    wrong["BOQ Review"] = {**sops["Incident Review"], "task_type": "BOQ Review", "department": "Procurement"}
    _, verdicts, _ = correspondence.evaluate(f, ev, wrong)
    v = verdicts.set_index("task_type").loc["BOQ Review"]
    # Incident Review SOP (2 approvals, 2 dependencies) relabelled as BOQ Review: every BOQ ticket only "misses"
    # the Lead approval, but another Procurement SOP explains the path as well and the time scale far better.
    assert v.verdict == "does_not_correspond"
    assert v.closest_sop_by_time != v.sop_id


def test_pipeline_excludes_non_corresponding_sop(tmp_path):
    """An SOP that passes stage 1 but describes a Lead-approved process is excluded in stage 3b."""
    from process_intel import pipeline
    sop_dir = tmp_path / "sops"
    shutil.copytree(config.SOP_DIR, sop_dir)
    path = sop_dir / "SOP-013_BOQ_Review.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("  - {stage: Incharge, condition: always}", "  - {stage: Lead, condition: always}")
    text = text.replace("    name: Incharge review\n    role: Incharge", "    name: Lead review\n    role: Lead")
    path.write_text(text, encoding="utf-8")
    r = pipeline.run(output_dir=tmp_path / "out", processed_dir=tmp_path / "proc", sop_dir=sop_dir)
    srep = r["sop_report"]
    assert srep[(srep.sop_id == "SOP-013") & (srep.severity == "error") & (srep.status == "fail")].empty
    corr = r["correspondence"].set_index("task_type")
    assert corr.loc["BOQ Review", "verdict"] == "does_not_correspond"
    assert "BOQ Review" not in r["sops_used"]
    conf = r["conformance"]
    assert (conf[conf.task_type == "BOQ Review"].conformance_mode == "sop_excluded_no_correspondence").all()
    feats = r["features"]
    assert (feats[feats.task_type == "BOQ Review"].sop_band == "n/a").all()
    mismatch = r["deviations"][r["deviations"].deviation_type == "SOP_LOG_MISMATCH"]
    assert len(mismatch) == 1 and mismatch.iloc[0].classification == "sop_mismatch"
    assert "approval_by_Incharge_not_in_sop" in mismatch.iloc[0].candidate_causes
