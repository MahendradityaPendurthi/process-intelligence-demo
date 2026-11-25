# Process Intelligence --- Phase 1 Prototype

## AI Agent Implementation Context

Version: 1.0 Status: Prototype using synthetic data

## 1. Objective

Build an AI-powered Process Intelligence and Performance Analytics
system on top of an existing organizational workflow platform.

The organization follows:

Executor -\> Incharge -\> Lead -\> HOD

The existing platform records tasks/tickets and audit history. The new
system analyzes this data to understand workflow, duration, waiting,
workload, rework, rejection, bottlenecks, baselines, and meaningful
deviations.

The system must NOT automatically label an employee as good/bad or
underperforming. It should provide evidence-backed signals for
managerial investigation.

## 2. Current Constraint

There is no company data yet. Phase 1 must use synthetic data.

The supplied prototype contains approximately: - 66 synthetic
employees - 3,000 synthetic tickets - 22,243 synthetic audit events - 12
synthetic SOPs - synthetic absence and assignment data

The agent must first prove the analytical pipeline using this data.

## 3. Core Pipeline

Raw data -\> validation -\> normalization -\> process mining -\> feature
engineering -\> historical baselines -\> deviation detection -\> context
analysis -\> root-cause analysis -\> LLM explanation -\> ML prediction
-\> dashboard/API

Do NOT start with ML. First prove that the underlying data and analytics
are correct.

------------------------------------------------------------------------

# STAGE 0 --- PROJECT AND DATA INSPECTION

First inspect the complete project.

Read: - README.md - docs/data_contract.md - data/raw/* - data/sops/* -
src/\*

Check: - row counts - columns and data types - missing values -
duplicate IDs - timestamp ranges - foreign-key consistency - employee
hierarchy - task distribution - event/action distribution - SOP mappings

Do not rewrite the project before understanding it.

Deliverable: `outputs/data_quality_report.csv`

------------------------------------------------------------------------

# STAGE 1 --- DATA VALIDATION

Validate:

-   required columns
-   unique ticket IDs
-   unique event IDs
-   valid employee IDs
-   valid SOP IDs
-   valid timestamps
-   events linked to existing tickets
-   tickets linked to valid employees
-   malformed hierarchy values
-   impossible timestamps

Never silently discard important records.

Keep raw data unchanged.

Recommended structure:

data/raw/ data/processed/ outputs/

Document assumptions.

------------------------------------------------------------------------

# STAGE 2 --- EVENT NORMALIZATION

Create a canonical event vocabulary.

Example:

Created -\> CREATED Assigned -\> ASSIGNED Updated -\> UPDATED Submitted
-\> SUBMITTED Rejected -\> REJECTED Resubmitted -\> RESUBMITTED Approved
-\> APPROVED Closed -\> CLOSED

Preserve:

raw_event_type event_type

Canonical event fields:

event_id ticket_id employee_id event_type timestamp stage
previous_status new_status previous_value new_value rejection_reason
comments metadata

Sort events by:

ticket_id + timestamp + event_id

------------------------------------------------------------------------

# STAGE 3 --- PROCESS MINING / LIFECYCLE RECONSTRUCTION

For every ticket:

1.  collect all events
2.  sort chronologically
3.  reconstruct the lifecycle
4.  identify stages
5.  identify transitions
6.  calculate time between events
7.  count rejection/rework
8.  count approvals
9.  identify closure

Example:

Created -\> Assigned -\> Updated -\> Submitted -\> Rejected -\> Updated
-\> Resubmitted -\> Approved -\> Closed

Must handle: - repeated updates - multiple rejections - multiple
resubmissions - reassignment - escalation - reopened tickets - missing
optional events - different approval paths

Output: `outputs/ticket_lifecycles.csv`

------------------------------------------------------------------------

# STAGE 4 --- TICKET FEATURE ENGINEERING

For each ticket calculate:

Duration: - total_duration - processing_time where reliably derivable -
waiting_time - approval_waiting_time - queue_time

Process: - rejection_count - resubmission_count - rework_cycles -
update_count - handoff_count - stage_count

SLA: - sla_met - sla_delay

Context: - task_type - complexity - priority - department -
dependency_count - approval_count - SOP step count

If a metric is estimated, label it as estimated rather than presenting
it as exact.

Output: `outputs/ticket_features.csv`

------------------------------------------------------------------------

# STAGE 5 --- EMPLOYEE AND TEAM METRICS

Aggregate daily, weekly, and monthly where possible.

Metrics: - tickets_completed - weighted_workload - average_duration -
median_duration - rejection_rate - rework_rate - SLA_compliance -
waiting_time - processing_time - task_mix - complexity_mix - trend

CRITICAL: Do not judge employees using raw ticket count alone.

Example: 20 simple tasks may represent less effort than 8 complex tasks.

Output: `outputs/employee_metrics.csv` and later:
`outputs/team_metrics.csv`

------------------------------------------------------------------------

# STAGE 6 --- TASK COMPLEXITY

Initial labels:

Simple Medium Complex

Use: - SOP steps - approval count - dependency count - task type -
priority - exception status - historical duration

The synthetic dataset already contains complexity.

Do not train a complexity model yet.

Later complexity can be estimated using rules, an LLM, or supervised ML.

------------------------------------------------------------------------

# STAGE 7 --- HISTORICAL BASELINES

Create contextual baselines.

Do not use one global average.

Prefer groups such as:

task_type complexity department priority when sufficient data exists

Calculate: - median duration - P75 duration - P90 duration - rejection
rate - rework rate - SLA rate - typical waiting time

Example:

Medium BOQ Review: median = 3.2 hours P75 = 4.5 hours P90 = 6.1 hours

Output: `outputs/baselines.csv`

------------------------------------------------------------------------

# STAGE 8 --- DEVIATION DETECTION

Start with simple, explainable statistics.

Example:

duration_ratio = actual_duration / expected_duration

Prototype rule:

duration_ratio \>= 1.75

This is only a demonstration threshold, not a production rule.

Also detect: - unusual rejection rate - unusual rework - persistent
decline - unusual waiting - unusual workload - bottleneck accumulation -
SLA deterioration

One unusual ticket should not automatically become an employee-level
alert.

Persistent patterns are more important.

Output: `outputs/deviations.csv`

------------------------------------------------------------------------

# STAGE 9 --- CONTEXT-AWARE ANALYSIS

Every deviation must be checked against:

-   complexity
-   priority
-   leave/absence
-   workload
-   dependency
-   reassignment
-   approval waiting
-   rejection/rework
-   team workload
-   system delays
-   cross-department dependencies

Example:

Expected = 3 hours Actual = 8 hours

If: Executor processing = 2 hours Approval waiting = 4 hours Rework = 1
hour Final processing = 1 hour

Then the system should identify approval waiting as the dominant
contributor.

It should NOT conclude that the executor was slow.

------------------------------------------------------------------------

# STAGE 10 --- ROOT-CAUSE ANALYSIS

Possible contributing causes:

-   approval bottleneck
-   cross-team dependency
-   rework
-   incorrect submission
-   high complexity
-   high workload
-   reassignment
-   missing information
-   SLA conflict
-   system delay
-   process bottleneck

Store:

deviation_type severity evidence candidate_causes confidence
source_event_ids

Do not make unsupported causal claims.

------------------------------------------------------------------------

# STAGE 11 --- LLM EXPLANATION

LLM is an explanation layer, NOT the calculation engine.

Python/deterministic code calculates: - counts - durations -
percentages - baselines - ratios - trends - deviation scores

LLM receives structured evidence and generates:

-   summary
-   evidence
-   likely causes
-   confidence
-   recommended investigation

The LLM must never invent metrics or events.

Every explanation must be traceable to deterministic evidence.

------------------------------------------------------------------------

# STAGE 12 --- ML LAYER

Only begin after the historical analytical dataset is validated.

Potential ML tasks:

1.  Expected completion time
2.  Expected effort
3.  Delay probability
4.  Rework/rejection probability

Candidate models: - Linear/regularized regression baseline - Random
Forest - Gradient Boosting - XGBoost - LightGBM

Do not select a model before inspecting the actual data.

Compare ML against simple baselines.

Regression metrics: MAE RMSE R²

Classification metrics: Precision Recall F1 ROC-AUC Calibration

ML predictions must remain explainable.

------------------------------------------------------------------------

# STAGE 13 --- ANALYTICS DATA MODEL

Create logical entities:

-   employees
-   tickets
-   events
-   ticket_lifecycles
-   ticket_features
-   employee_metrics
-   team_metrics
-   baselines
-   deviations
-   root_causes
-   ai_insights
-   model_predictions

Every insight must be traceable to source events and the
metric/baseline/model used.

------------------------------------------------------------------------

# STAGE 14 --- DASHBOARD/API

First demonstrate through CSV outputs.

Then expose through an API/dashboard.

Ticket view: - lifecycle - duration - waiting - rejection - rework -
SLA - baseline comparison - deviation - likely cause

Employee/team view: - workload - complexity-adjusted workload - trends -
rejection/rework - SLA - deviations requiring review

Management view: - department health - bottlenecks - approval delays -
process trends - recurring deviations

Do NOT create a simplistic best-to-worst employee ranking.

------------------------------------------------------------------------

# STAGE 15 --- ROLE-BASED VISIBILITY

Executor: own tasks and process issues

Incharge: team workload, deviations, bottlenecks

Lead: department trends and recurring issues

HOD: high-level department/process health

Use existing organizational permissions in the eventual production
integration.

------------------------------------------------------------------------

# PHASE 1 MVP DEFINITION

Phase 1 is successful when it can:

1.  Read synthetic data.
2.  Validate it.
3.  Normalize events.
4.  Reconstruct ticket lifecycles.
5.  Calculate ticket metrics.
6.  Calculate employee metrics.
7.  Create contextual baselines.
8.  Detect meaningful deviations.
9.  Produce evidence for deviations.
10. Identify likely process bottlenecks.
11. Export analytical outputs.
12. Run reproducibly from raw data.

Phase 1 does NOT require: - ML training - LLM integration - production
API - company database - live streaming - automated HR decisions

------------------------------------------------------------------------

# REQUIRED TESTING

Test:

-   event normalization
-   chronological ordering
-   lifecycle reconstruction
-   duration calculation
-   rejection counting
-   resubmission counting
-   baseline calculation
-   deviation detection
-   SLA calculation

Edge cases: - single-event ticket - no rejection - multiple rejections -
out-of-order events - duplicate event - missing employee - missing SOP -
missing timestamp - reopened ticket

------------------------------------------------------------------------

# DEMONSTRATION SCENARIOS

The prototype should demonstrate:

## A. Normal task

Task is within baseline. Expected: no significant deviation.

## B. Approval bottleneck

Task is slow because most extra time is approval waiting. Expected:
process bottleneck, not employee issue.

## C. Rework

Task has rejection/resubmission. Expected: show rejection and rework
contribution.

## D. Complexity difference

One employee handles fewer but more complex tasks. Expected: raw counts
are shown to be misleading.

## E. Persistent decline

Output decreases for several periods and context does not explain it.
Expected: persistent unexplained deviation requiring managerial review.

------------------------------------------------------------------------

# FUTURE COMPANY INTEGRATION

Once the synthetic pipeline is validated, replace the synthetic inputs
with company exports.

Possible integration methods:

-   CSV/Excel initially
-   API
-   Webhooks
-   Read-only database access
-   CDC
-   Polling

The existing platform remains the source of truth.

The analytics service must remain decoupled so an analytics failure
cannot stop the operational workflow.

------------------------------------------------------------------------

# FIRST ACTIONS FOR THE AI CODING AGENT

Do these in order:

1.  Inspect the project directory.
2.  Read README, data contract, raw data, SOPs, and source code.
3.  Generate the data-quality report.
4.  Review the existing pipeline.
5.  Identify what already works and what is incomplete.
6.  Do not rewrite everything.
7.  Implement/verify validation.
8.  Implement/verify normalization.
9.  Implement/verify lifecycle reconstruction.
10. Implement/verify feature engineering.
11. Implement/verify baselines.
12. Implement/verify deviation detection.
13. Run the pipeline.
14. Inspect every output.
15. Manually verify at least 10 tickets against their raw audit events.
16. Add unit tests.
17. Produce a short prototype demonstration report.
18. Stop at Phase 1 unless explicitly instructed to proceed.

------------------------------------------------------------------------

# ENGINEERING RULES

1.  Preserve raw data.
2.  Never silently drop records.
3.  Document assumptions.
4.  Keep deterministic analytics separate from AI.
5.  Do not train ML prematurely.
6.  Do not let LLM calculate core metrics.
7.  Do not let LLM invent evidence.
8.  Every insight must have evidence.
9.  Always account for complexity.
10. Account for dependencies and leave where available.
11. Distinguish process bottlenecks from individual deviations.
12. A deviation is a signal for investigation, not a final judgment.
13. Prefer simple methods before complex models.
14. Do not modify production data.
15. Make pipeline stages reproducible.
16. Add tests before major refactoring.
17. Avoid unnecessary infrastructure.
18. Keep the prototype understandable enough to demonstrate to a
    manager.
19. Use synthetic data until the analytical pipeline is validated.
20. The purpose of Phase 1 is to prove the methodology, not to create an
    impressive-looking AI demo.

------------------------------------------------------------------------

# FINAL SYSTEM QUESTION

The final system should eventually answer:

"What happened?"

"Is it unusual?"

"Compared with what?"

"Why is it unusual?"

"Is the cause related to the employee, task complexity, workload,
dependency, approval process, or another factor?"

"Is it a one-time event or persistent?"

"Is this an individual issue or a process bottleneck?"

"What should the manager investigate?"

The system provides operational intelligence and evidence. It does not
replace human managerial judgment.
