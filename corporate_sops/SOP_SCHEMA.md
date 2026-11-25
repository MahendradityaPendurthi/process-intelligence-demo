# SOP Schema v1.2 — Machine-Readable SOP Standard

Location: `corporate_sops/SOP_SCHEMA.md`. This is the single reference for SOP authors and the pipeline
(`process_intel/sop.py`, `sop_analysis.py`, `conformance.py`).

Applies to SOP-013 onward. SOP-001..012 are **legacy free-text SOPs**. They are kept unchanged and are never
parsed for parameters. A legacy SOP replaced by a schema SOP is listed in that SOP's `supersedes` field.

Purpose: make every SOP parseable so that the pipeline can:
- (a) **derive** task complexity from the SOP instead of only reading the declared label,
- (b) compare audit-log behaviour with the SOP (**conformance checking**),
- (c) **predict** elapsed time before a ticket starts, with an uncertainty band,
- (d) **explain** deviations by linking them to SOP steps and controls.

Each SOP file has two parts:
1. **YAML front matter** between the first two `---` lines. This is the only part the pipeline parses.
2. **Markdown body**: the human-readable procedure in ISO 9001 document structure (purpose, scope,
   references, definitions, RACI, procedure, exceptions, rejection reason codes, records, KPIs, revision
   history). The body must never contradict the YAML.

### Changes from v1.1
| # | Change | Why |
|---|---|---|
| 1 | `dependencies[].parallel_group`; waits in the same group combine as a **maximum**, not a sum (§7.1) | v1.1 summed dependencies that run at the same time (one DependencyWait covers both), overstating elapsed time for Vendor Onboarding and Incident Review |
| 2 | Effort coverage now compares **executor** effort only (§8) | v1.1 compared all SOP effort, including approvers' review time, with the executor's holding time |
| 3 | Defined how to read effort coverage **above 1** (§8) | v1.1 only explained values below 1. A standard above the observed upper bound is a finding, never a reason to edit times |
| 4 | Retrospective conformance (§9.1) | SOPs effective after the tickets were processed must be labelled as such |
| 5 | `quality_targets_source` field (§5) | `expected_first_pass_yield` needs the same independence evidence as standard times |
| 6 | Per-component comparison map from SOP terms to audit-log metrics (§7.3) | v1.1 named components without saying which measured value each one matches |
| 7 | Pipeline sequence made explicit (§11) | Stages must run in a fixed order |
| 8 | The validator enforces structural rules: inputs and outputs must be lists of strings, and names must be strings | Unquoted commas inside flow lists silently split one item into two |
| 9 | SOP-log correspondence gate (§9.2, stage 3b) | Confirms that each task type's logs are the process its SOP describes before any comparison |

---

## 1. Document control fields

| Field | Type | Req. | Meaning |
|---|---|---|---|
| `schema_version` | string | yes | `"1.2"` |
| `sop_id` | string | yes | `SOP-nnn`, unique |
| `title` | string | yes | Human-readable name |
| `version` | string | yes | Semantic version. Bump on **any** YAML change |
| `status` | enum | yes | Draft / Approved / Retired. The pipeline uses Approved and Draft and ignores Retired |
| `effective_date` | date | yes | `YYYY-MM-DD` |
| `review_cycle_months` | int | yes | Mandatory review interval |
| `owner_role` | enum | yes | Executor / Incharge / Lead / HOD |
| `department` | string | yes | Must equal `task_types.department` |
| `task_type` | string | yes | **Must exactly match** `task_types.task_type`. This is the join key. Only one Approved or Draft SOP is allowed per task type |
| `supersedes` | list | no | Legacy SOP ids this SOP replaces, e.g. `[SOP-003]` |
| `complexity_declared` | enum | yes | Must equal `task_types.complexity` |
| `standard_time_source` | enum | yes | `illustrative_expert_estimate`, `time_study` or `historical_calibration` |
| `standard_time_frozen` | date | yes | Date the time values were fixed. They may not change without a version bump |
| `quality_targets_source` | enum | yes | Source of `expected_first_pass_yield`: `illustrative_expert_estimate`, `policy_target`, `historical_calibration` or `unconfirmed` |

## 2. SLA and routing fields

| Field | Type | Meaning |
|---|---|---|
| `sla_hours` | map priority → hours | Must agree with the ticket `due_at` rule (High 6, Medium 12, Low 24) |
| `sop_steps` | int | Count of steps with `type: work` and `role: Executor`. **Must equal** `task_types.sop_steps` |
| `approval_count_base` | int | Approvals always required. Must equal the number of `always` rows in `approval_matrix` |
| `approval_count_max` | int | Approvals when every conditional rule fires. Must equal the length of `approval_matrix`. `task_types.approval_count` must lie in `[base, max]` |
| `approval_matrix` | list | Ordered approval stages `{stage, condition}`. `condition` is `always` or an expression on a driver. Every stage needs a matching `type: approval` step with that `role` |
| `dependency_count` | int | Declared external dependencies. **Must equal** `task_types.dependency_count`, and `dependencies` must list at least this many |
| `dependencies` | list | `{id, provider, item, blocking_step, parallel_group, typical_wait_h: {min, likely, max}}` |

`parallel_group`: dependencies with the same group value are requested together and resolved concurrently.
Their waits combine as the maximum (§7.1). Different groups run one after another.

The SOP states what the **business requires**, not what the audit log happens to show. Where the two differ,
conformance checking reports it. An example is approval_count=3 tasks that log only 2 approvals.

## 3. Steps

Each item in `steps`:

| Field | Meaning |
|---|---|
| `step_id` | `S1..` for intake and work, `A1..` for approvals, `D-..` for decisions, `R1..` for rework. Unique within the SOP |
| `name` | Short name. Always quote it if it contains `,`, `?`, `:`, `#`, `{`, `}`, `[` or `]` |
| `role` | Executor / Incharge / Lead / HOD / System / External |
| `type` | `intake`, `work`, `approval`, `decision` or `rework` |
| `mandatory` | true / false |
| `audit_actions` | Actions this step is expected to produce: `Created`, `Assigned`, `Updated`, `Submitted`, `Rejected`, `Resubmitted`, `DependencyWait`, `Approved` |
| `effort_min` | **Touch time** in minutes `{min, likely, max}`, with 0 ≤ min ≤ likely ≤ max |
| `effort_scaling` | Optional `{driver, per_unit_min, unit}` |
| `queue_wait_h` | Optional elapsed hours **before** the step starts `{min, likely, max}` |
| `inputs` / `outputs` | Lists of strings. Quote any item that contains a comma |
| `skill_level` | 1 (routine) to 3 (specialist judgement). Required for work steps |

### 3.1 Independence of standard times (mandatory)

`effort_min`, `queue_wait_h`, `typical_wait_h`, `rework_effort_min` and `expected_first_pass_yield` must be set
**without looking at the audit data being evaluated**. Acceptable sources are an expert, a time study, a policy
target or declared illustrative values. If they are fitted to the same audit data, the SOP estimate will match
the actuals by construction and the comparison proves nothing.

- The pipeline and its developers **must not edit** these values to improve agreement, including when a run
  shows that they disagree with the data (§8).
- Recalibration is allowed only as a new SOP version with `standard_time_source: historical_calibration`,
  fitted on an earlier period and evaluated on a later one (out-of-sample).
- When provenance cannot be confirmed, set `quality_targets_source: unconfirmed`. The pipeline then reports the
  FPY comparison as weak evidence.
- Every run records the SHA-256 of each SOP file in `outputs/run_manifest.json`.

### 3.2 Platform logging conventions (observed in the current export)

SOP authors map `audit_actions` to what the platform actually logs, not to an idealised event per step.

| Observation (1,200 tickets) | Consequence for SOPs and conformance |
|---|---|
| The executor logs `Created` and `Assigned` (self-assignment) | The intake step's role is Executor. There is no Incharge assignment event to check |
| `Updated` occurs 0–3 times per ticket regardless of `sop_steps`, and its detail is always "normal edit" | Executor work steps have **no audit footprint**. They drive the effort estimate only; conformance cannot check them |
| `DependencyWait` is logged by the executor **after** `Submitted`/`Resubmitted` and before the Incharge decision. It appears at most once per ticket, on 1,179 tickets, regardless of `dependency_count` (0, 1 or 2) | Model each dependency as a **pre-review hold** after submission, with `blocking_step` = the first approval. One event may cover several dependencies in the same `parallel_group` |
| Rejections come only from the Incharge, at most once per ticket, from a fixed vocabulary of 4 reasons (`Amount mismatch`, `Incorrect category`, `Required document missing`, `Wrong quantity`) | `rework_triggers.reason` **must** use these exact strings (validated against `config.PLATFORM_REJECTION_REASONS`). Task-specific meaning goes in the SOP body |
| Approvals: the Incharge always approves, even when `approval_count = 0`. The Lead approves (`change_type = final_review`) when `approval_count ≥ 2`. HOD approval is never logged | `approval_count = 3` SOPs list an HOD stage, and C1 will report it missing. That is the known DQ057 finding |

### 3.3 Three-point (PERT) estimate

```
mean     = (min + 4 × likely + max) / 6
variance = ((max − min) / 6)²
```
Scaled step: `mean = PERT(effort_min) + per_unit_min × driver_value`. When the driver is unknown, the scaling
term is 0 and the estimate is flagged `drivers_missing`.

## 4. Complexity drivers

`complexity_drivers` is a list of `{driver, source, bands, effect}`:
- `source` is one of `ticket_metadata`, `derived` or `sop`.
- `effect` is one of `effort`, `approval_route`, `rework_risk` or `dependency`.

Drivers with `source: ticket_metadata` are **data requests for the platform team**. They are absent from the
current export.

## 5. Rework and exceptions

| Field | Meaning |
|---|---|
| `rework_triggers` | `{code, reason, detected_at, preventable_by}`. `reason` is the exact text expected in `audit_logs.details` when `change_type = rejection_reason`. `detected_at` must be an approval `step_id` |
| `expected_first_pass_yield` | Share of tickets approved without any rejection, from 0 to 1. Its provenance is recorded in `quality_targets_source` |
| `rework_effort_min` | Three-point effort of one correction cycle |
| `max_rework_cycles` | Rejections allowed before escalation |
| `exceptions` | `{code, condition, action, adds_approval, adds_dependency_wait}`. `adds_dependency_wait: true` means a `DependencyWait` on a 0-dependency task is an **expected exception**, not an undeclared dependency |

## 6. Derived complexity score (computed by the pipeline)

```
CS = w_steps     × sop_steps
   + w_appr_base × approval_count_base
   + w_appr_cond × (approval_count_max − approval_count_base)
   + w_dep       × dependency_count
   + w_decision  × count(steps where type == decision)
   + w_driver    × count(complexity_drivers where effect == effort)
   + w_exception × count(exceptions)
   + w_skill     × (mean skill_level of Executor work steps − 1)
```

The `CS-v1` defaults live in `config.py`: w_steps 1.0, w_appr_base 2.0, w_appr_cond 1.0, w_dep 2.5,
w_decision 1.5, w_driver 1.0, w_exception 0.5, w_skill 1.0. The bands are CS < 12 Simple, 12–20 Medium and
> 20 Complex.

Disagreement between derived and declared complexity is **reported, never corrected**. The weights are a
hypothesis, and matching the declared labels is weak evidence because the same author wrote both. The real test
is whether CS rank-correlates with the observed median elapsed time across task types (Spearman ρ, reported
each run).

## 7. Estimates and allowed comparisons

### 7.1 Expected effort and elapsed time
```
E_effort_exec = Σ mean(effort) of applicable Executor work steps
              + (1 − expected_first_pass_yield) × mean(rework_effort_min)
E_effort      = E_effort_exec
              + mean(effort) of the intake step
              + Σ mean(effort) of applicable approval steps
E_wait        = Σ PERT mean of queue_wait_h for applicable steps
              + Σ over parallel groups of  max(typical_wait_h of applicable dependencies in the group)
E_elapsed     = E_effort / 60 + E_wait
SD            = sqrt(Σ variances of every term above; effort variances converted to hours²)
P10, P90      = E_elapsed ∓ 1.2816 × SD, with P10 floored at 0
```
- **Maximum of a parallel group.** The mean and variance of a maximum of independent waits use Clark's normal
  approximation, applied pairwise in list order. A group with a single dependency is just that dependency.
- **Approximations to note in outputs.** Steps are assumed sequential and independent, and the normal
  approximation understates the right tail.

### 7.2 Which conditional terms apply
- **Conditional approvals:** if the driver in the condition is available, evaluate it. Otherwise apply the
  first `ticket.approval_count − approval_count_base` conditional approvals in matrix order, and flag the
  estimate `approval_route_from_ticket`. A non-applicable approval contributes neither effort nor queue time.
- **Dependencies:** include the first `ticket.dependency_count` dependencies in list order. Exception-driven
  waits are not included in the prior.

### 7.3 Allowed comparisons and the component map

| SOP term | Audit-log metric it is compared with | Status |
|---|---|---|
| `E_elapsed` (P10–P90) | `total_duration_h` | **Primary**, like with like. Check C7 |
| `queue_wait_h` of the intake step | `queue_time_h` (Created → Assigned) | Allowed, per component |
| First approval: queue + review effort + waits of dependencies blocking it | `pre_decision_wait_h` (submission → Incharge decision, including the DependencyWait interval) | Allowed, per component |
| Lead approval: queue + review effort | `decision_wait_lead_h` | Allowed, per component |
| `E_effort_exec` | WIP-adjusted executor hold time (§8) | Allowed **only aggregated** (task type × month, n ≥ 20), as an upper-bound ratio |
| `E_effort` or `E_effort_exec` | raw hold time or `processing_time_est_h` | **Not allowed** |
| `1 − expected_first_pass_yield` | Observed share of tickets with ≥ 1 rejection | Allowed. Weak evidence when `quality_targets_source` is `unconfirmed` or `historical_calibration` on the same period |

## 8. WIP adjustment and effort coverage

The audit log shows how long an executor *holds* a ticket, not how long they *work* on it. When an executor
holds k tickets at once, raw hold time counts each clock hour k times.

**Holder.** For segments with `category ∈ {processing, rework}`, the holder is the ticket's
`assigned_employee_id`. Do not use `actor_employee_id`. In the current export the executor logs `Created` and
`Assigned` themselves, so the two coincide. On real platforms, however, the actor of `Assigned` is often the
Incharge, and the actor of a segment that starts at `Rejected` is always the reviewer.

**Algorithm (per executor e):**
1. Take all of e's processing and rework segments `[start, end)` across all tickets.
2. Sort all segment start and end points into breakpoints `t0 < t1 < … < tn`.
3. For each elementary interval `[ti, ti+1)`, let k be the number of e's segments covering it. If k > 0, add
   `(ti+1 − ti) / k` hours to each covering ticket.
4. Sum per ticket to get `executor_hold_wip_adj_h`.

**Properties (tested):**
- `executor_hold_wip_adj_h ≤ executor_processing_h + rework_time_h` for every ticket.
- For each executor, Σ `executor_hold_wip_adj_h` equals the length of the union of their hold intervals.
- With no overlaps, `executor_hold_wip_adj_h` equals raw hold time.

**Effort coverage.** For each task type × month with n ≥ 20:
`effort_coverage = (E_effort_exec / 60) / median(executor_hold_wip_adj_h)`. Hold time is still an **upper
bound** on effort, because it includes breaks, idle time and work done outside the system.

| Coverage | Reading | Pipeline flag |
|---|---|---|
| > 1.0 | The SOP executor effort exceeds the observed upper bound. Either the standard is too high, or work happens outside the ticket window (before `Created` or after `Submitted`) | `standard_exceeds_hold` |
| 0.5 – 1.0 | Plausible: the SOP effort fits inside the holding time | `plausible` |
| < 0.5 | Holding includes much non-SOP time (waiting on others, multitasking, idle), or the standard is too low | `low_coverage` |

These flags are findings for the SOP owner. They never trigger an edit of the time values (§3.1). Coverage is
**never** computed per employee.

## 9. Conformance checks (per ticket)

| Id | Check | Result values |
|---|---|---|
| C1 | Approval events vs SOP-required approvals for this ticket (§7.2) | ok / fewer / more |
| C2 | Approval stages appear in `approval_matrix` order | ok / out_of_order |
| C3 | DependencyWait on a task with `dependency_count = 0` | none / expected_exception / undeclared |
| C4 | Required audit actions present (`Created`, `Assigned`, `Submitted`, final `Approved`) | ok / missing:<list> |
| C5 | Rejections > `max_rework_cycles` without an escalation event | ok / exceeded |
| C6 | Each rejection reason matches a `rework_triggers.reason` (case-insensitive, trimmed) | ok / unmapped:<list> / n/a (no rejection) |
| C7 | Actual elapsed vs the SOP band | within / below_p10 / above_p90 |

`fitness = checks C1–C6 that pass / checks evaluated`, where `n/a` is not evaluated and C3 `none` counts as a
pass. C7 is reported separately because it is a time comparison, not a path check. C6 is informative only when
an SOP lists a subset of the platform reasons. When all 4 are listed, it can only fail on unknown reasons.

### 9.1 Retrospective conformance
A ticket created before the SOP's `effective_date` is still checked, but its result is labelled
`conformance_mode = retrospective`. It shows how far past practice was from the documented process. It is not
a breach of a rule that was in force at the time. Tickets created on or after `effective_date` are labelled
`in_force`.

### 9.2 SOP-log correspondence gate (before any SOP comparison)
The `task_type` label alone does not prove that a task type's logs are the process its SOP describes.
Before stages 4–6, every ticket is replayed on a process model built from its SOP:
- every actor belongs to the SOP's department and holds the role of the step it performs;
- intake is `Created` then `Assigned`, then `Updated*`, then `Submitted`;
- in review, an optional `DependencyWait` comes before the decision, approvals come only from `approval_matrix`
  stages and in matrix order, and rejections come only from stages named by `rework_triggers.detected_at`;
- rework is `Updated*` then `Resubmitted`, back to review;
- the ticket closes on an approval, with no activity afterwards.

| Ticket outcome | Meaning |
|---|---|
| `fits` | The path matches the SOP model |
| `fits_with_known_deviations` | The same process with conformance deviations only: approval count (C1), a hold the SOP forbids (C3), a reason not in the SOP (C6) |
| `does_not_fit` | The path cannot come from this SOP: wrong department or role, an approval stage the SOP lacks, wrong order, a foreign activity, or no closing approval |

Per task type, `correspondence` is the share of tickets that are not `does_not_fit`. Each task type is also
**cross-fitted** against every SOP, using a path score (fits 1, known deviation 0.5, no fit 0) and the time
scale (observed median vs the SOP's expected elapsed time). Approval stages the platform never logs are left out
of the time comparison, because completion is logged at the last recorded approval.

| Verdict | Rule | Effect |
|---|---|---|
| `corresponds` | correspondence ≥ 0.95, time ratio within [0.25, 4], and the time scale is closest to the labelled SOP | SOP used |
| `partial` | correspondence ≥ 0.80 and in range, but not fully identified | SOP used, `SOP_LOG_MISMATCH` (medium) raised |
| `does_not_correspond` | correspondence < 0.80, time out of range, or another SOP explains the path at least as well and the time scale better | SOP **excluded** from stages 4–6, `SOP_LOG_MISMATCH` (high) raised |

Limitation: executor work steps leave no audit footprint (§3.2). Two SOPs with the same routing therefore differ
in the logs only by time scale, and the `task_type` label decides between them. The report says so wherever the
path cannot discriminate.

## 10. Task-type registry

| SOP | task_type | Department | Supersedes |
|---|---|---|---|
| SOP-013 | BOQ Review | Procurement | – |
| SOP-014 | Purchase Request | Procurement | SOP-002 |
| SOP-015 | Invoice Verification | Finance | SOP-003 |
| SOP-016 | Expense Approval | Finance | SOP-004 |
| SOP-017 | Vendor Onboarding | Procurement | – |
| SOP-018 | Daily Operations Report | Operations | – |
| SOP-019 | Incident Review | Operations | – |
| SOP-020 | Leave Approval | HR | – |
| SOP-021 | Employee Document Verification | HR | – |

All standard times in SOP-013..021 are `illustrative_expert_estimate` for synthetic data. Their
`expected_first_pass_yield` provenance is `unconfirmed`.

## 11. Pipeline sequence

The stages run in this order. Each stage consumes only the outputs of earlier stages.

| # | Stage | Module | Output |
|---|---|---|---|
| 1 | **Read SOPs**: parse the front matter and validate it against this schema and `task_types.csv` | `sop.load_sops`, `sop.validate_sops` | `sop_validation_report.csv` |
| 2 | **Understand parameters**: CS, derived complexity, expected effort, elapsed time and band per task type | `sop.sop_parameters` | `sop_parameters.csv` |
| 3 | **Read the logs**: validate, normalize and reconstruct ticket lifecycles | `ingestion`, `normalization`, `lifecycle` | `data_quality_report.csv`, `ticket_lifecycles.csv` |
| 3b | **SOP-log correspondence gate**: replay every ticket on its SOP's process model, cross-fit against all SOPs, and exclude SOPs whose logs are a different process (§9.2) | `correspondence` | `sop_log_correspondence.csv`, `sop_crossfit.csv` |
| 4 | **Analyse time and complexity**: SOP expectation vs actual, historical baselines, WIP-adjusted hold, effort coverage, CS vs observed ρ | `features`, `baselines`, `wip`, `sop_analysis`, `metrics` | `ticket_features.csv`, `sop_time_complexity.csv`, `sop_effort_coverage.csv`, metrics |
| 5 | **Check deviations**: SOP conformance per ticket plus statistical deviations | `conformance`, `sop_deviations`, `deviations` | `conformance.csv`, deviation rows |
| 6 | **Find reasons**: rank causes and link each to the SOP step, control or clause | `root_cause` | `deviations.csv` |
| 7 | **Report** | `report` | `demo_report.md` (summary), `technical_report.md`, `deviation_report.md`, `run_manifest.json` |
