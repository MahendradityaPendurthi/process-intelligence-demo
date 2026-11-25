---
schema_version: "1.2"
sop_id: SOP-013
title: Bill of Quantities (BOQ) Review
version: 1.1.0
status: Approved
effective_date: 2026-10-14
review_cycle_months: 12
owner_role: Lead
department: Procurement
task_type: BOQ Review
supersedes: []
complexity_declared: Medium
standard_time_source: illustrative_expert_estimate
standard_time_frozen: 2026-10-14
quality_targets_source: unconfirmed

sla_hours: {High: 6, Medium: 12, Low: 24}
sop_steps: 3
approval_count_base: 1
approval_count_max: 1
approval_matrix:
  - {stage: Incharge, condition: always}

dependency_count: 1
dependencies:
  - id: D1
    provider: Operations (site engineering)
    item: "Confirmation of drawings revision and quantity take-off"
    blocking_step: A1
    parallel_group: P1
    typical_wait_h: {min: 0.5, likely: 1.5, max: 5.0}

complexity_drivers:
  - {driver: line_items, source: ticket_metadata, bands: {low: "<=25", medium: "26-100", high: ">100"}, effect: effort}
  - {driver: boq_value_inr, source: ticket_metadata, bands: {low: "<=500000", medium: "500001-2500000", high: ">2500000"}, effect: approval_route}
  - {driver: variance_pct, source: derived, bands: {low: "<=5", medium: "5-10", high: ">10"}, effect: approval_route}
  - {driver: non_standard_items, source: ticket_metadata, bands: {low: "0", medium: "1-5", high: ">5"}, effect: rework_risk}

steps:
  - step_id: S1
    name: Create and self-assign BOQ ticket
    role: Executor
    type: intake
    mandatory: true
    audit_actions: [Created, Assigned]
    effort_min: {min: 2, likely: 3, max: 5}
    queue_wait_h: {min: 0.05, likely: 0.25, max: 1.0}
    skill_level: 1
  - step_id: S2
    name: Completeness and format check
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 20, max: 40}
    effort_scaling: {driver: line_items, per_unit_min: 0.2, unit: line item}
    inputs: [BOQ draft, BOQ template checklist]
    outputs: [completeness checklist]
    skill_level: 1
  - step_id: S3
    name: Quantity and rate validation
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 30, likely: 60, max: 120}
    effort_scaling: {driver: line_items, per_unit_min: 0.8, unit: line item}
    inputs: [drawings, schedule of rates, last three purchase prices]
    outputs: [variance sheet]
    skill_level: 3
  - step_id: D-VAR
    name: "Variance above 10 percent or value above 25 lakh?"
    role: System
    type: decision
    mandatory: true
    audit_actions: []
    effort_min: {min: 0, likely: 0, max: 0}
  - step_id: S4
    name: Variance summary and submission
    role: Executor
    type: work
    mandatory: true
    audit_actions: [Submitted]
    effort_min: {min: 10, likely: 20, max: 35}
    inputs: [variance sheet]
    outputs: [BOQ review note]
    skill_level: 2
  - step_id: A1
    name: Incharge review
    role: Incharge
    type: approval
    mandatory: true
    audit_actions: [Approved, Rejected]
    effort_min: {min: 10, likely: 20, max: 40}
    queue_wait_h: {min: 0.25, likely: 1.0, max: 4.0}
    skill_level: 2
  - step_id: R1
    name: Correction and resubmission
    role: Executor
    type: rework
    mandatory: false
    audit_actions: [Updated, Resubmitted]
    effort_min: {min: 15, likely: 30, max: 60}

rework_triggers:
  - {code: RW-QTY, reason: Wrong quantity, detected_at: A1, preventable_by: "S3 take-off cross-check"}
  - {code: RW-AMT, reason: Amount mismatch, detected_at: A1, preventable_by: "S4 totals formula check"}
  - {code: RW-CAT, reason: Incorrect category, detected_at: A1, preventable_by: "S2 item-code mapping"}
  - {code: RW-DOC, reason: Required document missing, detected_at: A1, preventable_by: "S2 checklist"}
expected_first_pass_yield: 0.90
rework_effort_min: {min: 15, likely: 30, max: 60}
max_rework_cycles: 2

exceptions:
  - {code: EX-HIGHVAL, condition: "boq_value_inr > 2500000 or variance_pct > 10", action: "Route to Lead after Incharge review", adds_approval: Lead, adds_dependency_wait: false}
  - {code: EX-NEWITEM, condition: "non_standard_items > 5", action: "Attach at least two market quotations per non-standard item", adds_approval: Lead, adds_dependency_wait: false}
  - {code: EX-URGENT, condition: "priority == High and site work stopped", action: "Incharge may approve; Lead reviews within 2 working days", adds_approval: null, adds_dependency_wait: false}
---

# SOP-013: Bill of Quantities (BOQ) Review

## 1. Purpose
Confirm that a BOQ is complete, that quantities match the approved drawings, and that rates are within the
schedule of rates before the BOQ is used for tendering or purchase.

## 2. Scope
All BOQs raised by Procurement for projects, maintenance contracts and capital purchases. BOQs already approved
under a framework agreement are excluded.

## 3. References
ISO 9001:2015 §8.4 (control of externally provided products and services); company Schedule of Rates; SOP-014
Purchase Request.

## 4. Definitions
- **Variance %**: (BOQ total − estimate at schedule rates) ÷ estimate at schedule rates × 100.
- **Non-standard item**: an item with no entry in the schedule of rates.

## 5. Responsibilities (RACI)
| Activity | Executor | Incharge | Lead | Operations |
|---|---|---|---|---|
| Create and validate BOQ | R | A | – | C |
| Drawings and take-off confirmation (D1) | C | I | – | R |
| Review | I | R/A | A (exceptions only) | – |

## 6. Procedure
1. **S1** The Executor creates the ticket and assigns it to themselves.
2. **S2** Check that every line has description, unit, quantity and rate, using the BOQ template checklist.
3. **S3** Check quantities against the drawings and rates against the schedule of rates and the last three
   purchase prices. Record the variance per line.
4. **S4** Summarise the variance, list non-standard items and submit.
5. After submission, if the drawings revision or take-off is not yet confirmed by Operations, log
   `DependencyWait` (D1). The Incharge does not decide until D1 is confirmed.
6. **A1** The Incharge approves or rejects using a reason code from section 8.
7. **R1** On rejection, correct and resubmit. After 2 rejections, escalate to the Lead.

## 7. Exceptions
See YAML `exceptions`. High value or high variance (EX-HIGHVAL) and many non-standard items (EX-NEWITEM) add a
Lead approval.

## 8. Rejection reason codes
| Platform reason | Meaning for a BOQ |
|---|---|
| Wrong quantity | Quantity does not match drawings or take-off |
| Amount mismatch | Line or grand total arithmetic is wrong, or rate is above the schedule without justification |
| Incorrect category | Item mapped to the wrong item code or cost head |
| Required document missing | Drawings, rate references or quotations not attached |

## 9. Records
BOQ review note, variance sheet, completeness checklist, approval trail. Retain 8 years.

## 10. KPIs
| KPI | Target |
|---|---|
| SLA compliance | ≥ 95% |
| First-pass yield | ≥ 90% |

## 11. Revision history
| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-14 | Initial schema v1.1 release |
| 1.1.0 | 2026-10-14 | Schema v1.2: added `parallel_group` and `quality_targets_source`. Standard times unchanged |
