"""Draft the structure of every SOP with the selected local LLM and run the automatic checks.

    python run_sop_drafts.py                 # all SOPs
    python run_sop_drafts.py SOP-004 SOP-016 # selected SOPs
    streamlit run app/sop_review_app.py      # then review and approve them

Drafts go to data/sop_review/drafts/, a summary to outputs/sop_drafts_summary.csv.
"""
import sys

import pandas as pd

from process_intel import config, sop
from process_intel.llm import sop_review

if __name__ == "__main__":
    wanted = {a.upper() for a in sys.argv[1:] if not a.startswith("--")}
    use_cache = "--no-cache" not in sys.argv
    rows = []
    for rec in sop.load_sops():
        if wanted and rec["sop_id"] not in wanted:
            continue
        res = sop_review.draft(rec, use_cache=use_cache)
        sop_review.save_draft(res)
        sev = pd.Series([i["severity"] for i in res["checks"]], dtype=object).value_counts()
        cmp_ = res["comparison"] or {}
        rows.append({"sop_id": rec["sop_id"], "format": rec["format"], "valid": res["draft"] is not None,
                     "steps": len(res["draft"]["steps"]) if res["draft"] else None,
                     "approvals": " > ".join(a["stage"] for a in res["draft"]["approvals"]) if res["draft"] else "",
                     "dependencies": len(res["draft"]["dependencies"]) if res["draft"] else None,
                     "errors": int(sev.get("error", 0)), "warnings": int(sev.get("warning", 0)),
                     "agreement_with_yaml": cmp_.get("overall"), "seconds": res["seconds"]})
        print(f"{rec['sop_id']}  errors={rows[-1]['errors']} warnings={rows[-1]['warnings']}  ({res['seconds']}s)", flush=True)
    out = pd.DataFrame(rows)
    out.to_csv(config.OUTPUT_DIR / "sop_drafts_summary.csv", index=False)
    print(out.to_string(index=False))
