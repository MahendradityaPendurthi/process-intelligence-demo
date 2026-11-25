---
schema_version: "1.2"
sop_id: SOP-018
title: Daily Operations Report
version: 1.1.0
status: Approved
effective_date: 2026-10-14
review_cycle_months: 12
owner_role: Lead
department: Operations
task_type: Daily Operations Report
supersedes: []
complexity_declared: Simple
standard_time_source: illustrative_expert_estimate
standard_time_frozen: 2026-10-14
quality_targets_source: unconfirmed

sla_hours: {High: 6, Medium: 12, Low: 24}
sop_steps: 4
approval_count_base: 0
approval_count_max: 1
approval_matrix:
  - {stage: Incharge, condition: "kpi_breach == true or safety_event == true"}

dependency_count: 0
dependencies: []

complexity_drivers:
  - {driver: sites_reporting, source: ticket_metadata, bands: {low: "1", medium: "2-3", high: ">3"}, effect: effort}
  - {driver: kpi_breach, source: derived, bands: {low: "false", high: "true"}, effect: approval_route}
  - {driver: safety_event, source: ticket_metadata, bands: {low: "false", high: "true"}, effect: approval_route}

steps:
  - step_id: S1
    name: Create and self-assign daily report ticket
    role: Executor
    type: intake
    mandatory: true
    audit_actions: [Created, Assigned]
    effort_min: {min: 2, likely: 3, max: 5}
    queue_wait_h: {min: 0.05, likely: 0.25, max: 1.0}
    skill_level: 1
  - step_id: S2
    name: "Collect shift production, downtime and manpower data"
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 15, max: 30}
    effort_scaling: {driver: sites_reporting, per_unit_min: 8, unit: site}
    inputs: [shift logs, machine downtime log, attendance summary]
    outputs: [consolidated data sheet]
    skill_level: 1
  - step_id: S3
    name: Reconcile against plan and compute KPIs
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 10, likely: 15, max: 30}
    inputs: [daily plan, KPI definitions]
    outputs: [KPI table]
    skill_level: 2
  - step_id: S4
    name: "Record incidents, deviations and actions"
    role: Executor
    type: work
    mandatory: true
    audit_actions: []
    effort_min: {min: 5, likely: 10, max: 25}
    outputs: [deviation log]
    skill_level: 1
  - step_id: D-ESC
    name: "KPI breach or safety event?"
    role: System
    type: decision
    mandatory: true
    audit_actions: []
    effort_min: {min: 0, likely: 0, max: 0}
  - step_id: S5
    name: Compile and publish report
    role: Executor
    type: work
    mandatory: true
    audit_actions: [Submitted]
    effort_min: {min: 5, likely: 10, max: 20}
    outputs: [daily operations report]
    skill_level: 1
  - step_id: A1
    name: Incharge review of flagged report
    role: Incharge
    type: approval
    mandatory: false
    audit_actions: [Approved, Rejected]
    effort_min: {min: 5, likely: 10, max: 20}
    queue_wait_h: {min: 0.25, likely: 0.5, max: 2.0}
    skill_level: 2
  - step_id: R1
    name: Correction and republication
    role: Executor
    type: rework
    mandatory: false
    audit_actions: [Updated, Resubmitted]
    effort_min: {min: 5, likely: 15, max: 30}

rework_triggers:
  - {code: RW-QTY, reason: Wrong quantity, detected_at: A1, preventable_by: "S3 reconciliation against plan"}
  - {code: RW-AMT, reason: Amount mismatch, detected_at: A1, preventable_by: "S3 KPI formula check"}
  - {code: RW-CAT, reason: Incorrect category, detected_at: A1, preventable_by: "S4 downtime reason coding"}
  - {code: RW-DOC, reason: Required document missing, detected_at: A1, preventable_by: "S2 data completeness check"}
expected_first_pass_yield: 0.95
rework_effort_min: {min: 5, likely: 15, max: 30}
max_rework_cycles: 2

exceptions:
  - {code: EX-LATEDATA, condition: "site data not received by cut-off", action: "Publish with the site marked provisional; update next day. Do not hold the report.", adds_approval: null, adds_dependency_wait: false}
  - {code: EX-SAFETY, condition: "safety_event == true", action: "Notify HSE immediately and open an Incident Review (SOP-019)", adds_approval: null, adds_dependency_wait: false}
---

# SOP-018: Daily Operations Report

## 1. Purpose
Publish one accurate daily summary of production, downtime, manpower and incidents so that problems are visible
the same day.

## 2. Scope
All operating sites and shifts reporting to Operations.

## 3. References
ISO 9001:2015 §9.1 (monitoring, measurement, analysis and evaluation); KPI dictionary; SOP-019 Incident Review.

## 4. Definitions
- **KPI breach**: any KPI outside its daily control limit (for example output below 90% of plan, or unplanned
  downtime above 60 minutes).
- **Provisional**: a site figure published before final data was received.

## 5. Responsibilities (RACI)
| Activity | Executor | Incharge | Lead |
|---|---|---|---|
| Collect, reconcile, publish | R | A | I |
| Review of flagged reports | I | R/A | I |

## 6. Procedure
1. **S1** The Executor creates the ticket and assigns it to themselves.
2. **S2** Collect production, downtime and manpower data from every site.
3. **S3** Reconcile against the plan and compute the KPIs.
4. **S4** Record incidents, deviations and actions taken.
5. **S5** Compile and publish the report (Submitted).
6. **A1** Only when a KPI breach or safety event is flagged, the Incharge reviews and approves or rejects.
   Routine reports need **no approval** (`approval_count = 0`).
7. **R1** On rejection, correct and republish.

**This SOP has no external dependency.** Late site data is published as provisional (EX-LATEDATA); the report is
never held. A `DependencyWait`, or an approval on a report with no flagged breach, is non-conformant and is
reported as such.

## 7. Exceptions
See YAML `exceptions`.

## 8. Rejection reason codes
| Platform reason | Meaning for the daily report |
|---|---|
| Wrong quantity | Production or manpower figure does not reconcile with shift logs |
| Amount mismatch | KPI computed incorrectly |
| Incorrect category | Downtime or deviation coded to the wrong reason |
| Required document missing | Site data or incident note missing without the provisional flag |

## 9. Records
Daily report, consolidated data sheet, deviation log. Retain 3 years.

## 10. KPIs
| KPI | Target |
|---|---|
| Published within SLA | ≥ 98% |
| First-pass yield | ≥ 95% |

## 11. Revision history
| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-14 | Initial schema v1.1 release |
| 1.1.0 | 2026-10-14 | Schema v1.2: added `quality_targets_source`; quoted step names S2 and S4. Standard times unchanged |
