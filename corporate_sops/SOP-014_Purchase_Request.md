---
schema_version: "1.2"
sop_id: SOP-014
title: Purchase Request Processing
version: 1.1.0
status: Approved
effective_date: 2026-10-14
review_cycle_months: 12
owner_role: Lead
department: Procurement
task_type: Purchase Request
supersedes: [SOP-002]
complexity_declared: Medium
standard_time_source: illustrative_expert_estimate
standard_time_frozen: 2026-10-14
quality_targets_source: unconfirmed

sla_hours: {High: 6, Medium: 12, Low: 24}
sop_steps: 4
approval_count_base: 2
approval_count_max: 2
approval_matrix:
  - {stage: Incharge, condition: always}
  - {stage: Lead, condition: always}

dependency_count: 1
dependencies:
  - id: D1
    provider: Finance (budget control)
    item: "Budget availability confirmation for the cost centre"
    blocking_step: A1
    parallel_group: P1
    typical_wait_h: {min: 0.5, likely: 1.5, max: 4.0}

complexity_drivers:
  - {driver: line_items, source: ticket_metadata, bands: {low: "<=5", medium: "6-20", high: ">20"}, effect: effort}
  - {driver: pr_value_inr, source: ticket_metadata, bands: {low: "<=100000", medium: "100001-1000000", high: ">1000000"}, effect: approval_route}
  - {driver: sourcing_route, source: ticket_metadata, bands: {low: "rate_contract", medium: "competitive_quotes", high: "single_source"}, effect: rework_risk}

steps:
  - step_id: S1
    name: Create and self-assign purchase request
    role: Executor
    type: intake
    mandatory: true
    audit_actions: [Created, Assigned]
    effort_min: {min: 2, likely: 3, max: 5}
    queue_wait_h: {min: 0.05, likely: 0.25, max: 1.0}
    skill_level: 1
  - step_id: S2
    name: Validate requisition details and specifications
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 15, max: 30}
    effort_scaling: {driver: line_items, per_unit_min: 1.0, unit: line item}
    inputs: [requisition form, item specifications]
    outputs: [validated requisition]
    skill_level: 1
  - step_id: S3
    name: Check budget head and cost centre
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 5, likely: 10, max: 20}
    inputs: [budget report]
    outputs: [budget check note]
    skill_level: 1
  - step_id: D-SRC
    name: "Rate contract available?"
    role: System
    type: decision
    mandatory: true
    audit_actions: []
    effort_min: {min: 0, likely: 0, max: 0}
  - step_id: S4
    name: Determine sourcing route and estimate value
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 25, max: 50}
    inputs: [rate contracts, vendor list, past purchase prices]
    outputs: [sourcing recommendation, estimated value]
    skill_level: 2
  - step_id: S5
    name: Prepare purchase request note and submit
    role: Executor
    type: work
    mandatory: true
    audit_actions: [Submitted]
    effort_min: {min: 10, likely: 15, max: 25}
    outputs: [purchase request note]
    skill_level: 1
  - step_id: A1
    name: Incharge review
    role: Incharge
    type: approval
    mandatory: true
    audit_actions: [Approved, Rejected]
    effort_min: {min: 10, likely: 15, max: 30}
    queue_wait_h: {min: 0.25, likely: 0.75, max: 3.0}
    skill_level: 2
  - step_id: A2
    name: Lead approval
    role: Lead
    type: approval
    mandatory: true
    audit_actions: [Approved, Rejected]
    effort_min: {min: 5, likely: 10, max: 20}
    queue_wait_h: {min: 0.25, likely: 1.0, max: 4.0}
    skill_level: 3
  - step_id: D-HOD
    name: "Value above HOD limit?"
    role: System
    type: decision
    mandatory: true
    audit_actions: []
    effort_min: {min: 0, likely: 0, max: 0}
  - step_id: R1
    name: Correction and resubmission
    role: Executor
    type: rework
    mandatory: false
    audit_actions: [Updated, Resubmitted]
    effort_min: {min: 10, likely: 20, max: 45}

rework_triggers:
  - {code: RW-QTY, reason: Wrong quantity, detected_at: A1, preventable_by: "S2 requisition validation"}
  - {code: RW-AMT, reason: Amount mismatch, detected_at: A1, preventable_by: "S4 value estimate against past prices"}
  - {code: RW-CAT, reason: Incorrect category, detected_at: A1, preventable_by: "S3 budget head check"}
  - {code: RW-DOC, reason: Required document missing, detected_at: A1, preventable_by: "S5 attachment checklist"}
expected_first_pass_yield: 0.90
rework_effort_min: {min: 10, likely: 20, max: 45}
max_rework_cycles: 2

exceptions:
  - {code: EX-HODLIMIT, condition: "pr_value_inr > 1000000", action: "Route to HOD after Lead approval", adds_approval: HOD, adds_dependency_wait: false}
  - {code: EX-SINGLESRC, condition: "sourcing_route == single_source", action: "Attach single-source justification signed by the requester", adds_approval: null, adds_dependency_wait: false}
  - {code: EX-NOBUDGET, condition: "budget not available", action: "Reject with Incorrect category; requester raises a budget re-appropriation", adds_approval: null, adds_dependency_wait: false}
---

# SOP-014: Purchase Request Processing

## 1. Purpose
Turn a valid internal requisition into an approved purchase request with a confirmed budget and an agreed
sourcing route.

## 2. Scope
All requisitions for goods and services processed by Procurement. Emergency purchases under the petty-cash
policy are excluded. Supersedes SOP-002.

## 3. References
ISO 9001:2015 §8.4; delegation-of-authority matrix; SOP-013 BOQ Review; SOP-017 Vendor Onboarding.

## 4. Definitions
- **Rate contract**: a pre-negotiated price agreement with an approved vendor.
- **Single source**: purchase from one vendor without competitive quotes.

## 5. Responsibilities (RACI)
| Activity | Executor | Incharge | Lead | HOD | Finance |
|---|---|---|---|---|---|
| Validate and prepare PR | R | A | – | – | – |
| Budget confirmation (D1) | C | I | – | – | R |
| Review and approval | I | R | A | A (above HOD limit) | – |

## 6. Procedure
1. **S1** The Executor creates the ticket and assigns it to themselves.
2. **S2** Validate item descriptions, quantities, specifications and required-by date.
3. **S3** Check the budget head and cost centre against the latest budget report.
4. **S4** Choose the sourcing route (rate contract, competitive quotes, or single source) and estimate the value.
5. **S5** Prepare the PR note and submit.
6. After submission, if Finance has not yet confirmed budget availability, log `DependencyWait` (D1).
7. **A1** Incharge review, then **A2** Lead approval. HOD approval is added above ₹10 lakh (EX-HODLIMIT).
8. **R1** On rejection, correct and resubmit. After 2 rejections, escalate to the Lead.

## 7. Exceptions
See YAML `exceptions`.

## 8. Rejection reason codes
| Platform reason | Meaning for a purchase request |
|---|---|
| Wrong quantity | Quantity inconsistent with requisition or stock norms |
| Amount mismatch | Estimated value inconsistent with rate contract or past prices |
| Incorrect category | Wrong budget head, cost centre or item category |
| Required document missing | Specifications, quotations or single-source justification missing |

## 9. Records
Requisition, PR note, budget confirmation, sourcing justification, approval trail. Retain 8 years.

## 10. KPIs
| KPI | Target |
|---|---|
| SLA compliance | ≥ 95% |
| First-pass yield | ≥ 90% |

## 11. Revision history
| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-14 | Initial schema v1.1 release; supersedes SOP-002 |
| 1.1.0 | 2026-10-14 | Schema v1.2: added `parallel_group` and `quality_targets_source`. Standard times unchanged |
