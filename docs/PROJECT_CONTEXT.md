# Project Context: AI-Powered Process Intelligence & Performance Analytics

Version: 3.0 (adds SOP-driven analysis; supersedes v2.0)
Status: **Phase 1 complete + SOP layer (schema v1.2)** on synthetic data. No ML or LLM yet.
Last updated: 2026-10-14

Purpose: give an AI coding agent or a new developer everything needed to understand, run, verify
and extend this project without re-reading the conversation history. The requirements sources are:
- `docs/process_intelligence_phase1_context.md` (Phase 1 brief)
- `corporate_sops/SOP_SCHEMA.md` (SOP standard v1.2, including the stage sequence in §11)
- the v1.0 "AI Agent Context File" (full multi-phase vision, not stored in this repo)

---

## 1. Objective (unchanged)

Analyze workflow data from an organizational platform with the hierarchy
`Executor -> Incharge -> Lead -> HOD` in order to:
1. Read each task type's SOP and understand what it requires (steps, approvals, dependencies, time standards).
2. Reconstruct how each ticket actually flowed (process mining).
3. Measure time, waiting, rework, workload and SLA, and compare them with the SOP and with history.
4. Detect meaningful deviations: from the SOP (conformance) and from contextual baselines (statistics).
5. Explain each deviation with evidence: likely causes, the SOP step or control involved, process vs individual.
6. Later: ML predictions, LLM explanations, dashboard, live integration.

Non-negotiable principles:
- Deviations are **signals for managerial investigation**, never performance judgments.
  Never output "underperforming" or rank employees best-to-worst.
- Deterministic code computes all metrics. ML/LLM are added later and never calculate core metrics.
- Every insight is traceable to source ticket/event IDs, a versioned baseline and a hashed SOP version.
- Raw data and SOP standard times are never modified to fit results; no record is silently dropped.
- Simple, explainable methods before complex models.

---

## 2. Pipeline sequence (fixed order)

| # | Stage | What happens | Main outputs |
|---|---|---|---|
| 1 | **Read SOPs** | Parse YAML front matter of SOP-013..021; validate against schema v1.2 and `task_types.csv`; list legacy SOP-001..012 without parsing | `sop_validation_report.csv` |
| 2 | **Understand parameters** | Complexity score CS-v1, derived complexity, expected effort / elapsed time with P10-P90 band (PERT, parallel dependencies via Clark max) | `sop_parameters.csv` |
| 3 | **Read the logs** | Validate raw data, normalize events, reconstruct lifecycles | `data_quality_report.csv`, `ticket_lifecycles.csv`, `process_transitions.csv` |
| 3b | **SOP-log correspondence gate** | Replay every ticket on its SOP's process model (departments, roles, approval stages and order, rejection detectors, holds, rework loop, closure); cross-fit each task type against all SOPs by path and time scale; exclude SOPs whose logs are a different process | `sop_log_correspondence.csv`, `sop_crossfit.csv` |
| 4 | **Analyse time and complexity** | Ticket features, historical baselines, WIP-adjusted hold, SOP band per ticket, SOP vs actual per task type, effort coverage, CS vs observed Spearman rho, employee/team metrics | `ticket_features.csv`, `baselines.csv`, `sop_time_complexity.csv`, `sop_effort_coverage.csv`, metrics |
| 5 | **Check deviations** | Per-ticket SOP conformance C1-C7; SOP process deviations; statistical deviations (ticket, employee, process) | `conformance.csv` (+ deviation rows) |
| 6 | **Find reasons** | Rank causes; link to SOP steps, rework controls and clauses; classify process / rework / sop_standard / platform_logging / individual_signal | `deviations.csv` |
| 7 | **Report** | One-page plain-language summary, technical report in stage order, full deviation report, run manifest with hashes | `demo_report.md`, `technical_report.md`, `deviation_report.md`, `run_manifest.json` |

Corrections to the originally requested order: reading the logs (stage 3) must come before "analyse time"
and "check deviations", because both compare SOP expectations with what the logs show; and stage 3b confirms
that each log *is* the process its SOP describes before any SOP comparison is made.

---

## 3. Current results (synthetic data, 1,200 tickets, 2026-06-01..2026-09-25)

| Area | Result |
|---|---|
| SOPs | 9 schema SOPs valid (0 errors); 9 warnings = FPY provenance `unconfirmed`; 12 legacy SOPs listed |
| SOP-log correspondence | **9/9 `corresponds`**: 100% of tickets replay on their SOP model, 0 structural mismatches, time scale closest to the labelled SOP for every task type; logs never fit another department's SOP |
| Complexity | 9/9 derived = declared; **Spearman rho (CS vs observed median elapsed) = 0.95** |
| Data quality | 60 checks, 0 errors, 3 warnings (approval count mismatch DQ057-type, undeclared DependencyWait, no absence data) |
| Verification | 1,200/1,200 durations reconcile; 10/10 tickets independently recomputed from raw CSV match |
| SOP time band | 28% within P10-P90; 59% below P10 (illustrative standards high for 8 task types); above P90 mainly Leave (52%) and Expense (36%), driven by first-decision waits |
| Effort coverage | 31/36 task-type-months `standard_exceeds_hold` (SOP executor effort above observed upper bound) |
| Conformance | mean path fitness 0.90; all **retrospective** (SOPs effective after the data period) |
| Deviations | **94** total: 30 process-level, 5 employee-level, 59 ticket-level |

Key findings:
- **Correspondence caveats:** Expense and Leave logs resemble SOP-015 / SOP-021 by path (because of holds their own SOPs forbid), Vendor Onboarding resembles SOP-014 (missing HOD), and Daily Ops cannot be told apart from SOP-019 by path; in every case the time scale identifies the labelled SOP.
- **Platform logging gap:** HOD approval required by SOP-017 is never logged (0 HOD events in 1,200 tickets) -> 145 Vendor Onboarding tickets C1 `fewer`.
- **Routing rule not applied:** every Daily Operations Report gets an Incharge approval although SOP-018 requires one only on a KPI breach / safety event.
- **Holds on dependency-free tasks:** 358 tickets (Expense, Leave, Daily Ops) log DependencyWait although their SOPs forbid holds.
- **Approval bottleneck:** Finance and HR Incharge decision waits 1.46x / 1.36x the org median, and above the SOP standard.
- **Rework:** 36 of 59 slow tickets dominated by rework, each linked to its SOP preventing control; 5 task types have rejection rates >= 1.25x the SOP expectation.
- **Persistent individual signals:** E1001, E1002, E1014 unexplained processing increase (manager review); E1013 explained by doubled workload.
- **Operations SLA** fell 96.3% -> 88.7% over three months.

---

## 4. Tech stack and how to run

| Component | Choice | Notes |
|---|---|---|
| Language | Python 3.12 | |
| Data processing | pandas 2.1, numpy 1.26 | pandas 2.1: do NOT use `groupby.apply(..., include_groups=...)` |
| SOP parsing | PyYAML (`yaml.safe_load`) | Front matter only |
| Tests | pytest | 68 tests |
| Storage | CSV + Markdown + JSON manifest | No database yet |
| ML / LLM / API / dashboard | none | Deliberately out of scope so far |

```bash
pip install -r requirements.txt
python run_pipeline.py      # ~8 s; rewrites outputs/ and data/processed/
python -m pytest -q         # 68 passed (~1 min; three full pipeline runs)
```

---

## 5. Directory structure

```
process_intelligence_phase1_demo/
├── README.md                         Dataset notes
├── requirements.txt                  pandas, numpy, pyyaml, pytest
├── run_pipeline.py                   Entry point: process_intel.pipeline.run()
│
├── data/
│   ├── raw/                          INPUT, read-only (hash-checked by the end-to-end test)
│   │   ├── employees.csv  tickets.csv  audit_logs.csv  task_types.csv
│   └── processed/                    INTERMEDIATE, rewritten every run
│       ├── events_normalized.csv  events_quarantined.csv  lifecycle_segments.csv
│
├── corporate_sops/                   INPUT
│   ├── README.md                     Legacy vs schema SOPs
│   ├── SOP_SCHEMA.md                 SOP standard v1.2 (fields, formulas, checks, sequence)
│   ├── SOP-013 .. SOP-021_*.md       Schema SOPs, one per task type (YAML + ISO 9001 body)
│   └── SOP-001 .. SOP-012_*.md       Legacy free text, not parsed
│
├── docs/
│   ├── PROJECT_CONTEXT.md            THIS FILE
│   ├── process_intelligence_phase1_context.md   Phase 1 brief
│   ├── data_contract.md              Raw inputs + SOP inputs, privacy classes
│   └── assumptions.md                Numbered assumptions A1-A29
│
├── process_intel/
│   ├── config.py                     Paths, vocabularies, ALL thresholds and weights
│   ├── sop.py                        Stages 1-2: load, validate, CS, priors
│   ├── ingestion.py                  Stage 3: load raw + validate
│   ├── normalization.py              Stage 3: canonical events + quarantine
│   ├── lifecycle.py                  Stage 3: lifecycle reconstruction
│   ├── correspondence.py             Stage 3b: SOP-log correspondence gate
│   ├── features.py                   Stage 4: ticket features
│   ├── baselines.py                  Stage 4: historical baselines
│   ├── wip.py                        Stage 4: WIP-adjusted executor hold
│   ├── sop_analysis.py               Stage 4: SOP vs actual, effort coverage, rho
│   ├── metrics.py                    Stage 4: employee + team metrics
│   ├── conformance.py                Stage 5: per-ticket checks C1-C7
│   ├── sop_deviations.py             Stage 5: SOP-based process deviations
│   ├── deviations.py                 Stage 5: statistical deviations (+ baseline cause ranking)
│   ├── root_cause.py                 Stage 6: reasons, SOP references, controls
│   ├── report.py                     Stage 7: summary, technical + deviation reports, verification
│   └── pipeline.py                   Orchestration in stage order, manifest
│
├── tests/
│   ├── conftest.py  test_normalization.py (7)  test_lifecycle.py (7)  test_analytics.py (12)
│   ├── test_sop.py (18)  test_wip.py (5)  test_conformance.py (7, incl. end-to-end)
│   ├── test_correspondence.py (12, incl. pipeline exclusion of a wrong SOP)
│
└── outputs/                          RESULTS, rewritten every run (list in §8)
```

---

## 6. Inputs

### 6.1 Raw data (full spec: `docs/data_contract.md`)
| File | Rows | Key | Notes |
|---|---|---|---|
| employees.csv | 36 | employee_id | 4 departments x (6 Executors, Incharge, Lead, HOD) |
| tickets.csv | 1,200 | ticket_id | SLA: due = created + 6h (High) / 12h (Medium) / 24h (Low) |
| audit_logs.csv | 7,429 | event_id | Actions: Created, Assigned, Updated, Submitted, Rejected, Resubmitted, DependencyWait, Approved |
| task_types.csv | 9 | task_type | complexity, sop_steps, approval_count, dependency_count |

### 6.2 SOPs (spec: `corporate_sops/SOP_SCHEMA.md`)
One schema SOP per task type (SOP-013..021, version 1.1.0, schema 1.2). YAML front matter carries:
document control, SLA, `sop_steps`, approval matrix (base/max, conditions), dependencies with
`parallel_group`, complexity drivers, steps (role, type, audit actions, three-point effort and queue
times, skill level), rework triggers mapped to the 4 platform rejection reasons with `preventable_by`
controls, expected first-pass yield, exceptions. Standard times: `illustrative_expert_estimate`;
quality targets: `unconfirmed`. Effective date 2026-10-14 (after the data period).

---

## 7. Module specifications

### 7.1 `config.py`
Single source for paths, vocabularies, thresholds and weights. Never hard-code values elsewhere.

| Group | Names (values) |
|---|---|
| Paths | `RAW_DIR`, `PROCESSED_DIR`, `OUTPUT_DIR`, `SOP_DIR` |
| Vocabularies | `REQUIRED_COLUMNS`, `ROLE_LEVELS`, `COMPLEXITY_LEVELS`, `PRIORITY_LEVELS`, `COMPLETED_STATUSES`, `EVENT_TYPE_MAP` (+aliases) |
| SOP | `SOP_SCHEMA_VERSION` "1.2", `SOP_FILE_GLOB` "SOP-*.md", `SLA_HOURS`, `PLATFORM_REJECTION_REASONS` (4) |
| Complexity | `CS_VERSION` "CS-v1", `CS_WEIGHTS` (steps 1.0, appr_base 2.0, appr_cond 1.0, dep 2.5, decision 1.5, driver 1.0, exception 0.5, skill 1.0), `CS_BANDS` (12, 20), `Z_P10_P90` 1.2816 |
| Effort coverage | `EFFORT_COVERAGE_MIN_N` 20, `EFFORT_COVERAGE_HIGH` 1.0, `EFFORT_COVERAGE_LOW` 0.5 |
| SOP deviations | `CONFORMANCE_MIN_SHARE` 0.05, `CONFORMANCE_MIN_N` 5, `SOP_BAND_TAIL_SHARE` 0.20, `REWORK_SOP_MULTIPLIER` 1.25, `REWORK_SOP_MIN_COUNT` 5 |
| Baselines | `BASELINE_VERSION` "BL-v1", `MIN_BASELINE_N` 20 |
| Statistical deviations | `DURATION_RATIO_THRESHOLD` 1.75, `DURATION_RATIO_HIGH` 2.5, `DOMINANT_SHARE_*` 0.6/0.4, `PERSIST_*` (M, 5, 1.25, 2, 1.2), `CONTEXT_*` (1.3, 0.10, 0.15), `REJECTION_RATE_MULTIPLIER` 2.0, `REJECTION_MIN_COUNT` 4, `BOTTLENECK_*` (20, 1.3, 2.0) |

All are demonstration values for synthetic data. The run manifest records every numeric threshold.

### 7.2 `sop.py` (stages 1-2)
- `load_sops(sop_dir) -> list[dict]`: one record per `SOP-*.md`: `sop_id, file, sha256, format (schema|legacy), parse_error, data, body`. Parse errors are recorded, never raised.
- `validate_sops(records, task_types) -> (report, valid)`: ~37 checks per SOP (required fields, enums, step well-formedness incl. string-only lists, three-point ordering, skill levels, task_type/department/complexity/sop_steps/dependency_count vs `task_types`, approval base/max vs matrix, matrix stages have approval steps, dependencies listed and well-formed, `parallel_group` present, SLA vs due rule, rework reasons in platform vocabulary, `detected_at` is an approval step, FPY range, supersedes exist, times frozen before effective date, provenance confirmed, body present, derived vs declared complexity) plus registry checks (one active SOP per task type; every task type has one). SOPs with an error are excluded from `valid`.
- `complexity_score(d) -> dict`: CS-v1 total, derived label, per-term contributions.
- `pert(tp)`, `clark_max(m1, v1, m2, v2)`: three-point estimate; mean/variance of max of two normals.
- `ticket_prior(sops, task_type, approval_count, dependency_count) -> dict`: schema §7.1-7.2 for a routing; cached by SOP SHA-256. Returns `required_approvals, required_stages, e_effort_exec_h, e_effort_h, e_wait_h, e_elapsed_h, sd_h, p10_h, p90_h, exp_queue_h, exp_first_decision_h, exp_lead_decision_h, exp_hod_decision_h, estimate_flags` (`drivers_missing`, `approval_route_from_ticket`).
- `sop_parameters(sops, task_types) -> DataFrame`: one row per SOP at the task type's declared routing.
- `rework_trigger_map(sops)`: `(task_type, reason.lower()) -> trigger + sop_id`.

### 7.3 `ingestion.py` (stage 3)
`load_raw()` reads the 4 CSVs as strings. `validate()` returns 60 checks (profiles, required columns, missing
values, uniqueness, timestamps, foreign keys, hierarchy, ticket vs task_types, status vs due date, action
vocabulary, stages, event span vs completion, ordering, rejection reasons present, approvals vs
approval_count, DependencyWait vs dependency_count, absence data). SOP checks moved to `sop.py`.

### 7.4 `normalization.py` (stage 3)
`normalize_events(audit, employees) -> (events, quarantine)`: canonical event types (unknown -> `UNKNOWN`,
kept), raw values preserved, `rejection_reason` vs `comments` split, statuses upper-cased, department/role
joined (unknown employee -> `UNKNOWN`), duplicates and untimed events quarantined with a reason, sorted by
`ticket_id, timestamp, event_id`.

### 7.5 `lifecycle.py` (stage 3)
`reconstruct_ticket`, `reconstruct_all`, `transition_summary`. Interval category = state entered at the
first event (CREATED queue; ASSIGNED/REASSIGNED/REOPENED processing; UPDATED processing or rework inside a
rejection cycle; REJECTED rework; SUBMITTED/RESUBMITTED/ESCALATED/non-final APPROVED approval_wait;
DEPENDENCY_WAIT dependency_wait). `waiting_on` = stage of the next APPROVED/REJECTED. Sum of category hours
= lifecycle span (tested).

### 7.5b `correspondence.py` (stage 3b)
- `replay(events, ticket_department, model) -> (status, issues)`: state machine over intake, work, review, rework and closed phases; `fits` / `fits_with_known_deviations` (C1 count, forbidden hold, unmapped reason) / `does_not_fit` (department, role, stage not in SOP, order, detector, foreign activity, no closing approval).
- `evaluate(features, events, sops) -> (per_ticket, verdicts, crossfit)`: replays every ticket on every SOP; per task type reports fits / known / not fit, correspondence, own and best-other path score, time ratio (SOP time excludes stages never logged), closest SOP by time, known deviation counts, structural mismatches, verdict, notes.
- Verdict: `does_not_correspond` if correspondence < 0.80, time ratio outside [0.25, 4], or another SOP is at least as good by path and closer by time; `corresponds` if >= 0.95 and time identifies the labelled SOP; else `partial`. Excluded SOPs are removed from stages 4-6; `conformance_mode = sop_excluded_no_correspondence`; deviation `SOP_LOG_MISMATCH`.

### 7.6 `features.py`, `baselines.py`, `metrics.py` (stage 4)
- Features: durations (`total_duration_h`, `processing_time_est_h`, `executor_processing_h`, waits, `pre_decision_wait_h`), counts, SLA, ratios, `dependency_wait_undeclared`.
- Baselines: L2 task_type+complexity+priority (n >= 20) else L1; median/P25/P75/P90/MAD and component medians; `attach_baselines` adds `expected_*`, `duration_ratio`, `processing_ratio` (rework excluded), `above_p90`; `build_stage_baselines` per stage x dependency_count.
- Metrics: employee and team per week/month/overall; workload = `expected_effort_h` (sum of baseline medians).

### 7.7 `wip.py` (stage 4)
`wip_adjusted_hold(segments, tickets) -> Series`: per executor, processing+rework segments split across
concurrently held tickets; holder = `assigned_employee_id`. Properties tested: adjusted <= raw; per-executor
sum = union length; equals raw without overlap.

### 7.8 `sop_analysis.py` (stage 4)
- `attach_sop_priors(f, sops, wip_hold)`: adds `sop_id, sop_version, sop_expected_elapsed_h, sop_p10_h, sop_p90_h, sop_effort_exec_h, sop_exp_queue_h, sop_exp_first_decision_h, sop_exp_lead_decision_h, sop_required_approvals, sop_required_stages, sop_estimate_flags, sop_elapsed_ratio, sop_band (within/below_p10/above_p90/n/a), executor_hold_wip_adj_h`.
- `effort_coverage(f)`: task type x month; rows with n < 20 kept and flagged `insufficient_n`.
- `task_type_analysis(f, params, coverage)`: SOP vs actual per task type (elapsed, tails, components, coverage, rejection rate).
- `cs_rank_correlation(table)`: Spearman rho (ranked Pearson, no scipy).

### 7.9 `conformance.py` (stage 5)
`check_ticket(...)` / `check_all(features, events, sops)`: C1 approvals (ok/fewer/more), C2 order, C3
DependencyWait on 0-dependency task (none/expected_exception/undeclared), C4 required actions, C5 rework
cycles vs max without escalation, C6 rejection reasons mapped to rework triggers (ok/unmapped/n/a), C7 SOP
band. `fitness` = passing C1-C6 / evaluated. `conformance_mode` = retrospective if created before the SOP's
effective date, else in_force. Also records required vs observed approval stages, trigger codes and
`preventable_by`.

### 7.10 `sop_deviations.py` (stage 5, detection only)
| Type | Rule |
|---|---|
| `SOP_NONCONFORMANCE` | per task type x check x failing value: >= 5 tickets and >= 5% share |
| `SOP_ELAPSED_ABOVE_STANDARD` / `_BELOW_STANDARD` | > 20% of a task type's tickets above SOP P90 / below P10 (10% expected) |
| `SOP_EFFORT_STANDARD` | same non-plausible coverage flag in every eligible month |
| `REWORK_ABOVE_SOP_EXPECTATION` | rejection rate >= 1.25 x (1 - FPY) and >= 5 rejected tickets |

### 7.11 `deviations.py` (stage 5, statistical)
`TICKET_DURATION` (ratio >= 1.75, excess time ranked by component), `APPROVAL_STAGE_BOTTLENECK` (dept vs
org decision wait within the same dependency count, >= 1.3x), `SLA_DETERIORATION` (3 consecutive monthly
falls, >= 5 pts), `PERSISTENT_*_PROCESSING_INCREASE` (last 2 months >= 1.25x and >= 1.2x own history, then
context checks), `ELEVATED_REJECTION_RATE` (>= 2x peers, >= 4 rejected).

### 7.12 `root_cause.py` (stage 6)
`attach_reasons(devs, f, conf, sops, events)` adds `sop_id, sop_reference, preventable_by, reason_source`
and fills causes:
- C1 fewer -> `platform_logging` if the stage is never logged anywhere, else skipped approval.
- C1 more -> conditional approval applied by default; condition drivers missing.
- C3 undeclared -> two competing hypotheses (hold instead of rejection; reviewer queue logged as hold), confidence low.
- Elapsed band -> component medians actual vs SOP (queue, first decision, Lead decision, WIP-adjusted hold in aggregate), ranked by gap; below-band -> `sop_standard`.
- Effort standard -> standard too high / work outside window (or the reverse), confidence low.
- Rework vs SOP -> rejection reasons ranked with detection step and preventing control.
- Statistical rows: ticket rows gain SOP band + first-decision comparison and the preventing control for rework; rejection-rate rows gain controls; bottlenecks gain the SOP first-decision standard; employee rows note that SOP effort is never compared per employee.

### 7.13 `report.py` (stage 7)
`write_summary` (one-page manager summary in plain language, generated from the same outputs),
`write_report` (technical report in stage order, worked examples A/B/C, verification of 10 tickets, limitations),
`write_deviation_report` (every deviation: entity, severity/classification/confidence, measurement,
comparison basis, explanation, reason, ranked causes, SOP reference, preventable-by, recommendation, source
records, collapsible evidence JSON), `verify_tickets` (independent recomputation from raw CSV).

### 7.14 `pipeline.py`
`run(raw_dir, processed_dir, output_dir, sop_dir)` executes stages 1-7 in order, logs to console and
`pipeline_run.log`, enforces the canonical `deviations.csv` column order, writes `run_manifest.json`.

---

## 8. Outputs

Hours are calendar hours. Multi-valued ids are pipe-separated.

| File | Stage | Grain (rows) | Key columns |
|---|---|---|---|
| `sop_validation_report.csv` | 1 | check (337) | check_id, sop_id, check, severity, status, details |
| `sop_parameters.csv` | 2 | SOP (9) | sop_id, sop_version, task_type, cs + cs_* terms, complexity_derived/declared/match, sop_steps, approval base/max, dependency_count, decision_points, expected_first_pass_yield, expected_rejection_rate, required_stages, e_effort_exec_h, e_effort_h, e_wait_h, e_elapsed_h, sd_h, p10_h, p90_h, exp_queue_h, exp_first/lead/hod_decision_h, estimate_flags, sha256, file |
| `data_quality_report.csv` | 3 | check (60) | check_id, dataset, check, severity, status, affected_rows, details, example_ids |
| `sop_log_correspondence.csv` | 3b | task type (9) | sop_id, tickets, fits, fits_with_known_deviations, does_not_fit, correspondence, path_score_own, best_other_sop_by_path, path_score_best_other, observed_median_h, sop_expected_elapsed_h, time_ratio_own, closest_sop_by_time, known_deviation_counts, structural_mismatches, verdict, notes |
| `sop_crossfit.csv` | 3b | task type x SOP (81) | path_score, share_not_fit, time_ratio, time_distance |
| `ticket_lifecycles.csv` | 3 | ticket (1,200) | sequence, stages, transitions, handoffs, closure, counts, hours by category and approver stage, rejection_reasons, anomalies, source_event_ids |
| `process_transitions.csv` | 3 | event pair (14) | frequency, median_h, p90_h, total_h, share_of_tickets |
| `ticket_features.csv` | 4 | ticket (1,200) | attributes, durations, counts, SLA, baseline comparison, `duration_flag`, SOP columns (§7.8), `executor_hold_wip_adj_h` |
| `baselines.csv` / `stage_baselines.csv` | 4 | group (36) / stage x deps (5) | as in v2.0 |
| `sop_time_complexity.csv` | 4 | task type (9) | cs, complexity, observed median/P90, SOP expected + band, tail shares, component actual vs SOP, WIP-adjusted hold vs SOP effort, effort_coverage_overall, coverage_months_flagged, rejection observed vs SOP, quality_targets_source |
| `sop_effort_coverage.csv` | 4 | task type x month (36) | n, median_wip_adj_hold_h, median_raw_hold_h, sop_effort_exec_h, effort_coverage, coverage_flag |
| `employee_metrics.csv` / `team_metrics.csv` | 4 | employee/department x period (505 / 88) | as in v2.0 |
| `conformance.csv` | 5 | ticket (1,200) | sop_id, sop_version, conformance_mode, c1..c7, fitness, required/observed approval stages, rework_trigger_codes, preventable_by, correspondence_status, correspondence_issues |
| `deviations.csv` | 6 | deviation (94) | deviation_id, level, entity_id, department, employee_id, deviation_type, severity, metric, observed, expected, ratio, baseline_id, sop_id, classification, dominant_cause, confidence, candidate_causes (JSON), evidence (JSON), sop_reference, preventable_by, reason_source, recommended_investigation, source_ticket_ids, source_event_ids, explanation |
| `demo_report.md` | 7 | - | One-page manager summary: at a glance, main findings, where time goes, next steps |
| `technical_report.md` | 7 | - | Full technical report in stage order (tables, methods, worked examples, verification) |
| `deviation_report.md` | 7 | - | Every deviation with all details |
| `run_manifest.json` | 7 | - | run time, versions (BL-v1, CS-v1, schema 1.2), raw and SOP SHA-256, SOPs used, row counts, rho, thresholds |
| `pipeline_run.log` | all | - | stage log |

`classification` values: process, rework, executor_processing, individual_signal, context_explained,
mixed, sop_standard, platform_logging, sop_mismatch.

---

## 9. Tests (68)

| File | Covers |
|---|---|
| test_normalization.py (7) | mapping + aliases, raw preservation, ordering, tie-break, duplicate/timestamp quarantine, unknown employee |
| test_lifecycle.py (7) | durations and attribution, single event, multiple rejections, reopen, reassignment/escalation, missing events, multi-ticket |
| test_analytics.py (12) | duration, SLA, robust baselines, fallback, ticket deviation attribution, persistence rules, team-wide context, validation, weighted effort |
| test_sop.py (18) | repo SOPs valid, legacy listed, CS for all 9 task types, PERT, Clark max, parallel < sequential, conditional approval routing, band ordering, validation catches errors, broken YAML reported |
| test_wip.py (5) | no overlap, overlap split + union, separate executors, categories, zero hold |
| test_correspondence.py (12) | matching path fits; forbidden hold and missing approval are known deviations; other-process paths do not fit (stage not in SOP, other department, wrong detector, approval before submission, intake order, wrong actor role); all repo SOPs correspond and time identifies them; logs never fit another department's SOP; relabelled wrong SOP rejected; **pipeline excludes a Lead-approval SOP that passes stage 1** |
| test_conformance.py (7) | conformant path, HOD missing, unrequired approval + undeclared hold, reason -> control, unknown reason + missing action, retrospective vs in_force, **end-to-end 7-stage run** (all outputs exist, every deviation has a reason, HOD finding is platform_logging, manifest, raw files unchanged, no "underperform") |

---

## 10. Known data issues and key assumptions

Full list: `docs/assumptions.md` (A1-A29). Most important:
1. Processing vs waiting is **estimated**; WIP-adjusted hold is still an upper bound on effort.
2. The DependencyWait interval mixes dependency and reviewer wait; first-decision comparisons use the full submission-to-decision wait.
3. SOP standard times and FPY are illustrative/unconfirmed; SOP-vs-actual gaps are findings for the SOP owner, never a reason to edit times.
4. SOPs took effect after the data period -> all conformance is retrospective.
5. No complexity-driver values in the export -> estimates use base effort and route conditional approvals from `approval_count`.
6. HOD approvals never logged; approval_count=0 tasks still approved.
7. No leave/absence data. Baselines in-sample. Thresholds are demo values.

---

## 11. How to extend

- **New SOP:** copy a schema SOP, keep `task_type` exact, quote names/list items containing commas, run the pipeline and read `sop_validation_report.csv`. Bump `version` on any YAML change.
- **Recalibrate SOP times:** only as a new SOP version with `standard_time_source: historical_calibration`, fitted on an earlier period and evaluated on a later one.
- **New platform action:** alias in `EVENT_TYPE_MAP`; new canonical type needs a rule in `lifecycle._state_after` + test.
- **New conformance check:** add to `conformance.check_ticket` and `CHECK_COLUMNS`, add its reason handler in `root_cause._nonconformance`, add tests.
- **New detector:** return rows with the `deviations.csv` columns (stage 5), add reasons in `root_cause` (stage 6), add positive and negative tests.
- **Thresholds/weights:** only in `config.py`; bump `BASELINE_VERSION` / `CS_VERSION` when methods change.
- Language: "deviation requiring review"; never "underperforming"; no rankings. Per-employee SOP effort comparison is not allowed.

---

## 12. Roadmap

| Order | Work | Done when | Blocked on |
|---|---|---|---|
| 1 | Confirm SOP provenance and recalibrate out-of-sample | `quality_targets_source` confirmed; historical_calibration version fitted on Jun-Jul, evaluated on Aug-Sep | SOP owner |
| 2 | Phase 1 hardening: threshold sensitivity table; out-of-sample baselines; per-run output folders | findings stable across thresholds | mentor review |
| 3 | Platform data requests: complexity drivers, HOD approval events, dependency-resolved event, leave data | export carries them; drivers_missing flag disappears | platform team |
| 4 | LLM explanation layer over `deviations.csv` evidence (ids only, prompt versioned, numbers verified) | 100% of numbers in LLM text verifiable | API approval |
| 5 | Dashboard with role-based views (no rankings) | navigate department -> deviation -> ticket events | none |
| 6 | ML: expected elapsed time vs SOP prior and median baseline (time-based split) | ML beats both, explainably | ideally real data |
| 7 | Real data integration (exports, then read-only polling with checkpoint) | pipeline runs on company exports | data access |

---

## 13. Engineering rules (carry forward)

1. Inspect actual data before assuming schema. 2. Preserve raw data; never silently drop records.
3. Deterministic analytics separate from ML and LLM. 4. LLM never calculates metrics or invents evidence.
5. Every insight has evidence and source ids. 6. Account for complexity, workload, dependencies, leave (when available).
7. Distinguish process bottlenecks, platform logging gaps and SOP-standard issues from individual signals.
8. A deviation is a signal, not a verdict. 9. Prefer simple methods; add ML only if it beats simple baselines.
10. Test lifecycle and conformance logic. 11. Document assumptions; version baselines, scores, SOPs and prompts.
12. Never edit SOP standard times to fit the data. 13. Keep the analytics system decoupled from the production platform.
