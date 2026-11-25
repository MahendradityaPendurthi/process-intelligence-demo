"""Stage 0/1: load raw exports (read-only) and validate them.

Validation never drops data. It produces one row per check for
outputs/data_quality_report.csv; downstream stages decide what to quarantine.
"""
from __future__ import annotations

import pandas as pd

from . import config


def load_raw(raw_dir=config.RAW_DIR) -> dict[str, pd.DataFrame]:
    """Read every raw CSV as strings so nothing is coerced before validation."""
    return {
        name: pd.read_csv(raw_dir / f"{name}.csv", dtype=str, keep_default_na=False, na_values=[""])
        for name in config.REQUIRED_COLUMNS
    }


def _parse_ts(series: pd.Series) -> pd.Series:
    return pd.to_datetime(series, format=config.TIMESTAMP_FORMAT, errors="coerce")


class _Report:
    def __init__(self):
        self.rows = []

    def add(self, dataset, check, severity, affected, details="", examples=()):
        status = "pass" if affected == 0 or severity == "info" else "fail"
        self.rows.append({
            "check_id": f"DQ{len(self.rows) + 1:03d}",
            "dataset": dataset,
            "check": check,
            "severity": severity,
            "status": status,
            "affected_rows": int(affected),
            "details": details,
            "example_ids": "|".join(map(str, list(examples)[:5])),
        })

    def frame(self) -> pd.DataFrame:
        return pd.DataFrame(self.rows)


def validate(dfs: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rep = _Report()
    emp, tix, ev, tt = dfs["employees"], dfs["tickets"], dfs["audit_logs"], dfs["task_types"]

    # --- profile + required columns + missing values
    for name, df in dfs.items():
        rep.add(name, "row_count", "info", 0, f"{len(df)} rows, {len(df.columns)} columns")
        missing_cols = [c for c in config.REQUIRED_COLUMNS[name] if c not in df.columns]
        rep.add(name, "required_columns_present", "error", len(missing_cols),
                f"missing: {missing_cols}" if missing_cols else "all required columns present", missing_cols)
        if missing_cols:
            continue
        for col in config.REQUIRED_COLUMNS[name]:
            n = df[col].isna().sum()
            if n == 0:
                continue
            # Columns where blanks are expected by design
            expected_blank = (
                (name == "employees" and col == "reporting_to")
                or (name == "audit_logs" and col in ("previous_status", "change_type", "details"))
            )
            rep.add(name, f"missing_values:{col}", "info" if expected_blank else "error", n,
                    "blank by design" if expected_blank else "required value missing")

    if any(r["check"] == "required_columns_present" and r["status"] == "fail" for r in rep.rows):
        return rep.frame()  # cannot run relational checks without columns

    # --- uniqueness
    for name, df, key in [("employees", emp, "employee_id"), ("tickets", tix, "ticket_id"),
                          ("audit_logs", ev, "event_id"), ("task_types", tt, "task_type")]:
        dup = df[df[key].duplicated(keep=False)]
        rep.add(name, f"unique:{key}", "error", dup[key].nunique(), "duplicate identifiers", dup[key].unique())
    exact_dup = ev[ev.duplicated(keep="first")]
    rep.add("audit_logs", "exact_duplicate_events", "warning", len(exact_dup),
            "identical rows; deduplicated during normalization", exact_dup["event_id"])

    # --- timestamps
    ts = {}
    for name, df, cols in [("tickets", tix, ["created_at", "due_at", "completed_at"]), ("audit_logs", ev, ["timestamp"])]:
        for col in cols:
            parsed = _parse_ts(df[col])
            ts[(name, col)] = parsed
            bad = df[parsed.isna() & df[col].notna()]
            rep.add(name, f"timestamp_parseable:{col}", "error", len(bad),
                    f"expected format {config.TIMESTAMP_FORMAT}", bad.iloc[:, 0])
            if parsed.notna().any():
                rep.add(name, f"timestamp_range:{col}", "info", 0, f"{parsed.min()} .. {parsed.max()}")

    created, due, completed = ts[("tickets", "created_at")], ts[("tickets", "due_at")], ts[("tickets", "completed_at")]
    bad = tix[due < created]
    rep.add("tickets", "due_after_created", "error", len(bad), "due_at earlier than created_at", bad.ticket_id)
    bad = tix[completed < created]
    rep.add("tickets", "completed_after_created", "error", len(bad), "completed_at earlier than created_at", bad.ticket_id)

    # --- referential integrity
    emp_ids = set(emp.employee_id)
    bad = tix[~tix.assigned_employee_id.isin(emp_ids)]
    rep.add("tickets", "fk:assigned_employee_id->employees", "error", len(bad), "", bad.ticket_id)
    bad = ev[~ev.employee_id.isin(emp_ids)]
    rep.add("audit_logs", "fk:employee_id->employees", "error", len(bad), "", bad.event_id)
    bad = ev[~ev.ticket_id.isin(set(tix.ticket_id))]
    rep.add("audit_logs", "fk:ticket_id->tickets", "error", len(bad), "events for unknown tickets", bad.event_id)
    bad = tix[~tix.ticket_id.isin(set(ev.ticket_id))]
    rep.add("tickets", "tickets_without_events", "error", len(bad), "no audit history", bad.ticket_id)
    bad = tix[~tix.task_type.isin(set(tt.task_type))]
    rep.add("tickets", "fk:task_type->task_types", "error", len(bad), "", bad.ticket_id)

    # --- hierarchy
    bad = emp[~emp.role.isin(config.ROLE_LEVELS)]
    rep.add("employees", "valid_role", "error", len(bad), f"allowed: {list(config.ROLE_LEVELS)}", bad.employee_id)
    mgr = emp.merge(emp[["employee_id", "role", "department"]], left_on="reporting_to", right_on="employee_id",
                    how="left", suffixes=("", "_mgr"))
    non_hod = mgr[mgr.role != "HOD"]
    bad = non_hod[non_hod.employee_id_mgr.isna()]
    rep.add("employees", "reporting_to_exists", "error", len(bad), "non-HOD with unknown manager", bad.employee_id)
    ok = non_hod.employee_id_mgr.notna()
    lvl = non_hod.role.map(config.ROLE_LEVELS)
    lvl_mgr = non_hod.role_mgr.map(config.ROLE_LEVELS)
    bad = non_hod[ok & (lvl_mgr != lvl + 1)]
    rep.add("employees", "reporting_to_one_level_up", "warning", len(bad), "manager is not exactly one level up", bad.employee_id)
    bad = mgr[mgr.role.eq("HOD") & mgr.reporting_to.notna()]
    rep.add("employees", "hod_has_no_manager", "warning", len(bad), "", bad.employee_id)
    rep.add("employees", "hierarchy_profile", "info", 0, emp.groupby(["department", "role"]).size().to_dict().__repr__())

    # --- ticket attributes vs task_types metadata
    merged = tix.merge(tt, on="task_type", how="left", suffixes=("", "_tt"))
    for col in ["department", "complexity", "sop_steps", "approval_count", "dependency_count"]:
        bad = merged[merged[col] != merged[f"{col}_tt"]]
        rep.add("tickets", f"consistent_with_task_types:{col}", "warning", len(bad), "", bad.ticket_id)
    bad = tix[~tix.complexity.isin(config.COMPLEXITY_LEVELS)]
    rep.add("tickets", "valid_complexity", "error", len(bad), "", bad.ticket_id)
    bad = tix[~tix.priority.isin(config.PRIORITY_LEVELS)]
    rep.add("tickets", "valid_priority", "error", len(bad), "", bad.ticket_id)
    # SOP coverage and consistency are validated in Stage 1 (sop.validate_sops -> sop_validation_report.csv).

    # --- status consistency
    late = completed > due
    flagged_late = tix.final_status.eq("Completed_Late")
    bad = tix[late != flagged_late]
    rep.add("tickets", "final_status_matches_due_date", "warning", len(bad),
            "Completed_Late iff completed_at > due_at", bad.ticket_id)
    rep.add("tickets", "final_status_profile", "info", 0, tix.final_status.value_counts().to_dict().__repr__())

    # --- event-level checks
    ev_ts = ts[("audit_logs", "timestamp")]
    known = ev.action.str.lower().str.replace(r"[\s_]", "", regex=True).isin(config.EVENT_TYPE_MAP)
    rep.add("audit_logs", "known_action_vocabulary", "error", int((~known).sum()),
            "actions without a canonical mapping", ev.action[~known].unique())
    rep.add("audit_logs", "action_profile", "info", 0, ev.action.value_counts().to_dict().__repr__())
    bad = ev[~ev.stage.isin(config.ROLE_LEVELS)]
    rep.add("audit_logs", "valid_stage", "error", len(bad), "", bad.event_id)

    span = pd.DataFrame({"ticket_id": ev.ticket_id, "ts": ev_ts}).groupby("ticket_id").ts.agg(["min", "max"])
    t2 = tix.assign(created=created, completed=completed).set_index("ticket_id").join(span, how="inner")
    bad = t2[t2["min"] < t2.created]
    rep.add("audit_logs", "no_events_before_ticket_created", "error", len(bad), "", bad.index)
    bad = t2[t2["max"] != t2.completed]
    rep.add("tickets", "completed_at_equals_last_event", "warning", len(bad),
            "completion time should match the closing audit event", bad.index)

    e2 = ev.assign(ts=ev_ts)
    order_mismatch = (e2.sort_values(["ticket_id", "event_id"]).groupby("ticket_id").ts.diff().dt.total_seconds() < 0).sum()
    rep.add("audit_logs", "event_id_order_matches_time_order", "warning", int(order_mismatch),
            "events whose id order disagrees with timestamp order (pipeline sorts by timestamp, event_id)")
    ties = e2.duplicated(subset=["ticket_id", "ts"], keep=False).sum()
    rep.add("audit_logs", "timestamp_ties_within_ticket", "info", int(ties), "tie-break by event_id")

    bad = ev[ev.action.eq("Rejected") & ev.details.isna()]
    rep.add("audit_logs", "rejection_has_reason", "warning", len(bad), "", bad.event_id)

    approvals = ev[ev.action.eq("Approved")].groupby("ticket_id").size()
    exp = tix.set_index("ticket_id").approval_count.astype(int)
    obs = approvals.reindex(exp.index, fill_value=0)
    # Tickets with approval_count 0 still receive one Incharge approval in this export.
    bad = exp[(obs != exp.clip(lower=1))]
    rep.add("tickets", "approval_events_match_approval_count", "warning", len(bad),
            "observed approvals vs max(approval_count, 1)", bad.index)
    zero = (exp == 0).sum()
    rep.add("tickets", "approval_count_zero_still_approved", "info", int(zero),
            "tickets with approval_count=0 still contain one Incharge approval event")

    dep_events = ev[ev.action.eq("DependencyWait")].groupby("ticket_id").size()
    dep = tix.set_index("ticket_id").dependency_count.astype(int)
    has_dep_event = dep_events.reindex(dep.index, fill_value=0) > 0
    bad = dep[(dep == 0) & has_dep_event]
    rep.add("tickets", "dependency_wait_without_declared_dependency", "warning", len(bad),
            "DependencyWait logged although dependency_count=0; wait may be reviewer queue time", bad.index)
    bad = dep[(dep > 0) & ~has_dep_event]
    rep.add("tickets", "declared_dependency_without_wait_event", "info", len(bad), "", bad.index)

    exe = ev[ev.stage.eq("Executor")].merge(tix[["ticket_id", "assigned_employee_id"]], on="ticket_id")
    bad = exe[exe.employee_id != exe.assigned_employee_id]
    rep.add("audit_logs", "executor_events_by_assignee", "info", len(bad),
            "executor-stage events by someone other than the final assignee (possible reassignment)", bad.event_id)

    rep.add("all", "absence_data_available", "warning", 1,
            "no leave/absence dataset supplied; leave cannot be used as context")
    return rep.frame()
