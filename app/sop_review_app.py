"""SOP review screen: check the LLM draft of each SOP against its text, edit it, approve or reject it.

    python run_sop_drafts.py            # create the drafts first
    streamlit run app/sop_review_app.py
"""
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402
from pydantic import ValidationError  # noqa: E402

from process_intel import config, sop  # noqa: E402
from process_intel.llm import sop_review as sr  # noqa: E402

ROLES = ["Executor", "Incharge", "Lead", "HOD", "System", "External"]
TYPES = ["intake", "work", "approval", "decision", "rework"]
STAGES = ["Incharge", "Lead", "HOD"]
STATUS_ICON = {"to_review": "🟡", "approved": "✅", "changes_requested": "✏️", "rejected": "⛔", "stale": "⚠️",
               "no_draft": "⚪"}
SEV_ORDER = {"error": 0, "warning": 1, "info": 2}

st.set_page_config(page_title="SOP Review", page_icon="📋", layout="wide")


def records() -> dict:
    return {r["sop_id"]: r for r in sop.load_sops()}


def overview(recs: dict) -> pd.DataFrame:
    rows = []
    for sid, rec in recs.items():
        d = sr.load_draft(sid)
        dec = sr.load_decision(sid)
        current = dec["structure"] if dec and sr.status_of(rec) != "stale" else (d or {}).get("draft")
        issues = sr.check(current, sr.source_text(rec)) if current else []     # always the current rules
        rows.append({"SOP": sid, "status": sr.status_of(rec), "format": rec["format"],
                     "errors": sum(i["severity"] == "error" for i in issues),
                     "warnings": sum(i["severity"] == "warning" for i in issues)})
    return pd.DataFrame(rows)


def _clean(records_: list[dict]) -> list[dict]:
    out = []
    for r in records_:
        r = {k: (None if (v is None or (isinstance(v, float) and pd.isna(v)) or str(v).strip() == "") else v)
             for k, v in r.items()}
        if any(v is not None for v in r.values()):
            out.append(r)
    return out


def highlight(text: str, quotes: list[str]) -> str:
    body = html.escape(text)
    for q in sorted({q.strip() for q in quotes if q and q.strip()}, key=len, reverse=True):
        eq = html.escape(q)
        if eq in body:
            body = body.replace(eq, f"<mark>{eq}</mark>")
    # one line of HTML with <br> breaks, so the SOP's own markdown (# headings, lists) is shown as plain text
    body = body.replace("\r\n", "\n").replace("\n", "<br>")
    return (f"<div style='max-height:72vh;overflow-y:auto;font-size:0.85rem;line-height:1.5;"
            f"border:1px solid rgba(128,128,128,.35);border-radius:6px;padding:10px'>{body}</div>")


def show_issues(issues: list[dict]):
    if not issues:
        st.success("No issues found by the automatic checks.")
        return
    for i in sorted(issues, key=lambda x: SEV_ORDER[x["severity"]]):
        msg = f"**{i['field']}** {('· ' + i['item']) if i['item'] else ''} — {i['message']}"
        {"error": st.error, "warning": st.warning, "info": st.info}[i["severity"]](msg)


# --------------------------------------------------------------------------- sidebar
recs = records()
ov = overview(recs)
with st.sidebar:
    st.header("SOP review")
    reviewer = st.text_input("Reviewer name", key="reviewer")
    only_open = st.checkbox("Only SOPs still to review", value=False)
    view = ov[ov.status.isin(["to_review", "changes_requested", "stale"])] if only_open else ov
    if view.empty:
        st.info("Nothing to review.")
        st.stop()
    def _count(n, word):
        return f"{n} {word}{'' if n == 1 else 's'}"
    def _issues(r):
        return _count(r.errors, "error") if r.errors else _count(r.warnings, "warning") if r.warnings else "no issues"
    labels = {r.SOP: f"{STATUS_ICON.get(r.status, '')} {r.SOP} · {_issues(r)}" for r in view.itertuples()}
    sid = st.radio("SOP", list(labels), format_func=labels.get, key="sop")
    st.caption(f"{(ov.status == 'approved').sum()} of {len(ov)} approved · drafts by `{sr.selected_model()}`")

rec = recs[sid]
draft = sr.load_draft(sid)
if draft is None or draft["draft"] is None:
    st.warning(f"No usable draft for {sid}. Run `python run_sop_drafts.py {sid}`.")
    st.stop()
decision = sr.load_decision(sid)
status = sr.status_of(rec)
start = decision["structure"] if decision and status != "stale" else draft["draft"]
text = sr.source_text(rec)

st.title(f"{sid} · {start['title']}")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Status", f"{STATUS_ICON.get(status, '')} {status.replace('_', ' ')}")
c2.metric("Source", "structured SOP" if rec["format"] == "schema" else "legacy text")
c3.metric("Drafted by", draft["model"])
cmp_ = draft.get("comparison")
c4.metric("Agreement with approved YAML", f"{cmp_['overall']:.0%}" if cmp_ else "n/a (no YAML)")
if status == "stale":
    st.warning("The SOP text changed after the last decision. Review the new draft.")
if decision:
    st.caption(f"Last decision: **{decision['status']}** by {decision['reviewer']} on {decision['decided_at']}"
               + (f" — “{decision['notes']}”" if decision["notes"] else ""))

tab_review, tab_compare, tab_history = st.tabs(["Review", "Comparison with approved YAML", "History"])

with tab_review:
    left, right = st.columns([5, 6])
    with right:
        st.subheader("Approvals")
        appr = st.data_editor(pd.DataFrame(start["approvals"], columns=["stage", "condition", "evidence"]),
                              num_rows="dynamic", width="stretch", key=f"appr_{sid}",
                              column_config={"stage": st.column_config.SelectboxColumn(options=STAGES, required=True),
                                             "evidence": st.column_config.TextColumn(width="large")})
        st.subheader("Dependencies")
        deps = st.data_editor(pd.DataFrame(start["dependencies"],
                                           columns=["dep_id", "provider", "item", "parallel_group", "evidence"]),
                              num_rows="dynamic", width="stretch", key=f"deps_{sid}")
        st.subheader("Steps")
        steps = st.data_editor(pd.DataFrame(start["steps"], columns=["step_id", "name", "role", "type"]),
                               num_rows="dynamic", width="stretch", key=f"steps_{sid}",
                               column_config={"role": st.column_config.SelectboxColumn(options=ROLES, required=True),
                                              "type": st.column_config.SelectboxColumn(options=TYPES, required=True)})
        r1, r2 = st.columns([3, 1])
        reasons = r1.multiselect("Rejection reasons", config.PLATFORM_REJECTION_REASONS,
                                 default=start["rework_reasons"], key=f"reasons_{sid}")
        fpy_val = start.get("first_pass_yield_target")
        fpy = r2.number_input("FPY target", 0.0, 1.0, value=float(fpy_val) if fpy_val is not None else None,
                               step=0.01, key=f"fpy_{sid}")

    edited = {"sop_id": start["sop_id"], "title": start["title"], "steps": _clean(steps.to_dict("records")),
              "approvals": _clean(appr.to_dict("records")),
              "dependencies": _clean(deps.to_dict("records")), "rework_reasons": reasons,
              "first_pass_yield_target": fpy}
    for a in edited["approvals"]:
        a.setdefault("condition", "always")
        a["condition"] = a["condition"] or "always"
        a["evidence"] = a.get("evidence") or ""
    for x in edited["dependencies"]:
        x["evidence"] = x.get("evidence") or ""
        x.setdefault("parallel_group", None)
    try:
        edited = sr.DraftSOP.model_validate(edited).model_dump()
        issues, valid = sr.check(edited, text), True
    except ValidationError as exc:
        issues, valid = [{"severity": "error", "field": "form", "item": "", "message": str(exc).splitlines()[0]}], False

    with left:
        st.subheader("SOP text")
        st.caption("Highlighted: sentences the model quoted as evidence.")
        quotes = [a.get("evidence", "") for a in edited["approvals"]] + [d.get("evidence", "") for d in edited["dependencies"]]
        st.markdown(highlight(text, quotes), unsafe_allow_html=True)

    st.divider()
    st.subheader("Automatic checks")
    show_issues(issues)
    errors = [i for i in issues if i["severity"] == "error"]

    st.subheader("Decision")
    notes = st.text_area("Notes (required to approve with open errors)", key=f"notes_{sid}")
    override = st.checkbox(f"Approve despite {len(errors)} open errors", key=f"ovr_{sid}") if errors else False
    b1, b2, b3 = st.columns(3)
    clicked = None
    if b1.button("✅ Approve", type="primary", disabled=not valid, width="stretch", key=f"ok_{sid}"):
        clicked = "approved"
    if b2.button("✏️ Request changes", disabled=not valid, width="stretch", key=f"chg_{sid}"):
        clicked = "changes_requested"
    if b3.button("⛔ Reject", disabled=not valid, width="stretch", key=f"rej_{sid}"):
        clicked = "rejected"
    if clicked:
        try:
            sr.decide(sid, clicked, reviewer or "", edited, notes, override=override)
            st.success(f"Saved: {clicked.replace('_', ' ')}.")
            st.rerun()
        except ValueError as exc:
            st.error(str(exc))

with tab_compare:
    if not cmp_:
        st.info("This SOP has no approved structured version to compare with (legacy text only).")
    else:
        st.dataframe(pd.DataFrame([{k: cmp_[k] for k in ("steps", "approvals", "dependencies", "reasons", "fpy",
                                                         "overall")}]), hide_index=True)
        st.write(cmp_.get("detail") or "The draft agrees with the approved YAML on every scored field.")

with tab_history:
    log = sr.REVIEW_DIR / "review_log.jsonl"
    rows = [json.loads(line) for line in log.read_text(encoding="utf-8").splitlines()] if log.exists() else []
    rows = [r for r in rows if r["sop_id"] == sid]
    if rows:
        st.dataframe(pd.DataFrame(rows[::-1]), hide_index=True, width="stretch")
    else:
        st.caption("No decisions yet.")
