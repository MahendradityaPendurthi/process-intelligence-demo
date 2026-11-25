"""Stage 5 conformance checks C1-C7, and an end-to-end run of all 7 stages."""
import hashlib
import json
from types import SimpleNamespace

import pandas as pd
import pytest

from process_intel import config, conformance, ingestion, sop
from tests.conftest import normalized


@pytest.fixture(scope="module")
def sops():
    _, valid = sop.validate_sops(sop.load_sops(), ingestion.load_raw()["task_types"])
    return valid


def ticket(task_type, approval_count, dependency_count, band="within", created="2026-08-01 09:00:00"):
    return SimpleNamespace(ticket_id="T1", task_type=task_type, approval_count=approval_count,
                           dependency_count=dependency_count, sop_band=band, created_at=pd.Timestamp(created))


def run_check(sops, t, rows):
    d = sops[t.task_type]
    prior = sop.ticket_prior(sops, t.task_type, t.approval_count, t.dependency_count)
    return conformance.check_ticket(t, normalized(rows), d, prior, sop.rework_trigger_map(sops))


PATH = [("Created", "09:00", "E1", "Executor"), ("Assigned", "09:05", "E1", "Executor"),
        ("Submitted", "10:00", "E1", "Executor"), ("DependencyWait", "10:10", "E1", "Executor"),
        ("Approved", "11:00", "M1", "Incharge")]


def test_conformant_ticket(sops):
    res = run_check(sops, ticket("BOQ Review", 1, 1), PATH)
    assert res["c1_approvals"] == "ok" and res["c3_dependency_wait"] == "none"
    assert res["c4_required_actions"] == "ok" and res["c6_rejection_reasons"] == "n/a"
    assert res["fitness"] == 1.0


def test_missing_hod_approval_is_fewer(sops):
    rows = PATH + [("Approved", "12:00", "L1", "Lead")]
    res = run_check(sops, ticket("Vendor Onboarding", 3, 2), rows)
    assert res["c1_approvals"] == "fewer"
    assert res["required_approval_stages"] == "Incharge>Lead>HOD"
    assert res["observed_approval_stages"] == "Incharge>Lead"


def test_unrequired_approval_and_undeclared_hold(sops):
    res = run_check(sops, ticket("Daily Operations Report", 0, 0), PATH)
    assert res["c1_approvals"] == "more"
    assert res["c3_dependency_wait"] == "undeclared"
    assert res["fitness"] < 1.0


def test_rejection_reason_mapped_to_control(sops):
    rows = PATH[:3] + [("Rejected", "10:30", "M1", "Incharge", "rejection_reason", "Amount mismatch"),
                       ("Updated", "10:45", "E1", "Executor", "correction", "Amount mismatch"),
                       ("Resubmitted", "11:00", "E1", "Executor"), ("Approved", "11:30", "M1", "Incharge")]
    res = run_check(sops, ticket("Invoice Verification", 1, 1), rows)
    assert res["c6_rejection_reasons"] == "ok"
    assert res["rework_trigger_codes"] == "RW-AMT"
    assert res["preventable_by"] == "S3 three-way match"


def test_unknown_reason_and_missing_submission(sops):
    rows = [PATH[0], PATH[1], ("Rejected", "10:30", "M1", "Incharge", "rejection_reason", "Typo"),
            ("Approved", "11:30", "M1", "Incharge")]
    res = run_check(sops, ticket("Invoice Verification", 1, 1), rows)
    assert res["c6_rejection_reasons"] == "unmapped:Typo"
    assert res["c4_required_actions"] == "missing:SUBMITTED"


def test_retrospective_vs_in_force(sops):
    events = normalized(PATH)
    f = pd.DataFrame([
        {"ticket_id": "T1", "task_type": "BOQ Review", "department": "Procurement", "assigned_employee_id": "E1",
         "completed_month": "2026-08", "approval_count": 1, "dependency_count": 1, "sop_band": "within",
         "created_at": pd.Timestamp("2026-08-01")},
        {"ticket_id": "T2", "task_type": "BOQ Review", "department": "Procurement", "assigned_employee_id": "E1",
         "completed_month": "2026-11", "approval_count": 1, "dependency_count": 1, "sop_band": "within",
         "created_at": pd.Timestamp("2026-11-01")},
    ])
    events2 = pd.concat([events, events.assign(ticket_id="T2", event_id=events.event_id + "b")])
    out = conformance.check_all(f, events2, sops).set_index("ticket_id")
    assert out.loc["T1", "conformance_mode"] == "retrospective"
    assert out.loc["T2", "conformance_mode"] == "in_force"


def test_end_to_end_seven_stages(tmp_path):
    from process_intel import pipeline
    raw_hash = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in config.RAW_DIR.glob("*.csv")}
    r = pipeline.run(output_dir=tmp_path / "out", processed_dir=tmp_path / "proc")
    out = tmp_path / "out"
    for name in ["sop_validation_report.csv", "sop_parameters.csv", "data_quality_report.csv",
                 "ticket_lifecycles.csv", "ticket_features.csv", "sop_time_complexity.csv",
                 "sop_effort_coverage.csv", "conformance.csv", "deviations.csv", "demo_report.md", "technical_report.md",
                 "deviation_report.md", "run_manifest.json"]:
        assert (out / name).exists(), name
    devs = r["deviations"]
    assert devs.dominant_cause.astype(str).str.len().gt(0).all()
    assert devs.reason_source.isin(["sop", "baseline", "baseline+sop"]).all()
    hod = devs[(devs.deviation_type == "SOP_NONCONFORMANCE") & devs.entity_id.str.startswith("Vendor Onboarding:C1")]
    assert (hod.classification == "platform_logging").all() and len(hod) == 1
    manifest = json.loads((out / "run_manifest.json").read_text())
    assert len(manifest["sops_used"]) == 9 and manifest["cs_spearman_rho"] > 0.8
    assert raw_hash == {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in config.RAW_DIR.glob("*.csv")}
    assert "underperform" not in (out / "deviation_report.md").read_text(encoding="utf-8").lower()
