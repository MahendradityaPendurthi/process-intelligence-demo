"""Planted scenarios: what the simulator deliberately puts into the data, and what should detect it.

Each scenario has an id, a level (process / employee / ticket / platform / sop_standard / control),
the entity it affects, a period and the Phase 1 deviation types that ought to catch it.
`control` scenarios are negative controls: they must NOT be flagged.
"""
from __future__ import annotations

import datetime as dt

D = dt.date

SCENARIOS = [
    {"id": "SC01", "name": "finance_incharge_slowdown", "level": "process", "department": "Finance",
     "entity": "Finance:Incharge", "task_type": None, "start": D(2026, 2, 1), "end": D(2026, 3, 31),
     "effect": "Finance Incharge response latency x3 and review effort x2",
     "expected": ["APPROVAL_WAIT_INCREASE", "APPROVAL_STAGE_BOTTLENECK", "TICKET_DURATION"]},
    {"id": "SC02", "name": "executor_unexplained_slowdown", "level": "employee", "department": "Finance",
     "entity": "E1003", "task_type": None, "start": D(2026, 7, 1), "end": D(2026, 9, 30),
     "effect": "E1003 executor work x1.7 with unchanged workload",
     "expected": ["PERSISTENT_UNEXPLAINED_PROCESSING_INCREASE"]},
    {"id": "SC03", "name": "executor_slowdown_with_workload", "level": "employee", "department": "Operations",
     "entity": "E1015", "task_type": None, "start": D(2026, 6, 1), "end": D(2026, 9, 30),
     "effect": "E1015 receives 3x assignment share; work x1.4",
     "expected": ["PERSISTENT_PROCESSING_INCREASE_WITH_CONTEXT"]},
    {"id": "SC04", "name": "executor_long_leave", "level": "control", "department": "HR",
     "entity": "E1021", "task_type": None, "start": D(2026, 4, 6), "end": D(2026, 4, 24),
     "effect": "E1021 on approved leave; no tickets assigned. Must not be flagged",
     "expected": []},
    {"id": "SC05", "name": "invoice_category_rework_spike", "level": "process", "department": "Finance",
     "entity": "Invoice Verification", "task_type": "Invoice Verification", "start": D(2026, 5, 1),
     "end": D(2026, 6, 30), "effect": "Incorrect category rejections x5 (GL mapping control broken)",
     "expected": ["REWORK_INCREASE", "REWORK_ABOVE_SOP_EXPECTATION", "TICKET_DURATION"]},
    {"id": "SC06", "name": "purchase_lead_approval_skipped", "level": "process", "department": "Procurement",
     "entity": "Purchase Request", "task_type": "Purchase Request", "start": D(2026, 7, 1),
     "end": D(2026, 9, 30), "effect": "Lead approval skipped on 45% of Purchase Requests",
     "expected": ["SOP_NONCONFORMANCE"]},
    {"id": "SC07", "name": "vendor_screening_delay", "level": "process", "department": "Procurement",
     "entity": "Vendor Onboarding", "task_type": "Vendor Onboarding", "start": D(2026, 1, 1),
     "end": D(2026, 2, 28), "effect": "Legal/Compliance screening (D2) wait x3",
     "expected": ["APPROVAL_WAIT_INCREASE", "TICKET_DURATION"]},
    {"id": "SC08", "name": "operations_overload", "level": "process", "department": "Operations",
     "entity": "Operations", "task_type": None, "start": D(2026, 8, 15), "end": D(2026, 9, 30),
     "effect": "Operations volume x1.8; approver latency x2.5; executor work x1.2",
     "expected": ["SLA_DROP", "SLA_DETERIORATION", "APPROVAL_WAIT_INCREASE"]},
    {"id": "SC09", "name": "undeclared_holds", "level": "process", "department": None,
     "entity": "Expense Approval|Leave Approval|Daily Operations Report", "task_type": None,
     "start": D(2025, 10, 1), "end": D(2026, 9, 30),
     "effect": "Tickets with no SOP dependency put on hold (approver queue or missing info)",
     "expected": ["SOP_NONCONFORMANCE"]},
    {"id": "SC10", "name": "hod_approval_not_logged", "level": "platform", "department": "Procurement",
     "entity": "Vendor Onboarding", "task_type": "Vendor Onboarding", "start": D(2025, 10, 1),
     "end": D(2026, 9, 30), "effect": "HOD approval happens but the platform never logs it",
     "expected": ["SOP_NONCONFORMANCE"]},
    {"id": "SC11", "name": "dor_default_approval", "level": "process", "department": "Operations",
     "entity": "Daily Operations Report", "task_type": "Daily Operations Report", "start": D(2025, 10, 1),
     "end": D(2026, 9, 30), "effect": "Incharge approval on every report although the SOP makes it conditional",
     "expected": ["SOP_NONCONFORMANCE"]},
    {"id": "SC12", "name": "sop_standards_high", "level": "sop_standard", "department": None,
     "entity": "most task types", "task_type": None, "start": D(2025, 10, 1), "end": D(2026, 9, 30),
     "effect": "Real executor effort is 40-70% of SOP standard for most task types",
     "expected": ["SOP_EFFORT_STANDARD", "SOP_ELAPSED_BELOW_STANDARD"]},
    {"id": "SC13", "name": "reason_code_mislabel", "level": "ticket", "department": None, "entity": "all",
     "task_type": None, "start": D(2025, 10, 1), "end": D(2026, 9, 30),
     "effect": "15% of rejections carry a platform reason code that contradicts the reviewer's comment",
     "expected": ["LLM_COMMENT_CHECK"]},
    {"id": "SC14", "name": "steady_executor", "level": "control", "department": "Finance", "entity": "E1004",
     "task_type": None, "start": D(2025, 10, 1), "end": D(2026, 9, 30),
     "effect": "Normal performer throughout. Must not be flagged", "expected": []},
]

BY_ID = {s["id"]: s for s in SCENARIOS}


def active(sid: str, day: dt.date) -> bool:
    s = BY_ID[sid]
    return s["start"] <= day <= s["end"]
