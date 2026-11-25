"""Phase 2: LLM benchmark scoring (offline) and the SOP-driven simulator."""
import datetime as dt

import pandas as pd
import pytest

from process_intel import config, ingestion, sop
from process_intel.llm import benchmark
from process_intel.llm.sop_extract import Approval, ExtractedSOP
from process_intel.sim import generator


def _perfect(d):
    return ExtractedSOP(
        sop_id=d["sop_id"], title=d["title"],
        steps=[{k: s[k] for k in ("step_id", "name", "role", "type")} for s in d["steps"]],
        approvals=[{"stage": m["stage"], "condition": str(m["condition"])} for m in d["approval_matrix"]],
        dependencies=[{"dep_id": x["id"], "provider": x["provider"], "item": x["item"],
                       "parallel_group": x.get("parallel_group")} for x in d["dependencies"] or []],
        rework_reasons=[t["reason"] for t in d["rework_triggers"]],
        first_pass_yield_target=d["expected_first_pass_yield"])


@pytest.fixture(scope="module")
def schema_sops():
    return [r for r in sop.load_sops() if r["format"] == "schema" and r["data"]]


def test_perfect_extraction_scores_one(schema_sops):
    for r in schema_sops:
        assert benchmark.score(_perfect(r["data"]), r["data"], r["body"])["overall"] == 1.0


def test_perfect_extraction_scores_one_without_ids(schema_sops):
    for r in schema_sops:
        p = _perfect(r["data"])
        for i, s in enumerate(p.steps):          # the messy rewrites carry no identifiers
            s.step_id = f"X{i}"
        for i, d in enumerate(reversed(p.dependencies)):
            d.dep_id = f"Y{i}"
        assert benchmark.score(p, r["data"], r["body"], id_free=True)["overall"] == 1.0


def test_messy_rewrites_cover_every_sop(schema_sops):
    for r in schema_sops:
        text = (benchmark.MESSY_DIR / f"{r['sop_id']}.md").read_text(encoding="utf-8")
        assert r["sop_id"] in text
        assert not any(f"**{s['step_id']}**" in text for s in r["data"]["steps"])   # no step labels


def test_invalid_output_scores_zero(schema_sops):
    r = schema_sops[0]
    assert benchmark.score(None, r["data"], r["body"])["overall"] == 0.0


def test_scorer_penalises_extra_approval(schema_sops):
    r = next(x for x in schema_sops if x["sop_id"] == "SOP-016")
    p = _perfect(r["data"])
    p.approvals.append(Approval(stage="HOD", condition="always"))  # no SOP-016 route has an HOD
    sc = benchmark.score(p, r["data"], r["body"])
    assert sc["approvals"] == 0.0 and sc["steps"] == 1.0


@pytest.fixture(scope="module")
def sim(tmp_path_factory):
    out = tmp_path_factory.mktemp("sim")
    generator.generate(out, seed=7)
    return out


def test_simulator_writes_phase1_raw_format(sim):
    raw = ingestion.load_raw(sim / "raw")
    for name, cols in config.REQUIRED_COLUMNS.items():
        assert list(raw[name].columns[:len(cols)]) == cols or set(cols) <= set(raw[name].columns)
    t = raw["tickets"]
    assert len(t) > 3000 and t.ticket_id.is_unique
    assert set(raw["audit_logs"].ticket_id) == set(t.ticket_id)


def test_simulator_is_reproducible(sim, tmp_path):
    generator.generate(tmp_path, seed=7)
    for name in ("raw/tickets.csv", "raw/audit_logs.csv", "extra/comments.csv"):
        assert (sim / name).read_bytes() == (tmp_path / name).read_bytes()


def test_employee_on_leave_gets_no_tickets(sim):
    t = pd.read_csv(sim / "raw" / "tickets.csv", parse_dates=["created_at"])
    leave = t[(t.assigned_employee_id == "E1021")
              & t.created_at.dt.date.between(dt.date(2026, 4, 6), dt.date(2026, 4, 24))]
    assert leave.empty


def test_pipeline_finds_planted_scenarios(sim, tmp_path_factory):
    """End to end: simulate (seed 7) -> full pipeline -> score against the answer key."""
    from process_intel.pipeline import run
    from process_intel.sim import evaluate
    out = tmp_path_factory.mktemp("sim_out")
    run(raw_dir=sim / "raw", processed_dir=out / "processed", output_dir=out)
    scores, false_alarms = evaluate.evaluate(out, sim / "truth")
    s = evaluate.summarise(scores, false_alarms)
    assert s["detected"] >= 10 and s["controls_passed"] == "2/2" and s["false_alarms"] <= 1, s


def test_truth_kept_separate_and_complete(sim):
    truth = pd.read_csv(sim / "truth" / "tickets_truth.csv")
    tickets = pd.read_csv(sim / "raw" / "tickets.csv")
    assert set(truth.ticket_id) == set(tickets.ticket_id)
    assert not any("truth" in c or "scenario" in c for c in tickets.columns)
    comments = pd.read_csv(sim / "extra" / "comments.csv")
    ct = pd.read_csv(sim / "truth" / "comments_truth.csv")
    assert set(comments.comment_id) == set(ct.comment_id)
    events = pd.read_csv(sim / "raw" / "audit_logs.csv")
    assert set(comments.event_id) <= set(events.event_id)
