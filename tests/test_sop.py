"""Stages 1-2: SOP parsing, validation, complexity score and expected-time priors."""
import copy
import math

import pytest

from process_intel import config, ingestion, sop


@pytest.fixture(scope="module")
def task_types():
    return ingestion.load_raw()["task_types"]


@pytest.fixture(scope="module")
def repo_sops(task_types):
    report, valid = sop.validate_sops(sop.load_sops(), task_types)
    return report, valid


def test_repo_sops_all_valid(repo_sops, task_types):
    report, valid = repo_sops
    errors = report[(report.severity == "error") & (report.status == "fail")]
    assert errors.empty, errors.to_string()
    assert set(valid) == set(task_types.task_type)


def test_legacy_sops_listed_not_parsed(repo_sops):
    report, _ = repo_sops
    legacy = report[report.check == "legacy_free_text_sop"]
    assert len(legacy) == 12 and (legacy.status == "pass").all()


@pytest.mark.parametrize("task_type,cs,label", [
    ("BOQ Review", 12.5, "Medium"), ("Purchase Request", 16.25, "Medium"), ("Invoice Verification", 15.3, "Medium"),
    ("Expense Approval", 8.5, "Simple"), ("Vendor Onboarding", 26.0, "Complex"),
    ("Daily Operations Report", 8.75, "Simple"), ("Incident Review", 22.1429, "Complex"),
    ("Leave Approval", 8.0, "Simple"), ("Employee Document Verification", 14.6, "Medium"),
])
def test_complexity_score_matches_hand_calculation(repo_sops, task_type, cs, label):
    res = sop.complexity_score(repo_sops[1][task_type])
    assert res["cs"] == pytest.approx(cs, abs=1e-3)
    assert res["complexity_derived"] == label


def test_pert():
    assert sop.pert({"min": 1, "likely": 2, "max": 9}) == pytest.approx((3.0, (8 / 6) ** 2))


def test_clark_max_properties():
    m, v = sop.clark_max(1.0, 1.0, 1.0, 1.0)            # max of two iid N(1,1)
    assert m == pytest.approx(1 + 1 / math.sqrt(math.pi), rel=1e-6)
    assert v < 1.0
    m, _ = sop.clark_max(10.0, 0.01, 1.0, 0.01)         # dominated by the larger
    assert m == pytest.approx(10.0, abs=1e-6)
    assert sop.clark_max(2.0, 0.0, 3.0, 0.0) == (3.0, 0.0)


def test_parallel_dependencies_cost_less_than_sequential(repo_sops):
    d = repo_sops[1]["Vendor Onboarding"]
    parallel = sop._prior(d, 3, 2)
    seq = copy.deepcopy(d)
    seq["dependencies"][1]["parallel_group"] = "P2"
    sequential = sop._prior(seq, 3, 2)
    assert parallel["e_wait_h"] < sequential["e_wait_h"]
    longest = max(sop.pert(x["typical_wait_h"])[0] for x in d["dependencies"])
    total = sum(sop.pert(x["typical_wait_h"])[0] for x in d["dependencies"])
    dep_part = parallel["e_wait_h"] - (sequential["e_wait_h"] - total)
    assert longest <= dep_part < total


def test_conditional_approval_routed_from_ticket(repo_sops):
    d = repo_sops[1]["Daily Operations Report"]
    none = sop._prior(d, 0, 0)
    one = sop._prior(d, 1, 0)
    assert none["required_approvals"] == 0 and one["required_stages"] == "Incharge"
    assert "approval_route_from_ticket" in none["estimate_flags"]
    assert one["e_elapsed_h"] > none["e_elapsed_h"]


def test_band_contains_expected(repo_sops):
    for d in repo_sops[1].values():
        p = sop._prior(d, d["approval_count_base"], d["dependency_count"])
        assert 0 <= p["p10_h"] <= p["e_elapsed_h"] <= p["p90_h"]
        assert p["e_effort_exec_h"] <= p["e_effort_h"]


def _write_sop(tmp_path, name, text):
    (tmp_path / name).write_text(text, encoding="utf-8")


def test_validation_catches_inconsistencies(tmp_path, task_types):
    src = (config.SOP_DIR / "SOP-016_Expense_Approval.md").read_text(encoding="utf-8")
    bad = src.replace("sop_steps: 3", "sop_steps: 4").replace("reason: Amount mismatch", "reason: Typo in amount")
    _write_sop(tmp_path, "SOP-016_Expense_Approval.md", bad)
    _write_sop(tmp_path, "SOP-001_Legacy.md", "# Legacy SOP\nplain text")
    report, valid = sop.validate_sops(sop.load_sops(tmp_path), task_types)
    failed = set(report[report.status == "fail"].check)
    assert {"sop_steps_matches_task_types", "sop_steps_equals_counted_work_steps",
            "rework_reasons_in_platform_vocabulary", "every_task_type_has_sop"} <= failed
    assert valid == {}                                     # an SOP with errors is not used


def test_broken_yaml_reported_not_raised(tmp_path, task_types):
    _write_sop(tmp_path, "SOP-099_Broken.md", "---\nsop_id: SOP-099\nsteps: [unclosed\n---\nbody")
    report, valid = sop.validate_sops(sop.load_sops(tmp_path), task_types)
    row = report[report.check == "yaml_parses"].iloc[0]
    assert row.status == "fail" and valid == {}
