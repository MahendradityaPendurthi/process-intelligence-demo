"""Time prediction: walk-forward evaluation of P50 / P90 duration and SLA-miss risk at ticket creation.

    python run_prediction.py                                       # outputs/sim_v2/ticket_features.csv
    python run_prediction.py --out outputs/sim_v2_holdout_s7 --months 6

Writes to --out: predictions.csv (held-out months), prediction_eval.json, prediction_calibration.csv,
prediction_features.csv (what drives the P50 model).
Run the pipeline on the data first (it produces ticket_features.csv).
"""
import argparse
import json
from pathlib import Path

import pandas as pd

from process_intel import config, predict

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--out", type=Path, default=config.OUTPUT_DIR / "sim_v2", help="pipeline output folder")
    p.add_argument("--months", type=int, default=6, help="number of final months to predict walk-forward")
    a = p.parse_args()

    x = predict.build_features(pd.read_csv(a.out / "ticket_features.csv"))
    months = sorted(x.month.unique())[-a.months:]
    preds = predict.walk_forward(x, months)
    res = predict.evaluate(preds)
    cal = predict.calibration(preds)
    last = x[x.completed_at < pd.Period(months[-1], "M").start_time]
    imp = predict.feature_importance(predict.fit(last), x[x.month == months[-1]])

    preds.to_csv(a.out / "predictions.csv", index=False)
    cal.to_csv(a.out / "prediction_calibration.csv", index=False)
    imp.to_csv(a.out / "prediction_features.csv", index=False)
    (a.out / "prediction_eval.json").write_text(json.dumps(res, indent=2), encoding="utf-8")

    print(f"{res['tickets']} tickets predicted in {months[0]}..{months[-1]} (each month by a model trained on "
          "tickets completed before it)")
    for k in ("duration", "sla_risk"):
        print(pd.DataFrame(res[k]).T.to_string())
    print(pd.DataFrame(res["by_month"]).T.to_string())
    print(cal.to_string(index=False))
    print(imp.head(8).to_string(index=False))
