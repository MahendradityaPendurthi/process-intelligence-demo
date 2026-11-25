"""SOP Intelligence Engine, step 2: draft -> automatic checks -> human review.

1. draft():  the selected local LLM extracts the SOP structure from the prose. Every approval and dependency
             must carry `evidence`: the sentence of the document that states it, copied word for word.
2. check():  deterministic checks of the draft against the text (is the quote really there, does it name the
             approver, is it only boilerplate, does it contradict "no external dependency", ...).
3. compare_with_yaml(): agreement with the currently approved YAML, where one exists.
4. A reviewer edits and approves or rejects the draft (app/sop_review_app.py). Decisions are files plus an
   append-only log; an approval goes stale when the SOP text changes.

Nothing here feeds the pipeline automatically: an approved draft still lacks standard times, which only the
SOP owner can supply (schema §3.1).
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
from difflib import SequenceMatcher
from pathlib import Path

from pydantic import Field

from .. import config, sop
from .benchmark import _same_party, score
from .client import structured_chat
from .sop_extract import SYSTEM, Approval, Dependency, ExtractedSOP

REVIEW_DIR = Path(os.environ.get("SOP_REVIEW_DIR", config.ROOT / "data" / "sop_review"))
SELECTED = config.OUTPUT_DIR / "llm" / "selected_model.json"
OPTIONS = {"num_ctx": 8192,          # legacy SOPs are ~5k characters
           "num_predict": 3000}      # a draft needs ~1.5k tokens; caps runaway generation (seen once on SOP-021)


# One sentence is enough; the limit is enforced by the output grammar and stops copy loops
# (llama3.1 once repeated a table separator until the token cap on SOP-021).
EVIDENCE_MAX = 300


class ApprovalE(Approval):
    evidence: str = Field(max_length=EVIDENCE_MAX,
                          description="The sentence from the document that states this approval, copied word for word")


class DependencyE(Dependency):
    evidence: str = Field(max_length=EVIDENCE_MAX,
                          description="The sentence from the document that states this dependency, copied word for word")


class DraftSOP(ExtractedSOP):
    approvals: list[ApprovalE] = Field(description="Approval stages in the order they happen")
    dependencies: list[DependencyE] = Field(description="External inputs the ticket waits for; empty if none")


DRAFT_SYSTEM = SYSTEM + """
Evidence: for every approval and every dependency, copy into `evidence` the sentence of the document that
states it, word for word: one sentence, or one row of a table, never more. Do not paraphrase.
If no sentence states it, do not list it."""


def selected_model() -> str:
    try:
        return json.loads(SELECTED.read_text(encoding="utf-8"))["model"]
    except (OSError, KeyError, ValueError):
        return "llama3.1:latest"


def source_text(record: dict) -> str:
    """What the reviewer and the model read: the prose (YAML front matter is never shown to the model)."""
    return record["body"].strip()


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# --------------------------------------------------------------------------- drafting

def draft(record: dict, model: str | None = None, use_cache: bool = True) -> dict:
    model = model or selected_model()
    text = source_text(record)
    messages = [{"role": "system", "content": DRAFT_SYSTEM}, {"role": "user", "content": text}]
    res = structured_chat(model, messages, DraftSOP, options=OPTIONS, use_cache=use_cache)
    d = res["parsed"]
    out = {
        "sop_id": record["sop_id"], "file": record["file"], "format": record["format"], "model": model,
        "source_sha256": _sha(text), "drafted_at": dt.datetime.now().isoformat(timespec="seconds"),
        "seconds": round(res["seconds"], 1), "error": res["error"],
        "draft": d.model_dump() if d else None,
    }
    out["checks"] = check(out["draft"], text) if d else [_issue("error", "draft", "", f"invalid model output: {res['error']}")]
    out["comparison"] = compare_with_yaml(out["draft"], record) if d else None
    return out


# --------------------------------------------------------------------------- checks

BOILERPLATE = re.compile(r"glossary|definitions?|roles and responsibilities|identification|purpose|prerequisites",
                         re.I)
NO_DEPENDENCY = re.compile(r"no external dependency|no dependency|never held|not by (putting|holding)", re.I)
CONDITIONAL = re.compile(r"\b(only|if|above|over|more than|longer than|exceed\w*|when|where|major|any discrepancy|"
                         r"out-of-tolerance|out of tolerance|high-value|high value)\b", re.I)
ROLE_WORDS = {"Incharge": ["incharge", "in-charge"], "Lead": ["lead"],
              "HOD": ["hod", "head of department", "department head", "head of"]}


def _norm(s: str) -> str:
    s = re.sub(r"[*_`|#>]", " ", s.lower())
    s = s.replace("’", "'").replace("–", "-").replace("—", "-").replace("→", "->")
    return re.sub(r"\s+", " ", s).strip()


def locate(quote: str, text: str) -> tuple[float, int]:
    """(share of the quote found verbatim as one block in the text, position in the normalised text)."""
    q, t = _norm(quote), _norm(text)
    if not q:
        return 0.0, -1
    i = t.find(q)
    if i >= 0:
        return 1.0, i
    m = SequenceMatcher(None, t, q, autojunk=False).find_longest_match(0, len(t), 0, len(q))
    return m.size / len(q), m.a


def _section_of(pos: int, text: str) -> str:
    """Heading (markdown heading or short title line) above a position of the normalised text."""
    t_lines, seen = text.splitlines(), 0
    title = ""
    for line in t_lines:
        n = _norm(line)
        if seen + len(n) >= pos and n:
            # the line itself can open with a section label ("Roles and Responsibilities: ...")
            head = n.split(":")[0] if ":" in n[:40] else ""
            return head or title
        if line.lstrip().startswith("#") or (0 < len(n) < 40 and not n.endswith(".") and "|" not in line):
            title = n
        seen += len(n) + (1 if n else 0)
    return title


def table_cells(quote: str, text: str) -> list[tuple[str, str]]:
    """(column header, cell) pairs of every markdown table row that the quote comes from.
    Lets a quoted RACI row ("| Approval | I | R/A | A (exceptions only) |") support the role in its header."""
    q = _norm(quote)
    out, header = [], None
    for line in text.splitlines() + [""]:
        if not line.strip().startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue
        normed = [_norm(c) for c in cells]
        if q and (q in normed or (len(q) > 25 and q in _norm(line))):
            out += list(zip(header, cells))
    return out


def _supports_role(quote: str, stage: str, text: str) -> tuple[bool, str]:
    """(role supported, extra condition text from the RACI cell)."""
    if any(w in _norm(quote) for w in ROLE_WORDS[stage]):
        return True, ""
    for head, cell in table_cells(quote, text):
        if any(w in _norm(head) for w in ROLE_WORDS[stage]) and re.search(r"\b[AR]\b", cell):
            return True, " ".join(re.findall(r"\(([^)]*)\)", cell))
    return False, ""


def _supports_party(quote: str, provider: str, text: str) -> bool:
    if _same_party(quote, provider):
        return True
    return any(_same_party(head, provider) and re.search(r"\bR\b", cell) for head, cell in table_cells(quote, text))


def _issue(severity: str, field: str, item: str, message: str) -> dict:
    return {"severity": severity, "field": field, "item": item, "message": message}


def check(d: dict, text: str) -> list[dict]:
    """Deterministic checks of a draft against its source text. Severity: error > warning > info."""
    issues = []
    low = _norm(text)

    for a in d["approvals"]:
        item = f"{a['stage']} ({a['condition']})"
        found, pos = locate(a.get("evidence", ""), text)
        if found < 0.8:
            issues.append(_issue("error", "approvals", item, "Quoted evidence is not in the text"))
            continue
        quote = _norm(a["evidence"])
        supported, cell_condition = _supports_role(a["evidence"], a["stage"], text)
        if not supported:
            issues.append(_issue("error", "approvals", item, f"The quote does not mention the {a['stage']}"))
        quote = f"{quote} {cell_condition}"
        if BOILERPLATE.search(_section_of(pos, text)):
            issues.append(_issue("warning", "approvals", item,
                                 f"Only stated in a generic section ('{_section_of(pos, text)}'), not the procedure"))
        if a["condition"].strip().lower() in ("always", "", "none") and CONDITIONAL.search(quote):
            issues.append(_issue("warning", "approvals", item, "Marked 'always' but the quote states a condition"))
    stages = [a["stage"] for a in d["approvals"]]
    for s in sorted({s for s in stages if stages.count(s) > 1}):
        issues.append(_issue("warning", "approvals", s, "Approval stage listed more than once"))

    if d["dependencies"] and NO_DEPENDENCY.search(text):
        issues.append(_issue("error", "dependencies", "", "The text says there is no external dependency"))
    for x in d["dependencies"]:
        item = f"{x['dep_id']} {x['provider']}"
        found, _ = locate(x.get("evidence", ""), text)
        if found < 0.8:
            issues.append(_issue("error", "dependencies", item, "Quoted evidence is not in the text"))
        elif not _supports_party(x["evidence"], x["provider"], text):
            issues.append(_issue("warning", "dependencies", item, "The quote does not name this provider"))
    groups = [x["parallel_group"] for x in d["dependencies"] if x.get("parallel_group")]
    for g in sorted({g for g in groups if groups.count(g) == 1}):
        issues.append(_issue("info", "dependencies", g, "Parallel group with a single dependency"))

    types = [s["type"] for s in d["steps"]]
    if "intake" not in types:
        issues.append(_issue("warning", "steps", "", "No intake step (ticket creation / assignment)"))
    if d["approvals"] and "approval" not in types:
        issues.append(_issue("warning", "steps", "", "Approvals listed but no approval step"))
    if re.search(r"reject", low) and "rework" not in types:
        issues.append(_issue("warning", "steps", "", "The text mentions rejections but there is no rework step"))
    ids = [s["step_id"] for s in d["steps"]]
    for s in sorted({s for s in ids if ids.count(s) > 1}):
        issues.append(_issue("warning", "steps", s, "Duplicate step identifier"))

    for r in config.PLATFORM_REJECTION_REASONS:
        if r in d["rework_reasons"] and r.lower() not in low:
            issues.append(_issue("error", "rework_reasons", r, "Listed but not mentioned in the text"))
        if r not in d["rework_reasons"] and r.lower() in low:
            issues.append(_issue("warning", "rework_reasons", r, "Mentioned in the text but not listed"))

    fpy = d.get("first_pass_yield_target")
    if fpy is None:
        issues.append(_issue("info", "first_pass_yield_target", "", "No first-pass yield target found"))
    else:
        pct = round(fpy * 100 if fpy <= 1 else fpy)
        if not re.search(rf"\b{pct}\s?%", text):
            issues.append(_issue("warning", "first_pass_yield_target", f"{pct}%", "Value not written in the text as a %"))
    return issues


def compare_with_yaml(d: dict | None, record: dict) -> dict | None:
    """Agreement with the currently approved structured SOP (schema SOPs only)."""
    if d is None or record["format"] != "schema" or not record["data"]:
        return None
    plain = ExtractedSOP.model_validate(d)
    sc = score(plain, record["data"], record["body"])
    return {k: (round(v, 3) if isinstance(v, float) else v) for k, v in sc.items()}


# --------------------------------------------------------------------------- storage and decisions

def _dir(name: str) -> Path:
    p = REVIEW_DIR / name
    p.mkdir(parents=True, exist_ok=True)
    return p


def save_draft(result: dict) -> Path:
    path = _dir("drafts") / f"{result['sop_id']}.json"
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def load_draft(sop_id: str) -> dict | None:
    path = REVIEW_DIR / "drafts" / f"{sop_id}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def load_decision(sop_id: str) -> dict | None:
    path = REVIEW_DIR / "decisions" / f"{sop_id}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def decide(sop_id: str, status: str, reviewer: str, edited: dict, notes: str = "", override: bool = False) -> dict:
    """Record a review decision. status: approved | changes_requested | rejected.
    Approval with open errors requires override=True and a note."""
    if status not in ("approved", "changes_requested", "rejected"):
        raise ValueError(status)
    if not reviewer.strip():
        raise ValueError("reviewer name is required")
    rec = next(r for r in sop.load_sops() if r["sop_id"] == sop_id)
    text = source_text(rec)
    edited = DraftSOP.model_validate(edited).model_dump()          # schema still enforced after edits
    issues = check(edited, text)
    errors = [i for i in issues if i["severity"] == "error"]
    if status == "approved" and errors and not (override and notes.strip()):
        raise ValueError(f"{len(errors)} open errors: approve with override and a note, or fix them first")
    base = load_draft(sop_id) or {}
    decision = {
        "sop_id": sop_id, "status": status, "reviewer": reviewer.strip(), "notes": notes.strip(),
        "decided_at": dt.datetime.now().isoformat(timespec="seconds"), "source_sha256": _sha(text),
        "model": base.get("model"), "edited_by_reviewer": base.get("draft") != edited,
        "override_errors": bool(errors) and status == "approved", "open_issues": issues, "structure": edited,
    }
    (_dir("decisions") / f"{sop_id}.json").write_text(json.dumps(decision, indent=2, ensure_ascii=False), encoding="utf-8")
    approved = REVIEW_DIR / "approved" / f"{sop_id}.json"
    if status == "approved":
        _dir("approved")
        approved.write_text(json.dumps(decision, indent=2, ensure_ascii=False), encoding="utf-8")
    elif approved.exists():
        approved.unlink()                                          # a later rejection withdraws the approval
    with (REVIEW_DIR / "review_log.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({k: decision[k] for k in ("sop_id", "status", "reviewer", "decided_at", "notes",
                                                      "edited_by_reviewer", "override_errors", "source_sha256")}) + "\n")
    return decision


def status_of(record: dict) -> str:
    """draft missing | to_review | approved | changes_requested | rejected | stale (text changed since decision)."""
    dec = load_decision(record["sop_id"])
    if dec is None:
        return "to_review" if load_draft(record["sop_id"]) else "no_draft"
    if dec["source_sha256"] != _sha(source_text(record)):
        return "stale"
    return dec["status"]
