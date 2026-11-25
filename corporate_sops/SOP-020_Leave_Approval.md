---
schema_version: "1.2"
sop_id: SOP-020
title: Leave Application Processing
version: 1.1.0
status: Approved
effective_date: 2026-10-14
review_cycle_months: 12
owner_role: Lead
department: HR
task_type: Leave Approval
supersedes: []
complexity_declared: Simple
standard_time_source: illustrative_expert_estimate
standard_time_frozen: 2026-10-14
quality_targets_source: unconfirmed

sla_hours: {High: 6, Medium: 12, Low: 24}
sop_steps: 2
approval_count_base: 1
approval_count_max: 1
approval_matrix:
  - {stage: Incharge, condition: always}

dependency_count: 0
dependencies: []

complexity_drivers:
  - {driver: leave_days, source: ticket_metadata, bands: {low: "1-3", medium: "4-10", high: ">10"}, effect: approval_route}
  - {driver: leave_type, source: ticket_metadata, bands: {low: "casual", medium: "earned", high: "medical_or_special"}, effect: effort}
  - {driver: negative_balance, source: derived, bands: {low: "false", high: "true"}, effect: rework_risk}

steps:
  - step_id: S1
    name: Create and self-assign leave ticket
    role: Executor
    type: intake
    mandatory: true
    audit_actions: [Created, Assigned]
    effort_min: {min: 1, likely: 2, max: 5}
    queue_wait_h: {min: 0.05, likely: 0.25, max: 1.0}
    skill_level: 1
  - step_id: S2
    name: Check leave balance and policy eligibility
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 3, likely: 5, max: 12}
    effort_scaling: {driver: leave_type, per_unit_min: 5, unit: supporting certificate}
    inputs: [leave application, HRMS leave balance, leave policy]
    outputs: [eligibility check]
    skill_level: 1
  - step_id: D-LONG
    name: "Leave longer than 10 days?"
    role: System
    type: decision
    mandatory: true
    audit_actions: []
    effort_min: {min: 0, likely: 0, max: 0}
  - step_id: S3
    name: "Record dates, check holiday overlap and submit"
    role: Executor
    type: work
    mandatory: true
    audit_actions: [Submitted]
    effort_min: {min: 3, likely: 5, max: 10}
    inputs: [holiday calendar]
    outputs: [leave record]
    skill_level: 1
  - step_id: A1
    name: Incharge approval
    role: Incharge
    type: approval
    mandatory: true
    audit_actions: [Approved, Rejected]
    effort_min: {min: 3, likely: 5, max: 10}
    queue_wait_h: {min: 0.25, likely: 0.5, max: 2.0}
    skill_level: 1
  - step_id: R1
    name: Correction and resubmission
    role: Executor
    type: rework
    mandatory: false
    audit_actions: [Updated, Resubmitted]
    effort_min: {min: 3, likely: 8, max: 20}

rework_triggers:
  - {code: RW-QTY, reason: Wrong quantity, detected_at: A1, preventable_by: "S3 day count excluding holidays"}
  - {code: RW-AMT, reason: Amount mismatch, detected_at: A1, preventable_by: "S2 balance check"}
  - {code: RW-CAT, reason: Incorrect category, detected_at: A1, preventable_by: "S2 leave type eligibility"}
  - {code: RW-DOC, reason: Required document missing, detected_at: A1, preventable_by: "S2 certificate check"}
expected_first_pass_yield: 0.95
rework_effort_min: {min: 3, likely: 8, max: 20}
max_rework_cycles: 2

exceptions:
  - {code: EX-LONG, condition: "leave_days > 10", action: "Route to Lead after Incharge approval", adds_approval: Lead, adds_dependency_wait: false}
  - {code: EX-MEDICAL, condition: "leave_type == medical and leave_days > 2", action: "Medical certificate required; reject with Required document missing if absent", adds_approval: null, adds_dependency_wait: false}
  - {code: EX-NEGBAL, condition: "negative_balance == true", action: "Convert excess days to loss of pay with the employee's written consent", adds_approval: null, adds_dependency_wait: false}
---

# SOP-020: Leave Application Processing

## 1. Purpose
Process leave applications against the employee's balance and the leave policy, and keep the leave record
accurate for payroll.

## 2. Scope
Casual, earned, medical and special leave for all employees. Maternity and paternity leave follow the statutory
benefits procedure.

## 3. References
Leave policy; applicable labour and leave regulations; payroll cut-off calendar.

## 4. Definitions
- **Leave balance**: days available per leave type in the HRMS on the application date.
- **Loss of pay (LOP)**: days without balance that are deducted from salary.

## 5. Responsibilities (RACI)
| Activity | Executor | Incharge | Lead |
|---|---|---|---|
| Balance and eligibility check | R | A | – |
| Approval | I | R/A | A (more than 10 days) |

## 6. Procedure
1. **S1** The Executor creates the ticket and assigns it to themselves.
2. **S2** Check the balance and eligibility for the leave type.
3. **S3** Record the dates, exclude holidays and weekly offs, and submit.
4. **A1** The Incharge approves or rejects with a reason code.
5. **R1** On rejection, correct and resubmit.

**This SOP has no external dependency.** Missing certificates are handled by rejection, not by holding the
ticket. A `DependencyWait` on this task type is non-conformant and is reported as such.

## 7. Exceptions
See YAML `exceptions`.

## 8. Rejection reason codes
| Platform reason | Meaning for a leave application |
|---|---|
| Wrong quantity | Number of days counted incorrectly |
| Amount mismatch | Days applied exceed the available balance |
| Incorrect category | Wrong leave type for the situation or policy |
| Required document missing | Medical or supporting certificate missing |

## 9. Records
Leave application, eligibility check, approval trail. Retain for employment plus 3 years. Contains personal
data (PII).

## 10. KPIs
| KPI | Target |
|---|---|
| SLA compliance | ≥ 98% |
| First-pass yield | ≥ 95% |

## 11. Revision history
| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-14 | Initial schema v1.1 release |
| 1.1.0 | 2026-10-14 | Schema v1.2: added `quality_targets_source`; quoted step name S3. Standard times unchanged |
