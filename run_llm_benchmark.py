"""Benchmark local LLMs on SOP extraction and pick the model for Phase 2.

    python run_llm_benchmark.py                       # default candidates
    python run_llm_benchmark.py llama3.1:8b granite4.1:8b
    python run_llm_benchmark.py --no-cache ...        # force fresh LLM calls
"""
import json
import sys

from process_intel import config
from process_intel.llm import benchmark

DEFAULT_MODELS = ["granite4.1:8b", "ministral-3:8b", "llama3.1:latest"]


def main() -> None:
    args = sys.argv[1:]
    use_cache = "--no-cache" not in args
    models = [a for a in args if not a.startswith("--")] or DEFAULT_MODELS
    detail, summary = benchmark.run(models, use_cache=use_cache)
    out = config.OUTPUT_DIR / "llm"
    out.mkdir(parents=True, exist_ok=True)
    detail.to_csv(out / "llm_benchmark_detail.csv", index=False)
    summary.to_csv(out / "llm_benchmark_summary.csv", index=False)
    # selection: mean of the clean and messy scores; ties go to the faster model
    rank = (summary.pivot(index="model", columns="variant", values="overall")
            .assign(combined=lambda d: d.mean(axis=1),
                    median_seconds=detail.groupby("model").seconds.median())
            .sort_values(["combined", "median_seconds"], ascending=[False, True]).round(3))
    winner = rank.index[0]
    (out / "selected_model.json").write_text(json.dumps({
        "model": winner, "combined": float(rank.combined.iloc[0]),
        "by_variant": {k: float(v) for k, v in rank.iloc[0].drop(["combined", "median_seconds"]).items()},
        "median_seconds": float(rank.median_seconds.iloc[0]), "ranking": rank.reset_index().to_dict("records"),
        "task": "SOP structure extraction from prose (SOP-013..021): official text and messy rewrites",
    }, indent=2), encoding="utf-8")
    print(summary.to_string(index=False))
    print("\n" + rank.to_string())
    print(f"\nselected: {winner}")


if __name__ == "__main__":
    main()
