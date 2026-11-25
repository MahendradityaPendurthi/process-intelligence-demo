# Deviation Report

_357 deviations from `outputs/deviations.csv`, in pipeline order (process, employee, ticket). Each is a signal for investigation, not a judgment._

| level | deviation_type | count |
|---|---|---|
| employee | PERSISTENT_PROCESSING_INCREASE_WITH_CONTEXT | 2 |
| employee | PERSISTENT_UNEXPLAINED_PROCESSING_INCREASE | 1 |
| process | APPROVAL_WAIT_INCREASE | 5 |
| process | REWORK_ABOVE_SOP_EXPECTATION | 1 |
| process | SOP_EFFORT_STANDARD | 7 |
| process | SOP_ELAPSED_ABOVE_STANDARD | 4 |
| process | SOP_ELAPSED_BELOW_STANDARD | 4 |
| process | SOP_NONCONFORMANCE | 6 |
| ticket | TICKET_DURATION | 327 |

## Process and SOP-level deviations (27)

### `DEV-0001` SOP_NONCONFORMANCE

| field | value |
|---|---|
| Entity | Daily Operations Report:C1=more (Operations) |
| Severity / classification / confidence | high / process / medium |
| Measured | share of tickets with C1 = more: observed 1.0, expected 0.0, ratio nan |
| Compared with | SOP-018 v1.1.0 |
| What happened | 540 of 540 Daily Operations Report tickets (100%) fail C1 (more) against SOP-018. |
| Most likely reason | Incharge approval logged on every ticket although the SOP requires it only when 'kpi_breach == true or safety_event == true' |
| Ranked candidate causes | Incharge approval logged on every ticket although the SOP requires it only when 'kpi_breach == true or safety_event == true'; Routing condition cannot be verified: its drivers are not in the export |
| SOP reference | SOP-018 approval_matrix: Incharge (kpi_breach == true or safety_event == true) |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Check whether these tickets are routed for approval by default. Either configure the SOP condition on the platform or update the SOP. |
| Source records | 540 tickets: T00025, T00030, T00034, T00045, T00048, T00052, T00057, T00059, T00060, T00069 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Daily Operations Report",
  "check": "c1_approvals",
  "result": "more",
  "tickets": 540,
  "of": 540,
  "share": 1.0,
  "conformance_mode": {
    "retrospective": 540
  },
  "required_vs_observed_approvals": {
    "- vs Incharge": 540
  }
}
```
</details>

### `DEV-0002` SOP_NONCONFORMANCE

| field | value |
|---|---|
| Entity | Daily Operations Report:C3=undeclared (Operations) |
| Severity / classification / confidence | high / process / low |
| Measured | share of tickets with C3 = undeclared: observed 0.58, expected 0.0, ratio nan |
| Compared with | SOP-018 v1.1.0 |
| What happened | 313 of 540 Daily Operations Report tickets (58%) fail C3 (undeclared) against SOP-018. |
| Most likely reason | Ticket put on hold where the SOP requires rejection for missing information |
| Ranked candidate causes | Ticket put on hold where the SOP requires rejection for missing information; Reviewer queue time logged as DependencyWait (median hold 1.19h; first-decision wait 1.70h vs SOP 0.00h) |
| SOP reference | SOP-018 dependency_count: 0; procedure: 'This SOP has no external dependency' |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Ask Incharges and executors why these tickets are put on hold. If it is queue time, stop logging it as DependencyWait; if information is missing, reject with 'Required document missing'. |
| Source records | 313 tickets: T00034, T00045, T00059, T00069, T00076, T00098, T00118, T00126, T00174, T00201 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Daily Operations Report",
  "check": "c3_dependency_wait",
  "result": "undeclared",
  "tickets": 313,
  "of": 540,
  "share": 0.58,
  "conformance_mode": {
    "retrospective": 313
  },
  "required_vs_observed_approvals": {
    "- vs Incharge": 313
  }
}
```
</details>

### `DEV-0003` SOP_NONCONFORMANCE

| field | value |
|---|---|
| Entity | Expense Approval:C3=undeclared (Finance) |
| Severity / classification / confidence | high / process / low |
| Measured | share of tickets with C3 = undeclared: observed 0.587, expected 0.0, ratio nan |
| Compared with | SOP-016 v1.1.0 |
| What happened | 286 of 487 Expense Approval tickets (59%) fail C3 (undeclared) against SOP-016. |
| Most likely reason | Ticket put on hold where the SOP requires rejection for missing information |
| Ranked candidate causes | Ticket put on hold where the SOP requires rejection for missing information; Reviewer queue time logged as DependencyWait (median hold 2.25h; first-decision wait 2.76h vs SOP 0.89h) |
| SOP reference | SOP-016 dependency_count: 0; procedure: 'This SOP has no external dependency' |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Ask Incharges and executors why these tickets are put on hold. If it is queue time, stop logging it as DependencyWait; if information is missing, reject with 'Required document missing'. |
| Source records | 286 tickets: T00032, T00036, T00038, T00040, T00093, T00095, T00127, T00155, T00169, T00175 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Expense Approval",
  "check": "c3_dependency_wait",
  "result": "undeclared",
  "tickets": 286,
  "of": 487,
  "share": 0.587,
  "conformance_mode": {
    "retrospective": 286
  },
  "required_vs_observed_approvals": {
    "Incharge vs Incharge": 286
  }
}
```
</details>

### `DEV-0004` SOP_NONCONFORMANCE

| field | value |
|---|---|
| Entity | Leave Approval:C3=undeclared (HR) |
| Severity / classification / confidence | high / process / low |
| Measured | share of tickets with C3 = undeclared: observed 0.589, expected 0.0, ratio nan |
| Compared with | SOP-020 v1.1.0 |
| What happened | 314 of 533 Leave Approval tickets (59%) fail C3 (undeclared) against SOP-020. |
| Most likely reason | Ticket put on hold where the SOP requires rejection for missing information |
| Ranked candidate causes | Ticket put on hold where the SOP requires rejection for missing information; Reviewer queue time logged as DependencyWait (median hold 1.63h; first-decision wait 2.10h vs SOP 0.80h) |
| SOP reference | SOP-020 dependency_count: 0; procedure: 'This SOP has no external dependency' |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Ask Incharges and executors why these tickets are put on hold. If it is queue time, stop logging it as DependencyWait; if information is missing, reject with 'Required document missing'. |
| Source records | 314 tickets: T00009, T00014, T00066, T00074, T00075, T00078, T00083, T00110, T00115, T00121 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Leave Approval",
  "check": "c3_dependency_wait",
  "result": "undeclared",
  "tickets": 314,
  "of": 533,
  "share": 0.589,
  "conformance_mode": {
    "retrospective": 314
  },
  "required_vs_observed_approvals": {
    "Incharge vs Incharge": 314
  }
}
```
</details>

### `DEV-0005` SOP_NONCONFORMANCE

| field | value |
|---|---|
| Entity | Purchase Request:C1=fewer (Procurement) |
| Severity / classification / confidence | medium / process / medium |
| Measured | share of tickets with C1 = fewer: observed 0.14, expected 0.0, ratio nan |
| Compared with | SOP-014 v1.1.0 |
| What happened | 66 of 473 Purchase Request tickets (14%) fail C1 (fewer) against SOP-014. |
| Most likely reason | Required Lead approval skipped |
| Ranked candidate causes | Required Lead approval skipped |
| SOP reference | SOP-014 approval_matrix: Lead (always) |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Confirm with the platform team whether Lead approval happens outside the system or is skipped (see data-quality finding DQ057). |
| Source records | 66 tickets: T03433, T03486, T03490, T03543, T03547, T03554, T03557, T03560, T03562, T03563 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Purchase Request",
  "check": "c1_approvals",
  "result": "fewer",
  "tickets": 66,
  "of": 473,
  "share": 0.14,
  "conformance_mode": {
    "retrospective": 66
  },
  "required_vs_observed_approvals": {
    "Incharge>Lead vs Incharge": 66
  }
}
```
</details>

### `DEV-0006` SOP_NONCONFORMANCE

| field | value |
|---|---|
| Entity | Vendor Onboarding:C1=fewer (Procurement) |
| Severity / classification / confidence | high / platform_logging / high |
| Measured | share of tickets with C1 = fewer: observed 1.0, expected 0.0, ratio nan |
| Compared with | SOP-017 v1.1.0 |
| What happened | 494 of 494 Vendor Onboarding tickets (100%) fail C1 (fewer) against SOP-017. |
| Most likely reason | Platform never logs HOD approvals (0 HOD approval events in all 4663 tickets) |
| Ranked candidate causes | Platform never logs HOD approvals (0 HOD approval events in all 4663 tickets) |
| SOP reference | SOP-017 approval_matrix: HOD (always) |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Confirm with the platform team whether HOD approval happens outside the system or is skipped (see data-quality finding DQ057). |
| Source records | 494 tickets: T00001, T00007, T00016, T00024, T00065, T00080, T00082, T00094, T00100, T00103 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Vendor Onboarding",
  "check": "c1_approvals",
  "result": "fewer",
  "tickets": 494,
  "of": 494,
  "share": 1.0,
  "conformance_mode": {
    "retrospective": 494
  },
  "required_vs_observed_approvals": {
    "Incharge>Lead>HOD vs Incharge>Lead": 494
  }
}
```
</details>

### `DEV-0007` SOP_ELAPSED_BELOW_STANDARD

| field | value |
|---|---|
| Entity | BOQ Review:below_p10 (Procurement) |
| Severity / classification / confidence | medium / sop_standard / medium |
| Measured | median elapsed h vs SOP expected: observed 4.98, expected 5.89, ratio 0.85 |
| Compared with | SOP-013 v1.1.0 E_elapsed |
| What happened | 34% of BOQ Review tickets finish below the SOP P10 (10% expected). Median actual 4.98h vs SOP expected 5.89h. |
| Most likely reason | executor hold, WIP-adjusted (upper bound on effort): actual 0.93h vs SOP 1.85h (-0.91h) |
| Ranked candidate causes | executor hold, WIP-adjusted (upper bound on effort): actual 0.93h vs SOP 1.85h (-0.91h) (47%); first-decision wait (incl. DependencyWait): actual 2.88h vs SOP 3.65h (-0.78h) (40%); intake queue: actual 0.08h vs SOP 0.34h (-0.26h) (13%) |
| SOP reference | SOP-013 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | SOP time standards look high for this task type. Review them with the SOP owner; recalibrate only as a new SOP version fitted on an earlier period (schema §3.1). |
| Source records | 184 tickets: T00017, T00097, T00109, T00129, T00160, T00172, T00176, T00207, T00231, T00239 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "BOQ Review",
  "tickets": 539,
  "share_in_tail": 0.341,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    4.57,
    5.89,
    7.21
  ],
  "observed_p10_p50_p90_h": [
    3.72,
    4.98,
    6.85
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.08,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      2.88,
      3.65
    ],
    "Lead decision wait": [
      0.0,
      0.0
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      0.93,
      1.85
    ]
  },
  "tickets_in_tail": 184,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0008` SOP_ELAPSED_ABOVE_STANDARD

| field | value |
|---|---|
| Entity | Daily Operations Report:above_p90 (Operations) |
| Severity / classification / confidence | high / process / high |
| Measured | median elapsed h vs SOP expected: observed 2.15, expected 1.34, ratio 1.61 |
| Compared with | SOP-018 v1.1.0 E_elapsed |
| What happened | 77% of Daily Operations Report tickets finish above the SOP P90 (10% expected). Median actual 2.15h vs SOP expected 1.34h. |
| Most likely reason | first-decision wait (incl. DependencyWait): actual 1.44h vs SOP 0.00h (+1.44h) |
| Ranked candidate causes | first-decision wait (incl. DependencyWait): actual 1.44h vs SOP 0.00h (+1.44h) (100%); 290 of 415 tickets carry a DependencyWait the SOP does not allow |
| SOP reference | SOP-018 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Investigate the dominant component. Waits point to the approval queue or holds; executor hold points to work content. |
| Source records | 415 tickets: T00030, T00034, T00045, T00048, T00059, T00069, T00076, T00098, T00118, T00174 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Daily Operations Report",
  "tickets": 540,
  "share_in_tail": 0.769,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    1.09,
    1.34,
    1.58
  ],
  "observed_p10_p50_p90_h": [
    1.31,
    2.15,
    4.46
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.08,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      1.44,
      0.0
    ],
    "Lead decision wait": [
      0.0,
      0.0
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      0.85,
      0.94
    ]
  },
  "tickets_in_tail": 415,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0009` SOP_ELAPSED_ABOVE_STANDARD

| field | value |
|---|---|
| Entity | Expense Approval:above_p90 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | median elapsed h vs SOP expected: observed 3.02, expected 1.82, ratio 1.67 |
| Compared with | SOP-016 v1.1.0 E_elapsed |
| What happened | 77% of Expense Approval tickets finish above the SOP P90 (10% expected). Median actual 3.02h vs SOP expected 1.82h. |
| Most likely reason | first-decision wait (incl. DependencyWait): actual 2.55h vs SOP 0.89h (+1.66h) |
| Ranked candidate causes | first-decision wait (incl. DependencyWait): actual 2.55h vs SOP 0.89h (+1.66h) (86%); executor hold, WIP-adjusted (upper bound on effort): actual 0.81h vs SOP 0.53h (+0.28h) (14%); 254 of 374 tickets carry a DependencyWait the SOP does not allow |
| SOP reference | SOP-016 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Investigate the dominant component. Waits point to the approval queue or holds; executor hold points to work content. |
| Source records | 374 tickets: T00032, T00036, T00040, T00093, T00095, T00127, T00145, T00146, T00155, T00169 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Expense Approval",
  "tickets": 487,
  "share_in_tail": 0.768,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    1.38,
    1.82,
    2.26
  ],
  "observed_p10_p50_p90_h": [
    1.84,
    3.02,
    5.84
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.08,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      2.55,
      0.89
    ],
    "Lead decision wait": [
      0.0,
      0.0
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      0.81,
      0.53
    ]
  },
  "tickets_in_tail": 374,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0010` SOP_ELAPSED_BELOW_STANDARD

| field | value |
|---|---|
| Entity | Incident Review:below_p10 (Operations) |
| Severity / classification / confidence | medium / sop_standard / high |
| Measured | median elapsed h vs SOP expected: observed 8.99, expected 10.41, ratio 0.86 |
| Compared with | SOP-019 v1.1.0 E_elapsed |
| What happened | 47% of Incident Review tickets finish below the SOP P10 (10% expected). Median actual 8.99h vs SOP expected 10.41h. |
| Most likely reason | executor hold, WIP-adjusted (upper bound on effort): actual 2.01h vs SOP 3.78h (-1.77h) |
| Ranked candidate causes | executor hold, WIP-adjusted (upper bound on effort): actual 2.01h vs SOP 3.78h (-1.77h) (61%); Lead decision wait: actual 1.22h vs SOP 1.74h (-0.52h) (18%); first-decision wait (incl. DependencyWait): actual 4.13h vs SOP 4.50h (-0.37h) (13%); intake queue: actual 0.08h vs SOP 0.34h (-0.26h) (9%) |
| SOP reference | SOP-019 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | SOP time standards look high for this task type. Review them with the SOP owner; recalibrate only as a new SOP version fitted on an earlier period (schema §3.1). |
| Source records | 266 tickets: T00010, T00012, T00020, T00049, T00085, T00086, T00099, T00104, T00106, T00108 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Incident Review",
  "tickets": 568,
  "share_in_tail": 0.468,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    8.84,
    10.41,
    11.98
  ],
  "observed_p10_p50_p90_h": [
    7.0,
    8.99,
    12.47
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.08,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      4.13,
      4.5
    ],
    "Lead decision wait": [
      1.22,
      1.74
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      2.01,
      3.78
    ]
  },
  "tickets_in_tail": 266,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0011` SOP_ELAPSED_ABOVE_STANDARD

| field | value |
|---|---|
| Entity | Invoice Verification:above_p90 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | median elapsed h vs SOP expected: observed 5.04, expected 5.12, ratio 0.98 |
| Compared with | SOP-015 v1.1.0 E_elapsed |
| What happened | 21% of Invoice Verification tickets finish above the SOP P90 (10% expected). Median actual 5.04h vs SOP expected 5.12h. |
| Most likely reason | first-decision wait (incl. DependencyWait): actual 5.82h vs SOP 3.40h (+2.42h) |
| Ranked candidate causes | first-decision wait (incl. DependencyWait): actual 5.82h vs SOP 3.40h (+2.42h) (95%); executor hold, WIP-adjusted (upper bound on effort): actual 1.44h vs SOP 1.32h (+0.12h) (5%) |
| SOP reference | SOP-015 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Investigate the dominant component. Waits point to the approval queue or holds; executor hold points to work content. |
| Source records | 105 tickets: T00347, T00700, T00779, T00993, T01037, T01064, T01086, T01147, T01376, T01406 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Invoice Verification",
  "tickets": 496,
  "share_in_tail": 0.212,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    3.78,
    5.12,
    6.46
  ],
  "observed_p10_p50_p90_h": [
    3.52,
    5.04,
    7.48
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.08,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      5.82,
      3.4
    ],
    "Lead decision wait": [
      0.0,
      0.0
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      1.44,
      1.32
    ]
  },
  "tickets_in_tail": 105,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0012` SOP_ELAPSED_ABOVE_STANDARD

| field | value |
|---|---|
| Entity | Leave Approval:above_p90 (HR) |
| Severity / classification / confidence | high / process / high |
| Measured | median elapsed h vs SOP expected: observed 2.22, expected 1.38, ratio 1.61 |
| Compared with | SOP-020 v1.1.0 E_elapsed |
| What happened | 71% of Leave Approval tickets finish above the SOP P90 (10% expected). Median actual 2.22h vs SOP expected 1.38h. |
| Most likely reason | first-decision wait (incl. DependencyWait): actual 2.01h vs SOP 0.80h (+1.21h) |
| Ranked candidate causes | first-decision wait (incl. DependencyWait): actual 2.01h vs SOP 0.80h (+1.21h) (80%); executor hold, WIP-adjusted (upper bound on effort): actual 0.51h vs SOP 0.20h (+0.31h) (20%); 265 of 378 tickets carry a DependencyWait the SOP does not allow |
| SOP reference | SOP-020 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Investigate the dominant component. Waits point to the approval queue or holds; executor hold points to work content. |
| Source records | 378 tickets: T00009, T00014, T00027, T00050, T00066, T00070, T00071, T00072, T00074, T00075 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Leave Approval",
  "tickets": 533,
  "share_in_tail": 0.709,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    0.95,
    1.38,
    1.81
  ],
  "observed_p10_p50_p90_h": [
    1.35,
    2.22,
    4.39
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.08,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      2.01,
      0.8
    ],
    "Lead decision wait": [
      0.0,
      0.0
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      0.51,
      0.2
    ]
  },
  "tickets_in_tail": 378,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0013` SOP_ELAPSED_BELOW_STANDARD

| field | value |
|---|---|
| Entity | Purchase Request:below_p10 (Procurement) |
| Severity / classification / confidence | medium / sop_standard / medium |
| Measured | median elapsed h vs SOP expected: observed 5.54, expected 6.22, ratio 0.89 |
| Compared with | SOP-014 v1.1.0 E_elapsed |
| What happened | 29% of Purchase Request tickets finish below the SOP P10 (10% expected). Median actual 5.54h vs SOP expected 6.22h. |
| Most likely reason | Lead decision wait: actual 0.86h vs SOP 1.56h (-0.69h) |
| Ranked candidate causes | Lead decision wait: actual 0.86h vs SOP 1.56h (-0.69h) (42%); first-decision wait (incl. DependencyWait): actual 2.60h vs SOP 3.07h (-0.47h) (28%); intake queue: actual 0.08h vs SOP 0.34h (-0.26h) (16%); executor hold, WIP-adjusted (upper bound on effort): actual 0.96h vs SOP 1.20h (-0.25h) (15%) |
| SOP reference | SOP-014 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | SOP time standards look high for this task type. Review them with the SOP owner; recalibrate only as a new SOP version fitted on an earlier period (schema §3.1). |
| Source records | 139 tickets: T00042, T00088, T00173, T00189, T00221, T00252, T00263, T00274, T00275, T00280 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Purchase Request",
  "tickets": 473,
  "share_in_tail": 0.294,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    4.95,
    6.22,
    7.5
  ],
  "observed_p10_p50_p90_h": [
    4.18,
    5.54,
    7.21
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.08,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      2.6,
      3.07
    ],
    "Lead decision wait": [
      0.86,
      1.56
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      0.96,
      1.2
    ]
  },
  "tickets_in_tail": 139,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0014` SOP_ELAPSED_BELOW_STANDARD

| field | value |
|---|---|
| Entity | Vendor Onboarding:below_p10 (Procurement) |
| Severity / classification / confidence | high / sop_standard / medium |
| Measured | median elapsed h vs SOP expected: observed 8.9, expected 11.97, ratio 0.74 |
| Compared with | SOP-017 v1.1.0 E_elapsed |
| What happened | 67% of Vendor Onboarding tickets finish below the SOP P10 (10% expected). Median actual 8.90h vs SOP expected 11.97h. |
| Most likely reason | executor hold, WIP-adjusted (upper bound on effort): actual 1.78h vs SOP 2.83h (-1.05h) |
| Ranked candidate causes | executor hold, WIP-adjusted (upper bound on effort): actual 1.78h vs SOP 2.83h (-1.05h) (58%); Lead decision wait: actual 1.17h vs SOP 1.65h (-0.48h) (26%); intake queue: actual 0.08h vs SOP 0.34h (-0.26h) (14%); first-decision wait (incl. DependencyWait): actual 4.79h vs SOP 4.83h (-0.03h) (2%) |
| SOP reference | SOP-017 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | SOP time standards look high for this task type. Review them with the SOP owner; recalibrate only as a new SOP version fitted on an earlier period (schema §3.1). |
| Source records | 333 tickets: T00007, T00016, T00065, T00080, T00094, T00100, T00103, T00105, T00111, T00124 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Vendor Onboarding",
  "tickets": 494,
  "share_in_tail": 0.674,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    9.86,
    11.97,
    14.08
  ],
  "observed_p10_p50_p90_h": [
    6.59,
    8.9,
    13.55
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.08,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      4.79,
      4.83
    ],
    "Lead decision wait": [
      1.17,
      1.65
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      1.78,
      2.83
    ]
  },
  "tickets_in_tail": 333,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0015` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | BOQ Review:effort_coverage (Procurement) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 1.62, expected 1.0, ratio 1.62 |
| Compared with | SOP-013 v1.1.0 E_effort_exec |
| What happened | BOQ Review: SOP executor effort 1.85h vs median WIP-adjusted hold 1.14h (coverage 1.62, flag standard_exceeds_hold) in all 12 eligible months. |
| Most likely reason | SOP executor effort standard too high (illustrative_expert_estimate) |
| Ranked candidate causes | SOP executor effort standard too high (illustrative_expert_estimate); Work done outside the ticket window (before Created or after Submitted) |
| SOP reference | SOP-013 v1.1.0 work-step effort_min (schema §8) |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Review the standard with the SOP owner or run a short time study. Do not edit standard times to match the data (schema §3.1). |
| Source records | - |

<details><summary>Evidence (JSON)</summary>

```json
{
  "flag": "standard_exceeds_hold",
  "months": {
    "2025-10": {
      "n": 48,
      "coverage": 1.61,
      "median_wip_adj_hold_h": 1.14
    },
    "2025-11": {
      "n": 53,
      "coverage": 1.81,
      "median_wip_adj_hold_h": 1.02
    },
    "2025-12": {
      "n": 40,
      "coverage": 1.84,
      "median_wip_adj_hold_h": 1.0
    },
    "2026-01": {
      "n": 33,
      "coverage": 1.63,
      "median_wip_adj_hold_h": 1.13
    },
    "2026-02": {
      "n": 46,
      "coverage": 1.68,
      "median_wip_adj_hold_h": 1.1
    },
    "2026-03": {
      "n": 42,
      "coverage": 1.6,
      "median_wip_adj_hold_h": 1.15
    },
    "2026-04": {
      "n": 40,
      "coverage": 1.45,
      "median_wip_adj_hold_h": 1.27
    },
    "2026-05": {
      "n": 42,
      "coverage": 1.54,
      "median_wip_adj_hold_h": 1.2
    },
    "2026-06": {
      "n": 53,
      "coverage": 1.95,
      "median_wip_adj_hold_h": 0.95
    },
    "2026-07": {
      "n": 41,
      "coverage": 1.81,
      "median_wip_adj_hold_h": 1.02
    },
    "2026-08": {
      "n": 43,
      "coverage": 1.52,
      "median_wip_adj_hold_h": 1.22
    },
    "2026-09": {
      "n": 58,
      "coverage": 1.58,
      "median_wip_adj_hold_h": 1.17
    }
  },
  "sop_effort_exec_h": 1.85,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0016` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | Employee Document Verification:effort_coverage (HR) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 1.4, expected 1.0, ratio 1.4 |
| Compared with | SOP-021 v1.1.0 E_effort_exec |
| What happened | Employee Document Verification: SOP executor effort 1.40h vs median WIP-adjusted hold 1.00h (coverage 1.40, flag standard_exceeds_hold) in all 12 eligible months. |
| Most likely reason | SOP executor effort standard too high (illustrative_expert_estimate) |
| Ranked candidate causes | SOP executor effort standard too high (illustrative_expert_estimate); Work done outside the ticket window (before Created or after Submitted) |
| SOP reference | SOP-021 v1.1.0 work-step effort_min (schema §8) |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Review the standard with the SOP owner or run a short time study. Do not edit standard times to match the data (schema §3.1). |
| Source records | - |

<details><summary>Evidence (JSON)</summary>

```json
{
  "flag": "standard_exceeds_hold",
  "months": {
    "2025-10": {
      "n": 47,
      "coverage": 1.45,
      "median_wip_adj_hold_h": 0.96
    },
    "2025-11": {
      "n": 38,
      "coverage": 1.39,
      "median_wip_adj_hold_h": 1.01
    },
    "2025-12": {
      "n": 35,
      "coverage": 1.43,
      "median_wip_adj_hold_h": 0.98
    },
    "2026-01": {
      "n": 51,
      "coverage": 1.4,
      "median_wip_adj_hold_h": 1.0
    },
    "2026-02": {
      "n": 49,
      "coverage": 1.51,
      "median_wip_adj_hold_h": 0.93
    },
    "2026-03": {
      "n": 49,
      "coverage": 1.39,
      "median_wip_adj_hold_h": 1.01
    },
    "2026-04": {
      "n": 40,
      "coverage": 1.39,
      "median_wip_adj_hold_h": 1.0
    },
    "2026-05": {
      "n": 40,
      "coverage": 1.26,
      "median_wip_adj_hold_h": 1.11
    },
    "2026-06": {
      "n": 48,
      "coverage": 1.33,
      "median_wip_adj_hold_h": 1.05
    },
    "2026-07": {
      "n": 47,
      "coverage": 1.4,
      "median_wip_adj_hold_h": 1.0
    },
    "2026-08": {
      "n": 42,
      "coverage": 1.56,
      "median_wip_adj_hold_h": 0.89
    },
    "2026-09": {
      "n": 47,
      "coverage": 1.32,
      "median_wip_adj_hold_h": 1.06
    }
  },
  "sop_effort_exec_h": 1.4,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0017` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | Incident Review:effort_coverage (Operations) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 1.58, expected 1.0, ratio 1.58 |
| Compared with | SOP-019 v1.1.0 E_effort_exec |
| What happened | Incident Review: SOP executor effort 3.78h vs median WIP-adjusted hold 2.40h (coverage 1.58, flag standard_exceeds_hold) in all 12 eligible months. |
| Most likely reason | SOP executor effort standard too high (illustrative_expert_estimate) |
| Ranked candidate causes | SOP executor effort standard too high (illustrative_expert_estimate); Work done outside the ticket window (before Created or after Submitted) |
| SOP reference | SOP-019 v1.1.0 work-step effort_min (schema §8) |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Review the standard with the SOP owner or run a short time study. Do not edit standard times to match the data (schema §3.1). |
| Source records | - |

<details><summary>Evidence (JSON)</summary>

```json
{
  "flag": "standard_exceeds_hold",
  "months": {
    "2025-10": {
      "n": 47,
      "coverage": 1.61,
      "median_wip_adj_hold_h": 2.34
    },
    "2025-11": {
      "n": 46,
      "coverage": 1.67,
      "median_wip_adj_hold_h": 2.26
    },
    "2025-12": {
      "n": 55,
      "coverage": 1.57,
      "median_wip_adj_hold_h": 2.41
    },
    "2026-01": {
      "n": 43,
      "coverage": 1.65,
      "median_wip_adj_hold_h": 2.3
    },
    "2026-02": {
      "n": 31,
      "coverage": 1.53,
      "median_wip_adj_hold_h": 2.47
    },
    "2026-03": {
      "n": 43,
      "coverage": 1.82,
      "median_wip_adj_hold_h": 2.08
    },
    "2026-04": {
      "n": 48,
      "coverage": 1.68,
      "median_wip_adj_hold_h": 2.25
    },
    "2026-05": {
      "n": 45,
      "coverage": 1.44,
      "median_wip_adj_hold_h": 2.62
    },
    "2026-06": {
      "n": 41,
      "coverage": 1.33,
      "median_wip_adj_hold_h": 2.84
    },
    "2026-07": {
      "n": 55,
      "coverage": 1.59,
      "median_wip_adj_hold_h": 2.38
    },
    "2026-08": {
      "n": 45,
      "coverage": 1.34,
      "median_wip_adj_hold_h": 2.83
    },
    "2026-09": {
      "n": 69,
      "coverage": 1.44,
      "median_wip_adj_hold_h": 2.63
    }
  },
  "sop_effort_exec_h": 3.78,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0018` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | Invoice Verification:effort_coverage (Finance) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 1.17, expected 1.0, ratio 1.17 |
| Compared with | SOP-015 v1.1.0 E_effort_exec |
| What happened | Invoice Verification: SOP executor effort 1.32h vs median WIP-adjusted hold 1.14h (coverage 1.17, flag standard_exceeds_hold) in all 12 eligible months. |
| Most likely reason | SOP executor effort standard too high (illustrative_expert_estimate) |
| Ranked candidate causes | SOP executor effort standard too high (illustrative_expert_estimate); Work done outside the ticket window (before Created or after Submitted) |
| SOP reference | SOP-015 v1.1.0 work-step effort_min (schema §8) |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Review the standard with the SOP owner or run a short time study. Do not edit standard times to match the data (schema §3.1). |
| Source records | - |

<details><summary>Evidence (JSON)</summary>

```json
{
  "flag": "standard_exceeds_hold",
  "months": {
    "2025-10": {
      "n": 36,
      "coverage": 1.34,
      "median_wip_adj_hold_h": 0.99
    },
    "2025-11": {
      "n": 32,
      "coverage": 1.31,
      "median_wip_adj_hold_h": 1.01
    },
    "2025-12": {
      "n": 45,
      "coverage": 1.14,
      "median_wip_adj_hold_h": 1.17
    },
    "2026-01": {
      "n": 37,
      "coverage": 1.41,
      "median_wip_adj_hold_h": 0.94
    },
    "2026-02": {
      "n": 35,
      "coverage": 1.24,
      "median_wip_adj_hold_h": 1.07
    },
    "2026-03": {
      "n": 42,
      "coverage": 1.14,
      "median_wip_adj_hold_h": 1.16
    },
    "2026-04": {
      "n": 39,
      "coverage": 1.19,
      "median_wip_adj_hold_h": 1.11
    },
    "2026-05": {
      "n": 54,
      "coverage": 1.03,
      "median_wip_adj_hold_h": 1.29
    },
    "2026-06": {
      "n": 51,
      "coverage": 1.31,
      "median_wip_adj_hold_h": 1.01
    },
    "2026-07": {
      "n": 40,
      "coverage": 1.03,
      "median_wip_adj_hold_h": 1.28
    },
    "2026-08": {
      "n": 36,
      "coverage": 1.12,
      "median_wip_adj_hold_h": 1.19
    },
    "2026-09": {
      "n": 49,
      "coverage": 1.09,
      "median_wip_adj_hold_h": 1.22
    }
  },
  "sop_effort_exec_h": 1.32,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0019` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | Leave Approval:effort_coverage (HR) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 0.42, expected 1.0, ratio 0.42 |
| Compared with | SOP-020 v1.1.0 E_effort_exec |
| What happened | Leave Approval: SOP executor effort 0.20h vs median WIP-adjusted hold 0.47h (coverage 0.42, flag low_coverage) in all 12 eligible months. |
| Most likely reason | Holding time includes much non-SOP time (waiting on others, multitasking, idle) |
| Ranked candidate causes | Holding time includes much non-SOP time (waiting on others, multitasking, idle); SOP executor effort standard too low |
| SOP reference | SOP-020 v1.1.0 work-step effort_min (schema §8) |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Review the standard with the SOP owner or run a short time study. Do not edit standard times to match the data (schema §3.1). |
| Source records | - |

<details><summary>Evidence (JSON)</summary>

```json
{
  "flag": "low_coverage",
  "months": {
    "2025-10": {
      "n": 51,
      "coverage": 0.42,
      "median_wip_adj_hold_h": 0.46
    },
    "2025-11": {
      "n": 38,
      "coverage": 0.43,
      "median_wip_adj_hold_h": 0.46
    },
    "2025-12": {
      "n": 56,
      "coverage": 0.44,
      "median_wip_adj_hold_h": 0.45
    },
    "2026-01": {
      "n": 51,
      "coverage": 0.4,
      "median_wip_adj_hold_h": 0.49
    },
    "2026-02": {
      "n": 36,
      "coverage": 0.37,
      "median_wip_adj_hold_h": 0.53
    },
    "2026-03": {
      "n": 48,
      "coverage": 0.46,
      "median_wip_adj_hold_h": 0.42
    },
    "2026-04": {
      "n": 42,
      "coverage": 0.41,
      "median_wip_adj_hold_h": 0.48
    },
    "2026-05": {
      "n": 43,
      "coverage": 0.37,
      "median_wip_adj_hold_h": 0.53
    },
    "2026-06": {
      "n": 48,
      "coverage": 0.44,
      "median_wip_adj_hold_h": 0.45
    },
    "2026-07": {
      "n": 42,
      "coverage": 0.42,
      "median_wip_adj_hold_h": 0.47
    },
    "2026-08": {
      "n": 43,
      "coverage": 0.39,
      "median_wip_adj_hold_h": 0.51
    },
    "2026-09": {
      "n": 35,
      "coverage": 0.43,
      "median_wip_adj_hold_h": 0.45
    }
  },
  "sop_effort_exec_h": 0.2,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0020` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | Purchase Request:effort_coverage (Procurement) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 1.1, expected 1.0, ratio 1.1 |
| Compared with | SOP-014 v1.1.0 E_effort_exec |
| What happened | Purchase Request: SOP executor effort 1.20h vs median WIP-adjusted hold 1.10h (coverage 1.10, flag standard_exceeds_hold) in all 12 eligible months. |
| Most likely reason | SOP executor effort standard too high (illustrative_expert_estimate) |
| Ranked candidate causes | SOP executor effort standard too high (illustrative_expert_estimate); Work done outside the ticket window (before Created or after Submitted) |
| SOP reference | SOP-014 v1.1.0 work-step effort_min (schema §8) |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Review the standard with the SOP owner or run a short time study. Do not edit standard times to match the data (schema §3.1). |
| Source records | - |

<details><summary>Evidence (JSON)</summary>

```json
{
  "flag": "standard_exceeds_hold",
  "months": {
    "2025-10": {
      "n": 41,
      "coverage": 1.01,
      "median_wip_adj_hold_h": 1.19
    },
    "2025-11": {
      "n": 38,
      "coverage": 1.13,
      "median_wip_adj_hold_h": 1.06
    },
    "2025-12": {
      "n": 45,
      "coverage": 1.08,
      "median_wip_adj_hold_h": 1.11
    },
    "2026-01": {
      "n": 35,
      "coverage": 1.12,
      "median_wip_adj_hold_h": 1.08
    },
    "2026-02": {
      "n": 29,
      "coverage": 1.16,
      "median_wip_adj_hold_h": 1.04
    },
    "2026-03": {
      "n": 39,
      "coverage": 1.0,
      "median_wip_adj_hold_h": 1.2
    },
    "2026-04": {
      "n": 44,
      "coverage": 1.07,
      "median_wip_adj_hold_h": 1.13
    },
    "2026-05": {
      "n": 39,
      "coverage": 1.06,
      "median_wip_adj_hold_h": 1.13
    },
    "2026-06": {
      "n": 34,
      "coverage": 1.15,
      "median_wip_adj_hold_h": 1.04
    },
    "2026-07": {
      "n": 42,
      "coverage": 1.17,
      "median_wip_adj_hold_h": 1.03
    },
    "2026-08": {
      "n": 42,
      "coverage": 1.11,
      "median_wip_adj_hold_h": 1.08
    },
    "2026-09": {
      "n": 45,
      "coverage": 1.04,
      "median_wip_adj_hold_h": 1.15
    }
  },
  "sop_effort_exec_h": 1.2,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0021` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | Vendor Onboarding:effort_coverage (Procurement) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 1.47, expected 1.0, ratio 1.47 |
| Compared with | SOP-017 v1.1.0 E_effort_exec |
| What happened | Vendor Onboarding: SOP executor effort 2.83h vs median WIP-adjusted hold 1.93h (coverage 1.47, flag standard_exceeds_hold) in all 12 eligible months. |
| Most likely reason | SOP executor effort standard too high (illustrative_expert_estimate) |
| Ranked candidate causes | SOP executor effort standard too high (illustrative_expert_estimate); Work done outside the ticket window (before Created or after Submitted) |
| SOP reference | SOP-017 v1.1.0 work-step effort_min (schema §8) |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Review the standard with the SOP owner or run a short time study. Do not edit standard times to match the data (schema §3.1). |
| Source records | - |

<details><summary>Evidence (JSON)</summary>

```json
{
  "flag": "standard_exceeds_hold",
  "months": {
    "2025-10": {
      "n": 41,
      "coverage": 1.35,
      "median_wip_adj_hold_h": 2.09
    },
    "2025-11": {
      "n": 40,
      "coverage": 1.48,
      "median_wip_adj_hold_h": 1.92
    },
    "2025-12": {
      "n": 36,
      "coverage": 1.46,
      "median_wip_adj_hold_h": 1.94
    },
    "2026-01": {
      "n": 36,
      "coverage": 1.38,
      "median_wip_adj_hold_h": 2.06
    },
    "2026-02": {
      "n": 45,
      "coverage": 1.52,
      "median_wip_adj_hold_h": 1.86
    },
    "2026-03": {
      "n": 43,
      "coverage": 1.38,
      "median_wip_adj_hold_h": 2.06
    },
    "2026-04": {
      "n": 44,
      "coverage": 1.55,
      "median_wip_adj_hold_h": 1.82
    },
    "2026-05": {
      "n": 44,
      "coverage": 1.37,
      "median_wip_adj_hold_h": 2.07
    },
    "2026-06": {
      "n": 32,
      "coverage": 1.68,
      "median_wip_adj_hold_h": 1.69
    },
    "2026-07": {
      "n": 50,
      "coverage": 1.48,
      "median_wip_adj_hold_h": 1.92
    },
    "2026-08": {
      "n": 45,
      "coverage": 1.42,
      "median_wip_adj_hold_h": 1.99
    },
    "2026-09": {
      "n": 37,
      "coverage": 1.73,
      "median_wip_adj_hold_h": 1.64
    }
  },
  "sop_effort_exec_h": 2.83,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0022` REWORK_ABOVE_SOP_EXPECTATION

| field | value |
|---|---|
| Entity | Invoice Verification:rework (Finance) |
| Severity / classification / confidence | medium / rework / low |
| Measured | share of tickets rejected at least once: observed 0.137, expected 0.1, ratio 1.37 |
| Compared with | SOP-015 v1.1.0 FPY |
| What happened | Invoice Verification: 14% of tickets rejected at least once vs 10% implied by the SOP first-pass yield (unconfirmed). |
| Most likely reason | Incorrect category (21): preventable by S4 GL and tax code check |
| Ranked candidate causes | Incorrect category (21) (29%); Amount mismatch (20) (27%); Required document missing (18) (25%); Wrong quantity (14) (19%) |
| SOP reference | SOP-015 rework_triggers; expected_first_pass_yield 0.9 |
| Preventable by | S4 GL and tax code check|S3 three-way match |
| Reason source | sop |
| Recommended investigation | Strengthen the upstream control 'S4 GL and tax code check' and re-measure the first-pass yield. |
| Source records | 68 tickets: T00347, T00700, T00829, T00993, T01037, T01064, T01112, T01132, T01147, T01230 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "tickets": 496,
  "rejected": 68,
  "reasons": {
    "Incorrect category": 21,
    "Amount mismatch": 20,
    "Required document missing": 18,
    "Wrong quantity": 14
  },
  "quality_targets_source": "unconfirmed"
}
```
</details>

### `DEV-0023` APPROVAL_WAIT_INCREASE

| field | value |
|---|---|
| Entity | Daily Operations Report:Incharge:2026-08..2026-09 (Operations) |
| Severity / classification / confidence | medium / process / medium |
| Measured | median wait for the Incharge decision (h): observed 1.76, expected 1.02, ratio 1.72 |
| Compared with | Daily Operations Report Incharge wait, own previous months 2026-02..2026-07 |
| What happened | In 2026-08..2026-09, Daily Operations Report tickets waited a median 1.76h for the Incharge decision vs 1.02h in the months before (1.7x). Likely cause: incharge approver queue for daily operations report (only this task type rose and it has no external dependency). |
| Most likely reason | Incharge approver queue for Daily Operations Report |
| Ranked candidate causes | Incharge approver queue for Daily Operations Report; Volume increase in the same months |
| SOP reference | SOP approval_matrix and approval-step queue_wait_h |
| Preventable by | - |
| Reason source | baseline |
| Recommended investigation | Check incharge approver queue for daily operations report for 2026-08..2026-09; process-level signal, not an executor issue. |
| Source records | 20 tickets: T04199, T04468, T04068, T04656, T04354, T04129, T04030, T04351, T04514, T04080 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "stage": "Incharge",
  "task_type": "Daily Operations Report",
  "window_start": "2026-08",
  "window_end": "2026-09",
  "baseline_periods": [
    "2026-02",
    "2026-03",
    "2026-04",
    "2026-05",
    "2026-06",
    "2026-07"
  ],
  "baseline_median_wait_h": 1.02,
  "monthly_tickets_and_median_wait_h": {
    "2026-08": [
      50,
      1.66
    ],
    "2026-09": [
      89,
      1.81
    ]
  },
  "declared_dependencies": 0,
  "same_months_other_task_types": [],
  "note": "Incharge wait = submission -> first decision, including any DependencyWait interval."
}
```
</details>

### `DEV-0024` APPROVAL_WAIT_INCREASE

| field | value |
|---|---|
| Entity | Expense Approval:Incharge:2026-02..2026-03 (Finance) |
| Severity / classification / confidence | high / process / medium |
| Measured | median wait for the Incharge decision (h): observed 4.29, expected 1.77, ratio 2.42 |
| Compared with | Expense Approval Incharge wait, own previous months 2025-10..2026-01 |
| What happened | In 2026-02..2026-03, Expense Approval tickets waited a median 4.29h for the Incharge decision vs 1.77h in the months before (2.4x). Likely cause: incharge approver queue shared across finance task types (the same wait rose in Invoice Verification in the same months). |
| Most likely reason | Incharge approver queue shared across Finance task types |
| Ranked candidate causes | Incharge approver queue shared across Finance task types; Volume increase in the same months |
| SOP reference | SOP approval_matrix and approval-step queue_wait_h |
| Preventable by | - |
| Reason source | baseline |
| Recommended investigation | Check incharge approver queue shared across finance task types for 2026-02..2026-03; process-level signal, not an executor issue. |
| Source records | 20 tickets: T01701, T01644, T01895, T01793, T02027, T01893, T02044, T02109, T02045, T01766 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "stage": "Incharge",
  "task_type": "Expense Approval",
  "window_start": "2026-02",
  "window_end": "2026-03",
  "baseline_periods": [
    "2025-10",
    "2025-11",
    "2025-12",
    "2026-01"
  ],
  "baseline_median_wait_h": 1.77,
  "monthly_tickets_and_median_wait_h": {
    "2026-02": [
      44,
      4.43
    ],
    "2026-03": [
      44,
      4.18
    ]
  },
  "declared_dependencies": 0,
  "same_months_other_task_types": [
    "Invoice Verification"
  ],
  "note": "Incharge wait = submission -> first decision, including any DependencyWait interval."
}
```
</details>

### `DEV-0025` APPROVAL_WAIT_INCREASE

| field | value |
|---|---|
| Entity | Invoice Verification:Incharge:2026-02..2026-03 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | median wait for the Incharge decision (h): observed 5.71, expected 3.56, ratio 1.6 |
| Compared with | Invoice Verification Incharge wait, own previous months 2025-10..2026-01 |
| What happened | In 2026-02..2026-03, Invoice Verification tickets waited a median 5.71h for the Incharge decision vs 3.56h in the months before (1.6x). Likely cause: incharge approver queue shared across finance task types (the same wait rose in Expense Approval in the same months). |
| Most likely reason | Incharge approver queue shared across Finance task types |
| Ranked candidate causes | Incharge approver queue shared across Finance task types; Volume increase in the same months |
| SOP reference | SOP approval_matrix and approval-step queue_wait_h |
| Preventable by | - |
| Reason source | baseline |
| Recommended investigation | Check incharge approver queue shared across finance task types for 2026-02..2026-03; process-level signal, not an executor issue. |
| Source records | 20 tickets: T01539, T02059, T02129, T01544, T02103, T01690, T02043, T02237, T02178, T01871 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "stage": "Incharge",
  "task_type": "Invoice Verification",
  "window_start": "2026-02",
  "window_end": "2026-03",
  "baseline_periods": [
    "2025-10",
    "2025-11",
    "2025-12",
    "2026-01"
  ],
  "baseline_median_wait_h": 3.56,
  "monthly_tickets_and_median_wait_h": {
    "2026-02": [
      35,
      5.74
    ],
    "2026-03": [
      42,
      5.61
    ]
  },
  "declared_dependencies": 1,
  "same_months_other_task_types": [
    "Expense Approval"
  ],
  "note": "Incharge wait = submission -> first decision, including any DependencyWait interval."
}
```
</details>

### `DEV-0026` APPROVAL_WAIT_INCREASE

| field | value |
|---|---|
| Entity | Vendor Onboarding:Incharge:2026-01..2026-02 (Procurement) |
| Severity / classification / confidence | high / process / low |
| Measured | median wait for the Incharge decision (h): observed 10.55, expected 5.02, ratio 2.1 |
| Compared with | Vendor Onboarding Incharge wait, own previous months 2025-10..2025-12 |
| What happened | In 2026-01..2026-02, Vendor Onboarding tickets waited a median 10.55h for the Incharge decision vs 5.02h in the months before (2.1x). Likely cause: dependency wait for vendor onboarding (or its incharge approver) (only this task type rose and it declares external dependencies; the log cannot separate the two). |
| Most likely reason | Dependency wait for Vendor Onboarding (or its Incharge approver) |
| Ranked candidate causes | Dependency wait for Vendor Onboarding (or its Incharge approver); Volume increase in the same months |
| SOP reference | SOP approval_matrix and approval-step queue_wait_h |
| Preventable by | - |
| Reason source | baseline |
| Recommended investigation | Check dependency wait for vendor onboarding (or its incharge approver) for 2026-01..2026-02; process-level signal, not an executor issue. |
| Source records | 20 tickets: T01762, T01656, T01482, T01872, T01687, T01837, T01841, T01647, T01666, T01307 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "stage": "Incharge",
  "task_type": "Vendor Onboarding",
  "window_start": "2026-01",
  "window_end": "2026-02",
  "baseline_periods": [
    "2025-10",
    "2025-11",
    "2025-12"
  ],
  "baseline_median_wait_h": 5.02,
  "monthly_tickets_and_median_wait_h": {
    "2026-01": [
      36,
      10.13
    ],
    "2026-02": [
      45,
      10.6
    ]
  },
  "declared_dependencies": 2,
  "same_months_other_task_types": [],
  "note": "Incharge wait = submission -> first decision, including any DependencyWait interval."
}
```
</details>

### `DEV-0027` APPROVAL_WAIT_INCREASE

| field | value |
|---|---|
| Entity | Incident Review:Lead:2026-08..2026-09 (Operations) |
| Severity / classification / confidence | medium / process / low |
| Measured | median wait for the Lead decision (h): observed 2.44, expected 1.25, ratio 1.95 |
| Compared with | Incident Review Lead wait, own previous months 2026-02..2026-07 |
| What happened | In 2026-08..2026-09, Incident Review tickets waited a median 2.44h for the Lead decision vs 1.25h in the months before (2.0x). Likely cause: lead approver queue for incident review (only this task type rose and it has no external dependency). |
| Most likely reason | Lead approver queue for Incident Review |
| Ranked candidate causes | Lead approver queue for Incident Review; Volume increase in the same months |
| SOP reference | SOP approval_matrix and approval-step queue_wait_h |
| Preventable by | - |
| Reason source | baseline |
| Recommended investigation | Check lead approver queue for incident review for 2026-08..2026-09; process-level signal, not an executor issue. |
| Source records | 20 tickets: T04285, T04257, T04280, T04171, T04529, T04523, T04550, T04435, T04035, T04626 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "stage": "Lead",
  "task_type": "Incident Review",
  "window_start": "2026-08",
  "window_end": "2026-09",
  "baseline_periods": [
    "2026-02",
    "2026-03",
    "2026-04",
    "2026-05",
    "2026-06",
    "2026-07"
  ],
  "baseline_median_wait_h": 1.25,
  "monthly_tickets_and_median_wait_h": {
    "2026-08": [
      45,
      2.19
    ],
    "2026-09": [
      69,
      2.58
    ]
  },
  "declared_dependencies": 2,
  "same_months_other_task_types": [],
  "note": "Incharge wait = submission -> first decision, including any DependencyWait interval."
}
```
</details>


## Employee-level signals (3)

### `DEV-0028` PERSISTENT_UNEXPLAINED_PROCESSING_INCREASE

| field | value |
|---|---|
| Entity | E1003 (Finance) |
| Severity / classification / confidence | medium / individual_signal / medium |
| Measured | median_processing_ratio: observed 1.17, expected 1.0, ratio 1.17 |
| Compared with | BL-v1:task-type processing baselines |
| What happened | Executor processing time on E1003's tickets has been 1.17x the task-type baseline for 3 consecutive months (2026-07, 2026-08, 2026-09), up from 0.86x in the months before (1.36x change). Completed volume moved from 12.7 to 11.0 tickets/month. Complexity, workload, rejections, reassignment and peer trend do not explain it. |
| Most likely reason | No available context factor explains the change |
| Ranked candidate causes | No available context factor explains the change |
| SOP reference | n/a: SOP effort is never compared per employee (schema §8) |
| Preventable by | - |
| Reason source | baseline |
| Recommended investigation | Manager review recommended: persistent deviation not explained by complexity, workload, rejections, reassignment or team-wide trend. Check leave, other duties, tooling or support needs. |
| Source records | 33 tickets: T03425, T03459, T03493, T03549, T03582, T03611, T03615, T03649, T03652, T03664 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "periods": {
    "2025-10": {
      "tickets": 16,
      "median_processing_ratio": 0.8
    },
    "2025-11": {
      "tickets": 16,
      "median_processing_ratio": 0.88
    },
    "2025-12": {
      "tickets": 19,
      "median_processing_ratio": 0.83
    },
    "2026-01": {
      "tickets": 7,
      "median_processing_ratio": 0.71
    },
    "2026-02": {
      "tickets": 13,
      "median_processing_ratio": 0.94
    },
    "2026-03": {
      "tickets": 9,
      "median_processing_ratio": 1.02
    },
    "2026-04": {
      "tickets": 13,
      "median_processing_ratio": 0.91
    },
    "2026-05": {
      "tickets": 10,
      "median_processing_ratio": 0.76
    },
    "2026-06": {
      "tickets": 24,
      "median_processing_ratio": 0.82
    },
    "2026-07": {
      "tickets": 14,
      "median_processing_ratio": 1.21
    },
    "2026-08": {
      "tickets": 7,
      "median_processing_ratio": 1.09
    },
    "2026-09": {
      "tickets": 12,
      "median_processing_ratio": 1.21
    }
  },
  "recent_periods": [
    "2026-07",
    "2026-08",
    "2026-09"
  ],
  "window_start": "2026-07",
  "window_end": "2026-09",
  "baseline_periods": [
    "2026-01",
    "2026-02",
    "2026-03",
    "2026-04",
    "2026-05",
    "2026-06"
  ],
  "recent_median_processing_ratio": 1.17,
  "own_baseline_median_processing_ratio": 0.86,
  "change_vs_own_history": 1.36,
  "mann_whitney_p_value": 1.63e-07,
  "volume_per_period_recent_vs_earlier": [
    11.0,
    12.7
  ],
  "context_checks": {
    "complexity_shift": {
      "recent_complex_share": 0.0,
      "earlier_complex_share": 0.0,
      "explains": false
    },
    "workload_increase": {
      "recent_effort_h_per_period": 42.76,
      "earlier_effort_h_per_period": 50.64,
      "explains": false
    },
    "rejection_increase": {
      "recent_rate": 0.06,
      "earlier_rate": 0.12,
      "explains": false,
      "co_occurring_signal": false
    },
    "team_wide_trend": {
      "peer_recent_processing_ratio": 1.01,
      "peer_earlier_processing_ratio": 1.02,
      "peer_change": 0.99,
      "explains": false
    },
    "reassignments": {
      "recent_reassignments": 0,
      "explains": false
    },
    "approval_dependency_wait": {
      "note": "excluded by design: processing ratio measures executor-held time only",
      "explains": false
    },
    "task_mix": {
      "note": "controlled: each ticket compared with its own task-type baseline",
      "explains": false
    },
    "leave": {
      "note": "leave/absence data not available in this dataset",
      "explains": null
    }
  }
}
```
</details>

### `DEV-0029` PERSISTENT_PROCESSING_INCREASE_WITH_CONTEXT

| field | value |
|---|---|
| Entity | E1013 (Operations) |
| Severity / classification / confidence | medium / context_explained / low |
| Measured | median_processing_ratio: observed 1.1, expected 1.0, ratio 1.1 |
| Compared with | BL-v1:task-type processing baselines |
| What happened | Executor processing time on E1013's tickets has been 1.10x the task-type baseline for 2 consecutive months (2026-08, 2026-09), up from 0.86x in the months before (1.28x change). Completed volume moved from 14.8 to 15.0 tickets/month. Possible context: team_wide_trend. |
| Most likely reason | Context factor: team_wide_trend |
| Ranked candidate causes | Context factor: team_wide_trend |
| SOP reference | n/a: SOP effort is never compared per employee (schema §8) |
| Preventable by | - |
| Reason source | baseline |
| Recommended investigation | Review the listed context factors before any individual follow-up. |
| Source records | 30 tickets: T03842, T04020, T04084, T04090, T04110, T04114, T04119, T04149, T04160, T04165 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "periods": {
    "2025-10": {
      "tickets": 20,
      "median_processing_ratio": 0.83
    },
    "2025-11": {
      "tickets": 15,
      "median_processing_ratio": 0.83
    },
    "2025-12": {
      "tickets": 18,
      "median_processing_ratio": 0.82
    },
    "2026-01": {
      "tickets": 11,
      "median_processing_ratio": 0.93
    },
    "2026-02": {
      "tickets": 7,
      "median_processing_ratio": 0.89
    },
    "2026-03": {
      "tickets": 10,
      "median_processing_ratio": 0.73
    },
    "2026-04": {
      "tickets": 24,
      "median_processing_ratio": 0.91
    },
    "2026-05": {
      "tickets": 17,
      "median_processing_ratio": 0.83
    },
    "2026-06": {
      "tickets": 11,
      "median_processing_ratio": 0.65
    },
    "2026-07": {
      "tickets": 16,
      "median_processing_ratio": 0.87
    },
    "2026-08": {
      "tickets": 10,
      "median_processing_ratio": 1.11
    },
    "2026-09": {
      "tickets": 20,
      "median_processing_ratio": 1.06
    }
  },
  "recent_periods": [
    "2026-08",
    "2026-09"
  ],
  "window_start": "2026-08",
  "window_end": "2026-09",
  "baseline_periods": [
    "2026-01",
    "2026-03",
    "2026-04",
    "2026-05",
    "2026-06",
    "2026-07"
  ],
  "recent_median_processing_ratio": 1.1,
  "own_baseline_median_processing_ratio": 0.86,
  "change_vs_own_history": 1.28,
  "mann_whitney_p_value": 1.65e-05,
  "volume_per_period_recent_vs_earlier": [
    15.0,
    14.8
  ],
  "context_checks": {
    "complexity_shift": {
      "recent_complex_share": 0.5,
      "earlier_complex_share": 0.6,
      "explains": false
    },
    "workload_increase": {
      "recent_effort_h_per_period": 83.93,
      "earlier_effort_h_per_period": 92.24,
      "explains": false
    },
    "rejection_increase": {
      "recent_rate": 0.07,
      "earlier_rate": 0.1,
      "explains": false,
      "co_occurring_signal": false
    },
    "team_wide_trend": {
      "peer_recent_processing_ratio": 1.22,
      "peer_earlier_processing_ratio": 1.0,
      "peer_change": 1.23,
      "explains": true
    },
    "reassignments": {
      "recent_reassignments": 0,
      "explains": false
    },
    "approval_dependency_wait": {
      "note": "excluded by design: processing ratio measures executor-held time only",
      "explains": false
    },
    "task_mix": {
      "note": "controlled: each ticket compared with its own task-type baseline",
      "explains": false
    },
    "leave": {
      "note": "leave/absence data not available in this dataset",
      "explains": null
    }
  }
}
```
</details>

### `DEV-0030` PERSISTENT_PROCESSING_INCREASE_WITH_CONTEXT

| field | value |
|---|---|
| Entity | E1015 (Operations) |
| Severity / classification / confidence | high / context_explained / low |
| Measured | median_processing_ratio: observed 1.44, expected 1.0, ratio 1.44 |
| Compared with | BL-v1:task-type processing baselines |
| What happened | Executor processing time on E1015's tickets has been 1.44x the task-type baseline for 4 consecutive months (2026-06, 2026-07, 2026-08, 2026-09), up from 0.89x in the months before (1.62x change). Completed volume moved from 15.8 to 39.0 tickets/month. Possible context: workload_increase. |
| Most likely reason | Context factor: workload_increase |
| Ranked candidate causes | Context factor: workload_increase |
| SOP reference | n/a: SOP effort is never compared per employee (schema §8) |
| Preventable by | - |
| Reason source | baseline |
| Recommended investigation | Review the listed context factors before any individual follow-up. |
| Source records | 156 tickets: T03051, T03069, T03078, T03088, T03120, T03126, T03141, T03149, T03179, T03182 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "periods": {
    "2025-10": {
      "tickets": 15,
      "median_processing_ratio": 0.91
    },
    "2025-11": {
      "tickets": 7,
      "median_processing_ratio": 1.02
    },
    "2025-12": {
      "tickets": 17,
      "median_processing_ratio": 1.0
    },
    "2026-01": {
      "tickets": 16,
      "median_processing_ratio": 0.85
    },
    "2026-02": {
      "tickets": 8,
      "median_processing_ratio": 0.98
    },
    "2026-03": {
      "tickets": 19,
      "median_processing_ratio": 0.83
    },
    "2026-04": {
      "tickets": 8,
      "median_processing_ratio": 0.8
    },
    "2026-05": {
      "tickets": 12,
      "median_processing_ratio": 0.82
    },
    "2026-06": {
      "tickets": 25,
      "median_processing_ratio": 1.23
    },
    "2026-07": {
      "tickets": 39,
      "median_processing_ratio": 1.28
    },
    "2026-08": {
      "tickets": 35,
      "median_processing_ratio": 1.42
    },
    "2026-09": {
      "tickets": 57,
      "median_processing_ratio": 1.66
    }
  },
  "recent_periods": [
    "2026-06",
    "2026-07",
    "2026-08",
    "2026-09"
  ],
  "window_start": "2026-06",
  "window_end": "2026-09",
  "baseline_periods": [
    "2025-10",
    "2025-12",
    "2026-01",
    "2026-03",
    "2026-05"
  ],
  "recent_median_processing_ratio": 1.44,
  "own_baseline_median_processing_ratio": 0.89,
  "change_vs_own_history": 1.62,
  "mann_whitney_p_value": 3.3e-18,
  "volume_per_period_recent_vs_earlier": [
    39.0,
    15.8
  ],
  "context_checks": {
    "complexity_shift": {
      "recent_complex_share": 0.5,
      "earlier_complex_share": 0.48,
      "explains": false
    },
    "workload_increase": {
      "recent_effort_h_per_period": 217.32,
      "earlier_effort_h_per_period": 85.96,
      "explains": true
    },
    "rejection_increase": {
      "recent_rate": 0.08,
      "earlier_rate": 0.11,
      "explains": false,
      "co_occurring_signal": false
    },
    "team_wide_trend": {
      "peer_recent_processing_ratio": 1.01,
      "peer_earlier_processing_ratio": 0.96,
      "peer_change": 1.05,
      "explains": false
    },
    "reassignments": {
      "recent_reassignments": 0,
      "explains": false
    },
    "approval_dependency_wait": {
      "note": "excluded by design: processing ratio measures executor-held time only",
      "explains": false
    },
    "task_mix": {
      "note": "controlled: each ticket compared with its own task-type baseline",
      "explains": false
    },
    "leave": {
      "note": "leave/absence data not available in this dataset",
      "explains": null
    }
  }
}
```
</details>


## Ticket-level deviations (327)

### `DEV-0031` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00009 (HR) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 5.5, expected 2.15, ratio 2.56 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 5.5h vs an expected 2.2h (2.56x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Extended executor processing (2%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00009; 6 events: EV0000028, EV0000029, EV0000033, EV0000035, EV0000038, EV0000086 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 5.5,
  "duration_ratio": 2.56,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.52,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.2,
      0.6
    ],
    "dependency_wait": [
      4.73,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.5,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.93,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0032` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00034 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.53, expected 2.14, ratio 2.12 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 4.5h vs an expected 2.1h (2.12x). 90% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (90%); Extended executor processing (10%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00034; 5 events: EV0000185, EV0000186, EV0000191, EV0000194, EV0000214 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 4.53,
  "duration_ratio": 2.12,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.04,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.28,
      0.53
    ],
    "dependency_wait": [
      3.17,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.17,
    "assignee_typical_week_effort_h": 17.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.46,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0033` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00066 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.85, expected 2.36, ratio 2.05 |
| Compared with | BL-v1:L2:Leave Approval:Simple:High |
| What happened | Leave Approval (Simple, High) took 4.8h vs an expected 2.4h (2.05x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00066; 6 events: EV0000359, EV0000360, EV0000364, EV0000366, EV0000368, EV0000414 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.36,
  "actual_duration_h": 4.85,
  "duration_ratio": 2.05,
  "baseline_p90_h": 4.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.49,
      0.53
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.1,
      0.6
    ],
    "dependency_wait": [
      4.23,
      0.98
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 37.33,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.33,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0034` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00121 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.29, expected 2.15, ratio 1.99 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.3h vs an expected 2.2h (1.99x). 91% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (91%); Extended executor processing (9%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00121; 6 events: EV0000696, EV0000698, EV0000703, EV0000704, EV0000705, EV0000749 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.29,
  "duration_ratio": 1.99,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.72,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.1,
      0.6
    ],
    "dependency_wait": [
      3.42,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 21.42,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.52,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0035` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00132 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.32, expected 2.22, ratio 1.94 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.3h vs an expected 2.2h (1.94x). 61% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (61%); Rework after rejection (Amount mismatch) (32%); Extended executor processing (7%) |
| SOP reference | SOP-020 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00132; 7 events: EV0000781, EV0000782, EV0000785, EV0000796, EV0000803, EV0000804, EV0000811 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.32,
  "duration_ratio": 1.94,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.71,
      0.49
    ],
    "rework": [
      1.01,
      0.0
    ],
    "approval_wait": [
      2.54,
      0.58
    ],
    "dependency_wait": [
      0.0,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.72,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.54,
      0.8
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0036` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00159 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.09, expected 2.15, ratio 2.36 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 5.1h vs an expected 2.2h (2.36x). 93% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (93%); Extended executor processing (6%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00159; 6 events: EV0000940, EV0000941, EV0000942, EV0000943, EV0000944, EV0000959 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 5.09,
  "duration_ratio": 2.36,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.65,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.32,
      0.6
    ],
    "dependency_wait": [
      3.99,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 21.65,
    "assignee_typical_week_effort_h": 12.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.31,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0037` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00169 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.27, expected 2.94, ratio 1.8 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 5.3h vs an expected 2.9h (1.80x). 71% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (71%); Extended executor processing (25%); Approval wait at Incharge stage (2%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00169; 6 events: EV0000985, EV0000987, EV0000995, EV0000998, EV0001006, EV0001041 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 5.27,
  "duration_ratio": 1.8,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      1.44,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.65,
      0.58
    ],
    "dependency_wait": [
      3.08,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.61,
    "assignee_typical_week_effort_h": 13.0,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.73,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0038` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00174 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.9, expected 2.25, ratio 2.17 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.9h vs an expected 2.3h (2.17x). 92% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (92%); Extended executor processing (5%); Approval wait at Incharge stage (2%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00174; 5 events: EV0001014, EV0001018, EV0001024, EV0001032, EV0001082 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.9,
  "duration_ratio": 2.17,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.93,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.57,
      0.5
    ],
    "dependency_wait": [
      3.28,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 33.54,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.85,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0039` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00201 (Operations) |
| Severity / classification / confidence | high / executor_processing / high |
| Measured | total_duration_h: observed 6.26, expected 2.25, ratio 2.78 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 6.3h vs an expected 2.3h (2.78x). 98% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (98%); Assignment queue delay (1%); Approval wait at Incharge stage (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T00201; 5 events: EV0001184, EV0001187, EV0001219, EV0001222, EV0001228 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 6.26,
  "duration_ratio": 2.78,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      4.94,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.55,
      0.5
    ],
    "dependency_wait": [
      0.64,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 31.49,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      1.19,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0040` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00210 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.79, expected 2.15, ratio 1.76 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 3.8h vs an expected 2.2h (1.76x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00210; 5 events: EV0001252, EV0001253, EV0001258, EV0001260, EV0001277 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 3.79,
  "duration_ratio": 1.76,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.3,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.55,
      0.6
    ],
    "dependency_wait": [
      2.91,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 9.65,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.46,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0041` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00218 (Procurement) |
| Severity / classification / confidence | medium / process / low |
| Measured | total_duration_h: observed 15.99, expected 8.96, ratio 1.78 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 16.0h vs an expected 9.0h (1.78x). 34% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (34%); Cross-team / dependency wait (29%); Extended executor processing (25%); Rework after rejection (Required document missing) (13%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00218; 9 events: EV0001285, EV0001287, EV0001345, EV0001350, EV0001375, EV0001376, EV0001377, EV0001380, EV0001383 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 15.99,
  "duration_ratio": 1.78,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.1
    ],
    "executor_processing": [
      3.78,
      1.9
    ],
    "rework": [
      0.96,
      0.0
    ],
    "approval_wait": [
      4.33,
      1.79
    ],
    "dependency_wait": [
      6.82,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 48.08,
    "assignee_typical_week_effort_h": 32.36,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      8.78,
      4.83
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0042` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00240 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.91, expected 2.1, ratio 1.87 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.9h vs an expected 2.1h (1.87x). 79% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (79%); Extended executor processing (19%); Assignment queue delay (2%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00240; 5 events: EV0001420, EV0001421, EV0001432, EV0001436, EV0001452 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 3.91,
  "duration_ratio": 1.87,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.24,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.15,
      0.56
    ],
    "dependency_wait": [
      2.38,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 19.96,
    "assignee_typical_week_effort_h": 17.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.53,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0043` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00267 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.42, expected 2.15, ratio 2.05 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.4h vs an expected 2.2h (2.05x). 95% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (95%); Extended executor processing (4%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00267; 6 events: EV0001597, EV0001598, EV0001599, EV0001600, EV0001601, EV0001609 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.42,
  "duration_ratio": 2.05,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.57,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.32,
      0.6
    ],
    "dependency_wait": [
      3.43,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 25.12,
    "assignee_typical_week_effort_h": 9.93,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.75,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0044` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00273 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.06, expected 2.15, ratio 1.88 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.1h vs an expected 2.2h (1.88x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00273; 5 events: EV0001633, EV0001636, EV0001638, EV0001640, EV0001657 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.06,
  "duration_ratio": 1.88,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.32,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.37,
      0.6
    ],
    "dependency_wait": [
      3.25,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 9.32,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.62,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0045` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00308 (Procurement) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 10.44, expected 5.04, ratio 2.07 |
| Compared with | BL-v1:L2:BOQ Review:Medium:Medium |
| What happened | BOQ Review (Medium, Medium) took 10.4h vs an expected 5.0h (2.07x). 45% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (45%); Approval wait at Incharge stage (27%); Rework after rejection (Incorrect category) (24%); Extended executor processing (3%); Assignment queue delay (0%) |
| SOP reference | SOP-013 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00308; 9 events: EV0001839, EV0001840, EV0001850, EV0001854, EV0001858, EV0001934, EV0001940, EV0001943, EV0001947 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.04,
  "actual_duration_h": 10.44,
  "duration_ratio": 2.07,
  "baseline_p90_h": 6.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      1.25,
      1.06
    ],
    "rework": [
      1.35,
      0.0
    ],
    "approval_wait": [
      1.93,
      0.43
    ],
    "dependency_wait": [
      5.83,
      3.3
    ]
  },
  "context": {
    "task_type": "BOQ Review",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 24.07,
    "assignee_typical_week_effort_h": 28.42,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-013",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.89,
    "sop_p10_p90_h": [
      4.57,
      7.21
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.76,
      3.65
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0046` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00354 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.85, expected 2.93, ratio 2.34 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 6.9h vs an expected 2.9h (2.34x). 89% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (89%); Extended executor processing (11%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00354; 5 events: EV0002118, EV0002121, EV0002132, EV0002133, EV0002167 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 6.85,
  "duration_ratio": 2.34,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      1.27,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.48,
      0.65
    ],
    "dependency_wait": [
      5.05,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.74,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.53,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0047` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00365 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.82, expected 2.36, ratio 2.04 |
| Compared with | BL-v1:L2:Leave Approval:Simple:High |
| What happened | Leave Approval (Simple, High) took 4.8h vs an expected 2.4h (2.04x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Assignment queue delay (2%); Extended executor processing (0%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00365; 5 events: EV0002203, EV0002204, EV0002211, EV0002213, EV0002255 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.36,
  "actual_duration_h": 4.82,
  "duration_ratio": 2.04,
  "baseline_p90_h": 4.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.53,
      0.53
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.15,
      0.6
    ],
    "dependency_wait": [
      4.0,
      0.98
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.32,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.15,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0048` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00407 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.54, expected 2.22, ratio 2.04 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.5h vs an expected 2.2h (2.04x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00407; 5 events: EV0002444, EV0002445, EV0002448, EV0002450, EV0002462 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.54,
  "duration_ratio": 2.04,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.21,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.42,
      0.58
    ],
    "dependency_wait": [
      3.85,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.57,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.26,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0049` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00420 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.4, expected 2.93, ratio 1.84 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 5.4h vs an expected 2.9h (1.84x). 66% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (66%); Rework after rejection (Amount mismatch) (30%); Approval wait at Incharge stage (4%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00420; 8 events: EV0002518, EV0002519, EV0002528, EV0002529, EV0002535, EV0002537, EV0002538, EV0002540 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 5.4,
  "duration_ratio": 1.84,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.69,
      0.76
    ],
    "rework": [
      0.94,
      0.0
    ],
    "approval_wait": [
      0.77,
      0.65
    ],
    "dependency_wait": [
      2.88,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 43.91,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.66,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0050` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00423 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.73, expected 2.1, ratio 2.26 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.7h vs an expected 2.1h (2.26x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00423; 6 events: EV0002541, EV0002542, EV0002547, EV0002548, EV0002549, EV0002580 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.73,
  "duration_ratio": 2.26,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.75,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.22,
      0.56
    ],
    "dependency_wait": [
      3.73,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 26.72,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.95,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0051` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00441 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.6, expected 2.22, ratio 2.07 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.6h vs an expected 2.2h (2.07x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Extended executor processing (2%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00441; 5 events: EV0002646, EV0002648, EV0002653, EV0002654, EV0002685 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.6,
  "duration_ratio": 2.07,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.55,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.08,
      0.58
    ],
    "dependency_wait": [
      3.9,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 23.13,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.99,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0052` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00452 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 9.55, expected 5.35, ratio 1.79 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Low |
| What happened | Employee Document Verification (Medium, Low) took 9.6h vs an expected 5.3h (1.79x). 90% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (90%); Extended executor processing (10%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-021 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00452; 5 events: EV0002701, EV0002706, EV0002716, EV0002720, EV0002753 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.35,
  "actual_duration_h": 9.55,
  "duration_ratio": 1.79,
  "baseline_p90_h": 7.63,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      1.4,
      0.96
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.35,
      0.42
    ],
    "dependency_wait": [
      7.73,
      3.7
    ]
  },
  "context": {
    "task_type": "Employee Document Verification",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 21.07,
    "assignee_typical_week_effort_h": 12.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      8.08,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0053` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00455 (HR) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 4.45, expected 2.36, ratio 1.88 |
| Compared with | BL-v1:L2:Leave Approval:Simple:High |
| What happened | Leave Approval (Simple, High) took 4.5h vs an expected 2.4h (1.88x). 41% of the extra time is attributed to: rework after rejection (required document missing). |
| Most likely reason | Rework after rejection (Required document missing); preventable by S2 certificate check |
| Ranked candidate causes | Rework after rejection (Required document missing) (41%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (31%); Approval wait at Incharge stage (29%) |
| SOP reference | SOP-020 band above_p90; rework_trigger RW-DOC |
| Preventable by | S2 certificate check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00455; 8 events: EV0002717, EV0002718, EV0002722, EV0002724, EV0002732, EV0002735, EV0002737, EV0002741 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.36,
  "actual_duration_h": 4.45,
  "duration_ratio": 1.88,
  "baseline_p90_h": 4.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.34,
      0.53
    ],
    "rework": [
      1.01,
      0.0
    ],
    "approval_wait": [
      1.31,
      0.6
    ],
    "dependency_wait": [
      1.73,
      0.98
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.39,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.04,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0054` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00484 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.78, expected 2.1, ratio 1.8 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.8h vs an expected 2.1h (1.80x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00484; 5 events: EV0002913, EV0002914, EV0002918, EV0002919, EV0002926 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 3.78,
  "duration_ratio": 1.8,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.69,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.18,
      0.56
    ],
    "dependency_wait": [
      2.83,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.38,
    "assignee_typical_week_effort_h": 19.94,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.02,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0055` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00544 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.25, expected 2.93, ratio 1.79 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 5.3h vs an expected 2.9h (1.79x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Extended executor processing (1%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00544; 6 events: EV0003259, EV0003261, EV0003271, EV0003274, EV0003276, EV0003318 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 5.25,
  "duration_ratio": 1.79,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.78,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.38,
      0.65
    ],
    "dependency_wait": [
      3.98,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 25.13,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.37,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0056` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00549 (Operations) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 4.15, expected 2.25, ratio 1.84 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.1h vs an expected 2.3h (1.84x). 45% of the extra time is attributed to: rework after rejection (required document missing). |
| Most likely reason | Rework after rejection (Required document missing); preventable by S2 data completeness check |
| Ranked candidate causes | Rework after rejection (Required document missing) (45%); Approval wait at Incharge stage (30%); Extended executor processing (15%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (10%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; rework_trigger RW-DOC |
| Preventable by | S2 data completeness check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00549; 9 events: EV0003290, EV0003293, EV0003300, EV0003301, EV0003306, EV0003323, EV0003331, EV0003334, EV0003338 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.15,
  "duration_ratio": 1.84,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      1.11,
      0.79
    ],
    "rework": [
      0.95,
      0.0
    ],
    "approval_wait": [
      1.14,
      0.5
    ],
    "dependency_wait": [
      0.89,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 31.09,
    "assignee_typical_week_effort_h": 13.22,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.03,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>

### `DEV-0057` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00575 (Procurement) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 9.81, expected 5.04, ratio 1.95 |
| Compared with | BL-v1:L2:BOQ Review:Medium:Medium |
| What happened | BOQ Review (Medium, Medium) took 9.8h vs an expected 5.0h (1.95x). 42% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (42%); Rework after rejection (Amount mismatch) (30%); Approval wait at Incharge stage (25%); Extended executor processing (3%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-013 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00575; 9 events: EV0003463, EV0003465, EV0003472, EV0003474, EV0003477, EV0003516, EV0003521, EV0003523, EV0003527 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.04,
  "actual_duration_h": 9.81,
  "duration_ratio": 1.95,
  "baseline_p90_h": 6.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      1.19,
      1.06
    ],
    "rework": [
      1.48,
      0.0
    ],
    "approval_wait": [
      1.67,
      0.43
    ],
    "dependency_wait": [
      5.36,
      3.3
    ]
  },
  "context": {
    "task_type": "BOQ Review",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 41.54,
    "assignee_typical_week_effort_h": 28.42,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-013",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.89,
    "sop_p10_p90_h": [
      4.57,
      7.21
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.03,
      3.65
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0058` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00578 (HR) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 5.41, expected 2.15, ratio 2.51 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 5.4h vs an expected 2.2h (2.51x). 93% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (93%); Extended executor processing (7%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00578; 6 events: EV0003480, EV0003481, EV0003484, EV0003485, EV0003489, EV0003518 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 5.41,
  "duration_ratio": 2.51,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.7,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.6,
      0.6
    ],
    "dependency_wait": [
      4.07,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 4.38,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.67,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0059` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00611 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.1, expected 2.36, ratio 2.16 |
| Compared with | BL-v1:L2:Leave Approval:Simple:High |
| What happened | Leave Approval (Simple, High) took 5.1h vs an expected 2.4h (2.16x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Extended executor processing (1%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00611; 6 events: EV0003692, EV0003693, EV0003695, EV0003697, EV0003698, EV0003707 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.36,
  "actual_duration_h": 5.1,
  "duration_ratio": 2.16,
  "baseline_p90_h": 4.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.55,
      0.53
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.38,
      0.6
    ],
    "dependency_wait": [
      4.1,
      0.98
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 9.77,
    "assignee_typical_week_effort_h": 9.93,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.48,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0060` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00637 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.34, expected 2.94, ratio 1.82 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 5.3h vs an expected 2.9h (1.82x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00637; 7 events: EV0003846, EV0003847, EV0003849, EV0003850, EV0003852, EV0003858, EV0003890 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 5.34,
  "duration_ratio": 1.82,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.51,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.4,
      0.58
    ],
    "dependency_wait": [
      4.39,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 18.04,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.79,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0061` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00641 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.78, expected 2.15, ratio 1.76 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 3.8h vs an expected 2.2h (1.76x). 95% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (95%); Approval wait at Incharge stage (4%); Assignment queue delay (2%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00641; 6 events: EV0003868, EV0003870, EV0003871, EV0003872, EV0003878, EV0003897 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 3.78,
  "duration_ratio": 1.76,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.34,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.67,
      0.6
    ],
    "dependency_wait": [
      2.66,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 24.31,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.32,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0062` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00642 (HR) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 6.05, expected 2.36, ratio 2.56 |
| Compared with | BL-v1:L2:Leave Approval:Simple:High |
| What happened | Leave Approval (Simple, High) took 6.1h vs an expected 2.4h (2.56x). 61% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (61%); Rework after rejection (Wrong quantity) (18%); Approval wait at Incharge stage (17%); Extended executor processing (5%); Assignment queue delay (0%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00642; 10 events: EV0003873, EV0003874, EV0003879, EV0003880, EV0003883, EV0003885, EV0003900, EV0003901, EV0003902, EV0003906 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.36,
  "actual_duration_h": 6.05,
  "duration_ratio": 2.56,
  "baseline_p90_h": 4.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.73,
      0.53
    ],
    "rework": [
      0.68,
      0.0
    ],
    "approval_wait": [
      1.24,
      0.6
    ],
    "dependency_wait": [
      3.32,
      0.98
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.68,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.56,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0063` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00647 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.37, expected 2.22, ratio 1.96 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.4h vs an expected 2.2h (1.96x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00647; 7 events: EV0003914, EV0003915, EV0003917, EV0003919, EV0003923, EV0003926, EV0003973 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.37,
  "duration_ratio": 1.96,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.32,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.18,
      0.58
    ],
    "dependency_wait": [
      3.79,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 24.31,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.98,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0064` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00648 (Finance) |
| Severity / classification / confidence | high / process / medium |
| Measured | total_duration_h: observed 7.96, expected 2.93, ratio 2.71 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 8.0h vs an expected 2.9h (2.71x). 48% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (48%); Approval wait at Incharge stage (25%); Rework after rejection (Wrong quantity) (21%); Extended executor processing (5%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00648; 9 events: EV0003916, EV0003922, EV0003942, EV0003945, EV0003955, EV0003979, EV0003987, EV0003989, EV0004011 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 7.96,
  "duration_ratio": 2.71,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      1.05,
      0.76
    ],
    "rework": [
      1.19,
      0.0
    ],
    "approval_wait": [
      2.1,
      0.65
    ],
    "dependency_wait": [
      3.52,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 18.04,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.62,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0065` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00653 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.01, expected 2.22, ratio 1.8 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.0h vs an expected 2.2h (1.80x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00653; 6 events: EV0003930, EV0003931, EV0003938, EV0003941, EV0003950, EV0003977 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.01,
  "duration_ratio": 1.8,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.35,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.43,
      0.58
    ],
    "dependency_wait": [
      3.16,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 6.53,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.59,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0066` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00677 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.21, expected 2.1, ratio 2.01 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.2h vs an expected 2.1h (2.01x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00677; 6 events: EV0004100, EV0004101, EV0004102, EV0004103, EV0004104, EV0004114 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.21,
  "duration_ratio": 2.01,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.53,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.2,
      0.56
    ],
    "dependency_wait": [
      3.43,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 33.66,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.63,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0067` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00734 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.25, expected 2.93, ratio 1.79 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 5.2h vs an expected 2.9h (1.79x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00734; 6 events: EV0004449, EV0004450, EV0004454, EV0004460, EV0004462, EV0004497 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 5.25,
  "duration_ratio": 1.79,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.6,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.27,
      0.65
    ],
    "dependency_wait": [
      4.32,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 6.29,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.58,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0068` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00747 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 10.51, expected 5.35, ratio 1.97 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Low |
| What happened | Employee Document Verification (Medium, Low) took 10.5h vs an expected 5.3h (1.97x). 61% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (61%); Approval wait at Incharge stage (24%); Rework after rejection (Incorrect category) (14%); Assignment queue delay (1%) |
| SOP reference | SOP-021 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00747; 9 events: EV0004538, EV0004539, EV0004541, EV0004542, EV0004545, EV0004560, EV0004561, EV0004562, EV0004566 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.35,
  "actual_duration_h": 10.51,
  "duration_ratio": 1.97,
  "baseline_p90_h": 7.63,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.71,
      0.96
    ],
    "rework": [
      0.8,
      0.0
    ],
    "approval_wait": [
      1.77,
      0.42
    ],
    "dependency_wait": [
      7.11,
      3.7
    ]
  },
  "context": {
    "task_type": "Employee Document Verification",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.5,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      8.88,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0069` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00802 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.04, expected 3.36, ratio 1.8 |
| Compared with | BL-v1:L2:Expense Approval:Simple:High |
| What happened | Expense Approval (Simple, High) took 6.0h vs an expected 3.4h (1.80x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00802; 7 events: EV0004864, EV0004866, EV0004874, EV0004876, EV0004877, EV0004879, EV0004933 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.36,
  "actual_duration_h": 6.04,
  "duration_ratio": 1.8,
  "baseline_p90_h": 6.14,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.07
    ],
    "executor_processing": [
      0.68,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.27,
      0.6
    ],
    "dependency_wait": [
      5.03,
      1.72
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 6.29,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.29,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0070` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00825 (Procurement) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 9.7, expected 5.04, ratio 1.93 |
| Compared with | BL-v1:L2:BOQ Review:Medium:Medium |
| What happened | BOQ Review (Medium, Medium) took 9.7h vs an expected 5.0h (1.93x). 51% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (51%); Rework after rejection (Amount mismatch) (30%); Approval wait at Incharge stage (16%); Extended executor processing (3%); Assignment queue delay (1%) |
| SOP reference | SOP-013 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00825; 9 events: EV0005007, EV0005011, EV0005018, EV0005020, EV0005023, EV0005063, EV0005070, EV0005073, EV0005074 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.04,
  "actual_duration_h": 9.7,
  "duration_ratio": 1.93,
  "baseline_p90_h": 6.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      1.22,
      1.06
    ],
    "rework": [
      1.43,
      0.0
    ],
    "approval_wait": [
      1.18,
      0.43
    ],
    "dependency_wait": [
      5.75,
      3.3
    ]
  },
  "context": {
    "task_type": "BOQ Review",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 14.84,
    "assignee_typical_week_effort_h": 28.42,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-013",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.89,
    "sop_p10_p90_h": [
      4.57,
      7.21
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.93,
      3.65
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0071` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00918 (HR) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 5.4, expected 2.15, ratio 2.51 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 5.4h vs an expected 2.2h (2.51x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00918; 5 events: EV0005627, EV0005628, EV0005630, EV0005634, EV0005689 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 5.4,
  "duration_ratio": 2.51,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.43,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.35,
      0.6
    ],
    "dependency_wait": [
      4.57,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.2,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.92,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0072` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01022 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.11, expected 2.94, ratio 2.08 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 6.1h vs an expected 2.9h (2.08x). 94% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (94%); Extended executor processing (6%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01022; 5 events: EV0006246, EV0006247, EV0006248, EV0006251, EV0006261 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 6.11,
  "duration_ratio": 2.08,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      1.0,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.33,
      0.58
    ],
    "dependency_wait": [
      4.69,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 15.96,
    "assignee_typical_week_effort_h": 10.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.03,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0073` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01026 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.09, expected 2.22, ratio 2.29 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 5.1h vs an expected 2.2h (2.29x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Approval wait at Incharge stage (3%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01026; 6 events: EV0006271, EV0006272, EV0006273, EV0006274, EV0006275, EV0006278 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 5.09,
  "duration_ratio": 2.29,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.48,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.67,
      0.58
    ],
    "dependency_wait": [
      3.88,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.19,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.54,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0074` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01046 (Operations) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 3.73, expected 2.1, ratio 1.78 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.7h vs an expected 2.1h (1.78x). 43% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S3 KPI formula check |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (43%); Approval wait at Incharge stage (29%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (28%) |
| SOP reference | SOP-018 band above_p90; rework_trigger RW-AMT |
| Preventable by | S3 KPI formula check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T01046; 9 events: EV0006369, EV0006370, EV0006373, EV0006375, EV0006384, EV0006394, EV0006400, EV0006401, EV0006403 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 3.73,
  "duration_ratio": 1.78,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.66,
      0.78
    ],
    "rework": [
      0.84,
      0.0
    ],
    "approval_wait": [
      1.13,
      0.56
    ],
    "dependency_wait": [
      1.06,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.54,
    "assignee_typical_week_effort_h": 19.94,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.2,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>

### `DEV-0075` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01053 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.82, expected 2.14, ratio 1.79 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 3.8h vs an expected 2.1h (1.79x). 78% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (78%); Extended executor processing (22%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01053; 7 events: EV0006432, EV0006435, EV0006439, EV0006440, EV0006445, EV0006448, EV0006469 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 3.82,
  "duration_ratio": 1.79,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      1.21,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.42,
      0.53
    ],
    "dependency_wait": [
      2.14,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.58,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.56,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0076` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01068 (HR) |
| Severity / classification / confidence | high / process / medium |
| Measured | total_duration_h: observed 6.3, expected 2.15, ratio 2.92 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 6.3h vs an expected 2.2h (2.92x). 58% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (58%); Approval wait at Incharge stage (23%); Rework after rejection (Required document missing) (19%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01068; 9 events: EV0006516, EV0006517, EV0006518, EV0006520, EV0006523, EV0006557, EV0006568, EV0006569, EV0006586 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 6.3,
  "duration_ratio": 2.92,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.22,
      0.46
    ],
    "rework": [
      0.85,
      0.0
    ],
    "approval_wait": [
      1.64,
      0.6
    ],
    "dependency_wait": [
      3.5,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 29.91,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.14,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0077` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01088 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.09, expected 2.22, ratio 2.29 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 5.1h vs an expected 2.2h (2.29x). 82% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (82%); Extended executor processing (17%); Approval wait at Incharge stage (1%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01088; 5 events: EV0006636, EV0006637, EV0006649, EV0006654, EV0006685 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 5.09,
  "duration_ratio": 2.29,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      1.05,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.6,
      0.58
    ],
    "dependency_wait": [
      3.36,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.21,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.96,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0078` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01104 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.18, expected 2.15, ratio 1.94 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.2h vs an expected 2.2h (1.94x). 90% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (90%); Extended executor processing (7%); Approval wait at Incharge stage (3%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01104; 5 events: EV0006739, EV0006741, EV0006748, EV0006756, EV0006786 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.18,
  "duration_ratio": 1.94,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.6,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.67,
      0.6
    ],
    "dependency_wait": [
      2.84,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 9.49,
    "assignee_typical_week_effort_h": 9.93,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.51,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0079` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01117 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.69, expected 2.1, ratio 1.76 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.7h vs an expected 2.1h (1.76x). 89% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (89%); Extended executor processing (9%); Approval wait at Incharge stage (2%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01117; 5 events: EV0006821, EV0006822, EV0006826, EV0006828, EV0006831 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 3.69,
  "duration_ratio": 1.76,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.95,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.58,
      0.56
    ],
    "dependency_wait": [
      2.12,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 28.59,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.7,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0080` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01128 (HR) |
| Severity / classification / confidence | high / process / medium |
| Measured | total_duration_h: observed 7.51, expected 2.36, ratio 3.18 |
| Compared with | BL-v1:L2:Leave Approval:Simple:High |
| What happened | Leave Approval (Simple, High) took 7.5h vs an expected 2.4h (3.18x). 47% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (47%); Rework after rejection (Required document missing) (24%); Approval wait at Incharge stage (24%); Extended executor processing (4%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01128; 8 events: EV0006886, EV0006888, EV0006890, EV0006892, EV0006911, EV0006920, EV0006924, EV0006933 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.36,
  "actual_duration_h": 7.51,
  "duration_ratio": 3.18,
  "baseline_p90_h": 4.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.73,
      0.53
    ],
    "rework": [
      1.3,
      0.0
    ],
    "approval_wait": [
      1.88,
      0.6
    ],
    "dependency_wait": [
      3.47,
      0.98
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 15.21,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.34,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0081` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01139 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.7, expected 2.22, ratio 2.11 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.7h vs an expected 2.2h (2.11x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); Assignment queue delay (0%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01139; 5 events: EV0006959, EV0006960, EV0006961, EV0006964, EV0006983 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.7,
  "duration_ratio": 2.11,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.31,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.45,
      0.58
    ],
    "dependency_wait": [
      3.85,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.57,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.3,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0082` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01162 (Operations) |
| Severity / classification / confidence | medium / executor_processing / high |
| Measured | total_duration_h: observed 4.2, expected 2.25, ratio 1.86 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.2h vs an expected 2.3h (1.86x). 99% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (99%); Assignment queue delay (1%) |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T01162; 4 events: EV0007075, EV0007077, EV0007104, EV0007105 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.2,
  "duration_ratio": 1.86,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      3.73,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.37,
      0.5
    ],
    "dependency_wait": [
      0.0,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 24.51,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      0.37,
      0.0
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0083` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01172 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 10.5, expected 5.35, ratio 1.96 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Low |
| What happened | Employee Document Verification (Medium, Low) took 10.5h vs an expected 5.3h (1.96x). 64% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (64%); Approval wait at Incharge stage (24%); Rework after rejection (Incorrect category) (11%); Assignment queue delay (1%) |
| SOP reference | SOP-021 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01172; 8 events: EV0007143, EV0007145, EV0007153, EV0007157, EV0007201, EV0007203, EV0007204, EV0007208 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.35,
  "actual_duration_h": 10.5,
  "duration_ratio": 1.96,
  "baseline_p90_h": 7.63,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.9,
      0.96
    ],
    "rework": [
      0.58,
      0.0
    ],
    "approval_wait": [
      1.73,
      0.42
    ],
    "dependency_wait": [
      7.17,
      3.7
    ]
  },
  "context": {
    "task_type": "Employee Document Verification",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 10.7,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      8.9,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0084` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01197 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 18.09, expected 8.66, ratio 2.09 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 18.1h vs an expected 8.7h (2.09x). 88% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (88%); Approval wait at Incharge stage (10%); Extended executor processing (2%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01197; 6 events: EV0007320, EV0007321, EV0007327, EV0007330, EV0007369, EV0007371 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 18.09,
  "duration_ratio": 2.09,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      2.08,
      1.87
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      2.72,
      1.71
    ],
    "dependency_wait": [
      13.26,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 42.48,
    "assignee_typical_week_effort_h": 29.14,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      13.71,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0085` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01205 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 16.01, expected 8.66, ratio 1.85 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 16.0h vs an expected 8.7h (1.85x). 92% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (92%); Approval wait at Incharge stage (6%); Extended executor processing (2%); Assignment queue delay (0%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01205; 6 events: EV0007372, EV0007373, EV0007374, EV0007375, EV0007385, EV0007386 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 16.01,
  "duration_ratio": 1.85,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      2.01,
      1.87
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      2.16,
      1.71
    ],
    "dependency_wait": [
      11.74,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 19.52,
    "assignee_typical_week_effort_h": 28.42,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      12.32,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0086` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01220 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.95, expected 2.25, ratio 1.75 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.0h vs an expected 2.3h (1.75x). 93% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (93%); Extended executor processing (5%); Assignment queue delay (2%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01220; 6 events: EV0007443, EV0007445, EV0007452, EV0007453, EV0007454, EV0007459 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 3.95,
  "duration_ratio": 1.75,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.9,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.23,
      0.5
    ],
    "dependency_wait": [
      2.69,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 4.35,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.92,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0087` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01232 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.52, expected 2.25, ratio 2.0 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.5h vs an expected 2.3h (2.00x). 81% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (81%); Extended executor processing (15%); Approval wait at Incharge stage (3%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01232; 6 events: EV0007509, EV0007512, EV0007518, EV0007522, EV0007526, EV0007535 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.52,
  "duration_ratio": 2.0,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      1.15,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.57,
      0.5
    ],
    "dependency_wait": [
      2.68,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 29.67,
    "assignee_typical_week_effort_h": 17.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.25,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0088` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01257 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.88, expected 2.94, ratio 2.0 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 5.9h vs an expected 2.9h (2.00x). 95% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (95%); Extended executor processing (2%); Assignment queue delay (2%); Approval wait at Incharge stage (2%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01257; 5 events: EV0007681, EV0007682, EV0007685, EV0007691, EV0007733 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 5.88,
  "duration_ratio": 2.0,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.83,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.63,
      0.58
    ],
    "dependency_wait": [
      4.28,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.82,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.92,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0089` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01269 (Procurement) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 17.18, expected 8.66, ratio 1.99 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 17.2h vs an expected 8.7h (1.99x). 46% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (46%); Extended executor processing (29%); Rework after rejection (Incorrect category) (15%); Approval wait at Incharge stage (10%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01269; 9 events: EV0007730, EV0007734, EV0007783, EV0007784, EV0007801, EV0007802, EV0007803, EV0007804, EV0007805 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 17.18,
  "duration_ratio": 1.99,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      4.49,
      1.87
    ],
    "rework": [
      1.3,
      0.0
    ],
    "approval_wait": [
      2.55,
      1.71
    ],
    "dependency_wait": [
      8.71,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 36.92,
    "assignee_typical_week_effort_h": 24.64,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      10.65,
      4.83
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0090` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01291 (HR) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 5.63, expected 2.22, ratio 2.53 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 5.6h vs an expected 2.2h (2.53x). 71% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (71%); Rework after rejection (Amount mismatch) (25%); Extended executor processing (5%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01291; 9 events: EV0007870, EV0007873, EV0007876, EV0007877, EV0007878, EV0007898, EV0007904, EV0007907, EV0007916 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 5.63,
  "duration_ratio": 2.53,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.71,
      0.49
    ],
    "rework": [
      1.1,
      0.0
    ],
    "approval_wait": [
      3.73,
      0.58
    ],
    "dependency_wait": [
      0.0,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 21.37,
    "assignee_typical_week_effort_h": 12.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.73,
      0.8
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0091` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01294 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.51, expected 2.15, ratio 2.09 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.5h vs an expected 2.2h (2.09x). 96% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (96%); Extended executor processing (4%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01294; 5 events: EV0007901, EV0007902, EV0007909, EV0007912, EV0007922 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.51,
  "duration_ratio": 2.09,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.57,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.6,
      0.6
    ],
    "dependency_wait": [
      3.28,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 40.08,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.88,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0092` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01307 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 20.62, expected 8.96, ratio 2.3 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 20.6h vs an expected 9.0h (2.30x). 64% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (64%); Extended executor processing (16%); Approval wait at Incharge stage (14%); Rework after rejection (Incorrect category) (6%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01307; 11 events: EV0007977, EV0007978, EV0007989, EV0007994, EV0008001, EV0008004, EV0008010, EV0008016, EV0008019, EV0008028, EV0008037 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 20.62,
  "duration_ratio": 2.3,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.1
    ],
    "executor_processing": [
      3.83,
      1.9
    ],
    "rework": [
      0.76,
      0.0
    ],
    "approval_wait": [
      3.55,
      1.79
    ],
    "dependency_wait": [
      12.45,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 57.64,
    "assignee_typical_week_effort_h": 29.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      14.77,
      4.83
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0093` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01308 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 16.59, expected 9.33, ratio 1.78 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:High |
| What happened | Vendor Onboarding (Complex, High) took 16.6h vs an expected 9.3h (1.78x). 97% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (97%); Extended executor processing (3%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01308; 7 events: EV0007983, EV0007985, EV0007992, EV0007997, EV0007999, EV0008012, EV0008020 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 9.33,
  "actual_duration_h": 16.59,
  "duration_ratio": 1.78,
  "baseline_p90_h": 12.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.07
    ],
    "executor_processing": [
      2.27,
      2.01
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.03,
      1.67
    ],
    "dependency_wait": [
      13.21,
      5.36
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "High",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 42.95,
    "assignee_typical_week_effort_h": 32.36,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      13.47,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0094` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01334 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.83, expected 2.94, ratio 1.99 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 5.8h vs an expected 2.9h (1.99x). 96% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (96%); Extended executor processing (3%); Assignment queue delay (0%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01334; 5 events: EV0008144, EV0008149, EV0008163, EV0008176, EV0008248 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 5.83,
  "duration_ratio": 1.99,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.87,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.42,
      0.58
    ],
    "dependency_wait": [
      4.45,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 6.29,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.86,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0095` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01335 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 16.85, expected 9.33, ratio 1.81 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:High |
| What happened | Vendor Onboarding (Complex, High) took 16.8h vs an expected 9.3h (1.81x). 98% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (98%); Approval wait at Incharge stage (1%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01335; 6 events: EV0008145, EV0008151, EV0008171, EV0008181, EV0008260, EV0008261 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 9.33,
  "actual_duration_h": 16.85,
  "duration_ratio": 1.81,
  "baseline_p90_h": 12.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.07
    ],
    "executor_processing": [
      1.18,
      2.01
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.77,
      1.67
    ],
    "dependency_wait": [
      13.76,
      5.36
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "High",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 57.64,
    "assignee_typical_week_effort_h": 29.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      14.03,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0096` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01346 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.02, expected 2.36, ratio 2.12 |
| Compared with | BL-v1:L2:Leave Approval:Simple:High |
| What happened | Leave Approval (Simple, High) took 5.0h vs an expected 2.4h (2.12x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Extended executor processing (2%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01346; 6 events: EV0008208, EV0008209, EV0008219, EV0008221, EV0008231, EV0008254 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.36,
  "actual_duration_h": 5.02,
  "duration_ratio": 2.12,
  "baseline_p90_h": 4.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.58,
      0.53
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.45,
      0.6
    ],
    "dependency_wait": [
      3.87,
      0.98
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 29.11,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.32,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0097` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01362 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 17.1, expected 8.96, ratio 1.91 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 17.1h vs an expected 9.0h (1.91x). 100% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (100%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01362; 8 events: EV0008333, EV0008334, EV0008337, EV0008339, EV0008340, EV0008349, EV0008395, EV0008396 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 17.1,
  "duration_ratio": 1.91,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.1
    ],
    "executor_processing": [
      1.83,
      1.9
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.44,
      1.79
    ],
    "dependency_wait": [
      13.77,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 42.95,
    "assignee_typical_week_effort_h": 32.36,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      14.34,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0098` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01382 (Procurement) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 16.15, expected 8.96, ratio 1.8 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 16.1h vs an expected 9.0h (1.80x). 56% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (56%); Rework after rejection (Required document missing|Incorrect category) (32%); Cross-team / dependency wait (13%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01382; 12 events: EV0008437, EV0008439, EV0008455, EV0008456, EV0008465, EV0008467, EV0008468, EV0008469, EV0008470, EV0008471, EV0008472, EV0008473 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 16.15,
  "duration_ratio": 1.8,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.1
    ],
    "executor_processing": [
      1.76,
      1.9
    ],
    "rework": [
      2.49,
      0.0
    ],
    "approval_wait": [
      6.14,
      1.79
    ],
    "dependency_wait": [
      5.66,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 2,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 28.22,
    "assignee_typical_week_effort_h": 24.64,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      9.54,
      4.83
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0099` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01392 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.74, expected 2.1, ratio 2.26 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.7h vs an expected 2.1h (2.26x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Approval wait at Incharge stage (2%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01392; 5 events: EV0008507, EV0008509, EV0008514, EV0008525, EV0008553 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.74,
  "duration_ratio": 2.26,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.61,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.6,
      0.56
    ],
    "dependency_wait": [
      3.43,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 35.44,
    "assignee_typical_week_effort_h": 17.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.03,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0100` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01399 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.05, expected 2.15, ratio 2.35 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 5.0h vs an expected 2.2h (2.35x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Extended executor processing (2%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01399; 6 events: EV0008563, EV0008564, EV0008569, EV0008570, EV0008571, EV0008602 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 5.05,
  "duration_ratio": 2.35,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.53,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.12,
      0.6
    ],
    "dependency_wait": [
      4.33,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.53,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.45,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0101` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01411 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.94, expected 2.22, ratio 1.77 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 3.9h vs an expected 2.2h (1.77x). 96% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (96%); Assignment queue delay (2%); Extended executor processing (2%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01411; 5 events: EV0008630, EV0008631, EV0008635, EV0008640, EV0008654 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 3.94,
  "duration_ratio": 1.77,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.53,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.35,
      0.58
    ],
    "dependency_wait": [
      2.92,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 14.75,
    "assignee_typical_week_effort_h": 12.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.27,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0102` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01415 (Procurement) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 16.86, expected 9.33, ratio 1.81 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:High |
| What happened | Vendor Onboarding (Complex, High) took 16.9h vs an expected 9.3h (1.81x). 41% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (41%); Extended executor processing (26%); Approval wait at Incharge stage (19%); Rework after rejection (Amount mismatch) (14%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01415; 10 events: EV0008663, EV0008664, EV0008674, EV0008686, EV0008687, EV0008747, EV0008751, EV0008752, EV0008757, EV0008759 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 9.33,
  "actual_duration_h": 16.86,
  "duration_ratio": 1.81,
  "baseline_p90_h": 12.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.07
    ],
    "executor_processing": [
      4.01,
      2.01
    ],
    "rework": [
      1.06,
      0.0
    ],
    "approval_wait": [
      3.19,
      1.67
    ],
    "dependency_wait": [
      8.56,
      5.36
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "High",
    "dependency_count": 2,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 28.22,
    "assignee_typical_week_effort_h": 24.64,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      10.9,
      4.83
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0103` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01428 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 16.1, expected 8.66, ratio 1.86 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 16.1h vs an expected 8.7h (1.86x). 96% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (96%); Extended executor processing (4%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01428; 7 events: EV0008724, EV0008725, EV0008733, EV0008743, EV0008744, EV0008763, EV0008765 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 16.1,
  "duration_ratio": 1.86,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      2.15,
      1.87
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.52,
      1.71
    ],
    "dependency_wait": [
      12.32,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 47.59,
    "assignee_typical_week_effort_h": 29.14,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      12.95,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0104` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01439 (Procurement) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 16.16, expected 8.96, ratio 1.8 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 16.2h vs an expected 9.0h (1.80x). 42% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (42%); Approval wait at Incharge stage (31%); Rework after rejection (Amount mismatch|Wrong quantity) (24%); Extended executor processing (3%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01439; 13 events: EV0008807, EV0008810, EV0008815, EV0008819, EV0008820, EV0008828, EV0008829, EV0008830, EV0008831, EV0008832, EV0008833, EV0008834, EV0008835 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 16.16,
  "duration_ratio": 1.8,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.1
    ],
    "executor_processing": [
      2.13,
      1.9
    ],
    "rework": [
      1.86,
      0.0
    ],
    "approval_wait": [
      4.16,
      1.79
    ],
    "dependency_wait": [
      7.92,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 2,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 19.32,
    "assignee_typical_week_effort_h": 28.42,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      9.95,
      4.83
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0105` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01443 (HR) |
| Severity / classification / confidence | high / process / medium |
| Measured | total_duration_h: observed 7.94, expected 2.22, ratio 3.57 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 7.9h vs an expected 2.2h (3.57x). 48% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (48%); Approval wait at Incharge stage (27%); Rework after rejection (Required document missing) (20%); Extended executor processing (4%); Assignment queue delay (0%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01443; 8 events: EV0008841, EV0008842, EV0008844, EV0008848, EV0008877, EV0008894, EV0008900, EV0008913 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 7.94,
  "duration_ratio": 3.57,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.73,
      0.49
    ],
    "rework": [
      1.21,
      0.0
    ],
    "approval_wait": [
      2.22,
      0.58
    ],
    "dependency_wait": [
      3.68,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 9.46,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.91,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0106` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01461 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.17, expected 2.93, ratio 1.76 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 5.2h vs an expected 2.9h (1.76x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01461; 6 events: EV0008946, EV0008947, EV0008949, EV0008951, EV0008954, EV0008964 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 5.17,
  "duration_ratio": 1.76,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.66,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.4,
      0.65
    ],
    "dependency_wait": [
      4.04,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.98,
    "assignee_typical_week_effort_h": 10.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.44,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0107` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01473 (Operations) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 3.97, expected 2.1, ratio 1.9 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.0h vs an expected 2.1h (1.90x). 45% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S3 KPI formula check |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (45%); Approval wait at Incharge stage (41%); Extended executor processing (14%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; rework_trigger RW-AMT |
| Preventable by | S3 KPI formula check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T01473; 9 events: EV0009021, EV0009023, EV0009028, EV0009034, EV0009042, EV0009049, EV0009058, EV0009060, EV0009064 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 3.97,
  "duration_ratio": 1.9,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.15,
      0.78
    ],
    "rework": [
      1.18,
      0.0
    ],
    "approval_wait": [
      1.61,
      0.56
    ],
    "dependency_wait": [
      0.0,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 33.54,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      1.61,
      0.0
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0108` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01478 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 16.31, expected 8.96, ratio 1.82 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 16.3h vs an expected 9.0h (1.82x). 97% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (97%); Extended executor processing (3%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01478; 6 events: EV0009052, EV0009053, EV0009065, EV0009067, EV0009076, EV0009079 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 16.31,
  "duration_ratio": 1.82,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.1
    ],
    "executor_processing": [
      2.14,
      1.9
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.16,
      1.79
    ],
    "dependency_wait": [
      12.91,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 43.26,
    "assignee_typical_week_effort_h": 33.29,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      13.36,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0109` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01482 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 21.42, expected 8.96, ratio 2.39 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 21.4h vs an expected 9.0h (2.39x). 95% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (95%); Extended executor processing (5%); Assignment queue delay (0%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01482; 6 events: EV0009084, EV0009086, EV0009107, EV0009109, EV0009169, EV0009170 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 21.42,
  "duration_ratio": 2.39,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.1
    ],
    "executor_processing": [
      2.56,
      1.9
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.65,
      1.79
    ],
    "dependency_wait": [
      17.08,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.62,
    "assignee_typical_week_effort_h": 29.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      17.38,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0110` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01495 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.48, expected 2.22, ratio 2.01 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.5h vs an expected 2.2h (2.01x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01495; 7 events: EV0009171, EV0009172, EV0009175, EV0009177, EV0009178, EV0009184, EV0009204 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.48,
  "duration_ratio": 2.01,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.48,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.23,
      0.58
    ],
    "dependency_wait": [
      3.66,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.41,
    "assignee_typical_week_effort_h": 12.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.9,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0111` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01502 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.73, expected 2.15, ratio 2.2 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.7h vs an expected 2.2h (2.20x). 77% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (77%); Rework after rejection (Wrong quantity) (22%); Assignment queue delay (0%) |
| SOP reference | SOP-020 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01502; 7 events: EV0009200, EV0009203, EV0009207, EV0009211, EV0009215, EV0009216, EV0009236 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.73,
  "duration_ratio": 2.2,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.46,
      0.46
    ],
    "rework": [
      0.81,
      0.0
    ],
    "approval_wait": [
      3.37,
      0.6
    ],
    "dependency_wait": [
      0.0,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.9,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.37,
      0.8
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0112` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01505 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 15.21, expected 8.66, ratio 1.76 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 15.2h vs an expected 8.7h (1.76x). 100% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (100%); Assignment queue delay (0%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01505; 7 events: EV0009222, EV0009223, EV0009238, EV0009240, EV0009244, EV0009261, EV0009262 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 15.21,
  "duration_ratio": 1.76,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      1.63,
      1.87
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.3,
      1.71
    ],
    "dependency_wait": [
      12.19,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.62,
    "assignee_typical_week_effort_h": 29.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      12.55,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0113` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01513 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.63, expected 2.22, ratio 2.08 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.6h vs an expected 2.2h (2.08x). 95% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (95%); Extended executor processing (3%); Assignment queue delay (2%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01513; 5 events: EV0009272, EV0009273, EV0009279, EV0009282, EV0009306 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.63,
  "duration_ratio": 2.08,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.59,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.27,
      0.58
    ],
    "dependency_wait": [
      3.64,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.9,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.91,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0114` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01527 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 18.16, expected 8.66, ratio 2.1 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 18.2h vs an expected 8.7h (2.10x). 86% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (86%); Extended executor processing (14%); Assignment queue delay (0%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01527; 6 events: EV0009349, EV0009351, EV0009371, EV0009372, EV0009376, EV0009377 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 18.16,
  "duration_ratio": 2.1,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      3.39,
      1.87
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.99,
      1.71
    ],
    "dependency_wait": [
      13.7,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 14.12,
    "assignee_typical_week_effort_h": 29.14,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      13.86,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0115` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01539 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 11.78, expected 4.89, ratio 2.41 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Medium |
| What happened | Invoice Verification (Medium, Medium) took 11.8h vs an expected 4.9h (2.41x). 47% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (47%); Cross-team / dependency wait (39%); Rework after rejection (Amount mismatch) (14%) |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01539; 9 events: EV0009429, EV0009431, EV0009440, EV0009441, EV0009445, EV0009481, EV0009487, EV0009488, EV0009503 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 4.89,
  "actual_duration_h": 11.78,
  "duration_ratio": 2.41,
  "baseline_p90_h": 7.24,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.84,
      1.09
    ],
    "rework": [
      1.03,
      0.0
    ],
    "approval_wait": [
      3.81,
      0.4
    ],
    "dependency_wait": [
      6.04,
      3.16
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.82,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      9.85,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0116` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01544 (Finance) |
| Severity / classification / confidence | medium / process / low |
| Measured | total_duration_h: observed 12.18, expected 4.89, ratio 2.49 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Medium |
| What happened | Invoice Verification (Medium, Medium) took 12.2h vs an expected 4.9h (2.49x). 36% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (36%); Approval wait at Incharge stage (35%); Rework after rejection (Wrong quantity) (15%); Extended executor processing (14%); High assignee workload that week |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01544; 8 events: EV0009448, EV0009450, EV0009466, EV0009469, EV0009494, EV0009497, EV0009498, EV0009509 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 4.89,
  "actual_duration_h": 12.18,
  "duration_ratio": 2.49,
  "baseline_p90_h": 7.24,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      2.16,
      1.09
    ],
    "rework": [
      1.1,
      0.0
    ],
    "approval_wait": [
      2.98,
      0.4
    ],
    "dependency_wait": [
      5.88,
      3.16
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 32.85,
    "assignee_typical_week_effort_h": 10.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      8.86,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0117` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01554 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.67, expected 2.93, ratio 1.93 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 5.7h vs an expected 2.9h (1.93x). 89% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (89%); Extended executor processing (10%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01554; 4 events: EV0009528, EV0009531, EV0009539, EV0009578 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 5.67,
  "duration_ratio": 1.93,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.16,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      4.37,
      0.65
    ],
    "dependency_wait": [
      0.0,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 32.85,
    "assignee_typical_week_effort_h": 10.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.37,
      0.89
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0118` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01560 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.69, expected 2.93, ratio 1.94 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 5.7h vs an expected 2.9h (1.94x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01560; 6 events: EV0009557, EV0009558, EV0009559, EV0009561, EV0009567, EV0009600 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 5.69,
  "duration_ratio": 1.94,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.38,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.42,
      0.65
    ],
    "dependency_wait": [
      4.83,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 32.85,
    "assignee_typical_week_effort_h": 10.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.24,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0119` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01570 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.32, expected 2.94, ratio 2.15 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 6.3h vs an expected 2.9h (2.15x). 88% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (88%); Extended executor processing (12%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01570; 4 events: EV0009636, EV0009638, EV0009647, EV0009677 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 6.32,
  "duration_ratio": 2.15,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      1.34,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      4.89,
      0.58
    ],
    "dependency_wait": [
      0.0,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 32.85,
    "assignee_typical_week_effort_h": 10.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.89,
      0.89
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0120` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01576 (HR) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 3.96, expected 2.15, ratio 1.84 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.0h vs an expected 2.2h (1.84x). 51% of the extra time is attributed to: rework after rejection (incorrect category). |
| Most likely reason | Rework after rejection (Incorrect category); preventable by S2 leave type eligibility |
| Ranked candidate causes | Rework after rejection (Incorrect category) (51%); Approval wait at Incharge stage (47%); Assignment queue delay (2%); Extended executor processing (1%) |
| SOP reference | SOP-020 band above_p90; rework_trigger RW-CAT |
| Preventable by | S2 leave type eligibility |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T01576; 9 events: EV0009667, EV0009669, EV0009670, EV0009673, EV0009676, EV0009679, EV0009685, EV0009687, EV0009691 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 3.96,
  "duration_ratio": 1.84,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.47,
      0.46
    ],
    "rework": [
      1.09,
      0.0
    ],
    "approval_wait": [
      1.62,
      0.6
    ],
    "dependency_wait": [
      0.66,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 14.89,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.28,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0121` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01586 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 7.19, expected 2.94, ratio 2.45 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 7.2h vs an expected 2.9h (2.45x). 96% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (96%); Extended executor processing (4%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01586; 5 events: EV0009732, EV0009733, EV0009736, EV0009738, EV0009767 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 7.19,
  "duration_ratio": 2.45,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.97,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.27,
      0.58
    ],
    "dependency_wait": [
      5.93,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 10.76,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.2,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0122` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01589 (HR) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 9.5, expected 5.19, ratio 1.83 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Medium |
| What happened | Employee Document Verification (Medium, Medium) took 9.5h vs an expected 5.2h (1.83x). 57% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (57%); Rework after rejection (Required document missing) (20%); Approval wait at Incharge stage (17%); Extended executor processing (5%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-021 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01589; 9 events: EV0009741, EV0009744, EV0009754, EV0009756, EV0009757, EV0009769, EV0009771, EV0009772, EV0009773 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.19,
  "actual_duration_h": 9.5,
  "duration_ratio": 1.83,
  "baseline_p90_h": 7.35,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.16,
      0.96
    ],
    "rework": [
      0.89,
      0.0
    ],
    "approval_wait": [
      1.17,
      0.4
    ],
    "dependency_wait": [
      6.14,
      3.59
    ]
  },
  "context": {
    "task_type": "Employee Document Verification",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 15.12,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.31,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0123` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01590 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.78, expected 2.94, ratio 1.97 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 5.8h vs an expected 2.9h (1.97x). 99% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (99%); Assignment queue delay (1%) |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01590; 4 events: EV0009746, EV0009747, EV0009753, EV0009768 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 5.78,
  "duration_ratio": 1.97,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.54,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      5.1,
      0.58
    ],
    "dependency_wait": [
      0.0,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.45,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.1,
      0.89
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0124` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01595 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 9.44, expected 5.16, ratio 1.83 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 9.4h vs an expected 5.2h (1.83x). 55% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (55%); Rework after rejection (Required document missing) (26%); Cross-team / dependency wait (18%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01595; 9 events: EV0009780, EV0009782, EV0009785, EV0009790, EV0009792, EV0009822, EV0009836, EV0009837, EV0009845 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.16,
  "actual_duration_h": 9.44,
  "duration_ratio": 1.83,
  "baseline_p90_h": 7.62,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.76,
      1.11
    ],
    "rework": [
      1.27,
      0.0
    ],
    "approval_wait": [
      3.1,
      0.38
    ],
    "dependency_wait": [
      4.18,
      3.27
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 21.77,
    "assignee_typical_week_effort_h": 13.0,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.28,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0125` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01596 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.39, expected 2.94, ratio 1.84 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 5.4h vs an expected 2.9h (1.84x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Extended executor processing (2%); Assignment queue delay (1%); Approval wait at Incharge stage (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01596; 5 events: EV0009783, EV0009786, EV0009793, EV0009794, EV0009827 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 5.39,
  "duration_ratio": 1.84,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.81,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.6,
      0.58
    ],
    "dependency_wait": [
      3.88,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 21.77,
    "assignee_typical_week_effort_h": 13.0,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.48,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0126` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01597 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 17.68, expected 8.66, ratio 2.04 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 17.7h vs an expected 8.7h (2.04x). 94% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (94%); Approval wait at Incharge stage (3%); Extended executor processing (2%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01597; 6 events: EV0009787, EV0009789, EV0009797, EV0009801, EV0009857, EV0009858 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 17.68,
  "duration_ratio": 2.04,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      2.03,
      1.87
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      2.03,
      1.71
    ],
    "dependency_wait": [
      13.49,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 44.7,
    "assignee_typical_week_effort_h": 29.14,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      14.09,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0127` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01601 (Operations) |
| Severity / classification / confidence | medium / executor_processing / medium |
| Measured | total_duration_h: observed 5.46, expected 2.25, ratio 2.43 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 5.5h vs an expected 2.3h (2.43x). 41% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (41%); Approval wait at Incharge stage (31%); Rework after rejection (Amount mismatch) (28%); Assignment queue delay (0%) |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T01601; 8 events: EV0009804, EV0009806, EV0009826, EV0009833, EV0009838, EV0009842, EV0009843, EV0009844 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 5.46,
  "duration_ratio": 2.43,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      2.46,
      0.79
    ],
    "rework": [
      1.13,
      0.0
    ],
    "approval_wait": [
      1.79,
      0.5
    ],
    "dependency_wait": [
      0.0,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.09,
    "assignee_typical_week_effort_h": 13.22,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      1.79,
      0.0
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0128` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01610 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 17.24, expected 8.96, ratio 1.92 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 17.2h vs an expected 9.0h (1.92x). 100% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (100%); Assignment queue delay (0%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01610; 8 events: EV0009884, EV0009885, EV0009888, EV0009889, EV0009892, EV0009893, EV0009898, EV0009899 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 17.24,
  "duration_ratio": 1.92,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.1
    ],
    "executor_processing": [
      1.42,
      1.9
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.54,
      1.79
    ],
    "dependency_wait": [
      14.16,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 24.37,
    "assignee_typical_week_effort_h": 28.42,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      14.33,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0129` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01611 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.53, expected 2.93, ratio 2.23 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 6.5h vs an expected 2.9h (2.23x). 93% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (93%); Extended executor processing (6%); Assignment queue delay (1%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01611; 6 events: EV0009900, EV0009901, EV0009903, EV0009905, EV0009906, EV0009924 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 6.53,
  "duration_ratio": 2.23,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.02,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.42,
      0.65
    ],
    "dependency_wait": [
      4.96,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 2.93,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.38,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0130` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01613 (HR) |
| Severity / classification / confidence | medium / rework / low |
| Measured | total_duration_h: observed 5.04, expected 2.36, ratio 2.13 |
| Compared with | BL-v1:L2:Leave Approval:Simple:High |
| What happened | Leave Approval (Simple, High) took 5.0h vs an expected 2.4h (2.13x). 39% of the extra time is attributed to: rework after rejection (wrong quantity). |
| Most likely reason | Rework after rejection (Wrong quantity); preventable by S3 day count excluding holidays |
| Ranked candidate causes | Rework after rejection (Wrong quantity) (39%); Approval wait at Incharge stage (30%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (27%); Extended executor processing (4%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; rework_trigger RW-QTY |
| Preventable by | S3 day count excluding holidays |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T01613; 8 events: EV0009909, EV0009910, EV0009913, EV0009915, EV0009922, EV0009926, EV0009927, EV0009931 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.36,
  "actual_duration_h": 5.04,
  "duration_ratio": 2.13,
  "baseline_p90_h": 4.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.64,
      0.53
    ],
    "rework": [
      1.13,
      0.0
    ],
    "approval_wait": [
      1.48,
      0.6
    ],
    "dependency_wait": [
      1.76,
      0.98
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 15.12,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.24,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0131` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01614 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.25, expected 3.36, ratio 1.86 |
| Compared with | BL-v1:L2:Expense Approval:Simple:High |
| What happened | Expense Approval (Simple, High) took 6.3h vs an expected 3.4h (1.86x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Assignment queue delay (2%); Extended executor processing (0%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01614; 5 events: EV0009912, EV0009914, EV0009917, EV0009919, EV0009935 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.36,
  "actual_duration_h": 6.25,
  "duration_ratio": 1.86,
  "baseline_p90_h": 6.14,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.07
    ],
    "executor_processing": [
      0.79,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.3,
      0.6
    ],
    "dependency_wait": [
      5.03,
      1.72
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.45,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.33,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0132` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01627 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 16.99, expected 8.66, ratio 1.96 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 17.0h vs an expected 8.7h (1.96x). 88% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (88%); Rework after rejection (Incorrect category) (8%); Extended executor processing (2%); Approval wait at Incharge stage (1%); Assignment queue delay (0%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01627; 9 events: EV0009979, EV0009980, EV0009998, EV0010001, EV0010029, EV0010030, EV0010032, EV0010033, EV0010034 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 16.99,
  "duration_ratio": 1.96,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      2.02,
      1.87
    ],
    "rework": [
      0.72,
      0.0
    ],
    "approval_wait": [
      1.82,
      1.71
    ],
    "dependency_wait": [
      12.33,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.62,
    "assignee_typical_week_effort_h": 29.14,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      13.57,
      4.83
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0133` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01644 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 10.67, expected 3.36, ratio 3.18 |
| Compared with | BL-v1:L2:Expense Approval:Simple:High |
| What happened | Expense Approval (Simple, High) took 10.7h vs an expected 3.4h (3.18x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01644; 7 events: EV0010091, EV0010092, EV0010095, EV0010096, EV0010098, EV0010102, EV0010124 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.36,
  "actual_duration_h": 10.67,
  "duration_ratio": 3.18,
  "baseline_p90_h": 6.14,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.07
    ],
    "executor_processing": [
      0.66,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.45,
      0.6
    ],
    "dependency_wait": [
      9.44,
      1.72
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.45,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      9.89,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0134` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01647 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 18.5, expected 8.96, ratio 2.06 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 18.5h vs an expected 9.0h (2.06x). 98% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (98%); Extended executor processing (2%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01647; 7 events: EV0010127, EV0010128, EV0010145, EV0010148, EV0010151, EV0010224, EV0010225 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 18.5,
  "duration_ratio": 2.06,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.1
    ],
    "executor_processing": [
      2.13,
      1.9
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.58,
      1.79
    ],
    "dependency_wait": [
      14.76,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 97.92,
    "assignee_typical_week_effort_h": 29.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      15.09,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0135` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01649 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.01, expected 2.93, ratio 2.05 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 6.0h vs an expected 2.9h (2.05x). 92% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (92%); Extended executor processing (7%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01649; 4 events: EV0010131, EV0010132, EV0010141, EV0010181 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 6.01,
  "duration_ratio": 2.05,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.07,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      4.81,
      0.65
    ],
    "dependency_wait": [
      0.0,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 26.42,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.81,
      0.89
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0136` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01656 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 20.96, expected 8.66, ratio 2.42 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 21.0h vs an expected 8.7h (2.42x). 99% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (99%); Approval wait at Incharge stage (1%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01656; 6 events: EV0010167, EV0010168, EV0010179, EV0010180, EV0010226, EV0010227 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 20.96,
  "duration_ratio": 2.42,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.35,
      1.87
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.82,
      1.71
    ],
    "dependency_wait": [
      17.75,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 97.92,
    "assignee_typical_week_effort_h": 29.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      17.98,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0137` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01659 (HR) |
| Severity / classification / confidence | medium / rework / high |
| Measured | total_duration_h: observed 4.09, expected 2.15, ratio 1.9 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.1h vs an expected 2.2h (1.90x). 62% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S2 balance check |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (62%); Approval wait at Incharge stage (30%); Extended executor processing (7%); Assignment queue delay (2%) |
| SOP reference | SOP-020 band above_p90; rework_trigger RW-AMT |
| Preventable by | S2 balance check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T01659; 8 events: EV0010186, EV0010188, EV0010195, EV0010202, EV0010209, EV0010214, EV0010215, EV0010218 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.09,
  "duration_ratio": 1.9,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.6,
      0.46
    ],
    "rework": [
      1.28,
      0.0
    ],
    "approval_wait": [
      1.21,
      0.6
    ],
    "dependency_wait": [
      0.88,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.53,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.09,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0138` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01666 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 19.89, expected 8.96, ratio 2.22 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 19.9h vs an expected 9.0h (2.22x). 78% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (78%); Approval wait at Incharge stage (12%); Rework after rejection (Amount mismatch) (10%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01666; 10 events: EV0010241, EV0010242, EV0010245, EV0010251, EV0010252, EV0010267, EV0010268, EV0010269, EV0010270, EV0010301 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 19.89,
  "duration_ratio": 2.22,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.1
    ],
    "executor_processing": [
      1.33,
      1.9
    ],
    "rework": [
      1.2,
      0.0
    ],
    "approval_wait": [
      3.26,
      1.79
    ],
    "dependency_wait": [
      13.99,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 97.92,
    "assignee_typical_week_effort_h": 29.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      14.91,
      4.83
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0139` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01671 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.43, expected 2.94, ratio 2.19 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 6.4h vs an expected 2.9h (2.19x). 88% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (88%); Extended executor processing (12%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01671; 6 events: EV0010273, EV0010274, EV0010280, EV0010287, EV0010290, EV0010336 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 6.43,
  "duration_ratio": 2.19,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      1.23,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.38,
      0.58
    ],
    "dependency_wait": [
      4.7,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 20.25,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.09,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0140` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01672 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 7.05, expected 2.93, ratio 2.41 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 7.1h vs an expected 2.9h (2.41x). 85% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (85%); Extended executor processing (15%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01672; 7 events: EV0010275, EV0010276, EV0010291, EV0010293, EV0010294, EV0010302, EV0010345 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 7.05,
  "duration_ratio": 2.41,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      1.5,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.52,
      0.65
    ],
    "dependency_wait": [
      4.94,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 20.25,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.46,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0141` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01687 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 19.9, expected 8.96, ratio 2.22 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 19.9h vs an expected 9.0h (2.22x). 99% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (99%); Extended executor processing (1%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01687; 6 events: EV0010356, EV0010357, EV0010363, EV0010364, EV0010379, EV0010380 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 19.9,
  "duration_ratio": 2.22,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.1
    ],
    "executor_processing": [
      2.02,
      1.9
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.34,
      1.79
    ],
    "dependency_wait": [
      16.44,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 34.37,
    "assignee_typical_week_effort_h": 32.36,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      16.77,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0142` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01697 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.14, expected 2.25, ratio 1.84 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.1h vs an expected 2.3h (1.84x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01697; 7 events: EV0010418, EV0010419, EV0010420, EV0010421, EV0010422, EV0010425, EV0010433 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.14,
  "duration_ratio": 1.84,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.55,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.42,
      0.5
    ],
    "dependency_wait": [
      3.11,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 4.35,
    "assignee_typical_week_effort_h": 15.58,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.52,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0143` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01700 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 7.47, expected 3.36, ratio 2.22 |
| Compared with | BL-v1:L2:Expense Approval:Simple:High |
| What happened | Expense Approval (Simple, High) took 7.5h vs an expected 3.4h (2.22x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Extended executor processing (3%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01700; 6 events: EV0010438, EV0010439, EV0010444, EV0010446, EV0010450, EV0010511 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.36,
  "actual_duration_h": 7.47,
  "duration_ratio": 2.22,
  "baseline_p90_h": 6.14,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.07
    ],
    "executor_processing": [
      0.92,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.3,
      0.6
    ],
    "dependency_wait": [
      6.22,
      1.72
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 3.36,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.52,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0144` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01701 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 13.11, expected 2.94, ratio 4.46 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 13.1h vs an expected 2.9h (4.46x). 69% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (69%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (24%); Rework after rejection (Amount mismatch) (7%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01701; 8 events: EV0010440, EV0010442, EV0010452, EV0010454, EV0010492, EV0010497, EV0010500, EV0010536 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 13.11,
  "duration_ratio": 4.46,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.74,
      0.76
    ],
    "rework": [
      0.71,
      0.0
    ],
    "approval_wait": [
      7.9,
      0.58
    ],
    "dependency_wait": [
      3.65,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 24.28,
    "assignee_typical_week_effort_h": 10.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      11.55,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0145` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01709 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.38, expected 2.15, ratio 2.03 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.4h vs an expected 2.2h (2.03x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Assignment queue delay (2%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01709; 6 events: EV0010477, EV0010479, EV0010481, EV0010484, EV0010488, EV0010519 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.38,
  "duration_ratio": 2.03,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.39,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.35,
      0.6
    ],
    "dependency_wait": [
      3.51,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 20.4,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.86,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0146` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01718 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.84, expected 2.1, ratio 2.31 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.8h vs an expected 2.1h (2.31x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Approval wait at Incharge stage (3%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01718; 5 events: EV0010544, EV0010546, EV0010551, EV0010552, EV0010592 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.84,
  "duration_ratio": 2.31,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.71,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.63,
      0.56
    ],
    "dependency_wait": [
      3.43,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 31.41,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.06,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0147` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01719 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 15.66, expected 8.66, ratio 1.81 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 15.7h vs an expected 8.7h (1.81x). 98% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (98%); Extended executor processing (1%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01719; 6 events: EV0010548, EV0010550, EV0010564, EV0010568, EV0010626, EV0010627 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 15.66,
  "duration_ratio": 1.81,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.94,
      1.87
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.64,
      1.71
    ],
    "dependency_wait": [
      11.94,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 47.14,
    "assignee_typical_week_effort_h": 32.36,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      12.32,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0148` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01724 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.46, expected 2.36, ratio 2.31 |
| Compared with | BL-v1:L2:Leave Approval:Simple:High |
| What happened | Leave Approval (Simple, High) took 5.5h vs an expected 2.4h (2.31x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Assignment queue delay (2%); Approval wait at Incharge stage (1%); Extended executor processing (0%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01724; 5 events: EV0010563, EV0010565, EV0010571, EV0010582, EV0010615 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.36,
  "actual_duration_h": 5.46,
  "duration_ratio": 2.31,
  "baseline_p90_h": 4.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.54,
      0.53
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.63,
      0.6
    ],
    "dependency_wait": [
      4.15,
      0.98
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 27.46,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.79,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0149` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01739 (HR) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 10.35, expected 5.19, ratio 1.99 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Medium |
| What happened | Employee Document Verification (Medium, Medium) took 10.3h vs an expected 5.2h (1.99x). 49% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (49%); Approval wait at Incharge stage (28%); Rework after rejection (Incorrect category) (22%) |
| SOP reference | SOP-021 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01739; 8 events: EV0010656, EV0010658, EV0010675, EV0010680, EV0010704, EV0010706, EV0010707, EV0010708 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.19,
  "actual_duration_h": 10.35,
  "duration_ratio": 1.99,
  "baseline_p90_h": 7.35,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.82,
      0.96
    ],
    "rework": [
      1.23,
      0.0
    ],
    "approval_wait": [
      1.95,
      0.4
    ],
    "dependency_wait": [
      6.31,
      3.59
    ]
  },
  "context": {
    "task_type": "Employee Document Verification",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.69,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      8.26,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0150` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01751 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 16.65, expected 8.96, ratio 1.86 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 16.7h vs an expected 9.0h (1.86x). 71% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (71%); Extended executor processing (19%); Approval wait at Incharge stage (10%); Assignment queue delay (0%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01751; 7 events: EV0010732, EV0010735, EV0010750, EV0010758, EV0010762, EV0010793, EV0010794 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 16.65,
  "duration_ratio": 1.86,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.1
    ],
    "executor_processing": [
      3.47,
      1.9
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      2.59,
      1.79
    ],
    "dependency_wait": [
      10.45,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 39.5,
    "assignee_typical_week_effort_h": 33.29,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      10.55,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0151` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01755 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 15.43, expected 8.66, ratio 1.78 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 15.4h vs an expected 8.7h (1.78x). 100% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (100%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01755; 6 events: EV0010760, EV0010761, EV0010772, EV0010777, EV0010795, EV0010796 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 15.43,
  "duration_ratio": 1.78,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.81,
      1.87
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.33,
      1.71
    ],
    "dependency_wait": [
      12.25,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.56,
    "assignee_typical_week_effort_h": 29.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      12.84,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0152` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01762 (Procurement) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 23.58, expected 8.96, ratio 2.63 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 23.6h vs an expected 9.0h (2.63x). 95% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (95%); Extended executor processing (5%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01762; 6 events: EV0010802, EV0010803, EV0010820, EV0010824, EV0010913, EV0010916 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 23.58,
  "duration_ratio": 2.63,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.1
    ],
    "executor_processing": [
      2.64,
      1.9
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.58,
      1.79
    ],
    "dependency_wait": [
      19.33,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 38.8,
    "assignee_typical_week_effort_h": 24.64,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      19.75,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0153` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01766 (Finance) |
| Severity / classification / confidence | high / process / medium |
| Measured | total_duration_h: observed 8.61, expected 2.93, ratio 2.94 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 8.6h vs an expected 2.9h (2.94x). 59% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (59%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (28%); Rework after rejection (Wrong quantity) (13%) |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01766; 9 events: EV0010828, EV0010829, EV0010836, EV0010837, EV0010844, EV0010875, EV0010885, EV0010887, EV0010907 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 8.61,
  "duration_ratio": 2.94,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.71,
      0.76
    ],
    "rework": [
      0.83,
      0.0
    ],
    "approval_wait": [
      4.42,
      0.65
    ],
    "dependency_wait": [
      2.62,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 2.93,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.04,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0154` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01777 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 16.57, expected 8.66, ratio 1.91 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 16.6h vs an expected 8.7h (1.91x). 100% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (100%); Assignment queue delay (0%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01777; 7 events: EV0010880, EV0010881, EV0010893, EV0010897, EV0010900, EV0010917, EV0010918 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 16.57,
  "duration_ratio": 1.91,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      1.74,
      1.87
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.1,
      1.71
    ],
    "dependency_wait": [
      13.63,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 39.5,
    "assignee_typical_week_effort_h": 33.29,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      14.05,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0155` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01793 (Finance) |
| Severity / classification / confidence | high / process / medium |
| Measured | total_duration_h: observed 9.86, expected 2.93, ratio 3.36 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 9.9h vs an expected 2.9h (3.36x). 50% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (50%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (40%); Rework after rejection (Wrong quantity) (10%) |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01793; 8 events: EV0011004, EV0011005, EV0011009, EV0011012, EV0011049, EV0011055, EV0011063, EV0011112 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 9.86,
  "duration_ratio": 3.36,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.74,
      0.76
    ],
    "rework": [
      0.76,
      0.0
    ],
    "approval_wait": [
      4.46,
      0.65
    ],
    "dependency_wait": [
      3.87,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 8.09,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      8.33,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0156` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01798 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 16.83, expected 8.96, ratio 1.88 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 16.8h vs an expected 9.0h (1.88x). 87% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (87%); Extended executor processing (13%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01798; 7 events: EV0011027, EV0011028, EV0011050, EV0011065, EV0011069, EV0011129, EV0011132 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 16.83,
  "duration_ratio": 1.88,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.1
    ],
    "executor_processing": [
      3.07,
      1.9
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.25,
      1.79
    ],
    "dependency_wait": [
      12.42,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 49.22,
    "assignee_typical_week_effort_h": 24.64,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      12.71,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0157` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01799 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 7.26, expected 2.94, ratio 2.47 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 7.3h vs an expected 2.9h (2.47x). 96% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (96%); Extended executor processing (3%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01799; 7 events: EV0011037, EV0011038, EV0011044, EV0011045, EV0011047, EV0011048, EV0011117 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 7.26,
  "duration_ratio": 2.47,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.91,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.38,
      0.58
    ],
    "dependency_wait": [
      5.84,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 20.96,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.22,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0158` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01801 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 16.45, expected 8.66, ratio 1.9 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 16.4h vs an expected 8.7h (1.90x). 100% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (100%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01801; 6 events: EV0011041, EV0011042, EV0011058, EV0011068, EV0011134, EV0011135 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 16.45,
  "duration_ratio": 1.9,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      1.35,
      1.87
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.06,
      1.71
    ],
    "dependency_wait": [
      13.99,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 64.08,
    "assignee_typical_week_effort_h": 28.42,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      14.49,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0159` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01807 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 17.24, expected 8.66, ratio 1.99 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 17.2h vs an expected 8.7h (1.99x). 96% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (96%); Approval wait at Incharge stage (4%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01807; 7 events: EV0011062, EV0011066, EV0011086, EV0011090, EV0011093, EV0011136, EV0011145 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.66,
  "actual_duration_h": 17.24,
  "duration_ratio": 1.99,
  "baseline_p90_h": 12.77,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.42,
      1.87
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      2.1,
      1.71
    ],
    "dependency_wait": [
      13.69,
      4.63
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 64.08,
    "assignee_typical_week_effort_h": 28.42,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      13.81,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0160` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01827 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.05, expected 2.93, ratio 2.06 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 6.0h vs an expected 2.9h (2.06x). 93% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (93%); Extended executor processing (7%) |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01827; 4 events: EV0011199, EV0011200, EV0011214, EV0011253 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 6.05,
  "duration_ratio": 2.06,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.09,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      4.92,
      0.65
    ],
    "dependency_wait": [
      0.0,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 16.34,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.92,
      0.89
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0161` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01837 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 18.96, expected 8.96, ratio 2.12 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 19.0h vs an expected 9.0h (2.12x). 96% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (96%); Approval wait at Incharge stage (4%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01837; 6 events: EV0011278, EV0011279, EV0011285, EV0011288, EV0011331, EV0011333 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 18.96,
  "duration_ratio": 2.12,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.1
    ],
    "executor_processing": [
      1.01,
      1.9
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      2.24,
      1.79
    ],
    "dependency_wait": [
      15.61,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 42.13,
    "assignee_typical_week_effort_h": 32.36,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      15.88,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0162` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01841 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 17.12, expected 8.96, ratio 1.91 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 17.1h vs an expected 9.0h (1.91x). 100% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (100%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01841; 6 events: EV0011296, EV0011297, EV0011299, EV0011303, EV0011332, EV0011334 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 17.12,
  "duration_ratio": 1.91,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.1
    ],
    "executor_processing": [
      1.17,
      1.9
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.17,
      1.79
    ],
    "dependency_wait": [
      14.73,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 64.08,
    "assignee_typical_week_effort_h": 28.42,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      15.31,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0163` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01849 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 16.85, expected 8.96, ratio 1.88 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 16.9h vs an expected 9.0h (1.88x). 100% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (100%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01849; 6 events: EV0011344, EV0011345, EV0011354, EV0011361, EV0011418, EV0011419 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 16.85,
  "duration_ratio": 1.88,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.1
    ],
    "executor_processing": [
      1.56,
      1.9
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.45,
      1.79
    ],
    "dependency_wait": [
      13.76,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 64.08,
    "assignee_typical_week_effort_h": 28.42,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      14.09,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0164` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01853 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.89, expected 2.94, ratio 2.01 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 5.9h vs an expected 2.9h (2.01x). 90% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (90%); Extended executor processing (9%); Assignment queue delay (1%) |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01853; 4 events: EV0011357, EV0011359, EV0011365, EV0011404 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 5.89,
  "duration_ratio": 2.01,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.17,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      4.59,
      0.58
    ],
    "dependency_wait": [
      0.0,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.97,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.59,
      0.89
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0165` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01856 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 7.57, expected 3.36, ratio 2.25 |
| Compared with | BL-v1:L2:Expense Approval:Simple:High |
| What happened | Expense Approval (Simple, High) took 7.6h vs an expected 3.4h (2.25x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01856; 5 events: EV0011374, EV0011376, EV0011381, EV0011384, EV0011415 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.36,
  "actual_duration_h": 7.57,
  "duration_ratio": 2.25,
  "baseline_p90_h": 6.14,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.07
    ],
    "executor_processing": [
      0.79,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.53,
      0.6
    ],
    "dependency_wait": [
      6.13,
      1.72
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 20.96,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.66,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0166` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01860 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.24, expected 3.36, ratio 1.86 |
| Compared with | BL-v1:L2:Expense Approval:Simple:High |
| What happened | Expense Approval (Simple, High) took 6.2h vs an expected 3.4h (1.86x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Approval wait at Incharge stage (2%); Assignment queue delay (1%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01860; 5 events: EV0011390, EV0011393, EV0011396, EV0011402, EV0011416 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.36,
  "actual_duration_h": 6.24,
  "duration_ratio": 1.86,
  "baseline_p90_h": 6.14,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.07
    ],
    "executor_processing": [
      0.57,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.65,
      0.6
    ],
    "dependency_wait": [
      4.92,
      1.72
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 16.34,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.57,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0167` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01862 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.98, expected 2.93, ratio 2.04 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 6.0h vs an expected 2.9h (2.04x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01862; 5 events: EV0011422, EV0011423, EV0011427, EV0011434, EV0011478 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 5.98,
  "duration_ratio": 2.04,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.66,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.52,
      0.65
    ],
    "dependency_wait": [
      4.69,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 8.09,
    "assignee_typical_week_effort_h": 10.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.21,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0168` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01871 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 9.62, expected 5.16, ratio 1.87 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 9.6h vs an expected 5.2h (1.87x). 49% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (49%); Approval wait at Incharge stage (28%); Rework after rejection (Amount mismatch) (23%); Assignment queue delay (1%) |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01871; 8 events: EV0011455, EV0011456, EV0011468, EV0011469, EV0011514, EV0011520, EV0011521, EV0011524 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.16,
  "actual_duration_h": 9.62,
  "duration_ratio": 1.87,
  "baseline_p90_h": 7.62,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.06,
      1.11
    ],
    "rework": [
      1.1,
      0.0
    ],
    "approval_wait": [
      1.71,
      0.38
    ],
    "dependency_wait": [
      5.62,
      3.27
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 16.34,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.34,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0169` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01872 (Procurement) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 21.58, expected 8.96, ratio 2.41 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Low |
| What happened | Vendor Onboarding (Complex, Low) took 21.6h vs an expected 9.0h (2.41x). 93% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (93%); Extended executor processing (7%); High assignee workload that week |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01872; 6 events: EV0011464, EV0011466, EV0011482, EV0011484, EV0011528, EV0011529 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.96,
  "actual_duration_h": 21.58,
  "duration_ratio": 2.41,
  "baseline_p90_h": 14.11,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.1
    ],
    "executor_processing": [
      2.85,
      1.9
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.63,
      1.79
    ],
    "dependency_wait": [
      17.03,
      4.66
    ]
  },
  "context": {
    "task_type": "Vendor Onboarding",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 42.13,
    "assignee_typical_week_effort_h": 32.36,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-017",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 11.97,
    "sop_p10_p90_h": [
      9.86,
      14.08
    ],
    "first_decision_wait_actual_vs_sop_h": [
      17.11,
      4.83
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0170` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01874 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.83, expected 2.1, ratio 2.31 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.8h vs an expected 2.1h (2.31x). 84% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (84%); Extended executor processing (16%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01874; 5 events: EV0011474, EV0011475, EV0011487, EV0011490, EV0011515 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.83,
  "duration_ratio": 2.31,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      1.29,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.32,
      0.56
    ],
    "dependency_wait": [
      3.18,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.73,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.5,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0171` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01893 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 8.83, expected 2.93, ratio 3.01 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 8.8h vs an expected 2.9h (3.01x). 96% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (96%); Extended executor processing (4%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01893; 6 events: EV0011589, EV0011591, EV0011594, EV0011597, EV0011606, EV0011653 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 8.83,
  "duration_ratio": 3.01,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      1.0,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.65,
      0.65
    ],
    "dependency_wait": [
      7.06,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 22.09,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.71,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0172` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01895 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 10.36, expected 2.94, ratio 3.53 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 10.4h vs an expected 2.9h (3.53x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01895; 5 events: EV0011603, EV0011604, EV0011611, EV0011612, EV0011674 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 10.36,
  "duration_ratio": 3.53,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.75,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.23,
      0.58
    ],
    "dependency_wait": [
      9.33,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.98,
    "assignee_typical_week_effort_h": 10.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      9.56,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0173` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01908 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.67, expected 2.22, ratio 2.1 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.7h vs an expected 2.2h (2.10x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Extended executor processing (2%); Approval wait at Incharge stage (1%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01908; 6 events: EV0011688, EV0011690, EV0011693, EV0011694, EV0011698, EV0011726 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.67,
  "duration_ratio": 2.1,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.55,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.6,
      0.58
    ],
    "dependency_wait": [
      3.45,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 16.56,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.05,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0174` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01911 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.05, expected 2.22, ratio 1.82 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.1h vs an expected 2.2h (1.82x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01911; 5 events: EV0011702, EV0011703, EV0011707, EV0011709, EV0011747 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.05,
  "duration_ratio": 1.82,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.29,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.23,
      0.58
    ],
    "dependency_wait": [
      3.46,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.75,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.69,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0175` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01920 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.92, expected 2.93, ratio 2.36 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 6.9h vs an expected 2.9h (2.36x). 96% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (96%); Extended executor processing (4%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01920; 6 events: EV0011750, EV0011751, EV0011756, EV0011759, EV0011762, EV0011789 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 6.92,
  "duration_ratio": 2.36,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.96,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.08,
      0.65
    ],
    "dependency_wait": [
      5.81,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.69,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.89,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0176` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01924 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.84, expected 2.14, ratio 1.8 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 3.8h vs an expected 2.1h (1.80x). 88% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (88%); Extended executor processing (11%); Assignment queue delay (1%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01924; 5 events: EV0011794, EV0011795, EV0011806, EV0011808, EV0011838 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 3.84,
  "duration_ratio": 1.8,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      1.01,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.12,
      0.53
    ],
    "dependency_wait": [
      2.61,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 2.14,
    "assignee_typical_week_effort_h": 19.94,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.73,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0177` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01930 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 9.08, expected 5.16, ratio 1.76 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 9.1h vs an expected 5.2h (1.76x). 42% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (42%); Approval wait at Incharge stage (28%); Rework after rejection (Incorrect category) (20%); Extended executor processing (10%); High assignee workload that week |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01930; 8 events: EV0011815, EV0011816, EV0011834, EV0011837, EV0011890, EV0011896, EV0011898, EV0011901 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.16,
  "actual_duration_h": 9.08,
  "duration_ratio": 1.76,
  "baseline_p90_h": 7.62,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.55,
      1.11
    ],
    "rework": [
      0.84,
      0.0
    ],
    "approval_wait": [
      1.58,
      0.38
    ],
    "dependency_wait": [
      5.08,
      3.27
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 28.22,
    "assignee_typical_week_effort_h": 13.0,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.66,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0178` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01931 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.99, expected 2.14, ratio 2.34 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 5.0h vs an expected 2.1h (2.34x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Extended executor processing (3%); Assignment queue delay (0%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01931; 5 events: EV0011819, EV0011821, EV0011830, EV0011836, EV0011868 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 4.99,
  "duration_ratio": 2.34,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.85,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.37,
      0.53
    ],
    "dependency_wait": [
      3.69,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 15.36,
    "assignee_typical_week_effort_h": 13.22,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.06,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0179` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01942 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.58, expected 2.94, ratio 2.24 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 6.6h vs an expected 2.9h (2.24x). 91% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (91%); Extended executor processing (9%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01942; 5 events: EV0011871, EV0011873, EV0011888, EV0011891, EV0011909 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 6.58,
  "duration_ratio": 2.24,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      1.15,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.1,
      0.58
    ],
    "dependency_wait": [
      5.26,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 28.22,
    "assignee_typical_week_effort_h": 13.0,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.36,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0180` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01957 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 7.38, expected 2.93, ratio 2.52 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 7.4h vs an expected 2.9h (2.52x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Extended executor processing (2%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01957; 6 events: EV0011972, EV0011973, EV0011983, EV0011986, EV0011992, EV0012042 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 7.38,
  "duration_ratio": 2.52,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.88,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.53,
      0.65
    ],
    "dependency_wait": [
      5.89,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 22.09,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.42,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0181` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01963 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.66, expected 2.94, ratio 2.27 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 6.7h vs an expected 2.9h (2.27x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01963; 6 events: EV0012010, EV0012014, EV0012020, EV0012023, EV0012025, EV0012048 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 6.66,
  "duration_ratio": 2.27,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.65,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.12,
      0.58
    ],
    "dependency_wait": [
      5.77,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.69,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.89,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0182` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01970 (HR) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 9.57, expected 5.35, ratio 1.79 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Low |
| What happened | Employee Document Verification (Medium, Low) took 9.6h vs an expected 5.3h (1.79x). 55% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (55%); Approval wait at Incharge stage (29%); Rework after rejection (Required document missing) (16%); High assignee workload that week |
| SOP reference | SOP-021 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01970; 10 events: EV0012061, EV0012062, EV0012065, EV0012066, EV0012067, EV0012071, EV0012147, EV0012151, EV0012153, EV0012159 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.35,
  "actual_duration_h": 9.57,
  "duration_ratio": 1.79,
  "baseline_p90_h": 7.63,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.96,
      0.96
    ],
    "rework": [
      0.72,
      0.0
    ],
    "approval_wait": [
      1.72,
      0.42
    ],
    "dependency_wait": [
      6.15,
      3.7
    ]
  },
  "context": {
    "task_type": "Employee Document Verification",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 19.36,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.86,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0183` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01972 (HR) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 4.16, expected 2.22, ratio 1.87 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.2h vs an expected 2.2h (1.87x). 53% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (53%); Rework after rejection (Required document missing) (44%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (3%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01972; 8 events: EV0012072, EV0012073, EV0012074, EV0012077, EV0012094, EV0012110, EV0012112, EV0012129 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.16,
  "duration_ratio": 1.87,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.41,
      0.49
    ],
    "rework": [
      1.03,
      0.0
    ],
    "approval_wait": [
      1.81,
      0.58
    ],
    "dependency_wait": [
      0.85,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 19.36,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.66,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0184` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01973 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.8, expected 2.94, ratio 2.32 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 6.8h vs an expected 2.9h (2.32x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Extended executor processing (2%); Approval wait at Incharge stage (1%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01973; 6 events: EV0012075, EV0012076, EV0012086, EV0012093, EV0012103, EV0012155 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 6.8,
  "duration_ratio": 2.32,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.85,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.62,
      0.58
    ],
    "dependency_wait": [
      5.23,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 22.09,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.85,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0185` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01989 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.34, expected 2.15, ratio 2.02 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.3h vs an expected 2.2h (2.02x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01989; 6 events: EV0012198, EV0012199, EV0012200, EV0012201, EV0012202, EV0012205 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.34,
  "duration_ratio": 2.02,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.43,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.48,
      0.6
    ],
    "dependency_wait": [
      3.34,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 16.56,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.83,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0186` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02012 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.55, expected 2.93, ratio 1.89 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 5.5h vs an expected 2.9h (1.89x). 99% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (99%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02012; 5 events: EV0012330, EV0012332, EV0012338, EV0012339, EV0012368 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 5.55,
  "duration_ratio": 1.89,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.76,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      4.67,
      0.65
    ],
    "dependency_wait": [
      0.0,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 19.56,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.67,
      0.89
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0187` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02027 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 8.36, expected 3.36, ratio 2.49 |
| Compared with | BL-v1:L2:Expense Approval:Simple:High |
| What happened | Expense Approval (Simple, High) took 8.4h vs an expected 3.4h (2.49x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Approval wait at Incharge stage (1%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02027; 6 events: EV0012399, EV0012401, EV0012404, EV0012407, EV0012415, EV0012472 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.36,
  "actual_duration_h": 8.36,
  "duration_ratio": 2.49,
  "baseline_p90_h": 6.14,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.07
    ],
    "executor_processing": [
      0.57,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.63,
      0.6
    ],
    "dependency_wait": [
      7.09,
      1.72
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 9.22,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.72,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0188` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02031 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 7.08, expected 2.94, ratio 2.41 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 7.1h vs an expected 2.9h (2.41x). 98% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (98%); Assignment queue delay (1%); Extended executor processing (1%) |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02031; 4 events: EV0012420, EV0012422, EV0012440, EV0012474 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 7.08,
  "duration_ratio": 2.41,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.81,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      6.14,
      0.58
    ],
    "dependency_wait": [
      0.0,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.7,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.14,
      0.89
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0189` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02039 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.76, expected 2.1, ratio 1.79 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.8h vs an expected 2.1h (1.79x). 93% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (93%); Extended executor processing (7%); Assignment queue delay (0%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02039; 6 events: EV0012483, EV0012485, EV0012489, EV0012490, EV0012491, EV0012505 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 3.76,
  "duration_ratio": 1.79,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.93,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.32,
      0.56
    ],
    "dependency_wait": [
      2.43,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 2.1,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.75,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0190` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02041 (HR) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 9.98, expected 5.19, ratio 1.92 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Medium |
| What happened | Employee Document Verification (Medium, Medium) took 10.0h vs an expected 5.2h (1.92x). 49% of the extra time is attributed to: rework after rejection (amount mismatch|required document missing). |
| Most likely reason | Rework after rejection (Amount mismatch|Required document missing); preventable by S5 salary and grade cross-check with offer letter|S2 checklist |
| Ranked candidate causes | Rework after rejection (Amount mismatch|Required document missing) (49%); Cross-team / dependency wait (26%); Approval wait at Incharge stage (16%); Extended executor processing (8%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-021 band above_p90; rework_trigger RW-AMT|RW-DOC |
| Preventable by | S5 salary and grade cross-check with offer letter|S2 checklist |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T02041; 11 events: EV0012492, EV0012493, EV0012500, EV0012501, EV0012533, EV0012537, EV0012541, EV0012543, EV0012546, EV0012547, EV0012549 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.19,
  "actual_duration_h": 9.98,
  "duration_ratio": 1.92,
  "baseline_p90_h": 7.35,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.37,
      0.96
    ],
    "rework": [
      2.41,
      0.0
    ],
    "approval_wait": [
      1.21,
      0.4
    ],
    "dependency_wait": [
      4.87,
      3.59
    ]
  },
  "context": {
    "task_type": "Employee Document Verification",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 2,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 18.11,
    "assignee_typical_week_effort_h": 9.93,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.07,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0191` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02042 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 7.65, expected 2.93, ratio 2.61 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 7.6h vs an expected 2.9h (2.61x). 100% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (100%); Assignment queue delay (0%); Extended executor processing (0%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02042; 4 events: EV0012496, EV0012497, EV0012503, EV0012545 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 7.65,
  "duration_ratio": 2.61,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.76,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      6.79,
      0.65
    ],
    "dependency_wait": [
      0.0,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 19.56,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.79,
      0.89
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0192` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02043 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 10.91, expected 4.89, ratio 2.23 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Medium |
| What happened | Invoice Verification (Medium, Medium) took 10.9h vs an expected 4.9h (2.23x). 41% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (41%); Cross-team / dependency wait (27%); Extended executor processing (18%); Rework after rejection (Amount mismatch) (14%); Assignment queue delay (0%) |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02043; 8 events: EV0012504, EV0012506, EV0012515, EV0012519, EV0012548, EV0012551, EV0012552, EV0012557 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 4.89,
  "actual_duration_h": 10.91,
  "duration_ratio": 2.23,
  "baseline_p90_h": 7.24,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      2.19,
      1.09
    ],
    "rework": [
      0.86,
      0.0
    ],
    "approval_wait": [
      2.91,
      0.4
    ],
    "dependency_wait": [
      4.86,
      3.16
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.7,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.77,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0193` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02044 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 8.24, expected 2.94, ratio 2.81 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 8.2h vs an expected 2.9h (2.81x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); Extended executor processing (0%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02044; 5 events: EV0012507, EV0012508, EV0012510, EV0012512, EV0012553 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 8.24,
  "duration_ratio": 2.81,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.79,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.32,
      0.58
    ],
    "dependency_wait": [
      7.07,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 19.56,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.39,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0194` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02045 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 8.36, expected 2.93, ratio 2.85 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 8.4h vs an expected 2.9h (2.85x). 94% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (94%); Extended executor processing (5%); Assignment queue delay (1%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02045; 6 events: EV0012509, EV0012511, EV0012517, EV0012518, EV0012523, EV0012555 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 8.36,
  "duration_ratio": 2.85,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      1.08,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.4,
      0.65
    ],
    "dependency_wait": [
      6.77,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 9.22,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.17,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0195` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02050 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.57, expected 2.22, ratio 2.05 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.6h vs an expected 2.2h (2.05x). 93% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (93%); Extended executor processing (6%); Assignment queue delay (1%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02050; 5 events: EV0012559, EV0012560, EV0012561, EV0012563, EV0012601 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.57,
  "duration_ratio": 2.05,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.69,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.18,
      0.58
    ],
    "dependency_wait": [
      3.58,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.54,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.76,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0196` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02055 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.02, expected 2.22, ratio 1.81 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.0h vs an expected 2.2h (1.81x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02055; 7 events: EV0012573, EV0012575, EV0012577, EV0012578, EV0012579, EV0012584, EV0012608 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.02,
  "duration_ratio": 1.81,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.21,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.43,
      0.58
    ],
    "dependency_wait": [
      3.32,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 18.11,
    "assignee_typical_week_effort_h": 9.93,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.75,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0197` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02058 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.05, expected 2.93, ratio 2.06 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 6.0h vs an expected 2.9h (2.06x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Extended executor processing (3%); Assignment queue delay (0%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02058; 5 events: EV0012595, EV0012596, EV0012603, EV0012605, EV0012630 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 6.05,
  "duration_ratio": 2.06,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.88,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.4,
      0.65
    ],
    "dependency_wait": [
      4.67,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.98,
    "assignee_typical_week_effort_h": 13.0,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.07,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0198` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02059 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 11.39, expected 5.16, ratio 2.21 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 11.4h vs an expected 5.2h (2.21x). 74% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (74%); Rework after rejection (Required document missing) (13%); Approval wait at Incharge stage (12%); Assignment queue delay (0%) |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02059; 9 events: EV0012604, EV0012606, EV0012609, EV0012612, EV0012613, EV0012635, EV0012636, EV0012637, EV0012638 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.16,
  "actual_duration_h": 11.39,
  "duration_ratio": 2.21,
  "baseline_p90_h": 7.62,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      1.02,
      1.11
    ],
    "rework": [
      0.88,
      0.0
    ],
    "approval_wait": [
      1.2,
      0.38
    ],
    "dependency_wait": [
      8.2,
      3.27
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.98,
    "assignee_typical_week_effort_h": 13.0,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      9.39,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0199` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02065 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 7.62, expected 2.93, ratio 2.6 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 7.6h vs an expected 2.9h (2.60x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Extended executor processing (1%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02065; 5 events: EV0012645, EV0012646, EV0012647, EV0012650, EV0012664 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 7.62,
  "duration_ratio": 2.6,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.82,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.63,
      0.65
    ],
    "dependency_wait": [
      6.03,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 24.04,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.67,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0200` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02066 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 7.91, expected 2.94, ratio 2.69 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 7.9h vs an expected 2.9h (2.69x). 90% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (90%); Extended executor processing (10%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02066; 6 events: EV0012648, EV0012649, EV0012653, EV0012655, EV0012656, EV0012666 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 7.91,
  "duration_ratio": 2.69,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.35,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.15,
      0.58
    ],
    "dependency_wait": [
      6.37,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 24.04,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.52,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0201` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02069 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.42, expected 2.94, ratio 2.19 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 6.4h vs an expected 2.9h (2.19x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02069; 7 events: EV0012668, EV0012669, EV0012670, EV0012671, EV0012672, EV0012673, EV0012691 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 6.42,
  "duration_ratio": 2.19,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.38,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.2,
      0.58
    ],
    "dependency_wait": [
      5.79,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 18.85,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.99,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0202` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02070 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.8, expected 2.94, ratio 2.32 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 6.8h vs an expected 2.9h (2.32x). 100% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (100%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02070; 4 events: EV0012674, EV0012675, EV0012676, EV0012721 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 6.8,
  "duration_ratio": 2.32,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.47,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      6.28,
      0.58
    ],
    "dependency_wait": [
      0.0,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 18.85,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.28,
      0.89
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0203` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02085 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.36, expected 2.1, ratio 2.08 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.4h vs an expected 2.1h (2.08x). 89% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (89%); Extended executor processing (10%); Approval wait at Incharge stage (1%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02085; 6 events: EV0012758, EV0012759, EV0012766, EV0012768, EV0012770, EV0012806 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.36,
  "duration_ratio": 2.08,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.03,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.58,
      0.56
    ],
    "dependency_wait": [
      2.71,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 20.12,
    "assignee_typical_week_effort_h": 19.94,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.3,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0204` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02103 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 9.53, expected 4.89, ratio 1.95 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Medium |
| What happened | Invoice Verification (Medium, Medium) took 9.5h vs an expected 4.9h (1.95x). 94% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (94%); Extended executor processing (6%); High assignee workload that week |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02103; 5 events: EV0012869, EV0012870, EV0012876, EV0012880, EV0012951 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 4.89,
  "actual_duration_h": 9.53,
  "duration_ratio": 1.95,
  "baseline_p90_h": 7.24,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      1.38,
      1.09
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.28,
      0.4
    ],
    "dependency_wait": [
      7.82,
      3.16
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 18.85,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      8.11,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0205` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02109 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 8.29, expected 2.93, ratio 2.83 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 8.3h vs an expected 2.9h (2.83x). 97% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (97%); Extended executor processing (3%); Assignment queue delay (0%) |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02109; 4 events: EV0012891, EV0012892, EV0012899, EV0012964 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 8.29,
  "duration_ratio": 2.83,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.94,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      7.24,
      0.65
    ],
    "dependency_wait": [
      0.0,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.82,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.24,
      0.89
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0206` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02116 (Operations) |
| Severity / classification / confidence | high / executor_processing / high |
| Measured | total_duration_h: observed 6.28, expected 2.25, ratio 2.79 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 6.3h vs an expected 2.3h (2.79x). 73% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (73%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (27%) |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T02116; 6 events: EV0012921, EV0012922, EV0012950, EV0012954, EV0012959, EV0012971 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 6.28,
  "duration_ratio": 2.79,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      3.89,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.5,
      0.5
    ],
    "dependency_wait": [
      1.86,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 24.47,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.36,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0207` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02129 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 9.64, expected 5.16, ratio 1.87 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 9.6h vs an expected 5.2h (1.87x). 100% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (100%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02129; 6 events: EV0013001, EV0013003, EV0013006, EV0013008, EV0013011, EV0013049 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.16,
  "actual_duration_h": 9.64,
  "duration_ratio": 1.87,
  "baseline_p90_h": 7.62,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.56,
      1.11
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.23,
      0.38
    ],
    "dependency_wait": [
      8.76,
      3.27
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 18.85,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      9.0,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0208` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02133 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.05, expected 2.22, ratio 2.27 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 5.0h vs an expected 2.2h (2.27x). 93% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (93%); Extended executor processing (6%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02133; 6 events: EV0013042, EV0013043, EV0013045, EV0013047, EV0013048, EV0013051 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 5.05,
  "duration_ratio": 2.27,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.68,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.32,
      0.58
    ],
    "dependency_wait": [
      3.92,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 29.55,
    "assignee_typical_week_effort_h": 9.93,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.23,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0209` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02157 (Procurement) |
| Severity / classification / confidence | medium / process / low |
| Measured | total_duration_h: observed 9.22, expected 4.9, ratio 1.88 |
| Compared with | BL-v1:L2:BOQ Review:Medium:Low |
| What happened | BOQ Review (Medium, Low) took 9.2h vs an expected 4.9h (1.88x). 38% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (38%); Cross-team / dependency wait (37%); Rework after rejection (Incorrect category) (18%); Extended executor processing (7%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-013 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02157; 9 events: EV0013193, EV0013194, EV0013206, EV0013210, EV0013212, EV0013268, EV0013276, EV0013279, EV0013299 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 4.9,
  "actual_duration_h": 9.22,
  "duration_ratio": 1.88,
  "baseline_p90_h": 6.79,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      1.43,
      1.11
    ],
    "rework": [
      0.84,
      0.0
    ],
    "approval_wait": [
      2.14,
      0.42
    ],
    "dependency_wait": [
      4.73,
      3.05
    ]
  },
  "context": {
    "task_type": "BOQ Review",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 48.73,
    "assignee_typical_week_effort_h": 32.36,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-013",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.89,
    "sop_p10_p90_h": [
      4.57,
      7.21
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.87,
      3.65
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0210` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02182 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.25, expected 2.93, ratio 2.13 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 6.3h vs an expected 2.9h (2.13x). 97% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (97%); Extended executor processing (3%); Assignment queue delay (0%) |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02182; 5 events: EV0013342, EV0013344, EV0013346, EV0013348, EV0013394 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 6.25,
  "duration_ratio": 2.13,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.89,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      5.28,
      0.65
    ],
    "dependency_wait": [
      0.0,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 8.13,
    "assignee_typical_week_effort_h": 10.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.28,
      0.89
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0211` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02226 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.01, expected 2.22, ratio 1.8 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.0h vs an expected 2.2h (1.80x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02226; 5 events: EV0013609, EV0013611, EV0013615, EV0013619, EV0013632 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.01,
  "duration_ratio": 1.8,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.3,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.38,
      0.58
    ],
    "dependency_wait": [
      3.21,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 4.38,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.59,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0212` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02247 (Procurement) |
| Severity / classification / confidence | medium / executor_processing / medium |
| Measured | total_duration_h: observed 9.78, expected 5.47, ratio 1.79 |
| Compared with | BL-v1:L2:Purchase Request:Medium:Medium |
| What happened | Purchase Request (Medium, Medium) took 9.8h vs an expected 5.5h (1.79x). 41% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (41%); Cross-team / dependency wait (29%); Approval wait at Incharge stage (29%); Assignment queue delay (0%) |
| SOP reference | SOP-014 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T02247; 6 events: EV0013754, EV0013755, EV0013778, EV0013780, EV0013801, EV0013814 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.47,
  "actual_duration_h": 9.78,
  "duration_ratio": 1.79,
  "baseline_p90_h": 7.44,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      2.9,
      1.13
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      2.78,
      1.52
    ],
    "dependency_wait": [
      4.0,
      2.73
    ]
  },
  "context": {
    "task_type": "Purchase Request",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 33.29,
    "assignee_typical_week_effort_h": 33.29,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-014",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 6.22,
    "sop_p10_p90_h": [
      4.95,
      7.5
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.46,
      3.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0213` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02251 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.86, expected 2.15, ratio 1.79 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 3.9h vs an expected 2.2h (1.79x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02251; 7 events: EV0013768, EV0013771, EV0013774, EV0013775, EV0013776, EV0013777, EV0013794 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 3.86,
  "duration_ratio": 1.79,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.25,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.08,
      0.6
    ],
    "dependency_wait": [
      3.45,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 20.26,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.53,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0214` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02252 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.05, expected 2.15, ratio 1.88 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.0h vs an expected 2.2h (1.88x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Assignment queue delay (2%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02252; 6 events: EV0013784, EV0013785, EV0013786, EV0013787, EV0013788, EV0013808 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.05,
  "duration_ratio": 1.88,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.19,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.23,
      0.6
    ],
    "dependency_wait": [
      3.49,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.88,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.73,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0215` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02361 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.96, expected 2.36, ratio 2.1 |
| Compared with | BL-v1:L2:Leave Approval:Simple:High |
| What happened | Leave Approval (Simple, High) took 5.0h vs an expected 2.4h (2.10x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02361; 6 events: EV0014449, EV0014450, EV0014454, EV0014456, EV0014459, EV0014490 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.36,
  "actual_duration_h": 4.96,
  "duration_ratio": 2.1,
  "baseline_p90_h": 4.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.33,
      0.53
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.58,
      0.6
    ],
    "dependency_wait": [
      3.99,
      0.98
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 14.31,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.57,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0216` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02400 (HR) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 4.71, expected 2.15, ratio 2.19 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.7h vs an expected 2.2h (2.19x). 40% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (40%); Rework after rejection (Incorrect category) (29%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (24%); Extended executor processing (6%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02400; 9 events: EV0014671, EV0014672, EV0014677, EV0014678, EV0014681, EV0014686, EV0014692, EV0014693, EV0014700 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.71,
  "duration_ratio": 2.19,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.62,
      0.46
    ],
    "rework": [
      0.8,
      0.0
    ],
    "approval_wait": [
      1.71,
      0.6
    ],
    "dependency_wait": [
      1.55,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 30.79,
    "assignee_typical_week_effort_h": 12.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.26,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0217` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02420 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.76, expected 2.14, ratio 2.23 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 4.8h vs an expected 2.1h (2.23x). 96% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (96%); Extended executor processing (3%); Assignment queue delay (1%); Approval wait at Incharge stage (0%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02420; 5 events: EV0014782, EV0014783, EV0014785, EV0014787, EV0014813 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 4.76,
  "duration_ratio": 2.23,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.84,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.53,
      0.53
    ],
    "dependency_wait": [
      3.27,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 30.93,
    "assignee_typical_week_effort_h": 19.94,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.8,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0218` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02428 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.69, expected 2.25, ratio 2.08 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.7h vs an expected 2.3h (2.08x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02428; 6 events: EV0014826, EV0014828, EV0014834, EV0014838, EV0014841, EV0014857 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.69,
  "duration_ratio": 2.08,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.78,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.1,
      0.5
    ],
    "dependency_wait": [
      3.7,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 35.71,
    "assignee_typical_week_effort_h": 15.58,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.8,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0219` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02454 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 8.64, expected 4.89, ratio 1.77 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Medium |
| What happened | Invoice Verification (Medium, Medium) took 8.6h vs an expected 4.9h (1.77x). 54% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (54%); Approval wait at Incharge stage (31%); Rework after rejection (Amount mismatch) (15%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02454; 8 events: EV0014985, EV0014986, EV0014997, EV0015000, EV0015059, EV0015065, EV0015067, EV0015078 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 4.89,
  "actual_duration_h": 8.64,
  "duration_ratio": 1.77,
  "baseline_p90_h": 7.24,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.96,
      1.09
    ],
    "rework": [
      0.61,
      0.0
    ],
    "approval_wait": [
      1.64,
      0.4
    ],
    "dependency_wait": [
      5.34,
      3.16
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 33.11,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.97,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0220` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02464 (HR) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 3.95, expected 2.15, ratio 1.84 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.0h vs an expected 2.2h (1.84x). 54% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (54%); Rework after rejection (Incorrect category) (31%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (10%); Extended executor processing (6%) |
| SOP reference | SOP-020 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02464; 8 events: EV0015042, EV0015044, EV0015057, EV0015066, EV0015075, EV0015079, EV0015080, EV0015084 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 3.95,
  "duration_ratio": 1.84,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.57,
      0.46
    ],
    "rework": [
      0.6,
      0.0
    ],
    "approval_wait": [
      1.65,
      0.6
    ],
    "dependency_wait": [
      1.07,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.98,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.72,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0221` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02468 (Finance) |
| Severity / classification / confidence | medium / process / low |
| Measured | total_duration_h: observed 7.08, expected 2.93, ratio 2.41 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 7.1h vs an expected 2.9h (2.41x). 36% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (36%); Approval wait at Incharge stage (30%); Rework after rejection (Wrong quantity) (26%); Extended executor processing (8%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02468; 9 events: EV0015055, EV0015056, EV0015068, EV0015069, EV0015073, EV0015085, EV0015092, EV0015093, EV0015097 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 7.08,
  "duration_ratio": 2.41,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      1.14,
      0.76
    ],
    "rework": [
      1.27,
      0.0
    ],
    "approval_wait": [
      2.08,
      0.65
    ],
    "dependency_wait": [
      2.53,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.29,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.61,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0222` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02490 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 9.99, expected 5.35, ratio 1.87 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Low |
| What happened | Employee Document Verification (Medium, Low) took 10.0h vs an expected 5.3h (1.87x). 70% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (70%); Rework after rejection (Incorrect category) (16%); Approval wait at Incharge stage (14%); High assignee workload that week |
| SOP reference | SOP-021 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02490; 8 events: EV0015228, EV0015229, EV0015232, EV0015233, EV0015257, EV0015258, EV0015261, EV0015262 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.35,
  "actual_duration_h": 9.99,
  "duration_ratio": 1.87,
  "baseline_p90_h": 7.63,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.84,
      0.96
    ],
    "rework": [
      0.8,
      0.0
    ],
    "approval_wait": [
      1.13,
      0.42
    ],
    "dependency_wait": [
      7.18,
      3.7
    ]
  },
  "context": {
    "task_type": "Employee Document Verification",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 25.54,
    "assignee_typical_week_effort_h": 12.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      8.31,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0223` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02513 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.44, expected 2.15, ratio 2.06 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.4h vs an expected 2.2h (2.06x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02513; 5 events: EV0015354, EV0015356, EV0015361, EV0015375, EV0015415 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.44,
  "duration_ratio": 2.06,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.29,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.5,
      0.6
    ],
    "dependency_wait": [
      3.54,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 22.41,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.04,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0224` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02519 (Procurement) |
| Severity / classification / confidence | medium / process / low |
| Measured | total_duration_h: observed 11.03, expected 5.04, ratio 2.19 |
| Compared with | BL-v1:L2:BOQ Review:Medium:Medium |
| What happened | BOQ Review (Medium, Medium) took 11.0h vs an expected 5.0h (2.19x). 38% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (38%); Extended executor processing (34%); Rework after rejection (Incorrect category) (15%); Approval wait at Incharge stage (12%); Assignment queue delay (1%) |
| SOP reference | SOP-013 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02519; 10 events: EV0015376, EV0015377, EV0015408, EV0015411, EV0015414, EV0015417, EV0015436, EV0015437, EV0015439, EV0015440 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.04,
  "actual_duration_h": 11.03,
  "duration_ratio": 2.19,
  "baseline_p90_h": 6.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      3.18,
      1.06
    ],
    "rework": [
      0.93,
      0.0
    ],
    "approval_wait": [
      1.19,
      0.43
    ],
    "dependency_wait": [
      5.62,
      3.3
    ]
  },
  "context": {
    "task_type": "BOQ Review",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 34.72,
    "assignee_typical_week_effort_h": 33.29,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-013",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.89,
    "sop_p10_p90_h": [
      4.57,
      7.21
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.81,
      3.65
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0225` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02532 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.12, expected 2.1, ratio 1.97 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.1h vs an expected 2.1h (1.97x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); Extended executor processing (0%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02532; 6 events: EV0015488, EV0015490, EV0015495, EV0015496, EV0015498, EV0015518 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.12,
  "duration_ratio": 1.97,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.79,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.32,
      0.56
    ],
    "dependency_wait": [
      2.96,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 33.23,
    "assignee_typical_week_effort_h": 19.94,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.28,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0226` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02541 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.06, expected 2.25, ratio 2.25 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 5.1h vs an expected 2.3h (2.25x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); Assignment queue delay (0%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02541; 5 events: EV0015538, EV0015540, EV0015546, EV0015547, EV0015566 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 5.06,
  "duration_ratio": 2.25,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.55,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.45,
      0.5
    ],
    "dependency_wait": [
      3.98,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 22.37,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.43,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0227` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02544 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.28, expected 2.15, ratio 1.99 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.3h vs an expected 2.2h (1.99x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02544; 5 events: EV0015550, EV0015551, EV0015553, EV0015557, EV0015568 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.28,
  "duration_ratio": 1.99,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.4,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.4,
      0.6
    ],
    "dependency_wait": [
      3.38,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 22.41,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.78,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0228` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02611 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.46, expected 2.22, ratio 2.01 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.5h vs an expected 2.2h (2.01x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02611; 6 events: EV0015967, EV0015969, EV0015970, EV0015972, EV0015976, EV0016021 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.46,
  "duration_ratio": 2.01,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.37,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.22,
      0.58
    ],
    "dependency_wait": [
      3.81,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 14.75,
    "assignee_typical_week_effort_h": 12.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.02,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0229` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02623 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 5.21, expected 2.94, ratio 1.78 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 5.2h vs an expected 2.9h (1.78x). 55% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (55%); Extended executor processing (45%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02623; 6 events: EV0016018, EV0016020, EV0016052, EV0016054, EV0016057, EV0016074 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 5.21,
  "duration_ratio": 1.78,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      2.15,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.12,
      0.58
    ],
    "dependency_wait": [
      2.88,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 10.76,
    "assignee_typical_week_effort_h": 10.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.99,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0230` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02625 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.78, expected 2.36, ratio 2.03 |
| Compared with | BL-v1:L2:Leave Approval:Simple:High |
| What happened | Leave Approval (Simple, High) took 4.8h vs an expected 2.4h (2.03x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Extended executor processing (3%); Assignment queue delay (0%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02625; 5 events: EV0016030, EV0016032, EV0016043, EV0016050, EV0016077 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.36,
  "actual_duration_h": 4.78,
  "duration_ratio": 2.03,
  "baseline_p90_h": 4.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.61,
      0.53
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.52,
      0.6
    ],
    "dependency_wait": [
      3.57,
      0.98
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 2.36,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.09,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0231` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02635 (Operations) |
| Severity / classification / confidence | high / executor_processing / high |
| Measured | total_duration_h: observed 6.18, expected 2.1, ratio 2.95 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 6.2h vs an expected 2.1h (2.95x). 97% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (97%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (3%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T02635; 5 events: EV0016119, EV0016120, EV0016163, EV0016164, EV0016166 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 6.18,
  "duration_ratio": 2.95,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      4.96,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.5,
      0.56
    ],
    "dependency_wait": [
      0.66,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 33.46,
    "assignee_typical_week_effort_h": 13.22,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      1.16,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0232` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02636 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.27, expected 2.22, ratio 1.92 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.3h vs an expected 2.2h (1.92x). 81% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (81%); Rework after rejection (Wrong quantity) (18%); Assignment queue delay (1%) |
| SOP reference | SOP-020 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02636; 8 events: EV0016123, EV0016125, EV0016126, EV0016132, EV0016145, EV0016152, EV0016154, EV0016162 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.27,
  "duration_ratio": 1.92,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.41,
      0.49
    ],
    "rework": [
      0.57,
      0.0
    ],
    "approval_wait": [
      3.18,
      0.58
    ],
    "dependency_wait": [
      0.0,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 6.74,
    "assignee_typical_week_effort_h": 9.93,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.18,
      0.8
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0233` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02660 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.41, expected 2.94, ratio 1.84 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 5.4h vs an expected 2.9h (1.84x). 66% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (66%); Extended executor processing (32%); Assignment queue delay (2%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02660; 6 events: EV0016267, EV0016270, EV0016277, EV0016283, EV0016286, EV0016309 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 5.41,
  "duration_ratio": 1.84,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.74,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.35,
      0.58
    ],
    "dependency_wait": [
      3.19,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 30.61,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.54,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0234` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02694 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.31, expected 2.25, ratio 2.36 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 5.3h vs an expected 2.3h (2.36x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02694; 6 events: EV0016470, EV0016471, EV0016477, EV0016478, EV0016483, EV0016506 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 5.31,
  "duration_ratio": 2.36,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.73,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.42,
      0.5
    ],
    "dependency_wait": [
      4.06,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 28.95,
    "assignee_typical_week_effort_h": 19.94,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.48,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0235` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02766 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.08, expected 2.22, ratio 1.84 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.1h vs an expected 2.2h (1.84x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Assignment queue delay (2%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02766; 6 events: EV0016923, EV0016924, EV0016928, EV0016929, EV0016933, EV0016941 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.08,
  "duration_ratio": 1.84,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.4,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.55,
      0.58
    ],
    "dependency_wait": [
      3.0,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.37,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.55,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0236` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02792 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.29, expected 2.25, ratio 1.91 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.3h vs an expected 2.3h (1.91x). 96% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (96%); Approval wait at Incharge stage (4%); Assignment queue delay (0%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02792; 5 events: EV0017088, EV0017089, EV0017101, EV0017106, EV0017131 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.29,
  "duration_ratio": 1.91,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.7,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.58,
      0.5
    ],
    "dependency_wait": [
      2.92,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.73,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.51,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0237` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02796 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 9.87, expected 5.19, ratio 1.9 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Medium |
| What happened | Employee Document Verification (Medium, Medium) took 9.9h vs an expected 5.2h (1.90x). 67% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (67%); Approval wait at Incharge stage (14%); Rework after rejection (Amount mismatch) (12%); Extended executor processing (5%); Assignment queue delay (1%) |
| SOP reference | SOP-021 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02796; 8 events: EV0017099, EV0017102, EV0017115, EV0017119, EV0017141, EV0017142, EV0017143, EV0017144 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.19,
  "actual_duration_h": 9.87,
  "duration_ratio": 1.9,
  "baseline_p90_h": 7.35,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.21,
      0.96
    ],
    "rework": [
      0.6,
      0.0
    ],
    "approval_wait": [
      1.09,
      0.4
    ],
    "dependency_wait": [
      6.84,
      3.59
    ]
  },
  "context": {
    "task_type": "Employee Document Verification",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 14.98,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.93,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0238` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02809 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.27, expected 2.36, ratio 2.23 |
| Compared with | BL-v1:L2:Leave Approval:Simple:High |
| What happened | Leave Approval (Simple, High) took 5.3h vs an expected 2.4h (2.23x). 96% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (96%); Extended executor processing (4%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02809; 6 events: EV0017176, EV0017178, EV0017184, EV0017187, EV0017194, EV0017244 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.36,
  "actual_duration_h": 5.27,
  "duration_ratio": 2.23,
  "baseline_p90_h": 4.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.67,
      0.53
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.37,
      0.6
    ],
    "dependency_wait": [
      4.18,
      0.98
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 22.38,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.55,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0239` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02822 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.42, expected 2.22, ratio 2.44 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 5.4h vs an expected 2.2h (2.44x). 95% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (95%); Extended executor processing (4%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02822; 5 events: EV0017280, EV0017281, EV0017285, EV0017287, EV0017312 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 5.42,
  "duration_ratio": 2.44,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.63,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.52,
      0.58
    ],
    "dependency_wait": [
      4.14,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 22.16,
    "assignee_typical_week_effort_h": 9.93,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.66,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0240` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02862 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.55, expected 2.15, ratio 2.12 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.6h vs an expected 2.2h (2.12x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Extended executor processing (2%); Approval wait at Incharge stage (1%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02862; 7 events: EV0017528, EV0017529, EV0017531, EV0017532, EV0017533, EV0017538, EV0017554 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.55,
  "duration_ratio": 2.12,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.51,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.63,
      0.6
    ],
    "dependency_wait": [
      3.38,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.35,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.01,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0241` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02905 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.95, expected 2.22, ratio 2.22 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.9h vs an expected 2.2h (2.22x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); Assignment queue delay (0%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02905; 7 events: EV0017805, EV0017806, EV0017807, EV0017808, EV0017809, EV0017812, EV0017841 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.95,
  "duration_ratio": 2.22,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.32,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.28,
      0.58
    ],
    "dependency_wait": [
      4.24,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 2.22,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.53,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0242` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02920 (Procurement) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 9.73, expected 5.47, ratio 1.78 |
| Compared with | BL-v1:L2:Purchase Request:Medium:Medium |
| What happened | Purchase Request (Medium, Medium) took 9.7h vs an expected 5.5h (1.78x). 53% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (53%); Rework after rejection (Amount mismatch) (24%); Cross-team / dependency wait (16%); Extended executor processing (6%); Assignment queue delay (1%) |
| SOP reference | SOP-014 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02920; 10 events: EV0017905, EV0017906, EV0017907, EV0017911, EV0017913, EV0017915, EV0017920, EV0017921, EV0017927, EV0017941 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.47,
  "actual_duration_h": 9.73,
  "duration_ratio": 1.78,
  "baseline_p90_h": 7.44,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.38,
      1.13
    ],
    "rework": [
      1.03,
      0.0
    ],
    "approval_wait": [
      3.77,
      1.52
    ],
    "dependency_wait": [
      3.41,
      2.73
    ]
  },
  "context": {
    "task_type": "Purchase Request",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 34.31,
    "assignee_typical_week_effort_h": 33.29,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-014",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 6.22,
    "sop_p10_p90_h": [
      4.95,
      7.5
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.88,
      3.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0243` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02935 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.15, expected 2.1, ratio 1.98 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.2h vs an expected 2.1h (1.98x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Assignment queue delay (2%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02935; 5 events: EV0017989, EV0017991, EV0017995, EV0017998, EV0018012 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.15,
  "duration_ratio": 1.98,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.78,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.35,
      0.56
    ],
    "dependency_wait": [
      2.89,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 4.35,
    "assignee_typical_week_effort_h": 17.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.24,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0244` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02984 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.13, expected 2.22, ratio 1.86 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.1h vs an expected 2.2h (1.86x). 85% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (85%); Extended executor processing (15%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02984; 7 events: EV0018286, EV0018287, EV0018293, EV0018294, EV0018295, EV0018296, EV0018321 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.13,
  "duration_ratio": 1.86,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.87,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.3,
      0.58
    ],
    "dependency_wait": [
      2.89,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 9.64,
    "assignee_typical_week_effort_h": 12.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.19,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0245` TICKET_DURATION

| field | value |
|---|---|
| Entity | T02985 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.54, expected 2.15, ratio 2.11 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.5h vs an expected 2.2h (2.11x). 91% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (91%); Extended executor processing (9%); Assignment queue delay (0%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T02985; 5 events: EV0018297, EV0018298, EV0018306, EV0018310, EV0018328 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.54,
  "duration_ratio": 2.11,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.69,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.5,
      0.6
    ],
    "dependency_wait": [
      3.26,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.5,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.76,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0246` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03014 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 6.75, expected 3.36, ratio 2.01 |
| Compared with | BL-v1:L2:Expense Approval:Simple:High |
| What happened | Expense Approval (Simple, High) took 6.8h vs an expected 3.4h (2.01x). 50% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (50%); Rework after rejection (Wrong quantity) (27%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (15%); Extended executor processing (7%); Assignment queue delay (1%) |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03014; 8 events: EV0018475, EV0018478, EV0018487, EV0018492, EV0018503, EV0018507, EV0018508, EV0018512 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.36,
  "actual_duration_h": 6.75,
  "duration_ratio": 2.01,
  "baseline_p90_h": 6.14,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.07
    ],
    "executor_processing": [
      1.02,
      0.79
    ],
    "rework": [
      0.95,
      0.0
    ],
    "approval_wait": [
      2.4,
      0.6
    ],
    "dependency_wait": [
      2.27,
      1.72
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 8.25,
    "assignee_typical_week_effort_h": 10.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.68,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0247` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03036 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.16, expected 2.22, ratio 1.87 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.2h vs an expected 2.2h (1.87x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); Assignment queue delay (0%); Approval wait at Incharge stage (0%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03036; 6 events: EV0018611, EV0018612, EV0018615, EV0018618, EV0018629, EV0018653 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.16,
  "duration_ratio": 1.87,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.23,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.58,
      0.58
    ],
    "dependency_wait": [
      3.26,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.86,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.85,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0248` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03047 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.23, expected 2.22, ratio 1.9 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.2h vs an expected 2.2h (1.90x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03047; 6 events: EV0018684, EV0018685, EV0018689, EV0018690, EV0018698, EV0018749 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.23,
  "duration_ratio": 1.9,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.44,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.48,
      0.58
    ],
    "dependency_wait": [
      3.21,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 14.24,
    "assignee_typical_week_effort_h": 12.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.69,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0249` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03051 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.8, expected 2.25, ratio 2.13 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.8h vs an expected 2.3h (2.13x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%); Extended executor processing (0%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03051; 6 events: EV0018694, EV0018699, EV0018711, EV0018716, EV0018722, EV0018771 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.8,
  "duration_ratio": 2.13,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.8,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.37,
      0.5
    ],
    "dependency_wait": [
      3.52,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 15.95,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.89,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0250` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03069 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.74, expected 2.25, ratio 2.1 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.7h vs an expected 2.3h (2.10x). 78% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (78%); Extended executor processing (16%); Approval wait at Incharge stage (5%); Assignment queue delay (1%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03069; 6 events: EV0018822, EV0018824, EV0018831, EV0018835, EV0018840, EV0018855 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.74,
  "duration_ratio": 2.1,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      1.21,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.63,
      0.5
    ],
    "dependency_wait": [
      2.78,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 15.95,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.42,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0251` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03076 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.05, expected 2.14, ratio 1.9 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 4.1h vs an expected 2.1h (1.90x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Extended executor processing (2%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03076; 6 events: EV0018856, EV0018857, EV0018868, EV0018870, EV0018874, EV0018897 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 4.05,
  "duration_ratio": 1.9,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.8,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.35,
      0.53
    ],
    "dependency_wait": [
      2.85,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.26,
    "assignee_typical_week_effort_h": 13.22,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.2,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0252` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03081 (Finance) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 5.15, expected 2.94, ratio 1.75 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 5.1h vs an expected 2.9h (1.75x). 56% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S4 computation check |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (56%); Approval wait at Incharge stage (36%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (8%) |
| SOP reference | SOP-016 band above_p90; rework_trigger RW-AMT |
| Preventable by | S4 computation check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T03081; 9 events: EV0018877, EV0018878, EV0018882, EV0018884, EV0018890, EV0018896, EV0018900, EV0018901, EV0018903 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 5.15,
  "duration_ratio": 1.75,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.67,
      0.76
    ],
    "rework": [
      1.5,
      0.0
    ],
    "approval_wait": [
      1.54,
      0.58
    ],
    "dependency_wait": [
      1.39,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 10.76,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.93,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0253` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03082 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.93, expected 3.36, ratio 1.77 |
| Compared with | BL-v1:L2:Expense Approval:Simple:High |
| What happened | Expense Approval (Simple, High) took 5.9h vs an expected 3.4h (1.77x). 75% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (75%); Extended executor processing (22%); Assignment queue delay (2%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03082; 7 events: EV0018879, EV0018880, EV0018888, EV0018892, EV0018894, EV0018895, EV0018904 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.36,
  "actual_duration_h": 5.93,
  "duration_ratio": 1.77,
  "baseline_p90_h": 6.14,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.07
    ],
    "executor_processing": [
      1.46,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.35,
      0.6
    ],
    "dependency_wait": [
      3.99,
      1.72
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.45,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.34,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0254` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03147 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.02, expected 2.15, ratio 1.87 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.0h vs an expected 2.2h (1.87x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03147; 6 events: EV0019289, EV0019290, EV0019292, EV0019294, EV0019300, EV0019333 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.02,
  "duration_ratio": 1.87,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.37,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.58,
      0.6
    ],
    "dependency_wait": [
      3.02,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 20.19,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.6,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0255` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03155 (HR) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 4.6, expected 2.15, ratio 2.14 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.6h vs an expected 2.2h (2.14x). 49% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (49%); Rework after rejection (Wrong quantity) (43%); Extended executor processing (8%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03155; 9 events: EV0019358, EV0019359, EV0019360, EV0019361, EV0019363, EV0019368, EV0019374, EV0019376, EV0019390 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.6,
  "duration_ratio": 2.14,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.68,
      0.46
    ],
    "rework": [
      1.18,
      0.0
    ],
    "approval_wait": [
      1.95,
      0.6
    ],
    "dependency_wait": [
      0.74,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.03,
    "assignee_typical_week_effort_h": 9.93,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.69,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0256` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03207 (HR) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 5.03, expected 2.15, ratio 2.34 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 5.0h vs an expected 2.2h (2.34x). 53% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (53%); Rework after rejection (Incorrect category) (32%); Approval wait at Incharge stage (12%); Assignment queue delay (2%); Extended executor processing (1%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03207; 10 events: EV0019667, EV0019668, EV0019671, EV0019672, EV0019673, EV0019675, EV0019691, EV0019692, EV0019693, EV0019694 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 5.03,
  "duration_ratio": 2.34,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.49,
      0.46
    ],
    "rework": [
      0.97,
      0.0
    ],
    "approval_wait": [
      0.96,
      0.6
    ],
    "dependency_wait": [
      2.48,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.86,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.44,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0257` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03215 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.31, expected 2.93, ratio 1.81 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 5.3h vs an expected 2.9h (1.81x). 90% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (90%); Extended executor processing (10%); Assignment queue delay (0%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03215; 5 events: EV0019715, EV0019716, EV0019724, EV0019725, EV0019758 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 5.31,
  "duration_ratio": 1.81,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      1.12,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.1,
      0.65
    ],
    "dependency_wait": [
      4.0,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 2.93,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.1,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0258` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03267 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 8.69, expected 4.89, ratio 1.78 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Medium |
| What happened | Invoice Verification (Medium, Medium) took 8.7h vs an expected 4.9h (1.78x). 40% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (40%); Cross-team / dependency wait (37%); Rework after rejection (Incorrect category) (23%) |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03267; 8 events: EV0020024, EV0020027, EV0020032, EV0020038, EV0020058, EV0020061, EV0020062, EV0020065 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 4.89,
  "actual_duration_h": 8.69,
  "duration_ratio": 1.78,
  "baseline_p90_h": 7.24,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.59,
      1.09
    ],
    "rework": [
      1.04,
      0.0
    ],
    "approval_wait": [
      2.2,
      0.4
    ],
    "dependency_wait": [
      4.81,
      3.16
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 15.24,
    "assignee_typical_week_effort_h": 13.0,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.02,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0259` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03279 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.72, expected 2.25, ratio 2.09 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.7h vs an expected 2.3h (2.09x). 92% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (92%); Extended executor processing (8%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03279; 6 events: EV0020091, EV0020094, EV0020101, EV0020104, EV0020109, EV0020127 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.72,
  "duration_ratio": 2.09,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.02,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.5,
      0.5
    ],
    "dependency_wait": [
      3.17,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 35.08,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.67,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0260` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03336 (Operations) |
| Severity / classification / confidence | medium / executor_processing / high |
| Measured | total_duration_h: observed 4.51, expected 2.1, ratio 2.15 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.5h vs an expected 2.1h (2.15x). 90% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (90%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (10%) |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T03336; 6 events: EV0020436, EV0020438, EV0020465, EV0020470, EV0020479, EV0020489 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.51,
  "duration_ratio": 2.15,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      3.13,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.55,
      0.56
    ],
    "dependency_wait": [
      0.78,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.38,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      1.33,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0261` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03337 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.0, expected 2.15, ratio 2.32 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 5.0h vs an expected 2.2h (2.32x). 94% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (94%); Extended executor processing (6%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03337; 6 events: EV0020441, EV0020442, EV0020445, EV0020447, EV0020459, EV0020502 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 5.0,
  "duration_ratio": 2.32,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.63,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.55,
      0.6
    ],
    "dependency_wait": [
      3.72,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 32.95,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.27,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0262` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03361 (HR) |
| Severity / classification / confidence | medium / process / low |
| Measured | total_duration_h: observed 9.52, expected 5.19, ratio 1.84 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Medium |
| What happened | Employee Document Verification (Medium, Medium) took 9.5h vs an expected 5.2h (1.84x). 36% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (36%); Approval wait at Incharge stage (35%); Rework after rejection (Required document missing|Required document missing) (29%); High assignee workload that week |
| SOP reference | SOP-021 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03361; 12 events: EV0020592, EV0020593, EV0020600, EV0020607, EV0020609, EV0020632, EV0020633, EV0020634, EV0020636, EV0020637, EV0020638, EV0020639 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.19,
  "actual_duration_h": 9.52,
  "duration_ratio": 1.84,
  "baseline_p90_h": 7.35,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.96,
      0.96
    ],
    "rework": [
      1.3,
      0.0
    ],
    "approval_wait": [
      1.97,
      0.4
    ],
    "dependency_wait": [
      5.23,
      3.59
    ]
  },
  "context": {
    "task_type": "Employee Document Verification",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 2,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 32.95,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.21,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0263` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03419 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.88, expected 2.1, ratio 1.85 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.9h vs an expected 2.1h (1.85x). 79% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (79%); Extended executor processing (20%); Assignment queue delay (1%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03419; 5 events: EV0020950, EV0020953, EV0020961, EV0020965, EV0020980 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 3.88,
  "duration_ratio": 1.85,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      1.24,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.27,
      0.56
    ],
    "dependency_wait": [
      2.28,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 4.19,
    "assignee_typical_week_effort_h": 17.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.54,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0264` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03422 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.4, expected 2.15, ratio 2.04 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.4h vs an expected 2.2h (2.04x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03422; 7 events: EV0020964, EV0020966, EV0020967, EV0020969, EV0020970, EV0020973, EV0021007 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.4,
  "duration_ratio": 2.04,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.39,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.17,
      0.6
    ],
    "dependency_wait": [
      3.79,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.5,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.96,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0265` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03431 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.97, expected 2.15, ratio 1.84 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.0h vs an expected 2.2h (1.84x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Assignment queue delay (1%); Extended executor processing (0%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03431; 7 events: EV0021032, EV0021033, EV0021036, EV0021037, EV0021038, EV0021039, EV0021054 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 3.97,
  "duration_ratio": 1.84,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.47,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.23,
      0.6
    ],
    "dependency_wait": [
      3.15,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 4.31,
    "assignee_typical_week_effort_h": 9.93,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.38,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0266` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03438 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.32, expected 2.15, ratio 2.01 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.3h vs an expected 2.2h (2.01x). 63% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (63%); Rework after rejection (Amount mismatch) (27%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (10%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03438; 9 events: EV0021063, EV0021065, EV0021066, EV0021067, EV0021069, EV0021075, EV0021082, EV0021083, EV0021098 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.32,
  "duration_ratio": 2.01,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.33,
      0.46
    ],
    "rework": [
      0.67,
      0.0
    ],
    "approval_wait": [
      2.12,
      0.6
    ],
    "dependency_wait": [
      1.12,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 18.04,
    "assignee_typical_week_effort_h": 12.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.24,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0267` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03476 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.38, expected 2.15, ratio 2.03 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.4h vs an expected 2.2h (2.03x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Approval wait at Incharge stage (1%); Extended executor processing (1%); Assignment queue delay (0%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03476; 6 events: EV0021294, EV0021295, EV0021301, EV0021302, EV0021308, EV0021341 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.38,
  "duration_ratio": 2.03,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.48,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.63,
      0.6
    ],
    "dependency_wait": [
      3.19,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 14.58,
    "assignee_typical_week_effort_h": 12.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.82,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0268` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03505 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.31, expected 2.1, ratio 2.06 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.3h vs an expected 2.1h (2.06x). 89% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (89%); Extended executor processing (7%); Approval wait at Incharge stage (3%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03505; 5 events: EV0021450, EV0021452, EV0021458, EV0021469, EV0021486 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.31,
  "duration_ratio": 2.06,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.96,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.63,
      0.56
    ],
    "dependency_wait": [
      2.65,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 53.82,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.29,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0269` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03518 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.74, expected 2.22, ratio 2.13 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.7h vs an expected 2.2h (2.13x). 81% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (81%); Extended executor processing (18%); Assignment queue delay (2%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03518; 7 events: EV0021524, EV0021527, EV0021533, EV0021535, EV0021539, EV0021544, EV0021591 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.74,
  "duration_ratio": 2.13,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.05,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.27,
      0.58
    ],
    "dependency_wait": [
      3.29,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 14.15,
    "assignee_typical_week_effort_h": 9.93,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.56,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0270` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03523 (Operations) |
| Severity / classification / confidence | medium / executor_processing / high |
| Measured | total_duration_h: observed 4.94, expected 2.25, ratio 2.19 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.9h vs an expected 2.3h (2.19x). 91% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (91%); Approval wait at Incharge stage (9%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T03523; 4 events: EV0021550, EV0021552, EV0021603, EV0021609 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.94,
  "duration_ratio": 2.19,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      4.05,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.8,
      0.5
    ],
    "dependency_wait": [
      0.0,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 53.82,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      0.8,
      0.0
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0271` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03527 (Operations) |
| Severity / classification / confidence | medium / executor_processing / medium |
| Measured | total_duration_h: observed 5.49, expected 2.25, ratio 2.44 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 5.5h vs an expected 2.3h (2.44x). 56% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (56%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (43%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T03527; 5 events: EV0021574, EV0021575, EV0021608, EV0021613, EV0021621 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 5.49,
  "duration_ratio": 2.44,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      2.74,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.42,
      0.5
    ],
    "dependency_wait": [
      2.2,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 53.82,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.61,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0272` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03533 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.77, expected 2.36, ratio 2.02 |
| Compared with | BL-v1:L2:Leave Approval:Simple:High |
| What happened | Leave Approval (Simple, High) took 4.8h vs an expected 2.4h (2.02x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); Assignment queue delay (0%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03533; 5 events: EV0021637, EV0021638, EV0021642, EV0021647, EV0021672 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.36,
  "actual_duration_h": 4.77,
  "duration_ratio": 2.02,
  "baseline_p90_h": 4.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.43,
      0.53
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.52,
      0.6
    ],
    "dependency_wait": [
      3.74,
      0.98
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.56,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.26,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0273` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03572 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.89, expected 2.1, ratio 1.86 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.9h vs an expected 2.1h (1.86x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03572; 5 events: EV0021868, EV0021869, EV0021870, EV0021871, EV0021882 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 3.89,
  "duration_ratio": 1.86,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.52,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.25,
      0.56
    ],
    "dependency_wait": [
      3.07,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 31.13,
    "assignee_typical_week_effort_h": 19.94,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.32,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0274` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03584 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.04, expected 2.1, ratio 1.93 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.0h vs an expected 2.1h (1.93x). 94% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (94%); Extended executor processing (5%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03584; 6 events: EV0021933, EV0021934, EV0021939, EV0021941, EV0021949, EV0021979 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.04,
  "duration_ratio": 1.93,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.91,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.25,
      0.56
    ],
    "dependency_wait": [
      2.77,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 53.42,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.02,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0275` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03616 (HR) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 5.85, expected 2.22, ratio 2.63 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 5.8h vs an expected 2.2h (2.63x). 78% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (78%); Rework after rejection (Required document missing) (22%) |
| SOP reference | SOP-020 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03616; 7 events: EV0022122, EV0022124, EV0022134, EV0022142, EV0022145, EV0022146, EV0022151 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 5.85,
  "duration_ratio": 2.63,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.34,
      0.49
    ],
    "rework": [
      1.08,
      0.0
    ],
    "approval_wait": [
      4.38,
      0.58
    ],
    "dependency_wait": [
      0.0,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.95,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.38,
      0.8
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0276` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03625 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.31, expected 2.25, ratio 1.91 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.3h vs an expected 2.3h (1.91x). 96% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (96%); Approval wait at Incharge stage (4%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03625; 5 events: EV0022190, EV0022191, EV0022196, EV0022202, EV0022226 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.31,
  "duration_ratio": 1.91,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.58,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.6,
      0.5
    ],
    "dependency_wait": [
      3.08,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 53.42,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.68,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0277` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03629 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.03, expected 2.15, ratio 2.34 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 5.0h vs an expected 2.2h (2.34x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03629; 5 events: EV0022212, EV0022213, EV0022215, EV0022219, EV0022238 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 5.03,
  "duration_ratio": 2.34,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.39,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.5,
      0.6
    ],
    "dependency_wait": [
      4.08,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.72,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.58,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0278` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03730 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.61, expected 2.25, ratio 2.49 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 5.6h vs an expected 2.3h (2.49x). 81% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (81%); Extended executor processing (17%); Assignment queue delay (1%); Approval wait at Incharge stage (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03730; 5 events: EV0022828, EV0022829, EV0022847, EV0022852, EV0022869 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 5.61,
  "duration_ratio": 2.49,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      1.39,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.53,
      0.5
    ],
    "dependency_wait": [
      3.57,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 46.52,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.1,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0279` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03745 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.87, expected 2.22, ratio 2.19 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.9h vs an expected 2.2h (2.19x). 96% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (96%); Extended executor processing (4%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03745; 7 events: EV0022922, EV0022924, EV0022926, EV0022927, EV0022928, EV0022930, EV0022937 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.87,
  "duration_ratio": 2.19,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.61,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.42,
      0.58
    ],
    "dependency_wait": [
      3.78,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.24,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.19,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0280` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03750 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 9.69, expected 5.35, ratio 1.81 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Low |
| What happened | Employee Document Verification (Medium, Low) took 9.7h vs an expected 5.3h (1.81x). 68% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (68%); Rework after rejection (Incorrect category|Incorrect category) (31%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-021 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03750; 12 events: EV0022952, EV0022953, EV0022956, EV0022960, EV0022965, EV0022981, EV0022988, EV0022991, EV0023010, EV0023013, EV0023014, EV0023024 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.35,
  "actual_duration_h": 9.69,
  "duration_ratio": 1.81,
  "baseline_p90_h": 7.63,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.64,
      0.96
    ],
    "rework": [
      1.63,
      0.0
    ],
    "approval_wait": [
      3.99,
      0.42
    ],
    "dependency_wait": [
      3.32,
      3.7
    ]
  },
  "context": {
    "task_type": "Employee Document Verification",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 2,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.92,
    "assignee_typical_week_effort_h": 9.8,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.3,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0281` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03757 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.55, expected 2.22, ratio 2.49 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 5.5h vs an expected 2.2h (2.49x). 63% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (63%); Rework after rejection (Wrong quantity) (31%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (5%); Assignment queue delay (1%) |
| SOP reference | SOP-020 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03757; 8 events: EV0022992, EV0022994, EV0022999, EV0023004, EV0023012, EV0023019, EV0023020, EV0023031 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 5.55,
  "duration_ratio": 2.49,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.39,
      0.49
    ],
    "rework": [
      1.15,
      0.0
    ],
    "approval_wait": [
      2.92,
      0.58
    ],
    "dependency_wait": [
      0.98,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.57,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.89,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0282` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03797 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.41, expected 2.15, ratio 2.05 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.4h vs an expected 2.2h (2.05x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03797; 5 events: EV0023231, EV0023232, EV0023234, EV0023238, EV0023273 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.41,
  "duration_ratio": 2.05,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.45,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.57,
      0.6
    ],
    "dependency_wait": [
      3.32,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 22.24,
    "assignee_typical_week_effort_h": 9.93,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.89,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0283` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03842 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.53, expected 2.1, ratio 2.16 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.5h vs an expected 2.1h (2.16x). 81% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (81%); Extended executor processing (16%); Approval wait at Incharge stage (2%); Assignment queue delay (1%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03842; 6 events: EV0023525, EV0023526, EV0023529, EV0023534, EV0023537, EV0023542 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.53,
  "duration_ratio": 2.16,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      1.19,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.6,
      0.56
    ],
    "dependency_wait": [
      2.62,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 2.1,
    "assignee_typical_week_effort_h": 19.94,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.22,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0284` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03905 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.77, expected 2.94, ratio 1.96 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 5.8h vs an expected 2.9h (1.96x). 90% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (90%); Extended executor processing (10%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03905; 6 events: EV0023926, EV0023927, EV0023928, EV0023929, EV0023930, EV0023950 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 5.77,
  "duration_ratio": 1.96,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      1.11,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.48,
      0.58
    ],
    "dependency_wait": [
      4.12,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 8.09,
    "assignee_typical_week_effort_h": 12.98,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.61,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0285` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03939 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.98, expected 2.15, ratio 1.85 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.0h vs an expected 2.2h (1.85x). 93% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (93%); Extended executor processing (4%); Assignment queue delay (3%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03939; 5 events: EV0024112, EV0024113, EV0024117, EV0024123, EV0024144 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 3.98,
  "duration_ratio": 1.85,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.55,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.6,
      0.6
    ],
    "dependency_wait": [
      2.7,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 22.11,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.3,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0286` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03943 (HR) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 5.1, expected 2.15, ratio 2.37 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 5.1h vs an expected 2.2h (2.37x). 42% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (42%); Rework after rejection (Amount mismatch) (41%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (10%); Extended executor processing (7%) |
| SOP reference | SOP-020 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03943; 8 events: EV0024129, EV0024130, EV0024135, EV0024137, EV0024146, EV0024153, EV0024156, EV0024159 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 5.1,
  "duration_ratio": 2.37,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.66,
      0.46
    ],
    "rework": [
      1.28,
      0.0
    ],
    "approval_wait": [
      1.91,
      0.6
    ],
    "dependency_wait": [
      1.18,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 9.73,
    "assignee_typical_week_effort_h": 14.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.09,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0287` TICKET_DURATION

| field | value |
|---|---|
| Entity | T03993 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 6.22, expected 2.93, ratio 2.12 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 6.2h vs an expected 2.9h (2.12x). 52% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (52%); Rework after rejection (Amount mismatch) (27%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (12%); Extended executor processing (8%); Assignment queue delay (1%) |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T03993; 9 events: EV0024444, EV0024445, EV0024458, EV0024459, EV0024462, EV0024475, EV0024482, EV0024483, EV0024505 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 6.22,
  "duration_ratio": 2.12,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.08,
      0.76
    ],
    "rework": [
      1.06,
      0.0
    ],
    "approval_wait": [
      2.68,
      0.65
    ],
    "dependency_wait": [
      1.27,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.82,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.95,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0288` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04008 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.94, expected 2.14, ratio 2.31 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 4.9h vs an expected 2.1h (2.31x). 95% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (95%); Extended executor processing (3%); Assignment queue delay (2%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04008; 5 events: EV0024527, EV0024529, EV0024540, EV0024543, EV0024591 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 4.94,
  "duration_ratio": 2.31,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.85,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.22,
      0.53
    ],
    "dependency_wait": [
      3.74,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 76.2,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.96,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0289` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04012 (Operations) |
| Severity / classification / confidence | medium / executor_processing / medium |
| Measured | total_duration_h: observed 16.34, expected 8.83, ratio 1.85 |
| Compared with | BL-v1:L2:Incident Review:Complex:Medium |
| What happened | Incident Review (Complex, Medium) took 16.3h vs an expected 8.8h (1.85x). 47% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (47%); Approval wait at Incharge stage (36%); Cross-team / dependency wait (17%); High assignee workload that week |
| SOP reference | SOP-019 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04012; 7 events: EV0024545, EV0024546, EV0024597, EV0024602, EV0024605, EV0024618, EV0024619 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.83,
  "actual_duration_h": 16.34,
  "duration_ratio": 1.85,
  "baseline_p90_h": 12.44,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      6.03,
      2.41
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      4.62,
      1.8
    ],
    "dependency_wait": [
      5.62,
      4.3
    ]
  },
  "context": {
    "task_type": "Incident Review",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 29.15,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-019",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 10.41,
    "sop_p10_p90_h": [
      8.84,
      11.98
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.97,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0290` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04017 (Operations) |
| Severity / classification / confidence | high / executor_processing / high |
| Measured | total_duration_h: observed 7.95, expected 2.25, ratio 3.53 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 7.9h vs an expected 2.3h (3.53x). 81% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (81%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (18%); Approval wait at Incharge stage (1%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04017; 5 events: EV0024562, EV0024564, EV0024606, EV0024608, EV0024615 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 7.95,
  "duration_ratio": 3.53,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      5.53,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.58,
      0.5
    ],
    "dependency_wait": [
      1.73,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 29.15,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.32,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0291` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04030 (Operations) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 6.18, expected 2.25, ratio 2.74 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 6.2h vs an expected 2.3h (2.74x). 76% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (76%); Extended executor processing (24%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04030; 5 events: EV0024656, EV0024657, EV0024673, EV0024675, EV0024685 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 6.18,
  "duration_ratio": 2.74,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      1.88,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.08,
      0.5
    ],
    "dependency_wait": [
      4.17,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 76.2,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.25,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0292` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04031 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.45, expected 2.25, ratio 1.98 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.5h vs an expected 2.3h (1.98x). 72% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (72%); Extended executor processing (27%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04031; 5 events: EV0024666, EV0024669, EV0024678, EV0024679, EV0024684 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.45,
  "duration_ratio": 1.98,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      1.5,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.28,
      0.5
    ],
    "dependency_wait": [
      2.56,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 76.2,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.84,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0293` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04033 (Operations) |
| Severity / classification / confidence | high / process / medium |
| Measured | total_duration_h: observed 23.3, expected 8.83, ratio 2.64 |
| Compared with | BL-v1:L2:Incident Review:Complex:Medium |
| What happened | Incident Review (Complex, Medium) took 23.3h vs an expected 8.8h (2.64x). 50% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (50%); Cross-team / dependency wait (31%); Extended executor processing (11%); Rework after rejection (Required document missing) (7%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-019 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04033; 9 events: EV0024680, EV0024681, EV0024690, EV0024691, EV0024695, EV0024697, EV0024699, EV0024754, EV0024801 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.83,
  "actual_duration_h": 23.3,
  "duration_ratio": 2.64,
  "baseline_p90_h": 12.44,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      4.0,
      2.41
    ],
    "rework": [
      1.1,
      0.0
    ],
    "approval_wait": [
      9.2,
      1.8
    ],
    "dependency_wait": [
      8.87,
      4.3
    ]
  },
  "context": {
    "task_type": "Incident Review",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 76.2,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-019",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 10.41,
    "sop_p10_p90_h": [
      8.84,
      11.98
    ],
    "first_decision_wait_actual_vs_sop_h": [
      14.59,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0294` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04035 (Operations) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 18.42, expected 9.19, ratio 2.0 |
| Compared with | BL-v1:L2:Incident Review:Complex:High |
| What happened | Incident Review (Complex, High) took 18.4h vs an expected 9.2h (2.00x). 50% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (50%); Approval wait at Incharge stage (27%); Extended executor processing (23%); High assignee workload that week |
| SOP reference | SOP-019 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04035; 6 events: EV0024700, EV0024702, EV0024748, EV0024751, EV0024820, EV0024823 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 9.19,
  "actual_duration_h": 18.42,
  "duration_ratio": 2.0,
  "baseline_p90_h": 11.85,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.07
    ],
    "executor_processing": [
      4.58,
      2.34
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      4.61,
      1.94
    ],
    "dependency_wait": [
      9.18,
      4.32
    ]
  },
  "context": {
    "task_type": "Incident Review",
    "complexity": "Complex",
    "priority": "High",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 76.2,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-019",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 10.41,
    "sop_p10_p90_h": [
      8.84,
      11.98
    ],
    "first_decision_wait_actual_vs_sop_h": [
      9.45,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0295` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04043 (Operations) |
| Severity / classification / confidence | medium / executor_processing / medium |
| Measured | total_duration_h: observed 4.94, expected 2.25, ratio 2.19 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.9h vs an expected 2.3h (2.19x). 53% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (53%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (43%); Approval wait at Incharge stage (3%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04043; 5 events: EV0024735, EV0024737, EV0024762, EV0024770, EV0024794 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.94,
  "duration_ratio": 2.19,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      2.31,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.58,
      0.5
    ],
    "dependency_wait": [
      1.93,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 24.47,
    "assignee_typical_week_effort_h": 13.22,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.52,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0296` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04054 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.11, expected 3.36, ratio 1.82 |
| Compared with | BL-v1:L2:Expense Approval:Simple:High |
| What happened | Expense Approval (Simple, High) took 6.1h vs an expected 3.4h (1.82x). 88% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (88%); Extended executor processing (12%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04054; 5 events: EV0024792, EV0024793, EV0024804, EV0024807, EV0024819 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.36,
  "actual_duration_h": 6.11,
  "duration_ratio": 1.82,
  "baseline_p90_h": 6.14,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.07
    ],
    "executor_processing": [
      1.17,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.52,
      0.6
    ],
    "dependency_wait": [
      4.39,
      1.72
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 16.38,
    "assignee_typical_week_effort_h": 13.0,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.91,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0297` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04060 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.85, expected 2.93, ratio 1.99 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 5.8h vs an expected 2.9h (1.99x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04060; 5 events: EV0024833, EV0024835, EV0024839, EV0024845, EV0024899 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 5.85,
  "duration_ratio": 1.99,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      0.58,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.33,
      0.65
    ],
    "dependency_wait": [
      4.82,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 7.82,
    "assignee_typical_week_effort_h": 10.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.16,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0298` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04068 (Operations) |
| Severity / classification / confidence | high / process / medium |
| Measured | total_duration_h: observed 8.27, expected 2.1, ratio 3.95 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 8.3h vs an expected 2.1h (3.95x). 55% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (55%); Rework after rejection (Incorrect category) (19%); Approval wait at Incharge stage (15%); Extended executor processing (12%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04068; 8 events: EV0024870, EV0024871, EV0024887, EV0024888, EV0024910, EV0024914, EV0024915, EV0024920 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 8.27,
  "duration_ratio": 3.95,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.54,
      0.78
    ],
    "rework": [
      1.2,
      0.0
    ],
    "approval_wait": [
      1.5,
      0.56
    ],
    "dependency_wait": [
      4.0,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 76.2,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.5,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>

### `DEV-0299` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04073 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 17.96, expected 9.03, ratio 1.99 |
| Compared with | BL-v1:L2:Incident Review:Complex:Low |
| What happened | Incident Review (Complex, Low) took 18.0h vs an expected 9.0h (1.99x). 67% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (67%); Cross-team / dependency wait (17%); Rework after rejection (Required document missing) (9%); Extended executor processing (6%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-019 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04073; 11 events: EV0024894, EV0024895, EV0024903, EV0024904, EV0024909, EV0024912, EV0024922, EV0024923, EV0024924, EV0024925, EV0024932 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 9.03,
  "actual_duration_h": 17.96,
  "duration_ratio": 1.99,
  "baseline_p90_h": 12.52,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      3.1,
      2.51
    ],
    "rework": [
      0.85,
      0.0
    ],
    "approval_wait": [
      8.0,
      1.91
    ],
    "dependency_wait": [
      5.91,
      4.38
    ]
  },
  "context": {
    "task_type": "Incident Review",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 76.2,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-019",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 10.41,
    "sop_p10_p90_h": [
      8.84,
      11.98
    ],
    "first_decision_wait_actual_vs_sop_h": [
      9.66,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0300` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04080 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.44, expected 2.25, ratio 1.97 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.4h vs an expected 2.3h (1.97x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04080; 5 events: EV0024953, EV0024954, EV0024955, EV0024957, EV0024963 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.44,
  "duration_ratio": 1.97,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.37,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.5,
      0.5
    ],
    "dependency_wait": [
      3.54,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 15.83,
    "assignee_typical_week_effort_h": 15.58,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.04,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0301` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04093 (Operations) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 16.9, expected 9.19, ratio 1.84 |
| Compared with | BL-v1:L2:Incident Review:Complex:High |
| What happened | Incident Review (Complex, High) took 16.9h vs an expected 9.2h (1.84x). 47% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (47%); Cross-team / dependency wait (20%); Rework after rejection (Required document missing) (18%); Extended executor processing (14%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-019 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04093; 9 events: EV0025032, EV0025033, EV0025052, EV0025060, EV0025077, EV0025081, EV0025082, EV0025086, EV0025087 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 9.19,
  "actual_duration_h": 16.9,
  "duration_ratio": 1.84,
  "baseline_p90_h": 11.85,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.07
    ],
    "executor_processing": [
      3.48,
      2.34
    ],
    "rework": [
      1.48,
      0.0
    ],
    "approval_wait": [
      5.85,
      1.94
    ],
    "dependency_wait": [
      5.95,
      4.32
    ]
  },
  "context": {
    "task_type": "Incident Review",
    "complexity": "Complex",
    "priority": "High",
    "dependency_count": 2,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 42.13,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-019",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 10.41,
    "sop_p10_p90_h": [
      8.84,
      11.98
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.91,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0302` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04108 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.76, expected 2.14, ratio 1.76 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 3.8h vs an expected 2.1h (1.76x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Assignment queue delay (2%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04108; 6 events: EV0025117, EV0025118, EV0025124, EV0025125, EV0025126, EV0025143 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 3.76,
  "duration_ratio": 1.76,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.68,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.18,
      0.53
    ],
    "dependency_wait": [
      2.76,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.06,
    "assignee_typical_week_effort_h": 13.22,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.94,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0303` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04129 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.85, expected 2.1, ratio 2.31 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.8h vs an expected 2.1h (2.31x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Approval wait at Incharge stage (1%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04129; 5 events: EV0025243, EV0025247, EV0025250, EV0025255, EV0025283 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.85,
  "duration_ratio": 2.31,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.46,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.6,
      0.56
    ],
    "dependency_wait": [
      3.69,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 42.22,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.29,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0304` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04143 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.95, expected 2.1, ratio 1.88 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.9h vs an expected 2.1h (1.88x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04143; 6 events: EV0025340, EV0025342, EV0025346, EV0025347, EV0025348, EV0025382 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 3.95,
  "duration_ratio": 1.88,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.43,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.15,
      0.56
    ],
    "dependency_wait": [
      3.27,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 42.22,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.42,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0305` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04145 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.64, expected 2.1, ratio 2.22 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.6h vs an expected 2.1h (2.22x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Assignment queue delay (2%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04145; 6 events: EV0025353, EV0025355, EV0025359, EV0025368, EV0025372, EV0025393 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.64,
  "duration_ratio": 2.22,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.64,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.38,
      0.56
    ],
    "dependency_wait": [
      3.49,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 42.22,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.87,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0306` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04150 (Operations) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 16.87, expected 8.83, ratio 1.91 |
| Compared with | BL-v1:L2:Incident Review:Complex:Medium |
| What happened | Incident Review (Complex, Medium) took 16.9h vs an expected 8.8h (1.91x). 40% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (40%); Approval wait at Incharge stage (36%); Extended executor processing (23%); Assignment queue delay (0%) |
| SOP reference | SOP-019 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04150; 8 events: EV0025389, EV0025390, EV0025400, EV0025402, EV0025410, EV0025411, EV0025420, EV0025437 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.83,
  "actual_duration_h": 16.87,
  "duration_ratio": 1.91,
  "baseline_p90_h": 12.44,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      4.35,
      2.41
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      4.82,
      1.8
    ],
    "dependency_wait": [
      7.62,
      4.3
    ]
  },
  "context": {
    "task_type": "Incident Review",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 13.06,
    "assignee_typical_week_effort_h": 13.22,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-019",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 10.41,
    "sop_p10_p90_h": [
      8.84,
      11.98
    ],
    "first_decision_wait_actual_vs_sop_h": [
      8.2,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0307` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04174 (Operations) |
| Severity / classification / confidence | medium / executor_processing / high |
| Measured | total_duration_h: observed 5.6, expected 2.25, ratio 2.48 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 5.6h vs an expected 2.3h (2.48x). 87% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (87%); Approval wait at Incharge stage (13%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04174; 4 events: EV0025550, EV0025551, EV0025583, EV0025599 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 5.6,
  "duration_ratio": 2.48,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      4.49,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.07,
      0.5
    ],
    "dependency_wait": [
      0.0,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 57.69,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      1.07,
      0.0
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0308` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04178 (Operations) |
| Severity / classification / confidence | high / executor_processing / high |
| Measured | total_duration_h: observed 6.45, expected 2.1, ratio 3.08 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 6.4h vs an expected 2.1h (3.08x). 71% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (71%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (29%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04178; 6 events: EV0025558, EV0025559, EV0025584, EV0025596, EV0025601, EV0025621 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 6.45,
  "duration_ratio": 3.08,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      4.04,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.55,
      0.56
    ],
    "dependency_wait": [
      1.82,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 57.69,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.37,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0309` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04197 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.71, expected 2.93, ratio 1.95 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 5.7h vs an expected 2.9h (1.95x). 88% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (88%); Extended executor processing (11%); Assignment queue delay (1%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04197; 6 events: EV0025671, EV0025673, EV0025686, EV0025692, EV0025697, EV0025746 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 5.71,
  "duration_ratio": 1.95,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      1.15,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.42,
      0.65
    ],
    "dependency_wait": [
      4.01,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.71,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.43,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0310` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04199 (Operations) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 8.99, expected 2.25, ratio 3.99 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 9.0h vs an expected 2.3h (3.99x). 63% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (63%); Approval wait at Incharge stage (25%); Rework after rejection (Amount mismatch) (12%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04199; 8 events: EV0025678, EV0025679, EV0025687, EV0025695, EV0025757, EV0025762, EV0025764, EV0025767 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 8.99,
  "duration_ratio": 3.99,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.61,
      0.79
    ],
    "rework": [
      0.83,
      0.0
    ],
    "approval_wait": [
      2.29,
      0.5
    ],
    "dependency_wait": [
      5.21,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 44.79,
    "assignee_typical_week_effort_h": 19.94,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.5,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>

### `DEV-0311` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04213 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.94, expected 2.22, ratio 1.77 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 3.9h vs an expected 2.2h (1.77x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); Assignment queue delay (0%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04213; 6 events: EV0025776, EV0025777, EV0025780, EV0025781, EV0025782, EV0025802 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 3.94,
  "duration_ratio": 1.77,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      0.34,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.17,
      0.58
    ],
    "dependency_wait": [
      3.35,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 2.22,
    "assignee_typical_week_effort_h": 12.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.51,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0312` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04251 (Operations) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 5.26, expected 2.1, ratio 2.51 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 5.3h vs an expected 2.1h (2.51x). 67% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (67%); Rework after rejection (Amount mismatch) (32%); Extended executor processing (1%); Assignment queue delay (0%) |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04251; 7 events: EV0025965, EV0025968, EV0025980, EV0025994, EV0026002, EV0026004, EV0026012 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 5.26,
  "duration_ratio": 2.51,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.81,
      0.78
    ],
    "rework": [
      1.24,
      0.0
    ],
    "approval_wait": [
      3.11,
      0.56
    ],
    "dependency_wait": [
      0.0,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.5,
    "assignee_typical_week_effort_h": 17.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.11,
      0.0
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0313` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04283 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 9.03, expected 5.16, ratio 1.75 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 9.0h vs an expected 5.2h (1.75x). 44% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (44%); Approval wait at Incharge stage (27%); Rework after rejection (Amount mismatch) (24%); Extended executor processing (6%); High assignee workload that week |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04283; 10 events: EV0026154, EV0026156, EV0026167, EV0026168, EV0026172, EV0026178, EV0026205, EV0026206, EV0026207, EV0026209 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.16,
  "actual_duration_h": 9.03,
  "duration_ratio": 1.75,
  "baseline_p90_h": 7.62,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      1.37,
      1.11
    ],
    "rework": [
      0.99,
      0.0
    ],
    "approval_wait": [
      1.5,
      0.38
    ],
    "dependency_wait": [
      5.11,
      3.27
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 25.96,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.61,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0314` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04285 (Operations) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 17.5, expected 9.03, ratio 1.94 |
| Compared with | BL-v1:L2:Incident Review:Complex:Low |
| What happened | Incident Review (Complex, Low) took 17.5h vs an expected 9.0h (1.94x). 50% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (50%); Extended executor processing (36%); Cross-team / dependency wait (13%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-019 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04285; 7 events: EV0026157, EV0026160, EV0026200, EV0026201, EV0026203, EV0026215, EV0026218 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 9.03,
  "actual_duration_h": 17.5,
  "duration_ratio": 1.94,
  "baseline_p90_h": 12.52,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      5.6,
      2.51
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      6.25,
      1.91
    ],
    "dependency_wait": [
      5.52,
      4.38
    ]
  },
  "context": {
    "task_type": "Incident Review",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 37.49,
    "assignee_typical_week_effort_h": 17.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-019",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 10.41,
    "sop_p10_p90_h": [
      8.84,
      11.98
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.09,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0315` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04288 (HR) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 4.11, expected 2.22, ratio 1.85 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.1h vs an expected 2.2h (1.85x). 57% of the extra time is attributed to: rework after rejection (wrong quantity). |
| Most likely reason | Rework after rejection (Wrong quantity); preventable by S3 day count excluding holidays |
| Ranked candidate causes | Rework after rejection (Wrong quantity) (57%); Approval wait at Incharge stage (26%); Extended executor processing (17%) |
| SOP reference | SOP-020 band above_p90; rework_trigger RW-QTY |
| Preventable by | S3 day count excluding holidays |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T04288; 8 events: EV0026180, EV0026182, EV0026186, EV0026189, EV0026193, EV0026198, EV0026199, EV0026202 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.11,
  "duration_ratio": 1.85,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.87,
      0.49
    ],
    "rework": [
      1.28,
      0.0
    ],
    "approval_wait": [
      1.15,
      0.58
    ],
    "dependency_wait": [
      0.78,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 9.46,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      1.93,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0316` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04302 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.73, expected 2.1, ratio 1.78 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.7h vs an expected 2.1h (1.78x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04302; 6 events: EV0026291, EV0026292, EV0026298, EV0026299, EV0026305, EV0026342 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 3.73,
  "duration_ratio": 1.78,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.66,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.33,
      0.56
    ],
    "dependency_wait": [
      2.69,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 24.31,
    "assignee_typical_week_effort_h": 19.94,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.02,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0317` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04305 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.81, expected 2.1, ratio 1.82 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.8h vs an expected 2.1h (1.82x). 85% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (85%); Extended executor processing (9%); Approval wait at Incharge stage (6%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04305; 5 events: EV0026301, EV0026302, EV0026313, EV0026322, EV0026357 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 3.81,
  "duration_ratio": 1.82,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.95,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.67,
      0.56
    ],
    "dependency_wait": [
      2.13,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 48.5,
    "assignee_typical_week_effort_h": 13.22,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.79,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0318` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04329 (Operations) |
| Severity / classification / confidence | high / process / medium |
| Measured | total_duration_h: observed 6.62, expected 2.14, ratio 3.1 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 6.6h vs an expected 2.1h (3.10x). 45% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (45%); Extended executor processing (42%); Rework after rejection (Wrong quantity) (14%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04329; 7 events: EV0026438, EV0026439, EV0026466, EV0026481, EV0026487, EV0026490, EV0026497 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 6.62,
  "duration_ratio": 3.1,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      2.96,
      0.76
    ],
    "rework": [
      0.72,
      0.0
    ],
    "approval_wait": [
      2.91,
      0.53
    ],
    "dependency_wait": [
      0.0,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 69.22,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.91,
      0.0
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0319` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04342 (Operations) |
| Severity / classification / confidence | medium / executor_processing / high |
| Measured | total_duration_h: observed 17.87, expected 9.03, ratio 1.98 |
| Compared with | BL-v1:L2:Incident Review:Complex:Low |
| What happened | Incident Review (Complex, Low) took 17.9h vs an expected 9.0h (1.98x). 93% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (93%); Cross-team / dependency wait (7%); High assignee workload that week |
| SOP reference | SOP-019 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04342; 7 events: EV0026519, EV0026521, EV0026610, EV0026613, EV0026616, EV0026629, EV0026631 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 9.03,
  "actual_duration_h": 17.87,
  "duration_ratio": 1.98,
  "baseline_p90_h": 12.52,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      11.04,
      2.51
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.77,
      1.91
    ],
    "dependency_wait": [
      4.99,
      4.38
    ]
  },
  "context": {
    "task_type": "Incident Review",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 69.22,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-019",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 10.41,
    "sop_p10_p90_h": [
      8.84,
      11.98
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.59,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0320` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04351 (Operations) |
| Severity / classification / confidence | high / executor_processing / medium |
| Measured | total_duration_h: observed 11.9, expected 2.25, ratio 5.28 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 11.9h vs an expected 2.3h (5.28x). 56% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (56%); Approval wait at Incharge stage (35%); Rework after rejection (Wrong quantity) (9%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04351; 7 events: EV0026558, EV0026559, EV0026617, EV0026621, EV0026623, EV0026624, EV0026630 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 11.9,
  "duration_ratio": 5.28,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      6.71,
      0.79
    ],
    "rework": [
      0.9,
      0.0
    ],
    "approval_wait": [
      4.22,
      0.5
    ],
    "dependency_wait": [
      0.0,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 69.22,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.22,
      0.0
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0321` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04352 (Operations) |
| Severity / classification / confidence | high / executor_processing / high |
| Measured | total_duration_h: observed 8.33, expected 2.1, ratio 3.98 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 8.3h vs an expected 2.1h (3.98x). 91% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (91%); Approval wait at Incharge stage (9%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04352; 4 events: EV0026562, EV0026565, EV0026619, EV0026622 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 8.33,
  "duration_ratio": 3.98,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      7.09,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.15,
      0.56
    ],
    "dependency_wait": [
      0.0,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 69.22,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      1.15,
      0.0
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0322` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04354 (Operations) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 5.6, expected 2.1, ratio 2.67 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 5.6h vs an expected 2.1h (2.67x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04354; 6 events: EV0026572, EV0026574, EV0026577, EV0026587, EV0026590, EV0026618 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 5.6,
  "duration_ratio": 2.67,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.76,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.13,
      0.56
    ],
    "dependency_wait": [
      4.68,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 37.49,
    "assignee_typical_week_effort_h": 17.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.81,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0323` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04368 (Operations) |
| Severity / classification / confidence | medium / executor_processing / high |
| Measured | total_duration_h: observed 4.27, expected 2.14, ratio 2.0 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 4.3h vs an expected 2.1h (2.00x). 82% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (82%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (17%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04368; 6 events: EV0026656, EV0026661, EV0026689, EV0026694, EV0026695, EV0026698 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 4.27,
  "duration_ratio": 2.0,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      2.78,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.4,
      0.53
    ],
    "dependency_wait": [
      0.97,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 69.22,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      1.37,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0324` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04374 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.2, expected 2.14, ratio 1.97 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 4.2h vs an expected 2.1h (1.97x). 88% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (88%); Extended executor processing (12%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04374; 6 events: EV0026729, EV0026730, EV0026732, EV0026734, EV0026736, EV0026746 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 4.2,
  "duration_ratio": 1.97,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      1.07,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.08,
      0.53
    ],
    "dependency_wait": [
      2.96,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 48.5,
    "assignee_typical_week_effort_h": 13.22,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.05,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0325` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04384 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.94, expected 2.14, ratio 1.84 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 3.9h vs an expected 2.1h (1.84x). 81% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (81%); Extended executor processing (19%); Assignment queue delay (0%) |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04384; 5 events: EV0026794, EV0026795, EV0026800, EV0026805, EV0026831 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 3.94,
  "duration_ratio": 1.84,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      1.24,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      2.61,
      0.53
    ],
    "dependency_wait": [
      0.0,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 2.14,
    "assignee_typical_week_effort_h": 19.94,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.61,
      0.0
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0326` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04395 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 17.09, expected 9.03, ratio 1.89 |
| Compared with | BL-v1:L2:Incident Review:Complex:Low |
| What happened | Incident Review (Complex, Low) took 17.1h vs an expected 9.0h (1.89x). 64% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (64%); Approval wait at Incharge stage (33%); Extended executor processing (3%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-019 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04395; 6 events: EV0026839, EV0026840, EV0026883, EV0026892, EV0026933, EV0026934 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 9.03,
  "actual_duration_h": 17.09,
  "duration_ratio": 1.89,
  "baseline_p90_h": 12.52,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      2.79,
      2.51
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      4.58,
      1.91
    ],
    "dependency_wait": [
      9.62,
      4.38
    ]
  },
  "context": {
    "task_type": "Incident Review",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 53.37,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-019",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 10.41,
    "sop_p10_p90_h": [
      8.84,
      11.98
    ],
    "first_decision_wait_actual_vs_sop_h": [
      10.22,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0327` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04417 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.97, expected 2.22, ratio 2.24 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 5.0h vs an expected 2.2h (2.24x). 94% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (94%); Extended executor processing (6%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04417; 7 events: EV0026977, EV0026978, EV0026979, EV0026980, EV0026981, EV0026984, EV0027031 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.22,
  "actual_duration_h": 4.97,
  "duration_ratio": 2.24,
  "baseline_p90_h": 4.2,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.67,
      0.49
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.53,
      0.58
    ],
    "dependency_wait": [
      3.72,
      0.78
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 30.03,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.25,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0328` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04442 (Operations) |
| Severity / classification / confidence | high / process / medium |
| Measured | total_duration_h: observed 5.85, expected 2.1, ratio 2.79 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 5.9h vs an expected 2.1h (2.79x). 42% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (42%); Approval wait at Incharge stage (31%); Rework after rejection (Incorrect category) (21%); Extended executor processing (6%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04442; 8 events: EV0027103, EV0027104, EV0027114, EV0027117, EV0027155, EV0027163, EV0027165, EV0027171 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 5.85,
  "duration_ratio": 2.79,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      1.0,
      0.78
    ],
    "rework": [
      0.84,
      0.0
    ],
    "approval_wait": [
      1.77,
      0.56
    ],
    "dependency_wait": [
      2.18,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 53.37,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.96,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>

### `DEV-0329` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04454 (Procurement) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 9.12, expected 5.04, ratio 1.81 |
| Compared with | BL-v1:L2:BOQ Review:Medium:Medium |
| What happened | BOQ Review (Medium, Medium) took 9.1h vs an expected 5.0h (1.81x). 45% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (45%); Cross-team / dependency wait (29%); Rework after rejection (Incorrect category) (25%) |
| SOP reference | SOP-013 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04454; 8 events: EV0027194, EV0027195, EV0027198, EV0027200, EV0027233, EV0027250, EV0027253, EV0027274 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.04,
  "actual_duration_h": 9.12,
  "duration_ratio": 1.81,
  "baseline_p90_h": 6.91,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.97,
      1.06
    ],
    "rework": [
      1.11,
      0.0
    ],
    "approval_wait": [
      2.42,
      0.43
    ],
    "dependency_wait": [
      4.57,
      3.3
    ]
  },
  "context": {
    "task_type": "BOQ Review",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 15.68,
    "assignee_typical_week_effort_h": 29.14,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-013",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.89,
    "sop_p10_p90_h": [
      4.57,
      7.21
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.99,
      3.65
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0330` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04465 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.17, expected 3.36, ratio 1.84 |
| Compared with | BL-v1:L2:Expense Approval:Simple:High |
| What happened | Expense Approval (Simple, High) took 6.2h vs an expected 3.4h (1.84x). 62% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (62%); Rework after rejection (Required document missing) (34%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (4%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04465; 9 events: EV0027243, EV0027244, EV0027251, EV0027254, EV0027258, EV0027279, EV0027290, EV0027293, EV0027303 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.36,
  "actual_duration_h": 6.17,
  "duration_ratio": 1.84,
  "baseline_p90_h": 6.14,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.07
    ],
    "executor_processing": [
      0.46,
      0.79
    ],
    "rework": [
      1.13,
      0.0
    ],
    "approval_wait": [
      2.67,
      0.6
    ],
    "dependency_wait": [
      1.87,
      1.72
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 26.65,
    "assignee_typical_week_effort_h": 13.0,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.54,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0331` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04468 (Operations) |
| Severity / classification / confidence | high / process / medium |
| Measured | total_duration_h: observed 10.07, expected 2.1, ratio 4.81 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 10.1h vs an expected 2.1h (4.81x). 41% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (41%); Approval wait at Incharge stage (22%); Extended executor processing (19%); Rework after rejection (Required document missing) (17%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04468; 8 events: EV0027260, EV0027263, EV0027289, EV0027294, EV0027317, EV0027319, EV0027320, EV0027321 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 10.07,
  "duration_ratio": 4.81,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      2.36,
      0.78
    ],
    "rework": [
      1.38,
      0.0
    ],
    "approval_wait": [
      2.32,
      0.56
    ],
    "dependency_wait": [
      3.88,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 53.37,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.2,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>

### `DEV-0332` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04490 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.84, expected 2.25, ratio 2.15 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.8h vs an expected 2.3h (2.15x). 88% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (88%); Extended executor processing (12%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04490; 5 events: EV0027447, EV0027448, EV0027449, EV0027451, EV0027455 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.84,
  "duration_ratio": 2.15,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.17,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.15,
      0.5
    ],
    "dependency_wait": [
      3.49,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 53.37,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.64,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0333` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04509 (Operations) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 3.79, expected 2.14, ratio 1.77 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 3.8h vs an expected 2.1h (1.77x). 53% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (53%); Rework after rejection (Incorrect category) (23%); Extended executor processing (22%); Assignment queue delay (1%) |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04509; 7 events: EV0027551, EV0027554, EV0027566, EV0027571, EV0027576, EV0027580, EV0027602 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 3.79,
  "duration_ratio": 1.77,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      1.29,
      0.76
    ],
    "rework": [
      0.57,
      0.0
    ],
    "approval_wait": [
      1.81,
      0.53
    ],
    "dependency_wait": [
      0.0,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.61,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      1.81,
      0.0
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0334` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04514 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.91, expected 2.1, ratio 2.35 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.9h vs an expected 2.1h (2.35x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04514; 5 events: EV0027568, EV0027569, EV0027575, EV0027579, EV0027627 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.91,
  "duration_ratio": 2.35,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.64,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.17,
      0.56
    ],
    "dependency_wait": [
      4.01,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 26.56,
    "assignee_typical_week_effort_h": 13.22,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.18,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0335` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04519 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 9.45, expected 4.89, ratio 1.93 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Medium |
| What happened | Invoice Verification (Medium, Medium) took 9.5h vs an expected 4.9h (1.93x). 60% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (60%); Rework after rejection (Amount mismatch|Incorrect category) (38%); Extended executor processing (2%) |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04519; 11 events: EV0027587, EV0027588, EV0027610, EV0027617, EV0027640, EV0027649, EV0027652, EV0027657, EV0027660, EV0027663, EV0027668 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 4.89,
  "actual_duration_h": 9.45,
  "duration_ratio": 1.93,
  "baseline_p90_h": 7.24,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.21,
      1.09
    ],
    "rework": [
      1.97,
      0.0
    ],
    "approval_wait": [
      3.51,
      0.4
    ],
    "dependency_wait": [
      2.73,
      3.16
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "Medium",
    "dependency_count": 1,
    "rejection_count": 2,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.71,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.24,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0336` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04522 (Operations) |
| Severity / classification / confidence | medium / executor_processing / high |
| Measured | total_duration_h: observed 16.91, expected 9.19, ratio 1.84 |
| Compared with | BL-v1:L2:Incident Review:Complex:High |
| What happened | Incident Review (Complex, High) took 16.9h vs an expected 9.2h (1.84x). 61% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (61%); Cross-team / dependency wait (22%); Approval wait at Incharge stage (17%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-019 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04522; 7 events: EV0027599, EV0027603, EV0027656, EV0027664, EV0027665, EV0027674, EV0027676 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 9.19,
  "actual_duration_h": 16.91,
  "duration_ratio": 1.84,
  "baseline_p90_h": 11.85,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.07
    ],
    "executor_processing": [
      7.35,
      2.34
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      3.3,
      1.94
    ],
    "dependency_wait": [
      6.17,
      4.32
    ]
  },
  "context": {
    "task_type": "Incident Review",
    "complexity": "Complex",
    "priority": "High",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 95.74,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-019",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 10.41,
    "sop_p10_p90_h": [
      8.84,
      11.98
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.32,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0337` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04527 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.7, expected 2.1, ratio 2.24 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.7h vs an expected 2.1h (2.24x). 93% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (93%); Extended executor processing (6%); Assignment queue delay (1%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04527; 6 events: EV0027633, EV0027637, EV0027643, EV0027646, EV0027651, EV0027666 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.7,
  "duration_ratio": 2.24,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.98,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.28,
      0.56
    ],
    "dependency_wait": [
      3.34,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 17.61,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.63,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0338` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04528 (Operations) |
| Severity / classification / confidence | medium / executor_processing / high |
| Measured | total_duration_h: observed 17.17, expected 9.19, ratio 1.87 |
| Compared with | BL-v1:L2:Incident Review:Complex:High |
| What happened | Incident Review (Complex, High) took 17.2h vs an expected 9.2h (1.87x). 63% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (63%); Cross-team / dependency wait (22%); Approval wait at Incharge stage (15%); High assignee workload that week |
| SOP reference | SOP-019 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04528; 6 events: EV0027636, EV0027638, EV0027670, EV0027671, EV0027677, EV0027689 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 9.19,
  "actual_duration_h": 17.17,
  "duration_ratio": 1.87,
  "baseline_p90_h": 11.85,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.07
    ],
    "executor_processing": [
      7.7,
      2.34
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      3.19,
      1.94
    ],
    "dependency_wait": [
      6.21,
      4.32
    ]
  },
  "context": {
    "task_type": "Incident Review",
    "complexity": "Complex",
    "priority": "High",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 95.74,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-019",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 10.41,
    "sop_p10_p90_h": [
      8.84,
      11.98
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.33,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0339` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04539 (HR) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 9.3, expected 5.01, ratio 1.85 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:High |
| What happened | Employee Document Verification (Medium, High) took 9.3h vs an expected 5.0h (1.85x). 41% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (41%); Approval wait at Incharge stage (30%); Rework after rejection (Amount mismatch) (25%); Extended executor processing (4%) |
| SOP reference | SOP-021 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04539; 9 events: EV0027714, EV0027716, EV0027724, EV0027737, EV0027740, EV0027770, EV0027772, EV0027775, EV0027777 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.01,
  "actual_duration_h": 9.3,
  "duration_ratio": 1.85,
  "baseline_p90_h": 7.63,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.1
    ],
    "executor_processing": [
      1.1,
      0.92
    ],
    "rework": [
      1.15,
      0.0
    ],
    "approval_wait": [
      1.78,
      0.38
    ],
    "dependency_wait": [
      5.24,
      3.35
    ]
  },
  "context": {
    "task_type": "Employee Document Verification",
    "complexity": "Medium",
    "priority": "High",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 10.36,
    "assignee_typical_week_effort_h": 11.4,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.02,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0340` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04569 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.52, expected 2.25, ratio 2.01 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.5h vs an expected 2.3h (2.01x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Approval wait at Incharge stage (2%); Extended executor processing (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04569; 6 events: EV0027900, EV0027902, EV0027912, EV0027917, EV0027923, EV0027967 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.52,
  "duration_ratio": 2.01,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.81,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.55,
      0.5
    ],
    "dependency_wait": [
      3.12,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 24.42,
    "assignee_typical_week_effort_h": 17.76,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.67,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0341` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04575 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.56, expected 2.1, ratio 2.18 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 4.6h vs an expected 2.1h (2.18x). 95% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (95%); Extended executor processing (3%); Approval wait at Incharge stage (2%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04575; 5 events: EV0027928, EV0027929, EV0027944, EV0027951, EV0027984 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 4.56,
  "duration_ratio": 2.18,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      0.86,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.62,
      0.56
    ],
    "dependency_wait": [
      3.03,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 95.74,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.65,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0342` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04577 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.18, expected 2.15, ratio 2.41 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 5.2h vs an expected 2.2h (2.41x). 99% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (99%); Assignment queue delay (1%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04577; 5 events: EV0027932, EV0027935, EV0027937, EV0027943, EV0027989 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 5.18,
  "duration_ratio": 2.41,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.28,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.32,
      0.6
    ],
    "dependency_wait": [
      4.45,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 9.73,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.77,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0343` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04586 (Operations) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 5.42, expected 2.1, ratio 2.59 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 5.4h vs an expected 2.1h (2.59x). 70% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (70%); Extended executor processing (16%); Rework after rejection (Incorrect category) (14%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04586; 7 events: EV0028006, EV0028007, EV0028024, EV0028034, EV0028044, EV0028048, EV0028065 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 5.42,
  "duration_ratio": 2.59,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      1.42,
      0.78
    ],
    "rework": [
      0.57,
      0.0
    ],
    "approval_wait": [
      3.37,
      0.56
    ],
    "dependency_wait": [
      0.0,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 95.74,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.37,
      0.0
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0344` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04589 (Operations) |
| Severity / classification / confidence | medium / executor_processing / low |
| Measured | total_duration_h: observed 17.01, expected 9.03, ratio 1.88 |
| Compared with | BL-v1:L2:Incident Review:Complex:Low |
| What happened | Incident Review (Complex, Low) took 17.0h vs an expected 9.0h (1.88x). 35% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (35%); Cross-team / dependency wait (35%); Approval wait at Incharge stage (30%); High assignee workload that week |
| SOP reference | SOP-019 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04589; 7 events: EV0028013, EV0028016, EV0028055, EV0028070, EV0028075, EV0028160, EV0028170 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 9.03,
  "actual_duration_h": 17.01,
  "duration_ratio": 1.88,
  "baseline_p90_h": 12.52,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      5.38,
      2.51
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      4.38,
      1.91
    ],
    "dependency_wait": [
      7.22,
      4.38
    ]
  },
  "context": {
    "task_type": "Incident Review",
    "complexity": "Complex",
    "priority": "Low",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 95.74,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-019",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 10.41,
    "sop_p10_p90_h": [
      8.84,
      11.98
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.52,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0345` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04591 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 9.57, expected 5.35, ratio 1.79 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Low |
| What happened | Employee Document Verification (Medium, Low) took 9.6h vs an expected 5.3h (1.79x). 62% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (62%); Rework after rejection (Wrong quantity) (21%); Approval wait at Incharge stage (17%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-021 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04591; 8 events: EV0028022, EV0028025, EV0028036, EV0028050, EV0028117, EV0028131, EV0028134, EV0028139 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.35,
  "actual_duration_h": 9.57,
  "duration_ratio": 1.79,
  "baseline_p90_h": 7.63,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      0.88,
      0.96
    ],
    "rework": [
      0.93,
      0.0
    ],
    "approval_wait": [
      1.18,
      0.42
    ],
    "dependency_wait": [
      6.48,
      3.7
    ]
  },
  "context": {
    "task_type": "Employee Document Verification",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 18.27,
    "assignee_typical_week_effort_h": 9.93,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      7.66,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0346` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04592 (Operations) |
| Severity / classification / confidence | high / executor_processing / high |
| Measured | total_duration_h: observed 6.65, expected 2.1, ratio 3.17 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 6.6h vs an expected 2.1h (3.17x). 82% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (82%); Approval wait at Incharge stage (18%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04592; 4 events: EV0028027, EV0028029, EV0028078, EV0028101 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 6.65,
  "duration_ratio": 3.17,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.08
    ],
    "executor_processing": [
      5.08,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.48,
      0.56
    ],
    "dependency_wait": [
      0.0,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 95.74,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      1.48,
      0.0
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0347` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04600 (Operations) |
| Severity / classification / confidence | high / executor_processing / high |
| Measured | total_duration_h: observed 7.97, expected 2.1, ratio 3.8 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 8.0h vs an expected 2.1h (3.80x). 70% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (70%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (30%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04600; 5 events: EV0028071, EV0028072, EV0028144, EV0028150, EV0028161 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 7.97,
  "duration_ratio": 3.8,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      5.09,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.5,
      0.56
    ],
    "dependency_wait": [
      2.34,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 95.74,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.84,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0348` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04615 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.67, expected 2.93, ratio 1.93 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 5.7h vs an expected 2.9h (1.93x). 100% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (100%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04615; 5 events: EV0028190, EV0028192, EV0028196, EV0028197, EV0028224 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.93,
  "actual_duration_h": 5.67,
  "duration_ratio": 1.93,
  "baseline_p90_h": 6.0,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.58,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.3,
      0.65
    ],
    "dependency_wait": [
      4.72,
      0.8
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 12.71,
    "assignee_typical_week_effort_h": 12.08,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.02,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0349` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04617 (Operations) |
| Severity / classification / confidence | high / executor_processing / high |
| Measured | total_duration_h: observed 5.64, expected 2.25, ratio 2.51 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 5.6h vs an expected 2.3h (2.51x). 66% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (66%); Approval wait at Incharge stage (33%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04617; 4 events: EV0028198, EV0028201, EV0028222, EV0028231 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 5.64,
  "duration_ratio": 2.51,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.08
    ],
    "executor_processing": [
      3.63,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.92,
      0.5
    ],
    "dependency_wait": [
      0.0,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 95.74,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      1.92,
      0.0
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0350` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04618 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.82, expected 2.94, ratio 1.98 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 5.8h vs an expected 2.9h (1.98x). 81% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (81%); Extended executor processing (19%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04618; 6 events: EV0028199, EV0028200, EV0028204, EV0028209, EV0028210, EV0028233 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.94,
  "actual_duration_h": 5.82,
  "duration_ratio": 1.98,
  "baseline_p90_h": 5.36,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      1.47,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.25,
      0.58
    ],
    "dependency_wait": [
      4.08,
      1.17
    ]
  },
  "context": {
    "task_type": "Expense Approval",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 18.85,
    "assignee_typical_week_effort_h": 13.11,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-016",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.82,
    "sop_p10_p90_h": [
      1.38,
      2.26
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.33,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0351` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04634 (HR) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.25, expected 2.15, ratio 1.98 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.3h vs an expected 2.2h (1.98x). 98% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (98%); Assignment queue delay (2%); Extended executor processing (0%) |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04634; 6 events: EV0028292, EV0028293, EV0028296, EV0028297, EV0028303, EV0028321 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.15,
  "actual_duration_h": 4.25,
  "duration_ratio": 1.98,
  "baseline_p90_h": 4.38,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.08
    ],
    "executor_processing": [
      0.46,
      0.46
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.6,
      0.6
    ],
    "dependency_wait": [
      3.06,
      0.88
    ]
  },
  "context": {
    "task_type": "Leave Approval",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 2.15,
    "assignee_typical_week_effort_h": 11.91,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-020",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.38,
    "sop_p10_p90_h": [
      0.95,
      1.81
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.66,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0352` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04638 (Operations) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 4.42, expected 2.14, ratio 2.07 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 4.4h vs an expected 2.1h (2.07x). 92% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (92%); Extended executor processing (8%); Approval wait at Incharge stage (1%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04638; 6 events: EV0028331, EV0028332, EV0028333, EV0028336, EV0028339, EV0028350 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.14,
  "actual_duration_h": 4.42,
  "duration_ratio": 2.07,
  "baseline_p90_h": 4.03,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.08
    ],
    "executor_processing": [
      0.95,
      0.76
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.55,
      0.53
    ],
    "dependency_wait": [
      2.89,
      0.57
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "High",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 8.74,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.44,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0353` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04641 (Operations) |
| Severity / classification / confidence | medium / executor_processing / medium |
| Measured | total_duration_h: observed 16.61, expected 8.83, ratio 1.88 |
| Compared with | BL-v1:L2:Incident Review:Complex:Medium |
| What happened | Incident Review (Complex, Medium) took 16.6h vs an expected 8.8h (1.88x). 57% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (57%); Approval wait at Incharge stage (23%); Cross-team / dependency wait (19%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-019 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04641; 7 events: EV0028343, EV0028344, EV0028383, EV0028399, EV0028405, EV0028422, EV0028423 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.83,
  "actual_duration_h": 16.61,
  "duration_ratio": 1.88,
  "baseline_p90_h": 12.44,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      7.02,
      2.41
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      3.64,
      1.8
    ],
    "dependency_wait": [
      5.84,
      4.3
    ]
  },
  "context": {
    "task_type": "Incident Review",
    "complexity": "Complex",
    "priority": "Medium",
    "dependency_count": 2,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 31.41,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-019",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 10.41,
    "sop_p10_p90_h": [
      8.84,
      11.98
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.39,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0354` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04644 (Operations) |
| Severity / classification / confidence | high / executor_processing / high |
| Measured | total_duration_h: observed 6.75, expected 2.1, ratio 3.22 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 6.8h vs an expected 2.1h (3.22x). 83% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (83%); Approval wait at Incharge stage (16%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T04644; 5 events: EV0028357, EV0028359, EV0028406, EV0028408, EV0028416 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 6.75,
  "duration_ratio": 3.22,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.08
    ],
    "executor_processing": [
      5.21,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.43,
      0.56
    ],
    "dependency_wait": [
      0.0,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 31.41,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      1.43,
      0.0
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0355` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04656 (Operations) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 6.56, expected 2.1, ratio 3.13 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 6.6h vs an expected 2.1h (3.13x). 93% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (93%); Extended executor processing (5%); Approval wait at Incharge stage (2%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04656; 5 events: EV0028434, EV0028435, EV0028439, EV0028440, EV0028469 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.1,
  "actual_duration_h": 6.56,
  "duration_ratio": 3.13,
  "baseline_p90_h": 4.48,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.08
    ],
    "executor_processing": [
      1.01,
      0.78
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.65,
      0.56
    ],
    "dependency_wait": [
      4.85,
      0.52
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Medium",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 2.1,
    "assignee_typical_week_effort_h": 13.22,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.5,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0356` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04657 (Operations) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 4.84, expected 2.25, ratio 2.15 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 4.8h vs an expected 2.3h (2.15x). 52% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (52%); Extended executor processing (48%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04657; 7 events: EV0028437, EV0028438, EV0028444, EV0028446, EV0028447, EV0028451, EV0028463 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 4.84,
  "duration_ratio": 2.15,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      2.21,
      0.79
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.33,
      0.5
    ],
    "dependency_wait": [
      2.23,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 31.41,
    "assignee_typical_week_effort_h": 21.39,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.56,
      0.0
    ],
    "conformance_fitness": 0.6
  }
}
```
</details>

### `DEV-0357` TICKET_DURATION

| field | value |
|---|---|
| Entity | T04662 (Operations) |
| Severity / classification / confidence | high / process / medium |
| Measured | total_duration_h: observed 8.19, expected 2.25, ratio 3.64 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 8.2h vs an expected 2.3h (3.64x). 51% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (51%); Approval wait at Incharge stage (30%); Rework after rejection (Required document missing) (16%); Extended executor processing (3%) |
| SOP reference | SOP-018 band above_p90; C3 undeclared dependency wait (SOP-018 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T04662; 8 events: EV0028466, EV0028467, EV0028472, EV0028473, EV0028484, EV0028486, EV0028487, EV0028489 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.25,
  "actual_duration_h": 8.19,
  "duration_ratio": 3.64,
  "baseline_p90_h": 4.64,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.08
    ],
    "executor_processing": [
      0.95,
      0.79
    ],
    "rework": [
      0.99,
      0.0
    ],
    "approval_wait": [
      2.37,
      0.5
    ],
    "dependency_wait": [
      3.82,
      0.69
    ]
  },
  "context": {
    "task_type": "Daily Operations Report",
    "complexity": "Simple",
    "priority": "Low",
    "dependency_count": 0,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 8.74,
    "assignee_typical_week_effort_h": 19.96,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-018",
    "sop_band": "above_p90",
    "sop_expected_elapsed_h": 1.34,
    "sop_p10_p90_h": [
      1.09,
      1.58
    ],
    "first_decision_wait_actual_vs_sop_h": [
      6.19,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>
