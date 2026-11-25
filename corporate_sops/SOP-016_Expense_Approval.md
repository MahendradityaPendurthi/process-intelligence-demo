---
schema_version: "1.2"
sop_id: SOP-016
title: Employee Expense Claim Approval
version: 1.1.0
status: Approved
effective_date: 2026-10-14
review_cycle_months: 12
owner_role: Lead
department: Finance
task_type: Expense Approval
supersedes: [SOP-004]
complexity_declared: Simple
standard_time_source: illustrative_expert_estimate
standard_time_frozen: 2026-10-14
quality_targets_source: unconfirmed

sla_hours: {High: 6, Medium: 12, Low: 24}
sop_steps: 3
approval_count_base: 1
approval_count_max: 1
approval_matrix:
  - {stage: Incharge, condition: always}

dependency_count: 0
dependencies: []

complexity_drivers:
  - {driver: expense_lines, source: ticket_metadata, bands: {low: "<=3", medium: "4-10", high: ">10"}, effect: effort}
  - {driver: claim_value_inr, source: ticket_metadata, bands: {low: "<=10000", medium: "10001-50000", high: ">50000"}, effect: approval_route}
  - {driver: missing_receipts, source: derived, bands: {low: "0", medium: "1", high: ">1"}, effect: rework_risk}

steps:
  - step_id: S1
    name: Create and self-assign expense claim ticket
    role: Executor
    type: intake
    mandatory: true
    audit_actions: [Created, Assigned]
    effort_min: {min: 2, likely: 3, max: 5}
    queue_wait_h: {min: 0.05, likely: 0.25, max: 1.0}
    skill_level: 1
  - step_id: S2
    name: Check claim against travel and expense policy limits
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 5, likely: 10, max: 20}
    effort_scaling: {driver: expense_lines, per_unit_min: 1.0, unit: expense line}
    inputs: [claim form, expense policy]
    outputs: [policy check]
    skill_level: 1
  - step_id: D-LIMIT
    name: "Claim within policy limits?"
    role: System
    type: decision
    mandatory: true
    audit_actions: []
    effort_min: {min: 0, likely: 0, max: 0}
  - step_id: S3
    name: Verify receipts against claim lines
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 5, likely: 10, max: 25}
    effort_scaling: {driver: expense_lines, per_unit_min: 0.5, unit: receipt}
    inputs: [receipts]
    outputs: [receipt verification]
    skill_level: 1
  - step_id: S4
    name: Compute reimbursable amount and submit
    role: Executor
    type: work
    mandatory: true
    audit_actions: [Submitted]
    effort_min: {min: 5, likely: 8, max: 15}
    outputs: [reimbursement computation]
    skill_level: 1
  - step_id: A1
    name: Incharge approval
    role: Incharge
    type: approval
    mandatory: true
    audit_actions: [Approved, Rejected]
    effort_min: {min: 5, likely: 10, max: 20}
    queue_wait_h: {min: 0.25, likely: 0.5, max: 2.0}
    skill_level: 2
  - step_id: R1
    name: Correction and resubmission
    role: Executor
    type: rework
    mandatory: false
    audit_actions: [Updated, Resubmitted]
    effort_min: {min: 5, likely: 15, max: 30}

rework_triggers:
  - {code: RW-AMT, reason: Amount mismatch, detected_at: A1, preventable_by: "S4 computation check"}
  - {code: RW-QTY, reason: Wrong quantity, detected_at: A1, preventable_by: "S3 receipt to line matching"}
  - {code: RW-CAT, reason: Incorrect category, detected_at: A1, preventable_by: "S2 expense category mapping"}
  - {code: RW-DOC, reason: Required document missing, detected_at: A1, preventable_by: "S3 receipt verification"}
expected_first_pass_yield: 0.95
rework_effort_min: {min: 5, likely: 15, max: 30}
max_rework_cycles: 2

exceptions:
  - {code: EX-OVERLIMIT, condition: "claim exceeds policy limit or claim_value_inr > 50000", action: "Attach justification; route to Lead", adds_approval: Lead, adds_dependency_wait: false}
  - {code: EX-NORECEIPT, condition: "receipt lost and line value <= 500", action: "Accept signed self-declaration", adds_approval: null, adds_dependency_wait: false}
---

# SOP-016: Employee Expense Claim Approval

## 1. Purpose
Reimburse employee business expenses that are within policy and supported by receipts.

## 2. Scope
Travel, local conveyance, meals and incidental business expenses claimed by employees. Corporate-card
reconciliations are excluded. Supersedes SOP-004.

## 3. References
Travel and expense policy; delegation-of-authority matrix.

## 4. Definitions
- **Policy limit**: the per-day or per-item cap in the travel and expense policy for the employee's grade.

## 5. Responsibilities (RACI)
| Activity | Executor | Incharge | Lead |
|---|---|---|---|
| Policy and receipt checks | R | A | – |
| Approval | I | R/A | A (exceptions only) |

## 6. Procedure
1. **S1** The Executor creates the ticket and assigns it to themselves.
2. **S2** Check every line against policy limits for the claimant's grade and the expense category.
3. **S3** Match each line to a receipt.
4. **S4** Compute the reimbursable amount and submit.
5. **A1** The Incharge approves or rejects with a reason code.
6. **R1** On rejection, correct and resubmit.

**This SOP has no external dependency.** If a receipt or clarification is missing, reject with *Required
document missing*; do not put the ticket on hold. A `DependencyWait` on this task type is therefore
non-conformant and is reported as such.

## 7. Exceptions
See YAML `exceptions`.

## 8. Rejection reason codes
| Platform reason | Meaning for an expense claim |
|---|---|
| Amount mismatch | Claimed amount differs from receipts or exceeds the limit without justification |
| Wrong quantity | Number of days, nights or units claimed is inconsistent with the trip |
| Incorrect category | Expense booked under the wrong category |
| Required document missing | Receipt, approval mail or self-declaration missing |

## 9. Records
Claim form, receipts, policy check, approval trail. Retain 8 years.

## 10. KPIs
| KPI | Target |
|---|---|
| SLA compliance | ≥ 98% |
| First-pass yield | ≥ 95% |

## 11. Revision history
| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-14 | Initial schema v1.1 release; supersedes SOP-004 |
| 1.1.0 | 2026-10-14 | Schema v1.2: added `quality_targets_source`. Standard times unchanged |
