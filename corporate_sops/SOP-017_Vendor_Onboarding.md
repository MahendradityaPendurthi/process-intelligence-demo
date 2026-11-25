---
schema_version: "1.2"
sop_id: SOP-017
title: Vendor Onboarding and Due Diligence
version: 1.1.0
status: Approved
effective_date: 2026-10-14
review_cycle_months: 12
owner_role: Lead
department: Procurement
task_type: Vendor Onboarding
supersedes: []
complexity_declared: Complex
standard_time_source: illustrative_expert_estimate
standard_time_frozen: 2026-10-14
quality_targets_source: unconfirmed

sla_hours: {High: 6, Medium: 12, Low: 24}
sop_steps: 8
approval_count_base: 3
approval_count_max: 3
approval_matrix:
  - {stage: Incharge, condition: always}
  - {stage: Lead, condition: always}
  - {stage: HOD, condition: always}

dependency_count: 2
dependencies:
  - id: D1
    provider: Finance (treasury)
    item: "Bank account validation result"
    blocking_step: A1
    parallel_group: P1
    typical_wait_h: {min: 0.5, likely: 1.5, max: 6.0}
  - id: D2
    provider: Legal / Compliance
    item: "Sanctions, litigation and conflict-of-interest clearance"
    blocking_step: A1
    parallel_group: P1
    typical_wait_h: {min: 0.5, likely: 2.0, max: 8.0}

complexity_drivers:
  - {driver: supply_categories, source: ticket_metadata, bands: {low: "1", medium: "2-3", high: ">3"}, effect: effort}
  - {driver: annual_spend_inr, source: ticket_metadata, bands: {low: "<=1000000", medium: "1000001-10000000", high: ">10000000"}, effect: rework_risk}
  - {driver: risk_category, source: derived, bands: {low: "low", medium: "medium", high: "high"}, effect: effort}
  - {driver: foreign_vendor, source: ticket_metadata, bands: {low: "false", high: "true"}, effect: effort}

steps:
  - step_id: S1
    name: Create and self-assign onboarding ticket
    role: Executor
    type: intake
    mandatory: true
    audit_actions: [Created, Assigned]
    effort_min: {min: 2, likely: 3, max: 5}
    queue_wait_h: {min: 0.05, likely: 0.25, max: 1.0}
    skill_level: 1
  - step_id: S2
    name: Collect registration form and documents
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 20, max: 40}
    inputs: [vendor registration form, incorporation certificate, tax registrations]
    outputs: [document checklist]
    skill_level: 1
  - step_id: S3
    name: "KYC verification (PAN, GSTIN, MSME status)"
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 15, max: 30}
    inputs: [document checklist, government portals]
    outputs: [KYC result]
    skill_level: 2
  - step_id: S4
    name: Request bank account validation
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 5, likely: 10, max: 15}
    inputs: [cancelled cheque or bank letter]
    outputs: [validation request]
    skill_level: 1
  - step_id: S5
    name: "Sanctions, blacklist and conflict-of-interest screening request"
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 15, max: 30}
    effort_scaling: {driver: foreign_vendor, per_unit_min: 20, unit: foreign vendor}
    outputs: [screening request]
    skill_level: 3
  - step_id: S6
    name: Capability and quality assessment
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 20, likely: 40, max: 90}
    effort_scaling: {driver: supply_categories, per_unit_min: 10, unit: supply category}
    inputs: [capability questionnaire, references, certifications]
    outputs: [capability assessment]
    skill_level: 3
  - step_id: D-RISK
    name: "High-risk vendor?"
    role: System
    type: decision
    mandatory: true
    audit_actions: []
    effort_min: {min: 0, likely: 0, max: 0}
  - step_id: S7
    name: Risk categorisation
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 15, max: 30}
    outputs: [vendor risk rating]
    skill_level: 3
  - step_id: S8
    name: Commercial terms and NDA check
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 20, max: 45}
    inputs: [payment terms, NDA, code of conduct acknowledgement]
    outputs: [terms check]
    skill_level: 2
  - step_id: S9
    name: Draft vendor master record and submit
    role: Executor
    type: work
    mandatory: true
    audit_actions: [Submitted]
    effort_min: {min: 10, likely: 15, max: 25}
    outputs: [draft vendor master record]
    skill_level: 1
  - step_id: A1
    name: Incharge review
    role: Incharge
    type: approval
    mandatory: true
    audit_actions: [Approved, Rejected]
    effort_min: {min: 10, likely: 20, max: 40}
    queue_wait_h: {min: 0.25, likely: 1.0, max: 4.0}
    skill_level: 2
  - step_id: A2
    name: Lead approval
    role: Lead
    type: approval
    mandatory: true
    audit_actions: [Approved, Rejected]
    effort_min: {min: 10, likely: 15, max: 30}
    queue_wait_h: {min: 0.25, likely: 1.0, max: 4.0}
    skill_level: 3
  - step_id: A3
    name: HOD approval and vendor master activation
    role: HOD
    type: approval
    mandatory: true
    audit_actions: [Approved, Rejected]
    effort_min: {min: 5, likely: 10, max: 20}
    queue_wait_h: {min: 0.5, likely: 1.5, max: 6.0}
    skill_level: 3
  - step_id: R1
    name: Correction and resubmission
    role: Executor
    type: rework
    mandatory: false
    audit_actions: [Updated, Resubmitted]
    effort_min: {min: 15, likely: 30, max: 60}

rework_triggers:
  - {code: RW-DOC, reason: Required document missing, detected_at: A1, preventable_by: "S2 document checklist"}
  - {code: RW-CAT, reason: Incorrect category, detected_at: A1, preventable_by: "S7 risk and supply-category mapping"}
  - {code: RW-AMT, reason: Amount mismatch, detected_at: A1, preventable_by: "S8 commercial terms check"}
  - {code: RW-QTY, reason: Wrong quantity, detected_at: A1, preventable_by: "S6 capacity figures check"}
expected_first_pass_yield: 0.85
rework_effort_min: {min: 15, likely: 30, max: 60}
max_rework_cycles: 2

exceptions:
  - {code: EX-HIGHRISK, condition: "risk_category == high", action: "Enhanced due diligence: site visit or third-party report before S9", adds_approval: null, adds_dependency_wait: false}
  - {code: EX-FOREIGN, condition: "foreign_vendor == true", action: "Collect tax residency certificate and foreign bank details", adds_approval: null, adds_dependency_wait: false}
  - {code: EX-PROVISIONAL, condition: "priority == High and urgent single purchase", action: "Provisional activation for one PO; full onboarding within 7 days", adds_approval: null, adds_dependency_wait: false}
---

# SOP-017: Vendor Onboarding and Due Diligence

## 1. Purpose
Create a vendor in the vendor master only after identity, bank account, compliance screening, capability and
commercial terms have been verified.

## 2. Scope
All new vendors of goods and services, and re-activation of vendors inactive for more than 24 months.

## 3. References
ISO 9001:2015 §8.4.1 (evaluation and selection of external providers); ISO 37001 (anti-bribery due diligence);
supplier code of conduct; SOP-014 Purchase Request.

## 4. Definitions
- **Risk category**: low, medium or high, based on spend, supply criticality and screening results.
- **Vendor master**: the ERP record that enables purchase orders and payments.

## 5. Responsibilities (RACI)
| Activity | Executor | Incharge | Lead | HOD | Finance | Legal/Compliance |
|---|---|---|---|---|---|---|
| Documents, KYC, assessment | R | A | – | – | – | – |
| Bank validation (D1) | C | I | – | – | R | – |
| Screening clearance (D2) | C | I | – | – | – | R |
| Approval | I | R | R | A | – | – |

## 6. Procedure
1. **S1** The Executor creates the ticket and assigns it to themselves.
2. **S2** Collect the registration form and statutory documents.
3. **S3** Verify PAN, GSTIN and MSME status on the government portals.
4. **S4** Request bank account validation from Finance.
5. **S5** Request sanctions, blacklist and conflict-of-interest screening from Legal/Compliance.
6. **S6** Assess capability and quality (questionnaire, references, certifications).
7. **S7** Assign the risk category.
8. **S8** Check payment terms, NDA and code-of-conduct acknowledgement.
9. **S9** Draft the vendor master record and submit.
10. After submission, while the bank validation (D1) or screening clearance (D2) is outstanding, log
    `DependencyWait`. D1 and D2 are requested in S4 and S5 and run **in parallel** (`parallel_group: P1`);
    one event covers both.
11. **A1** Incharge review, **A2** Lead approval, **A3** HOD approval and activation.
12. **R1** On rejection, correct and resubmit. After 2 rejections, escalate to the Lead.

## 7. Exceptions
See YAML `exceptions`.

## 8. Rejection reason codes
| Platform reason | Meaning for vendor onboarding |
|---|---|
| Required document missing | Statutory document, bank proof or signed NDA missing |
| Incorrect category | Wrong supply category or risk category |
| Amount mismatch | Payment terms or price basis differ from what was negotiated |
| Wrong quantity | Declared capacity inconsistent with references or certifications |

## 9. Records
Registration form, KYC evidence, bank validation, screening clearance, risk rating, signed NDA, approval trail.
Retain for the vendor relationship plus 8 years.

## 10. KPIs
| KPI | Target |
|---|---|
| SLA compliance | ≥ 90% |
| First-pass yield | ≥ 85% |
| Vendors activated without screening | 0 |

## 11. Revision history
| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-14 | Initial schema v1.1 release |
| 1.1.0 | 2026-10-14 | Schema v1.2: D1 and D2 in parallel group P1; added `quality_targets_source`; quoted step name S5. Standard times unchanged |
