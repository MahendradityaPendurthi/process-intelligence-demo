"""LLM benchmark: rebuild SOP-013..021 from their prose and score against the hidden YAML (answer key).

Only fields the prose can support are scored:
    steps         every step whose identifier appears in the prose: found, role, type
    approvals     stage sequence (routine, or routine + exception approvals); condition per stage
    dependencies  count; provider (word-stem match) and parallel flag (groups of 2+) per dependency
    reasons       F1 over the platform rejection reasons
    fpy           first-pass yield target within 0.5 percentage points
Overall score = mean of the five group scores. JSON validity and latency are reported separately.
"""
from __future__ import annotations

import re
from collections import defaultdict
from difflib import SequenceMatcher

import pandas as pd

from .. import config, sop
from .sop_extract import ExtractedSOP, extract

GROUPS = ["steps", "approvals", "dependencies", "reasons", "fpy"]


def _same_party(pred: str, gold: str) -> bool:
    """Provider names match if any word of 3+ letters shares its first 4 letters with a word in the key
    ('Issuer / BGV agency' ~ 'issuing institution or background verification agency')."""
    gw = {w[:4] for w in re.findall(r"[a-z]{3,}", gold.lower())}
    return any(w[:4] in gw for w in re.findall(r"[a-z]{3,}", pred.lower()))


def _seq(seq) -> str:
    return " ".join(f"{r[:3]}/{t[:4]}" for r, t in seq)


def _mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs) if xs else 1.0


def score(pred: ExtractedSOP | None, gold: dict, body: str, id_free: bool = False) -> dict:
    """Return group scores (0..1) and per-field details for one SOP.

    `body` is always the official SOP prose: it decides which steps the text evidences. With `id_free`
    (the messy rewrites carry no S1/A1/D1 labels) steps are aligned by order on (role, type) and
    dependencies are matched by provider instead of by identifier.
    """
    if pred is None:
        return {**{g: 0.0 for g in GROUPS}, "overall": 0.0, "detail": "invalid output"}
    detail = []

    # steps: only those the official prose names by identifier
    evidenced = [s for s in gold["steps"] if re.search(rf"\b{re.escape(s['step_id'])}\b", body)]
    if id_free:
        # decision branch points are never written as steps in the prose: neither credited nor penalised
        g_seq = [(s["role"], s["type"]) for s in evidenced if s["type"] != "decision"]
        p_seq = [(p.role, p.type) for p in pred.steps if p.type != "decision"]
        steps = SequenceMatcher(None, g_seq, p_seq, autojunk=False).ratio()   # 2*matches / (len_g + len_p)
        if steps < 1:
            detail.append(f"steps: gold {len(g_seq)} {_seq(g_seq)}, got {len(p_seq)} {_seq(p_seq)}")
    else:
        by_id = {p.step_id.strip().upper(): p for p in pred.steps}
        step_scores = []
        for s in evidenced:
            p = by_id.get(s["step_id"].upper())
            found, role, typ = p is not None, p is not None and p.role == s["role"], p is not None and p.type == s["type"]
            step_scores.append((found + role + typ) / 3)
            if not (found and role and typ):
                detail.append(f"{s['step_id']}: gold {s['role']}/{s['type']}, got "
                              + (f"{p.role}/{p.type}" if p else "missing"))
        steps = _mean(step_scores)

    # approvals: the routine matrix, optionally plus the approvals that exceptions add (conditional).
    # Both readings of the prose are correct, so either one scores in full.
    rank = {"Incharge": 0, "Lead": 1, "HOD": 2}
    routine = [(m["stage"], str(m["condition"]).strip().lower() == "always") for m in gold["approval_matrix"]]
    extra = {x["adds_approval"] for x in gold.get("exceptions") or [] if x.get("adds_approval")}
    with_exc = sorted(routine + [(s, False) for s in extra - {s for s, _ in routine}], key=lambda x: rank[x[0]])
    p_app = [(a.stage, a.condition.strip().lower() in ("always", "", "none")) for a in pred.approvals]
    approvals, g_app = 0.0, routine
    for variant in (routine, with_exc):
        if [s for s, _ in variant] == [s for s, _ in p_app]:
            cond = _mean(float(ga == pa) for (_, ga), (_, pa) in zip(variant, p_app))
            if (1 + cond) / 2 >= approvals:
                approvals, g_app = (1 + cond) / 2, variant
    if approvals < 1:
        detail.append(f"approvals: gold {routine} (+ exception approvals {sorted(extra)}), got {p_app}")

    # dependencies
    g_dep = gold.get("dependencies") or []
    count_ok = float(len(pred.dependencies) == len(g_dep))
    if g_dep:
        p_dep = {d.dep_id.strip().upper(): d for d in pred.dependencies}
        unused = list(pred.dependencies)
        # "parallel" only means something when a group holds two or more dependencies
        sizes = defaultdict(int)
        for d in g_dep:
            sizes[d.get("parallel_group")] += 1
        prov, par = [], []
        for d in g_dep:
            if id_free:   # first unused prediction from the same party
                p = next((x for x in unused if _same_party(x.provider, str(d["provider"]))), None)
                if p is not None:
                    unused.remove(p)
            else:
                p = p_dep.get(str(d["id"]).upper())
            gold_par = bool(d.get("parallel_group")) and sizes[d.get("parallel_group")] > 1
            prov.append(float(p is not None and _same_party(p.provider, str(d["provider"]))))
            if gold_par:                    # single-member groups: either answer is right, not scored
                par.append(float(p is not None and bool(p.parallel_group)))
        dependencies = (count_ok + _mean(prov) + _mean(par)) / 3
    else:
        dependencies = count_ok
    if dependencies < 1:
        detail.append(f"dependencies: gold {[(d['id'], d['provider'], d.get('parallel_group')) for d in g_dep]}, "
                      f"got {[(d.dep_id, d.provider, d.parallel_group) for d in pred.dependencies]}")

    # rework reasons
    g_r = {t["reason"] for t in gold["rework_triggers"]}
    p_r = set(pred.rework_reasons)
    tp = len(g_r & p_r)
    reasons = 2 * tp / (len(g_r) + len(p_r)) if (g_r or p_r) else 1.0
    if reasons < 1:
        detail.append(f"reasons: missing {sorted(g_r - p_r)}, extra {sorted(p_r - g_r)}")

    # first-pass yield target
    g_fpy, p_fpy = float(gold["expected_first_pass_yield"]), pred.first_pass_yield_target
    if p_fpy is not None and p_fpy > 1:
        p_fpy = p_fpy / 100
    fpy = float(p_fpy is not None and abs(p_fpy - g_fpy) <= 0.005)
    if not fpy:
        detail.append(f"fpy: gold {g_fpy}, got {pred.first_pass_yield_target}")

    out = {"steps": steps, "approvals": approvals, "dependencies": dependencies, "reasons": reasons, "fpy": fpy}
    out["overall"] = _mean(out.values())
    out["evidenced_steps"] = len(evidenced)
    out["detail"] = "; ".join(detail)
    return out


MESSY_DIR = config.ROOT / "data" / "benchmark" / "sop_messy"


def run(models: list[str], use_cache: bool = True,
        variants: tuple[str, ...] = ("clean", "messy")) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return (per variant x model x SOP rows, per variant x model summary).

    clean: the official SOP prose (step and dependency IDs present, YAML hidden).
    messy: hand-written informal rewrites in data/benchmark/sop_messy (no IDs, no tables, boilerplate noise),
           scored against the same answer key.
    """
    records = [r for r in sop.load_sops() if r["format"] == "schema" and r["data"]]
    rows = []
    for variant in variants:
        for model in models:
            for r in records:
                text = r["body"] if variant == "clean" else (MESSY_DIR / f"{r['sop_id']}.md").read_text(encoding="utf-8")
                res = extract(text, model, use_cache=use_cache)
                sc = score(res["parsed"], r["data"], r["body"], id_free=(variant == "messy"))
                rows.append({"variant": variant, "model": model, "sop_id": r["sop_id"],
                             "valid_json": res["parsed"] is not None, "seconds": round(res["seconds"], 1),
                             **{k: (round(v, 3) if isinstance(v, float) else v) for k, v in sc.items()},
                             "error": res["error"] or ""})
    detail = pd.DataFrame(rows)
    summary = detail.groupby(["variant", "model"]).agg(
        overall=("overall", "mean"), steps=("steps", "mean"), approvals=("approvals", "mean"),
        dependencies=("dependencies", "mean"), reasons=("reasons", "mean"), fpy=("fpy", "mean"),
        valid_json=("valid_json", "mean"), median_seconds=("seconds", "median"), sops=("sop_id", "count"),
    ).round(3).reset_index().sort_values(["variant", "overall", "median_seconds"], ascending=[True, False, True])
    return detail, summary
