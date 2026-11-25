---
schema_version: "1.2"
sop_id: SOP-015
title: Invoice Verification (Three-Way Match)
version: 1.1.0
status: Approved
effective_date: 2026-10-14
review_cycle_months: 12
owner_role: Lead
department: Finance
task_type: Invoice Verification
supersedes: [SOP-003]
complexity_declared: Medium
standard_time_source: illustrative_expert_estimate
standard_time_frozen: 2026-10-14
quality_targets_source: unconfirmed

sla_hours: {High: 6, Medium: 12, Low: 24}
sop_steps: 5
approval_count_base: 1
approval_count_max: 1
approval_matrix:
  - {stage: Incharge, condition: always}

dependency_count: 1
dependencies:
  - id: D1
    provider: Stores / Operations
    item: "Goods Receipt Note or service completion certificate"
    blocking_step: A1
    parallel_group: P1
    typical_wait_h: {min: 0.5, likely: 1.5, max: 6.0}

complexity_drivers:
  - {driver: invoice_lines, source: ticket_metadata, bands: {low: "<=5", medium: "6-30", high: ">30"}, effect: effort}
  - {driver: invoice_value_inr, source: ticket_metadata, bands: {low: "<=100000", medium: "100001-1000000", high: ">1000000"}, effect: approval_route}
  - {driver: match_exceptions, source: derived, bands: {low: "0", medium: "1-2", high: ">2"}, effect: rework_risk}
  - {driver: foreign_currency, source: ticket_metadata, bands: {low: "false", high: "true"}, effect: effort}

steps:
  - step_id: S1
    name: Create and self-assign invoice ticket
    role: Executor
    type: intake
    mandatory: true
    audit_actions: [Created, Assigned]
    effort_min: {min: 2, likely: 3, max: 5}
    queue_wait_h: {min: 0.05, likely: 0.25, max: 1.0}
    skill_level: 1
  - step_id: S2
    name: Vendor, statutory and duplicate check
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 5, likely: 10, max: 20}
    inputs: [invoice, vendor master]
    outputs: ["GSTIN and PAN validity", duplicate check result]
    skill_level: 1
  - step_id: S3
    name: "Three-way match (invoice, PO, GRN)"
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 15, likely: 25, max: 50}
    effort_scaling: {driver: invoice_lines, per_unit_min: 1.5, unit: invoice line}
    inputs: [invoice, purchase order, GRN]
    outputs: [match sheet]
    skill_level: 2
  - step_id: D-TOL
    name: "Match within tolerance?"
    role: System
    type: decision
    mandatory: true
    audit_actions: []
    effort_min: {min: 0, likely: 0, max: 0}
  - step_id: S4
    name: GST input credit and TDS computation
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 15, max: 30}
    effort_scaling: {driver: foreign_currency, per_unit_min: 15, unit: foreign-currency invoice}
    inputs: [match sheet, tax rules]
    outputs: [tax computation]
    skill_level: 3
  - step_id: S5
    name: Advance and deduction adjustment
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 5, likely: 10, max: 20}
    inputs: [vendor ledger]
    outputs: [net payable computation]
    skill_level: 2
  - step_id: S6
    name: Prepare payment voucher and submit
    role: Executor
    type: work
    mandatory: true
    audit_actions: [Submitted]
    effort_min: {min: 5, likely: 10, max: 20}
    outputs: [payment voucher]
    skill_level: 1
  - step_id: A1
    name: Incharge verification
    role: Incharge
    type: approval
    mandatory: true
    audit_actions: [Approved, Rejected]
    effort_min: {min: 10, likely: 15, max: 30}
    queue_wait_h: {min: 0.25, likely: 0.75, max: 3.0}
    skill_level: 2
  - step_id: R1
    name: Correction and resubmission
    role: Executor
    type: rework
    mandatory: false
    audit_actions: [Updated, Resubmitted]
    effort_min: {min: 10, likely: 25, max: 60}

rework_triggers:
  - {code: RW-AMT, reason: Amount mismatch, detected_at: A1, preventable_by: "S3 three-way match"}
  - {code: RW-QTY, reason: Wrong quantity, detected_at: A1, preventable_by: "S3 three-way match against GRN"}
  - {code: RW-CAT, reason: Incorrect category, detected_at: A1, preventable_by: "S4 GL and tax code check"}
  - {code: RW-DOC, reason: Required document missing, detected_at: A1, preventable_by: "S2 attachment checklist"}
expected_first_pass_yield: 0.90
rework_effort_min: {min: 10, likely: 25, max: 60}
max_rework_cycles: 2

exceptions:
  - {code: EX-TOL, condition: "price variance > 2 percent or quantity variance > 0", action: "Write exception note; route to Lead", adds_approval: Lead, adds_dependency_wait: false}
  - {code: EX-HIGHVAL, condition: "invoice_value_inr > 1000000", action: "Route to Lead after Incharge verification", adds_approval: Lead, adds_dependency_wait: false}
  - {code: EX-FX, condition: "foreign_currency == true", action: "Apply the reference exchange rate on the invoice date", adds_approval: null, adds_dependency_wait: false}
---

# SOP-015: Invoice Verification (Three-Way Match)

## 1. Purpose
Ensure that a vendor invoice is paid only for goods or services that were ordered (PO), received (GRN) and
correctly billed, with correct tax treatment.

## 2. Scope
All vendor invoices against a purchase order. Non-PO invoices are out of scope. Supersedes SOP-003.

## 3. References
ISO 9001:2015 §8.4; internal-control principle of segregation of duties; GST and TDS rules in force; SOP-014
Purchase Request.

## 4. Definitions
- **Three-way match**: invoice vs PO vs GRN on item, quantity, rate and value.
- **Tolerance**: price variance ≤ 2% and quantity variance 0. Anything outside is a match exception.

## 5. Responsibilities (RACI)
| Activity | Executor | Incharge | Lead | Stores |
|---|---|---|---|---|
| Checks and match | R | A | – | C |
| GRN / completion certificate (D1) | C | I | – | R |
| Verification | I | R/A | A (exceptions only) | – |

The Executor who prepares the voucher must not approve it.

## 6. Procedure
1. **S1** The Executor creates the ticket and assigns it to themselves.
2. **S2** Validate the vendor's GSTIN and PAN, and check for duplicates (same vendor, invoice number and amount).
3. **S3** Match invoice, PO and GRN line by line.
4. **S4** Compute GST input credit and TDS.
5. **S5** Adjust advances and other deductions.
6. **S6** Prepare the payment voucher and submit.
7. After submission, if the GRN or completion certificate is not yet confirmed, log `DependencyWait` (D1).
8. **A1** The Incharge verifies and approves or rejects with a reason code. Out-of-tolerance or high-value
   invoices add a Lead approval.
9. **R1** On rejection, correct and resubmit. After 2 rejections, escalate to the Lead.

## 7. Exceptions
See YAML `exceptions`.

## 8. Rejection reason codes
| Platform reason | Meaning for an invoice |
|---|---|
| Amount mismatch | Rate or total differs from the PO beyond tolerance, or tax amount wrong |
| Wrong quantity | Billed quantity exceeds the GRN |
| Incorrect category | Wrong GL account, cost centre or tax code |
| Required document missing | GRN, PO copy or completion certificate not attached |

## 9. Records
Invoice, PO, GRN, match sheet, tax computation, voucher, approval trail. Retain 8 years.

## 10. KPIs
| KPI | Target |
|---|---|
| SLA compliance | ≥ 95% |
| First-pass yield | ≥ 90% |
| Duplicate payments | 0 |

## 11. Revision history
| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-14 | Initial schema v1.1 release; supersedes SOP-003 |
| 1.1.0 | 2026-10-14 | Schema v1.2: added `parallel_group` and `quality_targets_source`; quoted step name S3. Standard times unchanged |
