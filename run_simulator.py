"""Generate the SOP-driven simulated dataset (v2) with planted scenarios.

    python run_simulator.py                                        # -> data/simulated/v2 (seed 2026)
    python run_simulator.py data/simulated/v2_holdout --seed 99    # independent hold-out draw
    python run_pipeline.py --raw data/simulated/v2/raw --out outputs/sim_v2
"""
import argparse
from pathlib import Path

from process_intel import config
from process_intel.sim import generator

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("out", nargs="?", type=Path, default=config.ROOT / "data" / "simulated" / "v2")
    p.add_argument("--seed", type=int, default=2026)
    a = p.parse_args()
    for name, n in generator.generate(a.out, seed=a.seed).items():
        print(f"{n:>8,}  {name}")
