"""LLM comment check: read the free-text comments and compare them with what the platform recorded.

Two questions, each asked only of the comments where it makes sense:
    rejection / correction comments -> which rejection reason does the text give?
    hold comments                   -> what is the ticket waiting for (another party, the approver,
                                       the requester)?
Then two deterministic checks on the answers:
    reason code check  the platform reason code on a rejection vs the reason in the reviewer's comment.
                       A mismatch is a data-quality finding about the ticket, not about a person.
    hold kinds         what holds are really waiting for, per task type (SOPs with no dependency
                       should not have holds; the comment says why they do).

The model only labels text. Counting, comparing and flagging are plain code.
Each distinct comment text is classified once (cached on disk by the client).
"""
from __future__ import annotations

import re
from typing import Literal

import pandas as pd
from pydantic import BaseModel, Field

from .. import config
from .client import structured_chat

REASONS = ["Amount mismatch", "Wrong quantity", "Incorrect category", "Required document missing"]
HOLD_KINDS = ["external_dependency", "approver_queue", "missing_info"]
UNCLEAR = "unclear"
OPTIONS = {"num_ctx": 2048, "num_predict": 60}


class ReasonLabel(BaseModel):
    label: Literal["Amount mismatch", "Wrong quantity", "Incorrect category", "Required document missing",
                   "unclear"] = Field(description="the one reason the comment gives")


class HoldLabel(BaseModel):
    label: Literal["external_dependency", "approver_queue", "missing_info", "unclear"] = Field(
        description="what the ticket is waiting for")


REASON_GUIDE = """Reasons:
- Amount mismatch: a money value, total, price or tax amount is wrong or differs from a document.
- Wrong quantity: a count is wrong: number of items, units, days, nights, lines ("qty" and "no." mean quantity
  and number, whatever document they are compared with).
- Incorrect category: the ticket is filed under the wrong category, GL code, cost head, type or classification.
- Required document missing: something must be attached, uploaded or provided, or is "not in the ticket",
  whatever that something is (even a code or a form). Answer this when the fix is to add something.
- unclear: the comment gives none of these (e.g. "redo", "discussed on call", "done").
If the comment says something is fine and something else is wrong, answer with what is wrong.
If it is a money total that is wrong because a count is wrong, answer Wrong quantity."""

PROMPTS = {
    "rejection": ("A reviewer wrote this comment when rejecting a ticket. Which one reason does it give "
                  "for the rejection?\n" + REASON_GUIDE),
    "correction": ("The person who raised a ticket wrote this comment after fixing it following a rejection. "
                   "Which one reason was fixed?\n" + REASON_GUIDE),
    "hold": """The person working on a ticket wrote this comment when putting it on hold. Who is it waiting for?
- external_dependency: any other team, department or outside organisation (vendor, bank, insurer, legal, IT,
  finance, a client, a government office...) that must send, confirm or clear something.
- approver_queue: the reviewer or approver (incharge, manager, lead, HOD, "sir"...) has not acted yet.
- missing_info: the requester, employee or claimant who raised the ticket must send information or a document.
  Use this only when the comment points to that person.
"Need X from <team> before review" or "pending X from <team>": the ticket waits for that team, so it is
external_dependency whenever the team is not the requester or the approver.
- unclear: the comment names nobody it is waiting for (e.g. "on hold", "will check later").""",
}
SCHEMAS = {"rejection": ReasonLabel, "correction": ReasonLabel, "hold": HoldLabel}


def classify(text: str, context: str, model: str, use_cache: bool = True) -> dict:
    msgs = [{"role": "system", "content": PROMPTS[context]},
            {"role": "user", "content": f"Comment: {text}"}]
    r = structured_chat(model, msgs, SCHEMAS[context], OPTIONS, use_cache)
    return {"label": r["parsed"].label if r["parsed"] else UNCLEAR, "error": r["error"],
            "seconds": r["seconds"], "cached": r["cached"]}


# ------------------------------------------------------------------ keyword baseline (for comparison only)
_KW = {
    "rejection": [("Required document missing", r"missing|not attached|attach|upload|no .* in the ticket"),
                  ("Incorrect category", r"categor|\bgl\b|classif|head\b"),
                  ("Wrong quantity", r"qty|quantity|count|no\. of"),
                  ("Amount mismatch", r"amount|total|figure|value|tally")],
    "hold": [("approver_queue", r"approver|reviewer|incharge|queue"),
             ("missing_info", r"requester|employee|claimant|clarification"),
             ("external_dependency", r"waiting for|pending|yet to revert|on hold till|need .* from")],
}
_KW["correction"] = [("Required document missing", r"upload|attached|added"),
                     ("Incorrect category", r"categor|\bgl\b|reclassif"),
                     ("Wrong quantity", r"qty|quantity|count"),
                     ("Amount mismatch", r"amount|total")]


def keyword_label(text: str, context: str) -> str:
    t = text.lower()
    return next((lab for lab, rx in _KW[context] if re.search(rx, t)), UNCLEAR)


# ------------------------------------------------------------------ run on a dataset
CONTEXT_OF = {("Rejected", "rejection_reason"): "rejection", ("Updated", "correction"): "correction",
              ("DependencyWait", "dependency"): "hold"}


def comment_frame(comments: pd.DataFrame, events: pd.DataFrame, tickets: pd.DataFrame) -> pd.DataFrame:
    """Comments with the event they belong to; only those the check reads (rejection, correction, hold)."""
    ev = events[["event_id", "action", "change_type", "details", "stage"]]
    c = comments.merge(ev, on="event_id", how="left").merge(tickets[["ticket_id", "task_type", "department"]],
                                                            on="ticket_id", how="left")
    c["context"] = [CONTEXT_OF.get((a, ct)) for a, ct in zip(c.action, c.change_type.fillna(""))]
    c = c[c.context.notna()].copy()
    c["platform_code"] = c.details.where(c.context.isin(["rejection", "correction"]))
    return c.drop(columns=["details", "change_type"])


def label_comments(c: pd.DataFrame, model: str, use_cache: bool = True, progress=None) -> pd.DataFrame:
    uniq = c[["context", "text"]].drop_duplicates()
    out = []
    for i, (ctx, txt) in enumerate(uniq.itertuples(index=False), 1):
        r = classify(txt, ctx, model, use_cache)
        out.append({"context": ctx, "text": txt, "llm_label": r["label"], "llm_error": r["error"],
                    "llm_seconds": r["seconds"], "llm_cached": r["cached"]})
        if progress:
            progress(i, len(uniq), ctx, txt, r)
    return c.merge(pd.DataFrame(out), on=["context", "text"], how="left")


def reason_code_checks(labelled: pd.DataFrame) -> pd.DataFrame:
    """One row per rejection with a comment: platform code vs the reason in the comment.

    status: mismatch (comment clearly gives another reason) / agrees / unclear (comment gives no reason).
    The fix comment, when there is one, is shown as a second opinion and raises the confidence.
    """
    rej = labelled[labelled.context == "rejection"]
    fix = labelled[labelled.context == "correction"][["ticket_id", "platform_code", "llm_label", "text"]]
    fix = fix.rename(columns={"llm_label": "fix_label", "text": "fix_text"})
    # a correction belongs to the rejection with the same ticket and code; keep the first per pair
    fix = fix.drop_duplicates(["ticket_id", "platform_code"])
    r = rej.merge(fix, on=["ticket_id", "platform_code"], how="left")
    r["status"] = "agrees"
    r.loc[r.llm_label == UNCLEAR, "status"] = UNCLEAR
    r.loc[(r.llm_label != UNCLEAR) & (r.llm_label != r.platform_code), "status"] = "mismatch"
    r["confidence"] = ""
    mm = r.status == "mismatch"
    r.loc[mm, "confidence"] = "medium"
    r.loc[mm & (r.fix_label == r.llm_label), "confidence"] = "high"
    r.loc[mm & r.fix_label.notna() & (r.fix_label == r.platform_code), "confidence"] = "low"   # fix contradicts
    return r[["comment_id", "ticket_id", "event_id", "task_type", "department", "stage", "timestamp",
              "platform_code", "text", "llm_label", "fix_text", "fix_label", "status", "confidence"]]


def reason_counts(checks: pd.DataFrame) -> pd.DataFrame:
    """Rejections per reason as the platform recorded them vs as the comments describe them."""
    plat = checks.platform_code.value_counts().rename("platform_code")
    com = checks.llm_label.value_counts().rename("comment_says")
    return pd.concat([plat, com], axis=1).fillna(0).astype(int).rename_axis("reason").reset_index()


def hold_kinds(labelled: pd.DataFrame, sops: dict) -> pd.DataFrame:
    """Holds per task type by what the comment says they wait for, and whether the SOP has a dependency."""
    h = labelled[labelled.context == "hold"]
    t = (h.groupby(["task_type", "llm_label"]).size().unstack(fill_value=0)
         .reindex(columns=HOLD_KINDS + [UNCLEAR], fill_value=0))
    t["holds"] = t.sum(axis=1)
    t["sop_has_dependency"] = [bool(sops.get(tt, {}).get("dependencies")) for tt in t.index]
    t["not_an_external_dependency"] = t.approver_queue + t.missing_info
    return t.reset_index()


def summary(checks: pd.DataFrame, holds: pd.DataFrame) -> dict:
    mm = checks[checks.status == "mismatch"]
    no_dep = holds[~holds.sop_has_dependency]
    return {
        "rejections_with_comment": len(checks),
        "reason_code_mismatches": len(mm),
        "mismatch_share": round(len(mm) / max(len(checks), 1), 3),
        "mismatch_by_confidence": mm.confidence.value_counts().to_dict(),
        "unclear_comments": int((checks.status == UNCLEAR).sum()),
        "mismatch_by_task_type": mm.task_type.value_counts().to_dict(),
        "holds": int(holds.holds.sum()),
        "holds_on_sops_without_dependency": int(no_dep.holds.sum()),
        "of_which_approver_queue": int(no_dep.approver_queue.sum()),
        "of_which_missing_info": int(no_dep.missing_info.sum()),
        "dependency_holds_not_external": int(holds[holds.sop_has_dependency].not_an_external_dependency.sum()),
    }


def load_dataset(data_dir) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    return (pd.read_csv(data_dir / "extra" / "comments.csv"), pd.read_csv(data_dir / "raw" / "audit_logs.csv"),
            pd.read_csv(data_dir / "raw" / "tickets.csv"))


def score_labels(labelled: pd.DataFrame, truth: pd.DataFrame) -> pd.DataFrame:
    """Accuracy of the LLM labels (and the keyword baseline) against the simulator's hidden labels."""
    t = labelled.merge(truth[["comment_id", "true_label"]], on="comment_id")
    t["keyword_label"] = [keyword_label(x, c) for x, c in zip(t.text, t.context)]
    return (t.assign(llm_ok=t.llm_label == t.true_label, kw_ok=t.keyword_label == t.true_label)
            .groupby("context").agg(comments=("text", "size"), distinct_texts=("text", "nunique"),
                                    llm_accuracy=("llm_ok", "mean"), keyword_accuracy=("kw_ok", "mean"))
            .round(3).reset_index())


MESSY_FILES = {"tuning": config.ROOT / "data" / "benchmark" / "comments_messy.csv",       # the prompt was fixed once on this set
               "holdout": config.ROOT / "data" / "benchmark" / "comments_messy_holdout.csv"}  # written after; never tuned on


def messy_benchmark(model: str, use_cache: bool = True) -> pd.DataFrame:
    """Hand-written comments in styles the simulator's templates do not use (typos, negations, other wording)."""
    b = pd.concat([pd.read_csv(f).assign(set=k) for k, f in MESSY_FILES.items()], ignore_index=True)
    b["llm_label"] = [classify(t, c, model, use_cache)["label"] for t, c in zip(b.text, b.context)]
    b["keyword_label"] = [keyword_label(t, c) for t, c in zip(b.text, b.context)]
    return b
