"""SOP Intelligence Engine, step 1: extract an SOP's structure from its prose with a local LLM.

The output schema is constrained (Ollama JSON-schema format + Pydantic), so the model can only
return well-formed records with allowed roles, step types and platform rejection reasons.
Standard times, complexity drivers and other numeric parameters are NOT extracted: they are
not stated in the prose and must come from the SOP owner (schema §3.1).
"""
from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field

from .client import structured_chat

Role = Literal["Executor", "Incharge", "Lead", "HOD", "System", "External"]
StepType = Literal["intake", "work", "approval", "decision", "rework"]
Reason = Literal["Amount mismatch", "Incorrect category", "Required document missing", "Wrong quantity"]


class Step(BaseModel):
    step_id: str = Field(description="Identifier used in the document, e.g. S1, A1, R1")
    name: str
    role: Role
    type: StepType


class Approval(BaseModel):
    stage: Literal["Incharge", "Lead", "HOD"]
    condition: str = Field(description="'always', or the condition stated in the document")


class Dependency(BaseModel):
    dep_id: str = Field(description="Identifier used in the document, e.g. D1")
    provider: str = Field(description="Team or party that provides the input")
    item: str
    parallel_group: Optional[str] = Field(description="Group name if it runs in parallel with others, else null")


class ExtractedSOP(BaseModel):
    sop_id: str
    title: str
    steps: list[Step]
    approvals: list[Approval] = Field(description="Approval stages in the order they happen")
    dependencies: list[Dependency] = Field(description="External inputs the ticket waits for; empty if none")
    rework_reasons: list[Reason]
    first_pass_yield_target: Optional[float] = Field(description="First-pass yield KPI target as a fraction, e.g. 0.95")


SYSTEM = """You convert a Standard Operating Procedure (SOP) into structured JSON.
Use only information stated or clearly implied in the document. Do not invent steps.

Roles: Executor (does the work), Incharge (first reviewer/approver), Lead (second approver),
HOD (head of department), System (automatic check), External (another team or party).
Step types:
- intake: creating or assigning the ticket
- work: an activity the Executor performs (checks, calculations, drafting, submitting)
- approval: a review or approval by Incharge, Lead or HOD
- decision: a yes/no branch point
- rework: correction and resubmission after a rejection
List every step of the procedure in order. If the document gives step identifiers (S1, S2, A1, R1, ...),
use them; otherwise number them yourself: S1, S2, ... for intake and work steps, A1, A2, ... for approvals,
R1 for rework. Do not list escalation or exception handling as separate steps.
Approvals: list the approval stages in order. Use condition "always" unless the document states when the
approval is required; if an approval is only needed in certain cases, give that condition.
Dependencies: inputs from other teams or outside parties that the ticket must wait for. Use the document's
identifiers (D1, D2, ...) or number them yourself. provider = the team or party, item = what they provide.
Mark the same parallel_group (e.g. "P1") on dependencies the document says run in parallel or at the same
time. Return an empty list if the document says there is no external dependency.
Rework reasons: the platform rejection reasons listed in the document.
first_pass_yield_target: the first-pass yield KPI target as a fraction (95% -> 0.95), or null if absent."""


def extract(body: str, model: str, use_cache: bool = True) -> dict:
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": body.strip()}]
    return structured_chat(model, messages, ExtractedSOP, use_cache=use_cache)
