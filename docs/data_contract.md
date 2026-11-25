# Data Contract (Phase 1, synthetic exports)

Source for all files: synthetic CSV exports in `data/raw/` (static, read-only). Timestamps use
`YYYY-MM-DD HH:MM:SS`, are timezone-naive and are assumed to share one local timezone.

Privacy classes: **ID** = pseudonymous identifier (use internally), **PII** = personal data (do not
send to external services or show in analytics), **Ops** = operational, **Free** = free text that may
contain personal data in real exports.

## employees.csv (36 rows)

| Field | Type | Meaning | Req. | Example | Privacy |
|---|---|---|---|---|---|
| employee_id | string | Unique employee key | yes | `E1001`, `MFIN01` | ID |
| employee_name | string | Display name (synthetic) | no | `Finance Executor 1` | PII |
| department | string | Finance / Procurement / Operations / HR | yes | `Finance` | Ops |
| role | enum | Executor / Incharge / Lead / HOD | yes | `Executor` | Ops |
| reporting_to | string | Manager's employee_id; blank for HOD | yes (non-HOD) | `MFIN01` | ID |
| active_status | enum | Active / Inactive | yes | `Active` | Ops |

Each department has 6 Executors, 1 Incharge, 1 Lead, 1 HOD.

## tickets.csv (1,200 rows)

| Field | Type | Meaning | Req. | Example | Privacy |
|---|---|---|---|---|---|
| ticket_id | string | Unique ticket key | yes | `T00001` | ID |
| task_type | string | Task category, FK to task_types | yes | `Invoice Verification` | Ops |
| department | string | Owning department | yes | `Finance` | Ops |
| assigned_employee_id | string | Executor assigned (FK employees) | yes | `E1018` | ID |
| priority | enum | Low / Medium / High | yes | `Low` | Ops |
| complexity | enum | Simple / Medium / Complex (copied from task_types) | yes | `Complex` | Ops |
| sop_steps | int | Steps in the SOP for this task type | yes | `7` | Ops |
| approval_count | int | Required approvals (0-3) | yes | `2` | Ops |
| dependency_count | int | Declared dependencies (0-2) | yes | `2` | Ops |
| created_at | timestamp | Ticket creation | yes | `2026-08-21 09:00:00` | Ops |
| due_at | timestamp | SLA due time (High +6h, Medium +12h, Low +24h) | yes | `2026-08-22 09:00:00` | Ops |
| completed_at | timestamp | Completion = timestamp of the final audit event | yes | `2026-08-21 14:13:00` | Ops |
| final_status | enum | Completed / Completed_Late | yes | `Completed` | Ops |

Not present (in the generic contract but missing here): description, metadata, current_stage, SOP id,
project/customer/location.

## audit_logs.csv (7,429 rows): the main source

| Field | Type | Meaning | Req. | Example | Privacy |
|---|---|---|---|---|---|
| event_id | string | Unique event key; increases with time within a ticket | yes | `EV0000004` | ID |
| ticket_id | string | FK tickets | yes | `T00001` | ID |
| employee_id | string | Actor (FK employees) | yes | `MOPS01` | ID |
| action | enum | Created, Assigned, Updated, Submitted, Rejected, Resubmitted, DependencyWait, Approved | yes | `Rejected` | Ops |
| timestamp | timestamp | Event time | yes | `2026-08-21 10:37:00` | Ops |
| stage | enum | Hierarchy stage of the actor: Executor / Incharge / Lead | yes | `Incharge` | Ops |
| previous_status | string | Status before the event; blank for Created | no | `Submitted` | Ops |
| new_status | string | Status after the event | yes | `Rejected` | Ops |
| change_type | string | rejection_reason / correction / field_change / dependency / final_review | no | `rejection_reason` | Ops |
| details | string | Rejection reason or note | no | `Amount mismatch` | Free |

Observed vocabulary: no Closed, Escalated, Reassigned or Reopened events. Closure = final `Approved`.
The pipeline maps these and other common aliases anyway (`process_intel/config.py: EVENT_TYPE_MAP`).

## task_types.csv (9 rows)

| Field | Type | Meaning | Req. | Example |
|---|---|---|---|---|
| task_type | string | Unique task type | yes | `BOQ Review` |
| department | string | Owning department | yes | `Procurement` |
| complexity | enum | Simple / Medium / Complex | yes | `Medium` |
| sop_steps, approval_count, dependency_count | int | Same meaning as on tickets | yes | `3, 1, 1` |

## corporate_sops/ (9 schema SOPs + 12 legacy)

| Files | Format | Join key | Privacy |
|---|---|---|---|
| SOP-013..021 | YAML front matter (schema v1.2, `corporate_sops/SOP_SCHEMA.md`) + Markdown body | `task_type` (exact match to task_types) | Ops (no personal data) |
| SOP-001..012 | Legacy free text, identical bodies | none (not parsed) | Ops |

Front-matter fields used by the pipeline: document control (`sop_id`, `version`, `status`, `effective_date`,
`standard_time_source`, `standard_time_frozen`, `quality_targets_source`), routing (`sla_hours`, `sop_steps`,
`approval_count_base/max`, `approval_matrix`, `dependency_count`, `dependencies` with `parallel_group` and
`typical_wait_h`), `steps` (role, type, audit_actions, `effort_min`, `queue_wait_h`, skill_level),
`complexity_drivers`, `rework_triggers` (reason must be one of the 4 platform reasons, `detected_at`,
`preventable_by`), `expected_first_pass_yield`, `rework_effort_min`, `max_rework_cycles`, `exceptions`.
Each file's SHA-256 is recorded in `outputs/run_manifest.json`.

Data requests implied by the SOPs (`source: ticket_metadata` drivers absent from the export): line items,
document/claim/invoice values, sourcing route, severity, witnesses, leave days/type, sites reporting, and
others listed per SOP.

## Canonical event schema (data/processed/events_normalized.csv)

`event_id, ticket_id, employee_id, department, role, event_type, raw_event_type, timestamp, stage,
previous_status, new_status, previous_value, new_value, rejection_reason, comments, metadata,
raw_change_type, raw_details`. `previous_value` / `new_value` are empty because the export has no
field-level change data.

## Future integration questions for the real platform

1. Table/API for audit history, and whether it records field-level changes.
2. Timezone of stored timestamps.
3. How reassignment, escalation, cancellation and reopening are represented.
4. Whether the DependencyWait end time (dependency resolved) can be logged as its own event.
5. Source of leave/absence data.
6. Access method: API, webhook, CDC or read-only DB polling with an event_id checkpoint.
