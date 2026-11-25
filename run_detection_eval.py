"""Score a pipeline run on simulated data against the planted scenarios (answer key).

    python run_detection_eval.py                                   # outputs/sim_v2 vs data/simulated/v2/truth
    python run_detection_eval.py --out outputs/sim_v2 --truth data/simulated/v2/truth
"""
import argparse
import json
from pathlib import Path

import pandas as pd

from process_intel import config
from process_intel.sim import evaluate

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--out", type=Path, default=config.OUTPUT_DIR / "sim_v2", help="pipeline output folder")
    p.add_argument("--truth", type=Path, default=config.ROOT / "data" / "simulated" / "v2" / "truth")
    a = p.parse_args()
    scores, false_alarms = evaluate.evaluate(a.out, a.truth)
    summary = evaluate.summarise(scores, false_alarms)
    scores.to_csv(a.out / "detection_eval.csv", index=False)
    false_alarms.to_csv(a.out / "detection_false_alarms.csv", index=False)
    (a.out / "detection_eval.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    with pd.option_context("display.width", 200, "display.max_colwidth", 60):
        print(scores[["scenario", "name", "verdict", "found_types", "found", "coverage", "ticket_flag_lift"]]
              .to_string(index=False))
        print(json.dumps(summary, indent=2))
        if len(false_alarms):
            print(false_alarms[["deviation_type", "entity_id", "classification"]].to_string(index=False))
