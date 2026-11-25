"""Process map: step labels, merged repeats, arrow counts and times, DOT output."""
import pandas as pd

from process_intel import process_map as pm


def _events():
    rows = [  # ticket, type, stage, time, change type
        ("T1", "CREATED", "Executor", "2026-01-01 09:00", None),
        ("T1", "SUBMITTED", "Executor", "2026-01-01 10:00", None),
        ("T1", "APPROVED", "Incharge", "2026-01-01 12:00", None),
        ("T2", "CREATED", "Executor", "2026-01-01 09:00", None),
        ("T2", "UPDATED", "Executor", "2026-01-01 09:30", "field_change"),
        ("T2", "UPDATED", "Executor", "2026-01-01 09:45", "field_change"),     # merged with the edit before
        ("T2", "SUBMITTED", "Executor", "2026-01-01 10:00", None),
        ("T2", "REJECTED", "Incharge", "2026-01-01 11:00", None),
        ("T2", "UPDATED", "Executor", "2026-01-01 11:30", "correction"),
        ("T2", "RESUBMITTED", "Executor", "2026-01-01 12:00", None),
        ("T2", "APPROVED", "Incharge", "2026-01-01 13:00", None),
        ("T2", "APPROVED", "Lead", "2026-01-01 15:00", None),
    ]
    return pd.DataFrame(rows, columns=["ticket_id", "event_type", "stage", "timestamp", "raw_change_type"])


def test_steps_are_plain_and_repeats_merged():
    s = pm.ticket_steps(_events())
    t2 = s[s.ticket_id == "T2"].step.tolist()
    assert t2 == ["Created", "Working on it", "Submitted", "Sent back by Incharge", "Fixing after rejection",
                  "Resubmitted", "Approved by Incharge", "Approved by Lead"]


def test_arrows_count_tickets_and_time():
    s = pm.ticket_steps(_events())
    e = pm.edges(pm.transitions(s)).set_index(["step", "next_step"])
    assert e.loc[("Submitted", "Approved by Incharge"), "median_h"] == 2.0
    assert e.loc[("Start", "Created"), "tickets"] == 2
    assert e.loc[("Approved by Lead", "Done"), "tickets"] == 1
    assert e.loc[("Created", "Working on it"), "median_h"] == 0.5      # time to the first of the merged edits


def test_paths_summary_and_dot():
    s = pm.ticket_steps(_events())
    e = pm.edges(pm.transitions(s))
    p = pm.paths(s, pd.Series({"T1": 3.0, "T2": 6.0}))
    assert p.tickets.sum() == 2 and p.share.sum() == 1.0
    text = " ".join(pm.summary(e, p, s, 4.5))
    assert "50%" in text and "sent back" in text
    dot = pm.to_dot(e, 0.0)
    assert dot.startswith("digraph") and '"Submitted" -> "Sent back by Incharge"' in dot
