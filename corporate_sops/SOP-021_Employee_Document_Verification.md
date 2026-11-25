---
schema_version: "1.2"
sop_id: SOP-021
title: Employee Document Verification
version: 1.1.0
status: Approved
effective_date: 2026-10-14
review_cycle_months: 12
owner_role: Lead
department: HR
task_type: Employee Document Verification
supersedes: []
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
    provider: External (issuing institution or background verification agency)
    item: "Confirmation of education or employment credentials"
    blocking_step: A1
    parallel_group: P1
    typical_wait_h: {min: 0.5, likely: 2.0, max: 8.0}

complexity_drivers:
  - {driver: documents_count, source: ticket_metadata, bands: {low: "<=4", medium: "5-8", high: ">8"}, effect: effort}
  - {driver: discrepancies, source: derived, bands: {low: "0", medium: "1", high: ">1"}, effect: rework_risk}
  - {driver: foreign_credentials, source: ticket_metadata, bands: {low: "false", high: "true"}, effect: effort}

steps:
  - step_id: S1
    name: Create and self-assign verification ticket
    role: Executor
    type: intake
    mandatory: true
    audit_actions: [Created, Assigned]
    effort_min: {min: 2, likely: 3, max: 5}
    queue_wait_h: {min: 0.05, likely: 0.25, max: 1.0}
    skill_level: 1
  - step_id: S2
    name: Checklist completeness and legibility check
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 5, likely: 10, max: 20}
    effort_scaling: {driver: documents_count, per_unit_min: 1.0, unit: document}
    inputs: [submitted documents, document checklist for the role]
    outputs: [completeness check]
    skill_level: 1
  - step_id: S3
    name: Identity and address proof verification
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 15, max: 30}
    inputs: [identity proof, address proof]
    outputs: [identity verification]
    skill_level: 2
  - step_id: S4
    name: Education and employment certificate verification
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 15, likely: 25, max: 50}
    effort_scaling: {driver: foreign_credentials, per_unit_min: 20, unit: foreign credential}
    inputs: [degree certificates, relieving letters]
    outputs: [credential verification requests]
    skill_level: 2
  - step_id: D-DISC
    name: "Any discrepancy found?"
    role: System
    type: decision
    mandatory: true
    audit_actions: []
    effort_min: {min: 0, likely: 0, max: 0}
  - step_id: S5
    name: Cross-check against offer letter and HRMS record
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 15, max: 30}
    inputs: [offer letter, HRMS employee record]
    outputs: [consistency check]
    skill_level: 2
  - step_id: S6
    name: Record verification status and submit
    role: Executor
    type: work
    mandatory: true
    audit_actions: [Submitted]
    effort_min: {min: 5, likely: 10, max: 15}
    outputs: [verification summary]
    skill_level: 1
  - step_id: A1
    name: Incharge approval
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
    effort_min: {min: 10, likely: 20, max: 45}

rework_triggers:
  - {code: RW-DOC, reason: Required document missing, detected_at: A1, preventable_by: "S2 checklist"}
  - {code: RW-CAT, reason: Incorrect category, detected_at: A1, preventable_by: "S2 document type classification"}
  - {code: RW-AMT, reason: Amount mismatch, detected_at: A1, preventable_by: "S5 salary and grade cross-check with offer letter"}
  - {code: RW-QTY, reason: Wrong quantity, detected_at: A1, preventable_by: "S4 experience duration calculation"}
expected_first_pass_yield: 0.90
rework_effort_min: {min: 10, likely: 20, max: 45}
max_rework_cycles: 2

exceptions:
  - {code: EX-DISCREP, condition: "discrepancies >= 1", action: "Record the discrepancy and route to Lead", adds_approval: Lead, adds_dependency_wait: false}
  - {code: EX-FOREIGN, condition: "foreign_credentials == true", action: "Use an equivalence certificate or an international verification agency", adds_approval: null, adds_dependency_wait: false}
---

# SOP-021: Employee Document Verification

## 1. Purpose
Confirm that an employee's identity, address, education and employment documents are genuine and consistent
with the offer and the HRMS record.

## 2. Scope
New joiners, and existing employees asked to re-verify after a role change or audit finding.

## 3. References
ISO/IEC 27001:2022 Annex A 6.1 (screening); applicable data protection law; HR document checklist by role.

## 4. Definitions
- **Discrepancy**: any mismatch between a document and the offer letter, HRMS record or issuer confirmation.

## 5. Responsibilities (RACI)
| Activity | Executor | Incharge | Lead | Issuer / BGV agency |
|---|---|---|---|---|
| Document checks | R | A | – | – |
| Credential confirmation (D1) | C | I | – | R |
| Approval | I | R/A | A (discrepancies only) | – |

## 6. Procedure
1. **S1** The Executor creates the ticket and assigns it to themselves.
2. **S2** Check that the checklist for the role is complete and every document is legible.
3. **S3** Verify identity and address proofs.
4. **S4** Send education and employment confirmations to the issuers or the BGV agency.
5. **S5** Cross-check names, dates, grade and salary against the offer letter and HRMS.
6. **S6** Record the verification status and submit.
7. After submission, while credential confirmations (D1) are outstanding, log `DependencyWait`.
8. **A1** The Incharge approves or rejects with a reason code. Any discrepancy adds a Lead approval.
9. **R1** On rejection, correct and resubmit.

## 7. Exceptions
See YAML `exceptions`.

## 8. Rejection reason codes
| Platform reason | Meaning for document verification |
|---|---|
| Required document missing | A checklist document is missing or illegible |
| Incorrect category | Document filed under the wrong type |
| Amount mismatch | Salary or grade differs from the offer letter |
| Wrong quantity | Years of experience calculated incorrectly |

## 9. Records
Verification summary and confirmation responses. Retain for employment plus 8 years. All documents are personal
data (PII) and must not be sent to analytics or external services.

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
