"""Entry point.

    python run_pipeline.py                                              # data/raw -> outputs/
    python run_pipeline.py --raw data/simulated/v2/raw --out outputs/sim_v2
"""
import argparse
from pathlib import Path

from process_intel import config
from process_intel.pipeline import run

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--raw", type=Path, default=config.RAW_DIR, help="folder with the four raw CSVs")
    p.add_argument("--out", type=Path, default=config.OUTPUT_DIR, help="output folder")
    a = p.parse_args()
    processed = config.PROCESSED_DIR if a.out == config.OUTPUT_DIR else a.out / "processed"
    run(raw_dir=a.raw, processed_dir=processed, output_dir=a.out)
