"""Free-text comments for simulated tickets.

Comments are written the way people write on ticketing platforms: short, informal, sometimes with
abbreviations. Each comment carries a hidden label (in truth/comments_truth.csv) so an LLM classifier
can be scored. Template text is less varied than real text; this is stated in the evaluation.
"""
from __future__ import annotations

import random

DOCS = {
    "BOQ Review": ["BOQ sheet", "drawing ref", "rate analysis", "item list"],
    "Purchase Request": ["quotation", "budget code", "spec sheet", "PR form"],
    "Invoice Verification": ["invoice", "PO", "GRN", "tax invoice copy"],
    "Expense Approval": ["receipt", "hotel bill", "boarding pass", "taxi bill"],
    "Vendor Onboarding": ["GST certificate", "cancelled cheque", "PAN copy", "signed NDA"],
    "Daily Operations Report": ["shift log", "downtime sheet", "KPI tracker", "meter readings"],
    "Incident Review": ["incident log", "RCA draft", "CCTV note", "witness statement"],
    "Leave Approval": ["medical certificate", "leave form", "travel proof", "doctor's note"],
    "Employee Document Verification": ["degree certificate", "experience letter", "ID proof", "address proof"],
}

REJECT = {
    "Amount mismatch": [
        "Total on the {doc} does not match what is entered. Pls recheck the amount.",
        "Amount differs from {doc} by {n}. Correct and resend.",
        "Figures don't tally with the {doc}.",
        "Value entered is higher than the {doc} shows, please fix",
        "mismatch in totals vs {doc}",
    ],
    "Wrong quantity": [
        "Quantity is wrong, {doc} shows {n} not what you entered.",
        "Count of items doesn't match the {doc}.",
        "No. of days/units incorrect, check {doc} again",
        "qty mismatch - please correct to match {doc}",
    ],
    "Incorrect category": [
        "Booked under the wrong category/GL. Please reclassify.",
        "This should go under a different head, not this one. Check the {doc}.",
        "Wrong classification used, see policy and {doc}.",
        "category selected is incorrect, pls change",
        "GL code wrong for this item",
    ],
    "Required document missing": [
        "{doc} not attached. Please upload and resubmit.",
        "Missing {doc}, can't approve without it.",
        "Attach the {doc} first.",
        "no {doc} in the ticket",
        "supporting doc ({doc}) missing",
    ],
}

CORRECTION = {
    "Amount mismatch": ["Corrected amount as per {doc}.", "fixed totals", "amount updated to match {doc}"],
    "Wrong quantity": ["Quantity corrected.", "updated qty as per {doc}", "fixed count"],
    "Incorrect category": ["Moved to correct category.", "GL code changed", "reclassified as advised"],
    "Required document missing": ["Uploaded {doc}.", "{doc} attached now", "added missing {doc}"],
}

HOLD = {
    "external_dependency": [
        "Waiting for {provider} to send the {item}.",
        "On hold till {provider} confirms {item}.",
        "Pending {item} from {provider}.",
        "{provider} yet to revert on {item}, following up",
        "need {item} from {provider} before review",
    ],
    "approver_queue": [
        "Incharge busy today, parking this for now.",
        "In queue for review, reviewer tied up with month end.",
        "Keeping on hold until approver is free.",
        "waiting for reviewer to pick up",
        "no action yet from approver side",
    ],
    "missing_info": [
        "Asked the employee for the {doc}, waiting.",
        "Requester to share {doc}, holding till then.",
        "Need clarification from requester on the {doc}.",
        "waiting for {doc} from the claimant",
        "requester hasn't sent {doc} yet",
    ],
}

APPROVE_NOTE = ["ok", "Approved.", "fine, approved", "checked and approved", "approved - pls file the {doc}",
                "Looks good."]


def fill(rng: random.Random, template: str, task_type: str, provider: str = "", item: str = "") -> str:
    return template.format(doc=rng.choice(DOCS[task_type]), n=rng.randint(1, 12) * (rng.choice([1, 10, 100])),
                           provider=provider, item=item)


def rejection(rng, reason, task_type):
    return fill(rng, rng.choice(REJECT[reason]), task_type)


def correction(rng, reason, task_type):
    return fill(rng, rng.choice(CORRECTION[reason]), task_type)


def hold(rng, kind, task_type, provider="", item=""):
    return fill(rng, rng.choice(HOLD[kind]), task_type, provider, item.lower())


def approve_note(rng, task_type):
    return fill(rng, rng.choice(APPROVE_NOTE), task_type)
