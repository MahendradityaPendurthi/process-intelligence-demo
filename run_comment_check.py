"""LLM comment check: label rejection / correction / hold comments, then compare with the platform record.

    python run_comment_check.py                                  # data/simulated/v2 -> outputs/sim_v2
    python run_comment_check.py --data data/simulated/v2_holdout_s7 --out outputs/sim_v2_holdout_s7
    python run_comment_check.py --benchmark-only                 # just the hand-written messy comments

Writes to --out: comment_labels.csv, reason_code_checks.csv, reason_counts.csv, hold_kinds.csv,
comment_check.json, and (when the data has an answer key) comment_label_accuracy.csv.
"""
import argparse
import json
import sys
import time
from pathlib import Path

import pandas as pd

from process_intel import config, sop
from process_intel.llm import comment_check as cc
from process_intel.llm.sop_review import selected_model


def progress(i, n, ctx, txt, r):
    if not r["cached"] and (i % 25 == 0 or i == n):
        print(f"  {i}/{n} labelled ({ctx}: {r['seconds']:.1f}s)", flush=True)


def benchmark(model, out: Path, use_cache: bool) -> dict:
    b = cc.messy_benchmark(model, use_cache)
    b.to_csv(out / "comment_benchmark_messy.csv", index=False)
    b = b.assign(llm=b.llm_label == b.label, kw=b.keyword_label == b.label)
    res = {}
    for name, g in b.groupby("set"):
        acc = g.groupby("context")[["llm", "kw"]].mean().round(3)
        res[name] = {"items": len(g), "llm_accuracy": round(float(g.llm.mean()), 3),
                     "keyword_accuracy": round(float(g.kw.mean()), 3),
                     "by_context": acc.rename(columns={"llm": "llm_accuracy", "kw": "keyword_accuracy"})
                     .to_dict("index")}
    print("Messy hand-written comments:", json.dumps(res, indent=2))
    wrong = b[b.llm_label != b.label]
    if len(wrong):
        print(wrong[["set", "context", "text", "label", "llm_label"]].to_string(index=False))
    return res


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--data", type=Path, default=config.ROOT / "data" / "simulated" / "v2")
    p.add_argument("--out", type=Path, default=config.OUTPUT_DIR / "sim_v2")
    p.add_argument("--model", default=None)
    p.add_argument("--no-cache", action="store_true")
    p.add_argument("--benchmark-only", action="store_true")
    a = p.parse_args()
    model = a.model or selected_model()
    a.out.mkdir(parents=True, exist_ok=True)
    data = a.data.resolve()
    report = {"model": model,
              "data": data.relative_to(config.ROOT).as_posix() if data.is_relative_to(config.ROOT) else data.name}

    report["messy_benchmark"] = benchmark(model, a.out, not a.no_cache)
    if a.benchmark_only:
        sys.exit(0)

    t0 = time.perf_counter()
    comments, events, tickets = cc.load_dataset(a.data)
    c = cc.comment_frame(comments, events, tickets)
    print(f"{len(c)} comments to read ({c.text.nunique()} distinct texts) with {model}")
    lab = cc.label_comments(c, model, not a.no_cache, progress)
    checks = cc.reason_code_checks(lab)
    sops = {r["data"]["task_type"]: r["data"] for r in sop.load_sops() if r["format"] == "schema"}
    holds = cc.hold_kinds(lab, sops)

    lab.drop(columns=["llm_seconds", "llm_cached"]).to_csv(a.out / "comment_labels.csv", index=False)
    checks.to_csv(a.out / "reason_code_checks.csv", index=False)
    cc.reason_counts(checks).to_csv(a.out / "reason_counts.csv", index=False)
    holds.to_csv(a.out / "hold_kinds.csv", index=False)
    report["summary"] = cc.summary(checks, holds)
    report["llm_errors"] = int(lab.llm_error.notna().sum())
    report["seconds"] = round(time.perf_counter() - t0, 1)

    truth = a.data / "truth" / "comments_truth.csv"
    if truth.exists():
        acc = cc.score_labels(lab, pd.read_csv(truth))
        acc.to_csv(a.out / "comment_label_accuracy.csv", index=False)
        report["label_accuracy"] = acc.set_index("context").to_dict("index")
        print(acc.to_string(index=False))
    (a.out / "comment_check.json").write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    print(cc.reason_counts(checks).to_string(index=False))
    print(holds.to_string(index=False))
