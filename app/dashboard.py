"""Process intelligence dashboard: findings, SOP conformance, comment check and time predictions in one place.

    python run_pipeline.py ...           # pipeline outputs (deviations, ticket features, conformance)
    python run_comment_check.py ...      # optional: comment check
    python run_prediction.py ...         # optional: time prediction
    streamlit run app/dashboard.py

It only reads files from an output folder; it changes nothing. Tabs whose files are missing say which
command produces them. People are not ranked or scored anywhere on this screen.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import altair as alt  # noqa: E402
import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402

import importlib  # noqa: E402

from process_intel import config, plain, process_map  # noqa: E402

plain = importlib.reload(plain)   # pick up wording changes without restarting the server
process_map = importlib.reload(process_map)

# validated categorical palette (fixed order; colour follows the department, never its rank)
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]

st.set_page_config(page_title="Process Intelligence", page_icon="📊", layout="wide")


# --------------------------------------------------------------------------- data
def output_folders() -> list[Path]:
    root = config.OUTPUT_DIR
    found = [p for p in [root, *sorted(root.iterdir())] if p.is_dir() and (p / "deviations.csv").exists()]
    return sorted(found, key=lambda p: (p.name != "sim_v2", p.name))


@st.cache_data(show_spinner=False)
def _read(path: str, mtime: float) -> pd.DataFrame:
    return pd.read_csv(path, low_memory=False)


def read(folder: Path, name: str) -> pd.DataFrame | None:
    p = folder / name
    return _read(str(p), p.stat().st_mtime) if p.exists() else None


@st.cache_data(show_spinner=False)
def process_steps(path: str, mtime: float) -> pd.DataFrame:
    return process_map.ticket_steps(pd.read_csv(path, usecols=process_map.EVENT_COLS))


def read_json(folder: Path, name: str) -> dict | None:
    p = folder / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def missing(cmd: str):
    st.info(f"Not available for this folder yet. Produce it with `{cmd}`.")


# --------------------------------------------------------------------------- charts
def dept_colors(depts) -> alt.Scale:
    d = sorted(depts)
    return alt.Scale(domain=d, range=SERIES[:len(d)])


def line(df: pd.DataFrame, x: str, y: str, color: str, title: str, y_title: str, fmt: str = ".2f",
         scale: alt.Scale | None = None, height: int = 260):
    df = df.sort_values(x)
    order = list(dict.fromkeys(df[x]))
    if all(re.fullmatch(r"\d{4}-\d{2}", str(v)) for v in order):        # months: 'Oct 2025', in time order
        df = df.assign(**{x: df[x].map(plain.month)})
        order = [plain.month(v) for v in order]
    base = alt.Chart(df).encode(
        x=alt.X(f"{x}:O", title=None, sort=order, axis=alt.Axis(labelAngle=-30, grid=False)),
        y=alt.Y(f"{y}:Q", title=y_title, axis=alt.Axis(format=fmt, gridOpacity=0.35)),
        color=alt.Color(f"{color}:N", scale=scale, legend=alt.Legend(orient="top", title=None)),
        tooltip=[alt.Tooltip(f"{color}:N"), alt.Tooltip(f"{x}:O"), alt.Tooltip(f"{y}:Q", format=fmt)])
    chart = (base.mark_line(strokeWidth=2) + base.mark_point(size=40, filled=True, opacity=0.9)).properties(
        title=title, height=height)
    st.altair_chart(chart.interactive(bind_y=False), width="stretch")
    with st.expander("Show data"):
        st.dataframe(df.pivot_table(index=x, columns=color, values=y, sort=False).reindex(order), width="stretch")


def bars(df: pd.DataFrame, x: str, y: str, color: str, title: str, height: int = 260):
    chart = alt.Chart(df).mark_bar(cornerRadiusEnd=4, size=14).encode(
        y=alt.Y(f"{x}:N", title=None, sort="-x"), x=alt.X(f"{y}:Q", title=None),
        yOffset=alt.YOffset(f"{color}:N"),
        color=alt.Color(f"{color}:N", scale=alt.Scale(range=SERIES), legend=alt.Legend(orient="top", title=None)),
        tooltip=[x, color, y]).properties(title=title, height=height)
    st.altair_chart(chart, width="stretch")
    with st.expander("Show data"):
        st.dataframe(df.pivot_table(index=x, columns=color, values=y), width="stretch")


def ticket_list(ids: str, n: int = 12) -> str:
    ids = str(ids).split("|") if isinstance(ids, str) else []
    return ", ".join(ids[:n]) + (f" … (+{len(ids) - n})" if len(ids) > n else "")


# --------------------------------------------------------------------------- sidebar
folders = output_folders()
if not folders:
    st.error("No pipeline outputs found. Run `python run_pipeline.py` first.")
    st.stop()
with st.sidebar:
    st.header("Process intelligence")
    folder = st.selectbox("Output folder", folders, format_func=lambda p: p.relative_to(config.ROOT).as_posix(),
                          key="folder")
    manifest = read_json(folder, "run_manifest.json") or {}
    if manifest:
        st.caption(f"Pipeline run: {manifest.get('run_at', '—')}")
    st.caption("Read-only view of the output files. Nobody is ranked or scored here.")

feat = read(folder, "ticket_features.csv")
dev = read(folder, "deviations.csv")
team = read(folder, "team_metrics.csv")

tabs = st.tabs(["Overview", "Process map", "Findings", "SOP conformance", "Comment check", "Time prediction", "Simulation check"])

# --------------------------------------------------------------------------- overview
with tabs[0]:
    if feat is None:
        missing("python run_pipeline.py")
    else:
        closed = feat[feat.is_closed.astype(bool)]
        period = plain.months(str(feat.created_at.min())[:7], str(feat.created_at.max())[:7])
        on_time = closed.sla_met.astype(bool).mean()
        c = st.columns(5)
        c[0].metric("Tickets", f"{len(feat):,}")
        c[1].metric("Months covered", f"{feat.created_at.str[:7].nunique()}")
        c[1].caption(period)
        c[2].metric("Finished on time", f"{on_time:.0%}")
        c[3].metric("Typical ticket takes", plain.hours(closed.total_duration_h.median()))
        c[4].metric("Sent back at least once", f"{(closed.rework_cycles > 0).mean():.0%}")

        st.subheader("What stands out")
        points = [f"Over {period}, **{len(feat):,} tickets** were handled. **{on_time:.0%}** finished within their SLA "
                  f"and a typical ticket took **{plain.hours(closed.total_duration_h.median())}**."]
        if team is not None:
            m = team[team.period_type == "month"]
            # latest month with normal volume (a month that has only just started is not compared)
            vol = m.groupby("period").tickets_completed.sum()
            full = vol[vol >= 0.5 * vol.median()]
            last = full.index.max() if len(full) else m.period.max()
            m = m[m.period <= last]
            for dept, g in m.groupby("department"):
                now, before = g[g.period == last], g[g.period < last].tail(6)
                if now.empty or before.empty:
                    continue
                sla_now, sla_before = now.sla_compliance.iloc[0], before.sla_compliance.mean()
                vol_now, vol_before = now.tickets_completed.iloc[0], before.tickets_completed.mean()
                if sla_before - sla_now >= 0.05:
                    points.append(f"**{dept}**: {sla_now:.0%} on time in {plain.month(last)}, below its usual "
                                  f"{sla_before:.0%}.")
                if vol_before and vol_now >= 1.3 * vol_before:
                    points.append(f"**{dept}** handled {vol_now:.0f} tickets in {plain.month(last)}, well above its "
                                  f"usual {vol_before:.0f} a month.")
            if len(points) == 1:
                points.append(f"No department is noticeably slower or busier than usual in {plain.month(last)}.")
        if dev is not None:
            pf = dev[dev.level == "process"]
            kinds = pf.classification.map(plain.CLASSIFICATION).fillna(pf.classification).value_counts()
            points.append(f"**{len(pf)} things to look at** (Findings tab): "
                          + ", ".join(f"{n} × {k[0].lower() + k[1:] if not k.startswith('SOP') else k}"
                                      for k, n in kinds.items()) + ".")
            points.append(f"**{(dev.level == 'ticket').sum()} tickets** took far longer than similar ones; the "
                          "Findings tab lists them with the reason.")
        st.markdown("\n".join(f"- {p}" for p in points))

        if team is not None:
            st.subheader("Month by month, per department")
            m = team[team.period_type == "month"].copy()
            vol = m.groupby("period").tickets_completed.sum()
            partial = vol[vol < 0.5 * vol.median()].index        # a month that has only just started
            m = m[~m.period.isin(partial)]
            if len(partial):
                st.caption(f"Left out: {', '.join(plain.month(p) for p in partial)}, which has too few finished "
                           "tickets so far to compare.")
            dc = dept_colors(m.department.unique())
            a, b = st.columns(2)
            with a:
                line(m, "period", "sla_compliance", "department", "Share of tickets finished on time",
                     "on time", ".0%", dc)
            with b:
                line(m, "period", "median_duration_h", "department", "How long a typical ticket takes", "hours",
                     ".1f", dc)
            a, b = st.columns(2)
            with a:
                line(m, "period", "tickets_completed", "department", "Tickets finished", "tickets", "d", dc)
            with b:
                line(m, "period", "rework_rate", "department", "Share of tickets sent back at least once",
                     "sent back", ".0%", dc)

# --------------------------------------------------------------------------- process map
with tabs[1]:
    ev_path = folder / "processed" / "events_normalized.csv"
    if not ev_path.exists() or feat is None:
        missing("python run_pipeline.py")
    else:
        steps_all = process_steps(str(ev_path), ev_path.stat().st_mtime)
        meta = feat[["ticket_id", "department", "task_type", "total_duration_h"]]
        f1, f2, f3 = st.columns([2, 3, 2])
        pm_dept = f1.multiselect("Department", sorted(meta.department.dropna().unique()), key="pm_dept")
        tt_opts = sorted(meta[meta.department.isin(pm_dept) if pm_dept else meta.department.notna()].task_type.unique())
        pm_tt = f2.multiselect("Task type", tt_opts, key="pm_tt")
        detail = f3.slider("Hide routes used by fewer than", 0, 20, 2, format="%d%% of tickets", key="pm_min")
        sel = meta
        if pm_dept:
            sel = sel[sel.department.isin(pm_dept)]
        if pm_tt:
            sel = sel[sel.task_type.isin(pm_tt)]
        steps = steps_all[steps_all.ticket_id.isin(sel.ticket_id)]
        if steps.empty:
            st.info("No tickets match these filters.")
        else:
            e = process_map.edges(process_map.transitions(steps))
            top_paths = process_map.paths(steps, sel.set_index("ticket_id").total_duration_h)
            scope = (", ".join(pm_tt) if pm_tt else ", ".join(pm_dept) if pm_dept else "all task types")
            st.subheader(f"What stands out ({scope})")
            pts = process_map.summary(e, top_paths, steps, sel.total_duration_h.median())
            no_dep = feat[feat.ticket_id.isin(sel.ticket_id)].dependency_count.eq(0)
            if steps.step.eq("On hold").any() and no_dep.all():
                pts.append("The SOP for these tickets lists **no outside dependency**, so these holds are unplanned. "
                           "The Comment check tab shows what they were really waiting for.")
            st.markdown("\n".join(f"- {p}" for p in pts))
            st.subheader("How tickets move")
            st.caption("Each box is a step; each arrow is a move between steps. **Thicker** = more tickets. "
                       "**Darker blue** = longer time until the next step. **Orange** = the step that adds the "
                       "most waiting overall. Dashed = a less common route (under 10% of tickets). Labels: "
                       "number of tickets · typical time.")
            st.graphviz_chart(process_map.to_dot(e, detail / 100), width="content")
            with st.expander("Every move in a table"):
                t = e[~e.step.eq(process_map.START)].copy()
                st.dataframe(t[["step", "next_step", "tickets", "share", "median_h", "p90_h"]], hide_index=True,
                             width="stretch",
                             column_config={"step": "From", "next_step": "To", "tickets": "Tickets",
                                            "share": st.column_config.NumberColumn("Share of tickets",
                                                                                   format="percent"),
                                            "median_h": st.column_config.NumberColumn("Typical time (h)",
                                                                                      format="%.1f"),
                                            "p90_h": st.column_config.NumberColumn("Slow cases (h, 9 in 10 faster)",
                                                                                   format="%.1f")})
            st.subheader("Most common paths")
            st.dataframe(top_paths, hide_index=True, width="stretch",
                         column_config={"path": st.column_config.TextColumn("Path", width="large"),
                                        "tickets": "Tickets",
                                        "median_duration_h": st.column_config.NumberColumn(
                                            "Typical total time (h)", format="%.1f"),
                                        "share": st.column_config.NumberColumn("Share of tickets",
                                                                               format="percent")})

# --------------------------------------------------------------------------- findings
with tabs[2]:
    if dev is None:
        missing("python run_pipeline.py")
    else:
        proc = dev[dev.level == "process"].copy()
        f1, f2, f3 = st.columns(3)
        types = f1.multiselect("Finding type", sorted(proc.deviation_type.unique()), key="f_type",
                               format_func=lambda t: plain.TITLES.get(t, t))
        depts = f2.multiselect("Department", sorted(proc.department.dropna().unique()), key="f_dept")
        sev = f3.multiselect("Severity", ["high", "medium", "low"], key="f_sev")
        keep = pd.Series(True, index=proc.index)
        for col, chosen in (("deviation_type", types), ("department", depts), ("severity", sev)):
            if chosen:
                keep &= proc[col].isin(chosen)
        v = proc[keep]
        v = v.assign(_s=v.severity.map({"high": 0, "medium": 1, "low": 2})).sort_values(["_s", "deviation_type"])
        icon = {"high": "🔴", "medium": "🟠", "low": "⚪"}

        st.subheader("At a glance")
        st.caption("🔴 high · 🟠 medium · ⚪ low severity. Open any finding below for the details.")
        for r in v.itertuples():
            e = plain.explain(r)
            st.markdown(f"{icon.get(r.severity, '')} **{e['title']}** · {e['subject']}: {e['points'][0]}")

        st.subheader(f"Details ({len(v)} of {len(proc)} findings)")
        for r in v.itertuples():
            e = plain.explain(r)
            with st.expander(f"{icon.get(r.severity, '')} {e['title']} · {e['subject']}"):
                st.markdown("**What we found**")
                st.markdown("\n".join(f"- {p}" for p in e["points"]))
                if e["cause"]:
                    conf_txt = f" _({e['confidence']} confidence)_" if e["confidence"] else ""
                    st.markdown(f"**Likely cause**{conf_txt}: {e['cause']}")
                if e["action"]:
                    st.markdown(f"**What to do:** {e['action']}")
                st.caption(f"Type of issue: {e['kind']}"
                           + (f" · SOP: {r.sop_reference}" if isinstance(r.sop_reference, str) else ""))
                st.caption(f"Example tickets: {ticket_list(r.source_ticket_ids)}")
                try:
                    st.caption("Technical details (raw numbers behind this finding):")
                    st.json(json.loads(r.evidence), expanded=False)
                except (TypeError, ValueError):
                    pass

        st.divider()
        tk = dev[dev.level == "ticket"]
        st.subheader(f"Unusually long tickets ({len(tk)})")
        st.caption("Tickets that took longer than 9 out of 10 similar tickets, with the main reason for the extra "
                   "time. “ratio” = how many times longer than a typical similar ticket.")
        if len(tk):
            show = tk[["entity_id", "department", "observed", "expected", "ratio", "classification",
                       "dominant_cause"]].rename(columns={"entity_id": "ticket", "observed": "hours",
                                                          "expected": "typical hours"})
            show["classification"] = show.classification.map(plain.CLASSIFICATION).fillna(show.classification)
            show["dominant_cause"] = show.dominant_cause.map(plain.ticket_cause)
            st.dataframe(show.sort_values("ratio", ascending=False), hide_index=True, width="stretch",
                         column_config={"ratio": st.column_config.NumberColumn(format="%.1f×"),
                                        "hours": st.column_config.NumberColumn(format="%.1f"),
                                        "typical hours": st.column_config.NumberColumn(format="%.1f")})

        emp = dev[dev.level == "employee"]
        st.divider()
        st.subheader("Individual-level signals")
        st.caption("These are not ratings. Each one is a sustained change for one person compared with their own "
                   "history, with the context that may explain it. They are a prompt for a supportive conversation "
                   "with the line manager, and are hidden by default.")
        if st.toggle(f"Show {len(emp)} individual-level signals", key="show_emp"):
            for r in emp.itertuples():
                e = plain.explain(r)
                with st.expander(f"{e['title']} · {e['subject']}"):
                    st.markdown("\n".join(f"- {p}" for p in e["points"]))
                    if e["cause"]:
                        st.markdown(f"**Context:** {e['cause']}")
                    if e["action"]:
                        st.markdown(f"**Suggested next step:** {e['action']}")
                    st.caption(e["kind"])

# --------------------------------------------------------------------------- SOP conformance
with tabs[3]:
    corr, conf = read(folder, "sop_log_correspondence.csv"), read(folder, "conformance.csv")
    if conf is None:
        missing("python run_pipeline.py")
    else:
        st.caption("Each ticket is checked against its SOP: did it get the right approvals, in the right order, "
                   "without unplanned holds, within the SOP's time range? The table shows the share of tickets "
                   "passing each check. A blank means the check does not apply to that task type.")
        checks = [c for c in conf.columns if c.startswith("c") and c[1].isdigit()]
        summ = conf.groupby("task_type").agg(tickets=("ticket_id", "size"), mean_fitness=("fitness", "mean"))
        pct = {}
        for c in checks:
            name = plain.check_name(c)
            summ[name] = conf.groupby("task_type")[c].apply(
                lambda s: s.dropna().isin(["ok", "none", "within"]).mean() if s.notna().any() else None)
            pct[name] = st.column_config.NumberColumn(format="percent")

        st.subheader("What stands out")
        weak = []
        for tt, row in summ.iterrows():
            for c in checks:
                v = row[plain.check_name(c)]
                if pd.notna(v) and v < 0.8:
                    worst = conf.loc[(conf.task_type == tt) & ~conf[c].isin(["ok", "none", "within"]) & conf[c].notna(), c]
                    what = plain.result_word(worst.mode().iloc[0]) if len(worst) else ""
                    share = "no tickets pass" if v < 0.005 else f"only {v:.0%} of tickets pass"
                    weak.append((v, f"**{tt}**: {share} “{plain.check_name(c)}”"
                                    + (f" (mostly: {what})." if what else ".")))
        if weak:
            st.markdown("\n".join(f"- {t}" for _, t in sorted(weak)[:10]))
            st.caption("“Time within SOP range” failing for most task types usually means the SOP's time figures "
                       "need updating, not that the work is wrong. See the Findings tab.")
        else:
            st.markdown("- Every task type passes every check on at least 80% of tickets.")

        st.subheader("Share of tickets passing each check")
        st.dataframe(summ.reset_index(), hide_index=True, width="stretch",
                     column_config={"task_type": "Task type", "tickets": "Tickets",
                                    "mean_fitness": st.column_config.ProgressColumn(
                                        "Overall SOP fit", min_value=0, max_value=1, format="percent"), **pct})
        with st.expander("What each check found (number of tickets per result)"):
            long = conf.melt(id_vars="task_type", value_vars=checks, var_name="check", value_name="result")
            long["check"] = long.check.map(plain.check_name)
            long["result"] = long.result.map(plain.result_word)
            st.dataframe(long.groupby(["task_type", "check", "result"]).size().unstack(fill_value=0),
                         width="stretch")
        if corr is not None:
            st.subheader("Do the tickets match the SOP they are filed under?")
            st.caption("Checks that each task type's logged steps fit its own SOP better than any other SOP.")
            show = corr[["task_type", "sop_id", "tickets", "verdict", "correspondence", "time_ratio_own",
                         "structural_mismatches", "notes"]].copy()
            show["verdict"] = show.verdict.map(plain.CORR_VERDICT).fillna(show.verdict)
            show["structural_mismatches"] = show.structural_mismatches.replace({"none": "None"}).fillna("None")
            show["notes"] = [plain.corr_notes(n) + ("" if not isinstance(k, str) else
                                                    f" Known problems: {plain.known_deviations(k)}.")
                             for n, k in zip(show.notes, corr.known_deviation_counts)]
            show["notes"] = show.notes.str.replace(r"^— Known", "Known", regex=True)
            st.dataframe(show, hide_index=True, width="stretch",
                         column_config={"task_type": "Task type", "sop_id": "SOP", "tickets": "Tickets",
                                        "verdict": "Result",
                                        "correspondence": st.column_config.NumberColumn(
                                            "Tickets that fit", format="percent"),
                                        "time_ratio_own": st.column_config.NumberColumn(
                                            "Actual time ÷ SOP time", format="%.2f×"),
                                        "structural_mismatches": "Steps that don't fit",
                                        "notes": st.column_config.TextColumn("Notes", width="large")})

# --------------------------------------------------------------------------- comment check
with tabs[4]:
    chk, cj = read(folder, "reason_code_checks.csv"), read_json(folder, "comment_check.json")
    if chk is None or cj is None:
        missing("python run_comment_check.py --data <data folder> --out <this folder>")
    else:
        s = cj["summary"]
        allmm = chk[chk.status == "mismatch"]
        c = st.columns(4)
        c[0].metric("Rejection comments read", s["rejections_with_comment"])
        c[1].metric("Recorded reason doesn't match the comment", s["reason_code_mismatches"])
        c[1].caption(f"{s['mismatch_share']:.0%} of rejections")
        c[2].metric("Confirmed by the fix comment", s["mismatch_by_confidence"].get("high", 0))
        c[3].metric("Holds with no SOP reason", s["holds_on_sops_without_dependency"])

        st.subheader("What stands out")
        pts = [f"In **{s['reason_code_mismatches']} of {s['rejections_with_comment']} rejections "
               f"({s['mismatch_share']:.0%})**, the reason recorded on the platform is not what the reviewer wrote "
               f"in the comment. **{s['mismatch_by_confidence'].get('high', 0)}** of these are confirmed by the "
               "requester's own fix comment."]
        if len(allmm):
            pair = allmm.groupby(["platform_code", "llm_label"]).size().sort_values(ascending=False)
            (pc, lab), n = pair.index[0], pair.iloc[0]
            pts.append(f"Most common mix-up: recorded as “{pc}” when the comment describes “{lab}” ({n} times).")
            tt = allmm.task_type.value_counts()
            pts.append(f"Most affected task type: **{tt.index[0]}** ({tt.iloc[0]} rejections).")
        if s["holds_on_sops_without_dependency"]:
            pts.append(f"**{s['holds_on_sops_without_dependency']} holds** were on task types whose SOP has no "
                       f"outside dependency. The comments say **{s['of_which_approver_queue']}** were waiting for the "
                       f"approver and **{s['of_which_missing_info']}** for the requester.")
        if s.get("dependency_holds_not_external"):
            pts.append(f"{s['dependency_holds_not_external']} holds on task types with outside dependencies were "
                       "actually waiting for something else (the approver or the requester).")
        pts.append("Wrong reason codes make the rejection numbers in the other tabs less reliable; fixing how "
                   "reasons are picked on the platform (for example a clearer drop-down) would help.")
        st.markdown("\n".join(f"- {p}" for p in pts))
        st.caption(f"How this works: the local AI model (`{cj['model']}`) only reads each comment and says what "
                   "it is about; plain code then compares that with the platform record. On test comments the "
                   "AI was right about 9 times in 10, so check a ticket before correcting its record.")

        rc = read(folder, "reason_counts.csv")
        a, b = st.columns(2)
        with a:
            if rc is not None:
                bars(rc.melt(id_vars="reason", var_name="source", value_name="rejections").replace(
                    {"platform_code": "Recorded on the platform", "comment_says": "What the comment says"}),
                    "reason", "rejections", "source", "Rejections per reason: recorded vs what the comments say")
        with b:
            hk = read(folder, "hold_kinds.csv")
            if hk is not None:
                st.markdown("**What holds were waiting for, by task type**")
                h = hk[["task_type", "sop_has_dependency", "external_dependency", "approver_queue", "missing_info",
                        "unclear", "holds"]].copy()
                h["sop_has_dependency"] = h.sop_has_dependency.map({True: "Yes", False: "No"})
                st.dataframe(h.rename(columns=plain.HOLD_COLUMNS), hide_index=True, width="stretch")
                st.caption("Where the SOP expects no outside waits (“No”), every hold is unplanned. The comment "
                           "tells us whether it was the approver or the requester holding things up.")
        st.subheader("Rejections where the recorded reason doesn't match the comment")
        conf_f = st.multiselect("How sure", ["high", "medium", "low"], default=["high", "medium"], key="cc_conf",
                                format_func=lambda c: plain.CONFIDENCE_WORDS[c])
        mm = chk[(chk.status == "mismatch") & chk.confidence.isin(conf_f)].copy()
        mm["confidence"] = mm.confidence.map(plain.CONFIDENCE_WORDS)
        st.dataframe(mm[["ticket_id", "task_type", "platform_code", "text", "llm_label", "fix_text", "confidence"]]
                     .rename(columns={"ticket_id": "Ticket", "task_type": "Task type",
                                      "platform_code": "Recorded reason", "text": "Reviewer's comment",
                                      "llm_label": "Comment is about", "fix_text": "Requester's fix comment",
                                      "confidence": "How sure"}),
                     hide_index=True, width="stretch")

# --------------------------------------------------------------------------- prediction
with tabs[5]:
    pe, pr = read_json(folder, "prediction_eval.json"), read(folder, "predictions.csv")
    if pe is None or pr is None:
        missing("python run_prediction.py --out <this folder>")
    else:
        d, k = pe["duration"], pe["sla_risk"]
        mdl, seg = d["model"], d["segment_baseline"]
        win = plain.months(pe["months"][0], pe["months"][-1])
        c = st.columns(4)
        c[0].metric("Estimate is usually off by", plain.hours(mdl["p50_mae_h"]),
                    f"{plain.hours(abs(mdl['p50_mae_h'] - seg['p50_mae_h']))} "
                    f"{'better' if mdl['p50_mae_h'] <= seg['p50_mae_h'] else 'worse'} than a simple average",
                    delta_color="normal" if mdl["p50_mae_h"] <= seg["p50_mae_h"] else "inverse")
        c[1].metric("“Finish-by” time held for", f"{mdl['p90_coverage']:.0%} of tickets")
        c[1].caption("Aim: 9 in 10")
        c[2].metric("Late tickets flagged early", f"{k['model']['top10pct_recall']:.0%}")
        c[2].caption("of late tickets were in the top-10% risk list")
        c[3].metric("Tickets tested", f"{pe['tickets']:,}")
        c[3].caption(win)

        st.subheader("What stands out")
        bm = pd.DataFrame(pe["by_month"]).T.reset_index(names="month")
        worst = bm.loc[bm.p90_coverage.astype(float).idxmin()]
        imp = read(folder, "prediction_features.csv")
        pts = ["When a ticket is created, the system estimates three things: a **likely duration**, a **finish-by "
               "time** that should hold 9 times in 10, and the **chance of missing the SLA**. It uses only what is "
               "known at that moment and never who the ticket is assigned to.",
               f"Tested on **{pe['tickets']:,} tickets from {win}**. Each month was predicted using only earlier "
               "months, just as it would be used for real.",
               f"The likely duration was off by **{plain.hours(mdl['p50_mae_h'])}** on average (about "
               f"{mdl['p50_median_abs_pct_err']:.0%} of a typical ticket's time). A simple average for the same task "
               f"type and priority was off by {plain.hours(seg['p50_mae_h'])}.",
               f"The finish-by time held for **{mdl['p90_coverage']:.0%}** of tickets (aim: 90%). Its weakest month "
               f"was {plain.month(worst.month)} ({float(worst.p90_coverage):.0%}); sudden changes such as overloads "
               "take a couple of weeks to catch up with.",
               f"The 10% of tickets with the highest risk contained **{k['model']['top10pct_recall']:.0%} of all late "
               "tickets**, so that list is a good place to act early."]
        if imp is not None and len(imp):
            pts.append(f"The estimate depends most on: {plain.feature_name(imp.feature.iloc[0]).lower()}. That "
                       "means it follows slowdowns as they happen.")
        st.markdown("\n".join(f"- {p}" for p in pts))

        cov = bm.melt(id_vars="month", value_vars=["p90_coverage", "seg_p90_coverage"], var_name="method",
                      value_name="coverage").replace({"p90_coverage": "This system",
                                                      "seg_p90_coverage": "Simple average"})
        cov["coverage"] = cov.coverage.astype(float)
        a, b = st.columns(2)
        with a:
            line(cov, "month", "coverage", "method", "Tickets that finished by the “finish-by” time (aim: 90%)",
                 "share", ".0%", alt.Scale(domain=["This system", "Simple average"], range=SERIES[:2]))
        with b:
            st.markdown("**Can the risk numbers be trusted?**")
            cal = read(folder, "prediction_calibration.csv")
            if cal is not None:
                cal = cal.assign(risk_band=cal.risk_band.map(plain.risk_band))
                top = cal.iloc[-1]
                st.caption(f"When the system said {top.risk_band} risk (about {top.mean_predicted:.0%} on average), "
                           f"{top.observed_late:.0%} of those tickets were actually late. Close numbers in each row "
                           "mean the risk can be taken at face value.")
                st.dataframe(cal, hide_index=True, width="stretch",
                             column_config={"risk_band": "Predicted risk", "tickets": "Tickets",
                                            "mean_predicted": st.column_config.NumberColumn(
                                                "Average predicted risk", format="percent"),
                                            "observed_late": st.column_config.NumberColumn(
                                                "Actually late", format="percent")})
            if imp is not None:
                st.markdown("**What the duration estimate depends on most**")
                top8 = imp.head(8).copy()
                top8["share"] = top8.importance.clip(lower=0) / top8.importance.clip(lower=0).sum()
                top8["feature"] = top8.feature.map(plain.feature_name)
                st.dataframe(top8[["feature", "share"]], hide_index=True, width="stretch",
                             column_config={"feature": "Input", "share": st.column_config.ProgressColumn(
                                 "Influence (share of the top 8)", min_value=0, max_value=1, format="percent")})
        with st.expander("All accuracy numbers: this system vs simple methods"):
            methods = {"model": "This system", "segment_baseline": "Simple average (type + priority)",
                       "sop_estimate": "SOP's own estimate"}
            dur_cols = {"p50_mae_h": "Avg miss (h)", "p50_median_abs_pct_err": "Typical miss (% of time)",
                        "p90_coverage": "Finish-by held", "p90_pinball": "Finish-by score (lower = better)",
                        "p50_pinball": "Likely-duration score (lower = better)"}
            risk_cols = {"late_share": "Share of tickets late", "brier": "Risk accuracy score (lower = better)",
                         "top10pct_precision": "Top-10% list: share actually late",
                         "top10pct_recall": "Late tickets caught by top-10% list",
                         "auc": "Ranking quality (1 = perfect)"}
            st.dataframe(pd.DataFrame(d).T.rename(index=methods, columns=dur_cols), width="stretch")
            st.dataframe(pd.DataFrame(k).T.rename(index=methods, columns=risk_cols), width="stretch")
        st.subheader(f"Highest-risk tickets in {plain.month(pr.month.max())}")
        st.caption("In live use this list would appear as tickets are created, so they can be prioritised. Here "
                   "the last two columns show what actually happened.")
        last = pr[pr.month == pr.month.max()].sort_values("pred_late_prob", ascending=False).head(25).copy()
        last["late"] = last.late.map({1: "Yes", 0: "No", True: "Yes", False: "No"})
        st.dataframe(last[["ticket_id", "task_type", "priority", "sla_hours", "pred_p50_h", "pred_p90_h",
                           "pred_late_prob", "duration_h", "late"]],
                     hide_index=True, width="stretch",
                     column_config={"ticket_id": "Ticket", "task_type": "Task type", "priority": "Priority",
                                    "sla_hours": st.column_config.NumberColumn("SLA (h)", format="%d"),
                                    "pred_p50_h": st.column_config.NumberColumn("Likely duration (h)", format="%.1f"),
                                    "pred_p90_h": st.column_config.NumberColumn("Finish-by (h)", format="%.1f"),
                                    "pred_late_prob": st.column_config.ProgressColumn(
                                        "Chance of missing SLA", min_value=0, max_value=1, format="percent"),
                                    "duration_h": st.column_config.NumberColumn("Actual (h)", format="%.1f"),
                                    "late": "Was late?"})

# --------------------------------------------------------------------------- simulation check
with tabs[6]:
    ev, ej = read(folder, "detection_eval.csv"), read_json(folder, "detection_eval.json")
    if ev is None or ej is None:
        st.info("Only for simulated data with an answer key: `python run_detection_eval.py --out <this folder> "
                "--truth <data folder>/truth`.")
    else:
        c = st.columns(4)
        c[0].metric("Planted problems found", f"{ej['detected']} of {ej['scenarios_in_scope']}")
        c[1].metric("Normal cases left alone", ej["controls_passed"].replace("/", " of "))
        c[2].metric("False alarms", ej["false_alarms"])
        c[3].metric("Missed", ", ".join(ej["missed"]) or "None")
        st.caption("The test data has problems planted on purpose. Each row is one planted problem: what it was, "
                   "whether the system found it, how it described it, and where.")
        show = plain.plain_scenarios(ev)
        st.dataframe(show[["scenario", "name", "verdict", "found_types", "found", "window"]], hide_index=True,
                     width="stretch")
        for r in show[~ev.verdict.isin(["detected", "control_pass"])].itertuples():
            st.markdown(f"- **{r.scenario}: {r.name}** → {r.verdict}.")
        acc = read(folder, "comment_label_accuracy.csv")
        if acc is not None:
            st.markdown("**How often the AI read the comments correctly (checked against the answer key)**")
            acc = acc.assign(context=acc.context.map({"rejection": "Rejection comments", "correction":
                                                      "Fix comments", "hold": "Hold comments"}).fillna(acc.context))
            st.dataframe(acc, hide_index=True, width="stretch",
                         column_config={"context": "Comment type", "comments": "Comments",
                                        "distinct_texts": "Different wordings",
                                        "llm_accuracy": st.column_config.NumberColumn("AI right", format="percent"),
                                        "keyword_accuracy": st.column_config.NumberColumn(
                                            "Simple keyword rules right", format="percent")})
            st.caption("The test comments come from a small set of templates, so simple keyword rules do very well "
                       "on them. On varied, hand-written comments the AI was right about 9 times in 10 and the "
                       "keyword rules about 4 in 10.")
