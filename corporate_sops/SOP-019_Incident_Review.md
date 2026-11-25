---
schema_version: "1.2"
sop_id: SOP-019
title: Operational Incident Review and Root Cause Analysis
version: 1.1.0
status: Approved
effective_date: 2026-10-14
review_cycle_months: 12
owner_role: Lead
department: Operations
task_type: Incident Review
supersedes: []
complexity_declared: Complex
standard_time_source: illustrative_expert_estimate
standard_time_frozen: 2026-10-14
quality_targets_source: unconfirmed

sla_hours: {High: 6, Medium: 12, Low: 24}
sop_steps: 7
approval_count_base: 2
approval_count_max: 2
approval_matrix:
  - {stage: Incharge, condition: always}
  - {stage: Lead, condition: always}

dependency_count: 2
dependencies:
  - id: D1
    provider: Maintenance / Engineering
    item: "Technical findings on the failed equipment or system"
    blocking_step: A1
    parallel_group: P1
    typical_wait_h: {min: 0.5, likely: 2.0, max: 6.0}
  - id: D2
    provider: HSE (health, safety and environment)
    item: "Safety assessment and regulatory reportability decision"
    blocking_step: A1
    parallel_group: P1
    typical_wait_h: {min: 0.5, likely: 1.5, max: 5.0}

complexity_drivers:
  - {driver: severity, source: ticket_metadata, bands: {low: "minor", medium: "moderate", high: "major"}, effect: approval_route}
  - {driver: witnesses, source: ticket_metadata, bands: {low: "0-1", medium: "2-4", high: ">4"}, effect: effort}
  - {driver: repeat_incident_90d, source: derived, bands: {low: "0", medium: "1", high: ">1"}, effect: rework_risk}
  - {driver: regulatory_reportable, source: ticket_metadata, bands: {low: "false", high: "true"}, effect: effort}

steps:
  - step_id: S1
    name: Create and self-assign incident review ticket
    role: Executor
    type: intake
    mandatory: true
    audit_actions: [Created, Assigned]
    effort_min: {min: 2, likely: 3, max: 5}
    queue_wait_h: {min: 0.05, likely: 0.25, max: 1.0}
    skill_level: 1
  - step_id: S2
    name: Secure the incident record and classify severity
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 15, max: 30}
    inputs: [incident report]
    outputs: [severity classification]
    skill_level: 2
  - step_id: D-SEV
    name: "Major severity?"
    role: System
    type: decision
    mandatory: true
    audit_actions: []
    effort_min: {min: 0, likely: 0, max: 0}
  - step_id: S3
    name: Collect evidence
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 20, likely: 35, max: 75}
    effort_scaling: {driver: witnesses, per_unit_min: 10, unit: witness statement}
    inputs: [system logs, photographs, witness statements]
    outputs: [evidence pack]
    skill_level: 2
  - step_id: S4
    name: Reconstruct the timeline
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 15, likely: 25, max: 50}
    outputs: [incident timeline]
    skill_level: 2
  - step_id: S5
    name: "Root cause analysis (5-Why or fishbone)"
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 30, likely: 60, max: 120}
    outputs: [root cause statement]
    skill_level: 3
  - step_id: S6
    name: Impact assessment
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 20, max: 45}
    outputs: ["cost, downtime and safety impact"]
    skill_level: 2
  - step_id: S7
    name: Define corrective and preventive actions (CAPA)
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 15, likely: 30, max: 60}
    effort_scaling: {driver: regulatory_reportable, per_unit_min: 30, unit: regulatory notification}
    outputs: [CAPA list with owners and dates]
    skill_level: 3
  - step_id: S8
    name: Compile review report and submit
    role: Executor
    type: work
    mandatory: true
    audit_actions: [Submitted]
    effort_min: {min: 10, likely: 15, max: 30}
    outputs: [incident review report]
    skill_level: 1
  - step_id: A1
    name: Incharge review
    role: Incharge
    type: approval
    mandatory: true
    audit_actions: [Approved, Rejected]
    effort_min: {min: 15, likely: 25, max: 45}
    queue_wait_h: {min: 0.25, likely: 1.0, max: 4.0}
    skill_level: 2
  - step_id: A2
    name: Lead approval of root cause and CAPA
    role: Lead
    type: approval
    mandatory: true
    audit_actions: [Approved, Rejected]
    effort_min: {min: 10, likely: 20, max: 40}
    queue_wait_h: {min: 0.25, likely: 1.0, max: 4.0}
    skill_level: 3
  - step_id: R1
    name: Correction and resubmission
    role: Executor
    type: rework
    mandatory: false
    audit_actions: [Updated, Resubmitted]
    effort_min: {min: 20, likely: 40, max: 90}

rework_triggers:
  - {code: RW-DOC, reason: Required document missing, detected_at: A1, preventable_by: "S3 evidence checklist"}
  - {code: RW-CAT, reason: Incorrect category, detected_at: A1, preventable_by: "S2 severity and incident-type classification"}
  - {code: RW-AMT, reason: Amount mismatch, detected_at: A1, preventable_by: "S6 impact computation check"}
  - {code: RW-QTY, reason: Wrong quantity, detected_at: A1, preventable_by: "S4 timeline reconciliation"}
expected_first_pass_yield: 0.85
rework_effort_min: {min: 20, likely: 40, max: 90}
max_rework_cycles: 2

exceptions:
  - {code: EX-MAJOR, condition: "severity == major", action: "Route to HOD after Lead approval", adds_approval: HOD, adds_dependency_wait: false}
  - {code: EX-REPORTABLE, condition: "regulatory_reportable == true", action: "HSE files the statutory notification within the legal deadline", adds_approval: null, adds_dependency_wait: false}
  - {code: EX-REPEAT, condition: "repeat_incident_90d >= 1", action: "Review the effectiveness of the previous CAPA in S5", adds_approval: null, adds_dependency_wait: false}
---

# SOP-019: Operational Incident Review and Root Cause Analysis

## 1. Purpose
Establish what happened, why it happened and what will prevent recurrence, for every operational incident.

## 2. Scope
Equipment failures, process deviations, near misses and safety events in Operations. Information-security
incidents follow the IT incident procedure.

## 3. References
ISO 9001:2015 §10.2 (nonconformity and corrective action); ISO 45001:2018 §10.2 (incident investigation);
SOP-018 Daily Operations Report.

## 4. Definitions
- **Severity**: minor (no injury, < 1 h downtime), moderate (first aid or 1–8 h downtime), major (lost-time
  injury, environmental release or > 8 h downtime).
- **CAPA**: corrective and preventive action, each with an owner and a due date.

## 5. Responsibilities (RACI)
| Activity | Executor | Incharge | Lead | HOD | Maintenance | HSE |
|---|---|---|---|---|---|---|
| Investigation and report | R | A | – | – | C | C |
| Technical findings (D1) | C | I | – | – | R | – |
| Safety assessment (D2) | C | I | – | – | – | R |
| Approval | I | R | A | A (major only) | – | – |

## 6. Procedure
1. **S1** The Executor creates the ticket and assigns it to themselves.
2. **S2** Secure the incident record and classify severity.
3. **S3** Collect logs, photographs and witness statements.
4. **S4** Reconstruct the timeline.
5. **S5** Identify the root cause (5-Why or fishbone).
6. **S6** Assess cost, downtime and safety impact.
7. **S7** Define CAPA with owners and dates.
8. **S8** Compile the report and submit.
9. After submission, while technical findings (D1) or the HSE assessment (D2) are outstanding, log
   `DependencyWait`. D1 and D2 run **in parallel** (`parallel_group: P1`); one event covers both.
10. **A1** Incharge review, then **A2** Lead approval. Major incidents add HOD approval (EX-MAJOR).
11. **R1** On rejection, correct and resubmit. After 2 rejections, escalate to the Lead.

## 7. Exceptions
See YAML `exceptions`.

## 8. Rejection reason codes
| Platform reason | Meaning for an incident review |
|---|---|
| Required document missing | Evidence, witness statement or technical findings missing |
| Incorrect category | Wrong severity or incident type |
| Amount mismatch | Cost or downtime impact computed incorrectly |
| Wrong quantity | Timeline durations or counts inconsistent with logs |

## 9. Records
Incident report, evidence pack, timeline, root cause statement, CAPA list, approval trail. Retain 10 years.

## 10. KPIs
| KPI | Target |
|---|---|
| SLA compliance | ≥ 90% |
| First-pass yield | ≥ 85% |
| Repeat incidents within 90 days | ≤ 5% |

## 11. Revision history
| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-14 | Initial schema v1.1 release |
| 1.1.0 | 2026-10-14 | Schema v1.2: D1 and D2 in parallel group P1; added `quality_targets_source`; fixed S6 `outputs` (one item, not two). Standard times unchanged |
