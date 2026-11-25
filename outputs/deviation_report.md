# Deviation Report

_90 deviations from `outputs/deviations.csv`, in pipeline order (process, employee, ticket). Each is a signal for investigation, not a judgment._

| level | deviation_type | count |
|---|---|---|
| employee | ELEVATED_REJECTION_RATE | 1 |
| process | APPROVAL_STAGE_BOTTLENECK | 2 |
| process | REWORK_ABOVE_SOP_EXPECTATION | 5 |
| process | SLA_DETERIORATION | 1 |
| process | SOP_EFFORT_STANDARD | 7 |
| process | SOP_ELAPSED_ABOVE_STANDARD | 2 |
| process | SOP_ELAPSED_BELOW_STANDARD | 8 |
| process | SOP_NONCONFORMANCE | 5 |
| ticket | TICKET_DURATION | 59 |

## Process and SOP-level deviations (30)

### `DEV-0001` SOP_NONCONFORMANCE

| field | value |
|---|---|
| Entity | Daily Operations Report:C1=more (Operations) |
| Severity / classification / confidence | high / process / medium |
| Measured | share of tickets with C1 = more: observed 1.0, expected 0.0, ratio nan |
| Compared with | SOP-018 v1.1.0 |
| What happened | 122 of 122 Daily Operations Report tickets (100%) fail C1 (more) against SOP-018. |
| Most likely reason | Incharge approval logged on every ticket although the SOP requires it only when 'kpi_breach == true or safety_event == true' |
| Ranked candidate causes | Incharge approval logged on every ticket although the SOP requires it only when 'kpi_breach == true or safety_event == true'; Routing condition cannot be verified: its drivers are not in the export |
| SOP reference | SOP-018 approval_matrix: Incharge (kpi_breach == true or safety_event == true) |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Check whether these tickets are routed for approval by default. Either configure the SOP condition on the platform or update the SOP. |
| Source records | 122 tickets: T00006, T00023, T00043, T00065, T00074, T00077, T00078, T00079, T00104, T00112 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Daily Operations Report",
  "check": "c1_approvals",
  "result": "more",
  "tickets": 122,
  "of": 122,
  "share": 1.0,
  "conformance_mode": {
    "retrospective": 122
  },
  "required_vs_observed_approvals": {
    "- vs Incharge": 122
  }
}
```
</details>

### `DEV-0002` SOP_NONCONFORMANCE

| field | value |
|---|---|
| Entity | Daily Operations Report:C3=undeclared (Operations) |
| Severity / classification / confidence | high / process / low |
| Measured | share of tickets with C3 = undeclared: observed 0.959, expected 0.0, ratio nan |
| Compared with | SOP-018 v1.1.0 |
| What happened | 117 of 122 Daily Operations Report tickets (96%) fail C3 (undeclared) against SOP-018. |
| Most likely reason | Ticket put on hold where the SOP requires rejection for missing information |
| Ranked candidate causes | Ticket put on hold where the SOP requires rejection for missing information; Reviewer queue time logged as DependencyWait (median hold 0.37h; first-decision wait 0.52h vs SOP 0.00h) |
| SOP reference | SOP-018 dependency_count: 0; procedure: 'This SOP has no external dependency' |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Ask Incharges and executors why these tickets are put on hold. If it is queue time, stop logging it as DependencyWait; if information is missing, reject with 'Required document missing'. |
| Source records | 117 tickets: T00006, T00023, T00043, T00065, T00074, T00077, T00078, T00079, T00104, T00112 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Daily Operations Report",
  "check": "c3_dependency_wait",
  "result": "undeclared",
  "tickets": 117,
  "of": 122,
  "share": 0.959,
  "conformance_mode": {
    "retrospective": 117
  },
  "required_vs_observed_approvals": {
    "- vs Incharge": 117
  }
}
```
</details>

### `DEV-0003` SOP_NONCONFORMANCE

| field | value |
|---|---|
| Entity | Expense Approval:C3=undeclared (Finance) |
| Severity / classification / confidence | high / process / low |
| Measured | share of tickets with C3 = undeclared: observed 0.93, expected 0.0, ratio nan |
| Compared with | SOP-016 v1.1.0 |
| What happened | 120 of 129 Expense Approval tickets (93%) fail C3 (undeclared) against SOP-016. |
| Most likely reason | Ticket put on hold where the SOP requires rejection for missing information |
| Ranked candidate causes | Ticket put on hold where the SOP requires rejection for missing information; Reviewer queue time logged as DependencyWait (median hold 1.19h; first-decision wait 1.39h vs SOP 0.89h) |
| SOP reference | SOP-016 dependency_count: 0; procedure: 'This SOP has no external dependency' |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Ask Incharges and executors why these tickets are put on hold. If it is queue time, stop logging it as DependencyWait; if information is missing, reject with 'Required document missing'. |
| Source records | 120 tickets: T00017, T00050, T00052, T00056, T00060, T00066, T00083, T00099, T00101, T00107 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Expense Approval",
  "check": "c3_dependency_wait",
  "result": "undeclared",
  "tickets": 120,
  "of": 129,
  "share": 0.93,
  "conformance_mode": {
    "retrospective": 120
  },
  "required_vs_observed_approvals": {
    "Incharge vs Incharge": 120
  }
}
```
</details>

### `DEV-0004` SOP_NONCONFORMANCE

| field | value |
|---|---|
| Entity | Leave Approval:C3=undeclared (HR) |
| Severity / classification / confidence | high / process / low |
| Measured | share of tickets with C3 = undeclared: observed 0.96, expected 0.0, ratio nan |
| Compared with | SOP-020 v1.1.0 |
| What happened | 121 of 126 Leave Approval tickets (96%) fail C3 (undeclared) against SOP-020. |
| Most likely reason | Ticket put on hold where the SOP requires rejection for missing information |
| Ranked candidate causes | Ticket put on hold where the SOP requires rejection for missing information; Reviewer queue time logged as DependencyWait (median hold 1.05h; first-decision wait 1.25h vs SOP 0.80h) |
| SOP reference | SOP-020 dependency_count: 0; procedure: 'This SOP has no external dependency' |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Ask Incharges and executors why these tickets are put on hold. If it is queue time, stop logging it as DependencyWait; if information is missing, reject with 'Required document missing'. |
| Source records | 121 tickets: T00002, T00004, T00021, T00026, T00034, T00035, T00039, T00042, T00064, T00070 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Leave Approval",
  "check": "c3_dependency_wait",
  "result": "undeclared",
  "tickets": 121,
  "of": 126,
  "share": 0.96,
  "conformance_mode": {
    "retrospective": 121
  },
  "required_vs_observed_approvals": {
    "Incharge vs Incharge": 121
  }
}
```
</details>

### `DEV-0005` SOP_NONCONFORMANCE

| field | value |
|---|---|
| Entity | Vendor Onboarding:C1=fewer (Procurement) |
| Severity / classification / confidence | high / platform_logging / high |
| Measured | share of tickets with C1 = fewer: observed 1.0, expected 0.0, ratio nan |
| Compared with | SOP-017 v1.1.0 |
| What happened | 145 of 145 Vendor Onboarding tickets (100%) fail C1 (fewer) against SOP-017. |
| Most likely reason | Platform never logs HOD approvals (0 HOD approval events in all 1200 tickets) |
| Ranked candidate causes | Platform never logs HOD approvals (0 HOD approval events in all 1200 tickets) |
| SOP reference | SOP-017 approval_matrix: HOD (always) |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Confirm with the platform team whether HOD approval happens outside the system or is skipped (see data-quality finding DQ057). |
| Source records | 145 tickets: T00003, T00005, T00007, T00008, T00014, T00019, T00028, T00036, T00044, T00051 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Vendor Onboarding",
  "check": "c1_approvals",
  "result": "fewer",
  "tickets": 145,
  "of": 145,
  "share": 1.0,
  "conformance_mode": {
    "retrospective": 145
  },
  "required_vs_observed_approvals": {
    "Incharge>Lead>HOD vs Incharge>Lead": 145
  }
}
```
</details>

### `DEV-0006` SOP_ELAPSED_BELOW_STANDARD

| field | value |
|---|---|
| Entity | BOQ Review:below_p10 (Procurement) |
| Severity / classification / confidence | high / sop_standard / medium |
| Measured | median elapsed h vs SOP expected: observed 2.77, expected 5.89, ratio 0.47 |
| Compared with | SOP-013 v1.1.0 E_elapsed |
| What happened | 94% of BOQ Review tickets finish below the SOP P10 (10% expected). Median actual 2.77h vs SOP expected 5.89h. |
| Most likely reason | first-decision wait (incl. DependencyWait): actual 1.80h vs SOP 3.65h (-1.85h) |
| Ranked candidate causes | first-decision wait (incl. DependencyWait): actual 1.80h vs SOP 3.65h (-1.85h) (56%); executor hold, WIP-adjusted (upper bound on effort): actual 0.62h vs SOP 1.85h (-1.23h) (37%); intake queue: actual 0.13h vs SOP 0.34h (-0.21h) (6%) |
| SOP reference | SOP-013 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | SOP time standards look high for this task type. Review them with the SOP owner; recalibrate only as a new SOP version fitted on an earlier period (schema §3.1). |
| Source records | 121 tickets: T00009, T00011, T00058, T00059, T00067, T00071, T00072, T00073, T00076, T00080 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "BOQ Review",
  "tickets": 129,
  "share_in_tail": 0.938,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    4.57,
    5.89,
    7.21
  ],
  "observed_p10_p50_p90_h": [
    1.85,
    2.77,
    3.95
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.13,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      1.8,
      3.65
    ],
    "Lead decision wait": [
      0.0,
      0.0
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      0.62,
      1.85
    ]
  },
  "tickets_in_tail": 121,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0007` SOP_ELAPSED_BELOW_STANDARD

| field | value |
|---|---|
| Entity | Daily Operations Report:below_p10 (Operations) |
| Severity / classification / confidence | high / sop_standard / high |
| Measured | median elapsed h vs SOP expected: observed 1.03, expected 1.34, ratio 0.77 |
| Compared with | SOP-018 v1.1.0 E_elapsed |
| What happened | 58% of Daily Operations Report tickets finish below the SOP P10 (10% expected). Median actual 1.03h vs SOP expected 1.34h. |
| Most likely reason | executor hold, WIP-adjusted (upper bound on effort): actual 0.25h vs SOP 0.94h (-0.69h) |
| Ranked candidate causes | executor hold, WIP-adjusted (upper bound on effort): actual 0.25h vs SOP 0.94h (-0.69h) (77%); intake queue: actual 0.13h vs SOP 0.34h (-0.21h) (23%) |
| SOP reference | SOP-018 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | SOP time standards look high for this task type. Review them with the SOP owner; recalibrate only as a new SOP version fitted on an earlier period (schema §3.1). |
| Source records | 71 tickets: T00006, T00023, T00043, T00065, T00074, T00078, T00079, T00104, T00112, T00114 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Daily Operations Report",
  "tickets": 122,
  "share_in_tail": 0.582,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    1.09,
    1.34,
    1.58
  ],
  "observed_p10_p50_p90_h": [
    0.8,
    1.03,
    1.7
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.13,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      0.47,
      0.0
    ],
    "Lead decision wait": [
      0.0,
      0.0
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      0.25,
      0.94
    ]
  },
  "tickets_in_tail": 71,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0008` SOP_ELAPSED_BELOW_STANDARD

| field | value |
|---|---|
| Entity | Employee Document Verification:below_p10 (HR) |
| Severity / classification / confidence | high / sop_standard / high |
| Measured | median elapsed h vs SOP expected: observed 2.8, expected 5.86, ratio 0.48 |
| Compared with | SOP-021 v1.1.0 E_elapsed |
| What happened | 87% of Employee Document Verification tickets finish below the SOP P10 (10% expected). Median actual 2.80h vs SOP expected 5.86h. |
| Most likely reason | first-decision wait (incl. DependencyWait): actual 1.74h vs SOP 4.07h (-2.33h) |
| Ranked candidate causes | first-decision wait (incl. DependencyWait): actual 1.74h vs SOP 4.07h (-2.33h) (71%); executor hold, WIP-adjusted (upper bound on effort): actual 0.64h vs SOP 1.40h (-0.76h) (23%); intake queue: actual 0.15h vs SOP 0.34h (-0.19h) (6%) |
| SOP reference | SOP-021 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | SOP time standards look high for this task type. Review them with the SOP owner; recalibrate only as a new SOP version fitted on an earlier period (schema §3.1). |
| Source records | 118 tickets: T00010, T00018, T00030, T00031, T00032, T00038, T00047, T00055, T00061, T00062 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Employee Document Verification",
  "tickets": 135,
  "share_in_tail": 0.874,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    4.13,
    5.86,
    7.59
  ],
  "observed_p10_p50_p90_h": [
    1.64,
    2.8,
    4.27
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.15,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      1.74,
      4.07
    ],
    "Lead decision wait": [
      0.0,
      0.0
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      0.64,
      1.4
    ]
  },
  "tickets_in_tail": 118,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0009` SOP_ELAPSED_ABOVE_STANDARD

| field | value |
|---|---|
| Entity | Expense Approval:above_p90 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | median elapsed h vs SOP expected: observed 1.95, expected 1.82, ratio 1.07 |
| Compared with | SOP-016 v1.1.0 E_elapsed |
| What happened | 36% of Expense Approval tickets finish above the SOP P90 (10% expected). Median actual 1.95h vs SOP expected 1.82h. |
| Most likely reason | first-decision wait (incl. DependencyWait): actual 1.97h vs SOP 0.89h (+1.08h) |
| Ranked candidate causes | first-decision wait (incl. DependencyWait): actual 1.97h vs SOP 0.89h (+1.08h) (93%); executor hold, WIP-adjusted (upper bound on effort): actual 0.62h vs SOP 0.53h (+0.08h) (7%); 43 of 46 tickets carry a DependencyWait the SOP does not allow |
| SOP reference | SOP-016 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Investigate the dominant component. Waits point to the approval queue or holds; executor hold points to work content. |
| Source records | 46 tickets: T00050, T00052, T00066, T00083, T00108, T00164, T00201, T00230, T00262, T00354 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Expense Approval",
  "tickets": 129,
  "share_in_tail": 0.357,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    1.38,
    1.82,
    2.26
  ],
  "observed_p10_p50_p90_h": [
    1.08,
    1.95,
    3.14
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.17,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      1.97,
      0.89
    ],
    "Lead decision wait": [
      0.0,
      0.0
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      0.62,
      0.53
    ]
  },
  "tickets_in_tail": 46,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0010` SOP_ELAPSED_BELOW_STANDARD

| field | value |
|---|---|
| Entity | Expense Approval:below_p10 (Finance) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | median elapsed h vs SOP expected: observed 1.95, expected 1.82, ratio 1.07 |
| Compared with | SOP-016 v1.1.0 E_elapsed |
| What happened | 21% of Expense Approval tickets finish below the SOP P10 (10% expected). Median actual 1.95h vs SOP expected 1.82h. |
| Most likely reason | executor hold, WIP-adjusted (upper bound on effort): actual 0.25h vs SOP 0.53h (-0.28h) |
| Ranked candidate causes | executor hold, WIP-adjusted (upper bound on effort): actual 0.25h vs SOP 0.53h (-0.28h) (39%); first-decision wait (incl. DependencyWait): actual 0.65h vs SOP 0.89h (-0.24h) (33%); intake queue: actual 0.13h vs SOP 0.34h (-0.21h) (29%) |
| SOP reference | SOP-016 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | SOP time standards look high for this task type. Review them with the SOP owner; recalibrate only as a new SOP version fitted on an earlier period (schema §3.1). |
| Source records | 27 tickets: T00017, T00099, T00120, T00318, T00334, T00347, T00361, T00555, T00663, T00750 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Expense Approval",
  "tickets": 129,
  "share_in_tail": 0.209,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    1.38,
    1.82,
    2.26
  ],
  "observed_p10_p50_p90_h": [
    1.08,
    1.95,
    3.14
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.13,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      0.65,
      0.89
    ],
    "Lead decision wait": [
      0.0,
      0.0
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      0.25,
      0.53
    ]
  },
  "tickets_in_tail": 27,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0011` SOP_ELAPSED_BELOW_STANDARD

| field | value |
|---|---|
| Entity | Incident Review:below_p10 (Operations) |
| Severity / classification / confidence | high / sop_standard / high |
| Measured | median elapsed h vs SOP expected: observed 7.07, expected 10.41, ratio 0.68 |
| Compared with | SOP-019 v1.1.0 E_elapsed |
| What happened | 80% of Incident Review tickets finish below the SOP P10 (10% expected). Median actual 7.07h vs SOP expected 10.41h. |
| Most likely reason | executor hold, WIP-adjusted (upper bound on effort): actual 1.37h vs SOP 3.78h (-2.41h) |
| Ranked candidate causes | executor hold, WIP-adjusted (upper bound on effort): actual 1.37h vs SOP 3.78h (-2.41h) (60%); first-decision wait (incl. DependencyWait): actual 3.38h vs SOP 4.50h (-1.12h) (28%); Lead decision wait: actual 1.43h vs SOP 1.74h (-0.31h) (8%); intake queue: actual 0.15h vs SOP 0.34h (-0.19h) (5%) |
| SOP reference | SOP-019 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | SOP time standards look high for this task type. Review them with the SOP owner; recalibrate only as a new SOP version fitted on an earlier period (schema §3.1). |
| Source records | 108 tickets: T00001, T00013, T00020, T00033, T00037, T00040, T00046, T00049, T00053, T00057 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Incident Review",
  "tickets": 135,
  "share_in_tail": 0.8,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    8.84,
    10.41,
    11.98
  ],
  "observed_p10_p50_p90_h": [
    4.78,
    7.07,
    9.42
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.15,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      3.38,
      4.5
    ],
    "Lead decision wait": [
      1.43,
      1.74
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      1.37,
      3.78
    ]
  },
  "tickets_in_tail": 108,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0012` SOP_ELAPSED_BELOW_STANDARD

| field | value |
|---|---|
| Entity | Invoice Verification:below_p10 (Finance) |
| Severity / classification / confidence | high / sop_standard / high |
| Measured | median elapsed h vs SOP expected: observed 3.02, expected 5.12, ratio 0.59 |
| Compared with | SOP-015 v1.1.0 E_elapsed |
| What happened | 79% of Invoice Verification tickets finish below the SOP P10 (10% expected). Median actual 3.02h vs SOP expected 5.12h. |
| Most likely reason | first-decision wait (incl. DependencyWait): actual 1.90h vs SOP 3.40h (-1.50h) |
| Ranked candidate causes | first-decision wait (incl. DependencyWait): actual 1.90h vs SOP 3.40h (-1.50h) (63%); executor hold, WIP-adjusted (upper bound on effort): actual 0.63h vs SOP 1.32h (-0.69h) (29%); intake queue: actual 0.15h vs SOP 0.34h (-0.19h) (8%) |
| SOP reference | SOP-015 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | SOP time standards look high for this task type. Review them with the SOP owner; recalibrate only as a new SOP version fitted on an earlier period (schema §3.1). |
| Source records | 118 tickets: T00012, T00015, T00045, T00048, T00082, T00084, T00085, T00098, T00102, T00105 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Invoice Verification",
  "tickets": 150,
  "share_in_tail": 0.787,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    3.78,
    5.12,
    6.46
  ],
  "observed_p10_p50_p90_h": [
    1.97,
    3.02,
    5.15
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.15,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      1.9,
      3.4
    ],
    "Lead decision wait": [
      0.0,
      0.0
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      0.63,
      1.32
    ]
  },
  "tickets_in_tail": 118,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0013` SOP_ELAPSED_ABOVE_STANDARD

| field | value |
|---|---|
| Entity | Leave Approval:above_p90 (HR) |
| Severity / classification / confidence | high / process / high |
| Measured | median elapsed h vs SOP expected: observed 1.82, expected 1.38, ratio 1.33 |
| Compared with | SOP-020 v1.1.0 E_elapsed |
| What happened | 52% of Leave Approval tickets finish above the SOP P90 (10% expected). Median actual 1.82h vs SOP expected 1.38h. |
| Most likely reason | first-decision wait (incl. DependencyWait): actual 1.65h vs SOP 0.80h (+0.85h) |
| Ranked candidate causes | first-decision wait (incl. DependencyWait): actual 1.65h vs SOP 0.80h (+0.85h) (79%); executor hold, WIP-adjusted (upper bound on effort): actual 0.43h vs SOP 0.20h (+0.23h) (21%); 63 of 66 tickets carry a DependencyWait the SOP does not allow |
| SOP reference | SOP-020 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Investigate the dominant component. Waits point to the approval queue or holds; executor hold points to work content. |
| Source records | 66 tickets: T00002, T00035, T00039, T00088, T00109, T00151, T00170, T00226, T00228, T00234 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Leave Approval",
  "tickets": 126,
  "share_in_tail": 0.524,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    0.95,
    1.38,
    1.81
  ],
  "observed_p10_p50_p90_h": [
    1.17,
    1.82,
    2.72
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.13,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      1.65,
      0.8
    ],
    "Lead decision wait": [
      0.0,
      0.0
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      0.43,
      0.2
    ]
  },
  "tickets_in_tail": 66,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0014` SOP_ELAPSED_BELOW_STANDARD

| field | value |
|---|---|
| Entity | Purchase Request:below_p10 (Procurement) |
| Severity / classification / confidence | medium / sop_standard / high |
| Measured | median elapsed h vs SOP expected: observed 5.95, expected 6.22, ratio 0.96 |
| Compared with | SOP-014 v1.1.0 E_elapsed |
| What happened | 29% of Purchase Request tickets finish below the SOP P10 (10% expected). Median actual 5.95h vs SOP expected 6.22h. |
| Most likely reason | first-decision wait (incl. DependencyWait): actual 1.67h vs SOP 3.07h (-1.40h) |
| Ranked candidate causes | first-decision wait (incl. DependencyWait): actual 1.67h vs SOP 3.07h (-1.40h) (64%); executor hold, WIP-adjusted (upper bound on effort): actual 0.63h vs SOP 1.20h (-0.57h) (26%); intake queue: actual 0.13h vs SOP 0.34h (-0.21h) (10%) |
| SOP reference | SOP-014 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | SOP time standards look high for this task type. Review them with the SOP owner; recalibrate only as a new SOP version fitted on an earlier period (schema §3.1). |
| Source records | 37 tickets: T00024, T00029, T00069, T00132, T00177, T00212, T00235, T00251, T00272, T00276 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Purchase Request",
  "tickets": 129,
  "share_in_tail": 0.287,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    4.95,
    6.22,
    7.5
  ],
  "observed_p10_p50_p90_h": [
    4.04,
    5.95,
    7.83
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.13,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      1.67,
      3.07
    ],
    "Lead decision wait": [
      1.68,
      1.56
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      0.63,
      1.2
    ]
  },
  "tickets_in_tail": 37,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0015` SOP_ELAPSED_BELOW_STANDARD

| field | value |
|---|---|
| Entity | Vendor Onboarding:below_p10 (Procurement) |
| Severity / classification / confidence | high / sop_standard / high |
| Measured | median elapsed h vs SOP expected: observed 8.33, expected 11.97, ratio 0.7 |
| Compared with | SOP-017 v1.1.0 E_elapsed |
| What happened | 74% of Vendor Onboarding tickets finish below the SOP P10 (10% expected). Median actual 8.33h vs SOP expected 11.97h. |
| Most likely reason | executor hold, WIP-adjusted (upper bound on effort): actual 1.37h vs SOP 2.83h (-1.46h) |
| Ranked candidate causes | executor hold, WIP-adjusted (upper bound on effort): actual 1.37h vs SOP 2.83h (-1.46h) (61%); first-decision wait (incl. DependencyWait): actual 4.20h vs SOP 4.83h (-0.63h) (26%); intake queue: actual 0.15h vs SOP 0.34h (-0.19h) (8%); Lead decision wait: actual 1.55h vs SOP 1.65h (-0.10h) (4%) |
| SOP reference | SOP-017 v1.1.0 §7.1 E_elapsed band |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | SOP time standards look high for this task type. Review them with the SOP owner; recalibrate only as a new SOP version fitted on an earlier period (schema §3.1). |
| Source records | 107 tickets: T00003, T00005, T00007, T00008, T00019, T00028, T00036, T00051, T00063, T00119 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "task_type": "Vendor Onboarding",
  "tickets": 145,
  "share_in_tail": 0.738,
  "expected_tail_share": 0.1,
  "sop_band_h": [
    9.86,
    11.97,
    14.08
  ],
  "observed_p10_p50_p90_h": [
    5.35,
    8.33,
    10.87
  ],
  "component_medians_actual_vs_sop_h": {
    "intake queue": [
      0.15,
      0.34
    ],
    "first-decision wait (incl. DependencyWait)": [
      4.2,
      4.83
    ],
    "Lead decision wait": [
      1.55,
      1.65
    ],
    "executor hold, WIP-adjusted (upper bound on effort)": [
      1.37,
      2.83
    ]
  },
  "tickets_in_tail": 107,
  "note": "executor hold is compared in aggregate only (schema \u00a77.3)"
}
```
</details>

### `DEV-0016` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | BOQ Review:effort_coverage (Procurement) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 2.9, expected 1.0, ratio 2.9 |
| Compared with | SOP-013 v1.1.0 E_effort_exec |
| What happened | BOQ Review: SOP executor effort 1.85h vs median WIP-adjusted hold 0.64h (coverage 2.90, flag standard_exceeds_hold) in all 4 eligible months. |
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
    "2026-06": {
      "n": 33,
      "coverage": 3.16,
      "median_wip_adj_hold_h": 0.58
    },
    "2026-07": {
      "n": 42,
      "coverage": 2.61,
      "median_wip_adj_hold_h": 0.71
    },
    "2026-08": {
      "n": 31,
      "coverage": 2.64,
      "median_wip_adj_hold_h": 0.7
    },
    "2026-09": {
      "n": 23,
      "coverage": 3.36,
      "median_wip_adj_hold_h": 0.55
    }
  },
  "sop_effort_exec_h": 1.85,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0017` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | Daily Operations Report:effort_coverage (Operations) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 2.88, expected 1.0, ratio 2.88 |
| Compared with | SOP-018 v1.1.0 E_effort_exec |
| What happened | Daily Operations Report: SOP executor effort 0.94h vs median WIP-adjusted hold 0.33h (coverage 2.88, flag standard_exceeds_hold) in all 4 eligible months. |
| Most likely reason | SOP executor effort standard too high (illustrative_expert_estimate) |
| Ranked candidate causes | SOP executor effort standard too high (illustrative_expert_estimate); Work done outside the ticket window (before Created or after Submitted) |
| SOP reference | SOP-018 v1.1.0 work-step effort_min (schema §8) |
| Preventable by | - |
| Reason source | sop |
| Recommended investigation | Review the standard with the SOP owner or run a short time study. Do not edit standard times to match the data (schema §3.1). |
| Source records | - |

<details><summary>Evidence (JSON)</summary>

```json
{
  "flag": "standard_exceeds_hold",
  "months": {
    "2026-06": {
      "n": 28,
      "coverage": 2.52,
      "median_wip_adj_hold_h": 0.38
    },
    "2026-07": {
      "n": 30,
      "coverage": 3.24,
      "median_wip_adj_hold_h": 0.29
    },
    "2026-08": {
      "n": 35,
      "coverage": 3.33,
      "median_wip_adj_hold_h": 0.28
    },
    "2026-09": {
      "n": 29,
      "coverage": 2.27,
      "median_wip_adj_hold_h": 0.42
    }
  },
  "sop_effort_exec_h": 0.94,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0018` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | Employee Document Verification:effort_coverage (HR) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 1.95, expected 1.0, ratio 1.95 |
| Compared with | SOP-021 v1.1.0 E_effort_exec |
| What happened | Employee Document Verification: SOP executor effort 1.40h vs median WIP-adjusted hold 0.72h (coverage 1.95, flag standard_exceeds_hold) in all 4 eligible months. |
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
    "2026-06": {
      "n": 38,
      "coverage": 1.89,
      "median_wip_adj_hold_h": 0.74
    },
    "2026-07": {
      "n": 34,
      "coverage": 2.02,
      "median_wip_adj_hold_h": 0.69
    },
    "2026-08": {
      "n": 30,
      "coverage": 1.68,
      "median_wip_adj_hold_h": 0.83
    },
    "2026-09": {
      "n": 33,
      "coverage": 2.21,
      "median_wip_adj_hold_h": 0.63
    }
  },
  "sop_effort_exec_h": 1.4,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0019` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | Incident Review:effort_coverage (Operations) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 2.63, expected 1.0, ratio 2.63 |
| Compared with | SOP-019 v1.1.0 E_effort_exec |
| What happened | Incident Review: SOP executor effort 3.78h vs median WIP-adjusted hold 1.44h (coverage 2.63, flag standard_exceeds_hold) in all 4 eligible months. |
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
    "2026-06": {
      "n": 26,
      "coverage": 2.91,
      "median_wip_adj_hold_h": 1.3
    },
    "2026-07": {
      "n": 40,
      "coverage": 2.77,
      "median_wip_adj_hold_h": 1.37
    },
    "2026-08": {
      "n": 45,
      "coverage": 2.31,
      "median_wip_adj_hold_h": 1.63
    },
    "2026-09": {
      "n": 24,
      "coverage": 2.49,
      "median_wip_adj_hold_h": 1.52
    }
  },
  "sop_effort_exec_h": 3.78,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0020` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | Invoice Verification:effort_coverage (Finance) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 2.04, expected 1.0, ratio 2.04 |
| Compared with | SOP-015 v1.1.0 E_effort_exec |
| What happened | Invoice Verification: SOP executor effort 1.32h vs median WIP-adjusted hold 0.65h (coverage 2.04, flag standard_exceeds_hold) in all 4 eligible months. |
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
    "2026-06": {
      "n": 35,
      "coverage": 1.99,
      "median_wip_adj_hold_h": 0.67
    },
    "2026-07": {
      "n": 41,
      "coverage": 2.09,
      "median_wip_adj_hold_h": 0.63
    },
    "2026-08": {
      "n": 40,
      "coverage": 2.15,
      "median_wip_adj_hold_h": 0.62
    },
    "2026-09": {
      "n": 34,
      "coverage": 1.39,
      "median_wip_adj_hold_h": 0.95
    }
  },
  "sop_effort_exec_h": 1.32,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0021` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | Purchase Request:effort_coverage (Procurement) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 1.76, expected 1.0, ratio 1.76 |
| Compared with | SOP-014 v1.1.0 E_effort_exec |
| What happened | Purchase Request: SOP executor effort 1.20h vs median WIP-adjusted hold 0.68h (coverage 1.76, flag standard_exceeds_hold) in all 4 eligible months. |
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
    "2026-06": {
      "n": 47,
      "coverage": 1.76,
      "median_wip_adj_hold_h": 0.68
    },
    "2026-07": {
      "n": 33,
      "coverage": 1.81,
      "median_wip_adj_hold_h": 0.67
    },
    "2026-08": {
      "n": 29,
      "coverage": 1.76,
      "median_wip_adj_hold_h": 0.68
    },
    "2026-09": {
      "n": 20,
      "coverage": 1.72,
      "median_wip_adj_hold_h": 0.7
    }
  },
  "sop_effort_exec_h": 1.2,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0022` SOP_EFFORT_STANDARD

| field | value |
|---|---|
| Entity | Vendor Onboarding:effort_coverage (Procurement) |
| Severity / classification / confidence | medium / sop_standard / low |
| Measured | effort coverage (SOP executor effort / median WIP-adjusted hold): observed 2.03, expected 1.0, ratio 2.03 |
| Compared with | SOP-017 v1.1.0 E_effort_exec |
| What happened | Vendor Onboarding: SOP executor effort 2.83h vs median WIP-adjusted hold 1.39h (coverage 2.03, flag standard_exceeds_hold) in all 4 eligible months. |
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
    "2026-06": {
      "n": 39,
      "coverage": 2.02,
      "median_wip_adj_hold_h": 1.4
    },
    "2026-07": {
      "n": 38,
      "coverage": 2.08,
      "median_wip_adj_hold_h": 1.36
    },
    "2026-08": {
      "n": 33,
      "coverage": 2.05,
      "median_wip_adj_hold_h": 1.38
    },
    "2026-09": {
      "n": 35,
      "coverage": 1.93,
      "median_wip_adj_hold_h": 1.47
    }
  },
  "sop_effort_exec_h": 2.83,
  "standard_time_source": "illustrative_expert_estimate",
  "note": "aggregated only (task type x month); never computed per employee"
}
```
</details>

### `DEV-0023` REWORK_ABOVE_SOP_EXPECTATION

| field | value |
|---|---|
| Entity | Invoice Verification:rework (Finance) |
| Severity / classification / confidence | medium / rework / low |
| Measured | share of tickets rejected at least once: observed 0.127, expected 0.1, ratio 1.27 |
| Compared with | SOP-015 v1.1.0 FPY |
| What happened | Invoice Verification: 13% of tickets rejected at least once vs 10% implied by the SOP first-pass yield (unconfirmed). |
| Most likely reason | Incorrect category (7): preventable by S4 GL and tax code check |
| Ranked candidate causes | Incorrect category (7) (37%); Amount mismatch (5) (26%); Wrong quantity (4) (21%); Required document missing (3) (16%) |
| SOP reference | SOP-015 rework_triggers; expected_first_pass_yield 0.9 |
| Preventable by | S4 GL and tax code check|S3 three-way match |
| Reason source | sop |
| Recommended investigation | Strengthen the upstream control 'S4 GL and tax code check' and re-measure the first-pass yield. |
| Source records | 19 tickets: T00210, T00271, T00379, T00403, T00446, T00519, T00525, T00532, T00636, T00716 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "tickets": 150,
  "rejected": 19,
  "reasons": {
    "Incorrect category": 7,
    "Amount mismatch": 5,
    "Wrong quantity": 4,
    "Required document missing": 3
  },
  "quality_targets_source": "unconfirmed"
}
```
</details>

### `DEV-0024` REWORK_ABOVE_SOP_EXPECTATION

| field | value |
|---|---|
| Entity | Expense Approval:rework (Finance) |
| Severity / classification / confidence | medium / rework / low |
| Measured | share of tickets rejected at least once: observed 0.078, expected 0.05, ratio 1.55 |
| Compared with | SOP-016 v1.1.0 FPY |
| What happened | Expense Approval: 8% of tickets rejected at least once vs 5% implied by the SOP first-pass yield (unconfirmed). |
| Most likely reason | Required document missing (4): preventable by S3 receipt verification |
| Ranked candidate causes | Required document missing (4) (40%); Incorrect category (3) (30%); Wrong quantity (2) (20%); Amount mismatch (1) (10%) |
| SOP reference | SOP-016 rework_triggers; expected_first_pass_yield 0.95 |
| Preventable by | S3 receipt verification|S2 expense category mapping |
| Reason source | sop |
| Recommended investigation | Strengthen the upstream control 'S3 receipt verification' and re-measure the first-pass yield. |
| Source records | 10 tickets: T00201, T00262, T00410, T00442, T00602, T00921, T00991, T01026, T01095, T01115 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "tickets": 129,
  "rejected": 10,
  "reasons": {
    "Required document missing": 4,
    "Incorrect category": 3,
    "Wrong quantity": 2,
    "Amount mismatch": 1
  },
  "quality_targets_source": "unconfirmed"
}
```
</details>

### `DEV-0025` REWORK_ABOVE_SOP_EXPECTATION

| field | value |
|---|---|
| Entity | Daily Operations Report:rework (Operations) |
| Severity / classification / confidence | medium / rework / low |
| Measured | share of tickets rejected at least once: observed 0.066, expected 0.05, ratio 1.31 |
| Compared with | SOP-018 v1.1.0 FPY |
| What happened | Daily Operations Report: 7% of tickets rejected at least once vs 5% implied by the SOP first-pass yield (unconfirmed). |
| Most likely reason | Amount mismatch (3): preventable by S3 KPI formula check |
| Ranked candidate causes | Amount mismatch (3) (38%); Incorrect category (2) (25%); Required document missing (2) (25%); Wrong quantity (1) (12%) |
| SOP reference | SOP-018 rework_triggers; expected_first_pass_yield 0.95 |
| Preventable by | S3 KPI formula check|S4 downtime reason coding |
| Reason source | sop |
| Recommended investigation | Strengthen the upstream control 'S3 KPI formula check' and re-measure the first-pass yield. |
| Source records | 8 tickets: T00209, T00405, T00612, T00762, T00764, T00786, T00957, T01166 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "tickets": 122,
  "rejected": 8,
  "reasons": {
    "Amount mismatch": 3,
    "Incorrect category": 2,
    "Required document missing": 2,
    "Wrong quantity": 1
  },
  "quality_targets_source": "unconfirmed"
}
```
</details>

### `DEV-0026` REWORK_ABOVE_SOP_EXPECTATION

| field | value |
|---|---|
| Entity | Leave Approval:rework (HR) |
| Severity / classification / confidence | medium / rework / low |
| Measured | share of tickets rejected at least once: observed 0.071, expected 0.05, ratio 1.43 |
| Compared with | SOP-020 v1.1.0 FPY |
| What happened | Leave Approval: 7% of tickets rejected at least once vs 5% implied by the SOP first-pass yield (unconfirmed). |
| Most likely reason | Required document missing (4): preventable by S2 certificate check |
| Ranked candidate causes | Required document missing (4) (44%); Amount mismatch (3) (33%); Incorrect category (2) (22%) |
| SOP reference | SOP-020 rework_triggers; expected_first_pass_yield 0.95 |
| Preventable by | S2 certificate check|S2 balance check |
| Reason source | sop |
| Recommended investigation | Strengthen the upstream control 'S2 certificate check' and re-measure the first-pass yield. |
| Source records | 9 tickets: T00228, T00386, T00518, T00577, T00637, T00767, T00845, T00854, T00982 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "tickets": 126,
  "rejected": 9,
  "reasons": {
    "Required document missing": 4,
    "Amount mismatch": 3,
    "Incorrect category": 2
  },
  "quality_targets_source": "unconfirmed"
}
```
</details>

### `DEV-0027` REWORK_ABOVE_SOP_EXPECTATION

| field | value |
|---|---|
| Entity | Employee Document Verification:rework (HR) |
| Severity / classification / confidence | medium / rework / low |
| Measured | share of tickets rejected at least once: observed 0.141, expected 0.1, ratio 1.41 |
| Compared with | SOP-021 v1.1.0 FPY |
| What happened | Employee Document Verification: 14% of tickets rejected at least once vs 10% implied by the SOP first-pass yield (unconfirmed). |
| Most likely reason | Incorrect category (8): preventable by S2 document type classification |
| Ranked candidate causes | Incorrect category (8) (42%); Wrong quantity (5) (26%); Amount mismatch (4) (21%); Required document missing (2) (11%) |
| SOP reference | SOP-021 rework_triggers; expected_first_pass_yield 0.9 |
| Preventable by | S2 document type classification|S4 experience duration calculation |
| Reason source | sop |
| Recommended investigation | Strengthen the upstream control 'S2 document type classification' and re-measure the first-pass yield. |
| Source records | 19 tickets: T00081, T00225, T00290, T00335, T00366, T00375, T00435, T00493, T00687, T00730 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "tickets": 135,
  "rejected": 19,
  "reasons": {
    "Incorrect category": 8,
    "Wrong quantity": 5,
    "Amount mismatch": 4,
    "Required document missing": 2
  },
  "quality_targets_source": "unconfirmed"
}
```
</details>

### `DEV-0028` APPROVAL_STAGE_BOTTLENECK

| field | value |
|---|---|
| Entity | Finance:Incharge:deps=0 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | median Incharge decision wait (h): observed 1.37, expected 0.93, ratio 1.46 |
| Compared with | BL-v1:stage:Incharge:deps=0 |
| What happened | In Finance, tickets with 0 declared dependencies wait a median 1.37h for the Incharge decision vs 0.93h across the organization (1.46x), while median executor processing is 0.35h. Waiting for this decision is 66% of ticket time. |
| Most likely reason | Incharge approval queue (Finance) |
| Ranked candidate causes | Incharge approval capacity/queue in Finance; Unrecorded dependency waits (DependencyWait without declared dependency); Relative to the SOP standard (0.89h) the observed wait (1.37h) is higher; the bottleneck is against both the SOP and other departments. |
| SOP reference | SOP-016 first approval queue_wait_h + review effort + dependencies |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review Finance Incharge approval queue and turnaround; this is a process-level signal, not an executor issue. |
| Source records | 20 tickets: T01041, T00566, T00368, T00201, T00410, T00991, T00442, T00262, T01095, T00735 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "stage": "Incharge",
  "dependency_count": 0,
  "tickets": 129,
  "task_types": {
    "Expense Approval": 129
  },
  "dept_median_wait_h": 1.37,
  "org_median_wait_h_same_stratum": 0.93,
  "org_p90_wait_h_same_stratum": 1.97,
  "wait_share_of_ticket_time": 0.663,
  "median_executor_processing_h": 0.35,
  "monthly_median_wait_h": {
    "2026-06": 1.5,
    "2026-07": 1.33,
    "2026-08": 1.3,
    "2026-09": 1.07
  },
  "dept_sla_compliance": 0.993,
  "undeclared_dependency_wait_tickets": 120,
  "note": "Incharge decision wait = submission -> first-level decision, including the DependencyWait interval (cannot be separated in the audit log).",
  "sop_first_decision_expected_h": 0.89,
  "observed_vs_sop": 1.54
}
```
</details>

### `DEV-0029` APPROVAL_STAGE_BOTTLENECK

| field | value |
|---|---|
| Entity | HR:Incharge:deps=0 (HR) |
| Severity / classification / confidence | medium / process / medium |
| Measured | median Incharge decision wait (h): observed 1.27, expected 0.93, ratio 1.36 |
| Compared with | BL-v1:stage:Incharge:deps=0 |
| What happened | In HR, tickets with 0 declared dependencies wait a median 1.27h for the Incharge decision vs 0.93h across the organization (1.36x), while median executor processing is 0.30h. Waiting for this decision is 66% of ticket time. |
| Most likely reason | Incharge approval queue (HR) |
| Ranked candidate causes | Incharge approval capacity/queue in HR; Unrecorded dependency waits (DependencyWait without declared dependency); Relative to the SOP standard (0.80h) the observed wait (1.27h) is higher; the bottleneck is against both the SOP and other departments. |
| SOP reference | SOP-020 first approval queue_wait_h + review effort + dependencies |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review HR Incharge approval queue and turnaround; this is a process-level signal, not an executor issue. |
| Source records | 20 tickets: T00518, T00228, T00854, T00767, T00637, T00386, T00456, T01056, T00265, T00962 ... |

<details><summary>Evidence (JSON)</summary>

```json
{
  "stage": "Incharge",
  "dependency_count": 0,
  "tickets": 126,
  "task_types": {
    "Leave Approval": 126
  },
  "dept_median_wait_h": 1.27,
  "org_median_wait_h_same_stratum": 0.93,
  "org_p90_wait_h_same_stratum": 1.97,
  "wait_share_of_ticket_time": 0.662,
  "median_executor_processing_h": 0.3,
  "monthly_median_wait_h": {
    "2026-06": 1.48,
    "2026-07": 1.25,
    "2026-08": 1.12,
    "2026-09": 1.35
  },
  "dept_sla_compliance": 1.0,
  "undeclared_dependency_wait_tickets": 121,
  "note": "Incharge decision wait = submission -> first-level decision, including the DependencyWait interval (cannot be separated in the audit log).",
  "sop_first_decision_expected_h": 0.8,
  "observed_vs_sop": 1.58
}
```
</details>

### `DEV-0030` SLA_DETERIORATION

| field | value |
|---|---|
| Entity | Operations:SLA (Operations) |
| Severity / classification / confidence | medium / mixed / low |
| Measured | monthly SLA compliance: observed 0.887, expected 0.963, ratio 0.921 |
| Compared with | Operations SLA compliance 2026-06 |
| What happened | Operations SLA compliance fell for 3 consecutive months: 96.3% -> 94.3% -> 93.8% -> 88.7%. |
| Most likely reason | Most late tickets in 2026-09: E1013 (2 of 6) |
| Ranked candidate causes | late tickets assigned to E1013; late tickets assigned to E1015; late tickets assigned to E1018 |
| SOP reference | SOP sla_hours (High 6 / Medium 12 / Low 24) |
| Preventable by | - |
| Reason source | baseline |
| Recommended investigation | Cross-check with persistent employee-level and bottleneck signals in this department. |
| Source records | 6 tickets: T00092, T00191, T00224, T00397, T00693, T00722 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "monthly_sla_compliance": {
    "2026-06": 0.963,
    "2026-07": 0.943,
    "2026-08": 0.938,
    "2026-09": 0.887
  },
  "late_tickets_last_period": 6,
  "late_by_priority_all_periods": {
    "High": 17
  }
}
```
</details>


## Employee-level signals (1)

### `DEV-0031` ELEVATED_REJECTION_RATE

| field | value |
|---|---|
| Entity | E1002 (Finance) |
| Severity / classification / confidence | medium / individual_signal / medium |
| Measured | rejection_rate: observed 0.184, expected 0.091, ratio 2.02 |
| Compared with | peer rejection rate (Finance) |
| What happened | E1002: 18% of tickets were rejected at least once vs 9% for department peers. |
| Most likely reason | Top reason: Amount mismatch |
| Ranked candidate causes | Amount mismatch; Incorrect category; Required document missing |
| SOP reference | rework_triggers of SOP-015, SOP-016 |
| Preventable by | S4 GL and tax code check|S3 three-way match |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons; consider checklist or guidance for the top reason. Most relevant SOP controls: S4 GL and tax code check (3), S3 three-way match (2). |
| Source records | 7 tickets: T00403, T00410, T00602, T00716, T01058, T01151, T01185 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "tickets": 38,
  "rejected_tickets": 7,
  "peer_rate": 0.091,
  "task_mix_of_rejected": {
    "Invoice Verification": 5,
    "Expense Approval": 2
  }
}
```
</details>


## Ticket-level deviations (59)

### `DEV-0032` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00089 (Procurement) |
| Severity / classification / confidence | medium / rework / high |
| Measured | total_duration_h: observed 5.0, expected 2.73, ratio 1.83 |
| Compared with | BL-v1:L2:BOQ Review:Medium:Low |
| What happened | BOQ Review (Medium, Low) took 5.0h vs an expected 2.7h (1.83x). 71% of the extra time is attributed to: rework after rejection (incorrect category). |
| Most likely reason | Rework after rejection (Incorrect category); preventable by S2 item-code mapping |
| Ranked candidate causes | Rework after rejection (Incorrect category) (71%); Approval wait at Incharge stage (29%) |
| SOP reference | SOP-013 band within; rework_trigger RW-CAT |
| Preventable by | S2 item-code mapping |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00089; 8 events: EV0000526, EV0000527, EV0000528, EV0000529, EV0000530, EV0000531, EV0000532, EV0000533 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.73,
  "actual_duration_h": 5.0,
  "duration_ratio": 1.83,
  "baseline_p90_h": 4.07,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.13
    ],
    "executor_processing": [
      0.67,
      0.67
    ],
    "rework": [
      1.73,
      0.0
    ],
    "approval_wait": [
      1.63,
      0.92
    ],
    "dependency_wait": [
      0.85,
      1.03
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
    "assignee_week_expected_effort_h": 11.36,
    "assignee_typical_week_effort_h": 22.28,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-013",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.89,
    "sop_p10_p90_h": [
      4.57,
      7.21
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.48,
      3.65
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0033` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00127 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 7.2, expected 2.99, ratio 2.41 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:High |
| What happened | Invoice Verification (Medium, High) took 7.2h vs an expected 3.0h (2.41x). 100% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (100%) |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00127; 5 events: EV0000752, EV0000753, EV0000754, EV0000755, EV0000756 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.99,
  "actual_duration_h": 7.2,
  "duration_ratio": 2.41,
  "baseline_p90_h": 4.84,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.14
    ],
    "executor_processing": [
      0.57,
      0.68
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.88,
      0.9
    ],
    "dependency_wait": [
      5.62,
      1.22
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "High",
    "dependency_count": 1,
    "rejection_count": 0,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 9.03,
    "assignee_typical_week_effort_h": 8.02,
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
      6.5,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0034` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00201 (Finance) |
| Severity / classification / confidence | high / rework / medium |
| Measured | total_duration_h: observed 5.13, expected 1.95, ratio 2.63 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 5.1h vs an expected 1.9h (2.63x). 50% of the extra time is attributed to: rework after rejection (wrong quantity). |
| Most likely reason | Rework after rejection (Wrong quantity); preventable by S3 receipt to line matching |
| Ranked candidate causes | Rework after rejection (Wrong quantity) (50%); Approval wait at Incharge stage (27%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (23%) |
| SOP reference | SOP-016 band above_p90; rework_trigger RW-QTY |
| Preventable by | S3 receipt to line matching |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00201; 8 events: EV0001204, EV0001205, EV0001206, EV0001207, EV0001208, EV0001209, EV0001210, EV0001211 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.95,
  "actual_duration_h": 5.13,
  "duration_ratio": 2.63,
  "baseline_p90_h": 2.99,
  "components_actual_vs_expected_h": {
    "queue": [
      0.1,
      0.16
    ],
    "executor_processing": [
      0.32,
      0.32
    ],
    "rework": [
      1.68,
      0.0
    ],
    "approval_wait": [
      1.1,
      0.17
    ],
    "dependency_wait": [
      1.93,
      1.17
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
    "assignee_week_expected_effort_h": 6.93,
    "assignee_typical_week_effort_h": 8.02,
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
      3.03,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0035` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00208 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 7.12, expected 3.03, ratio 2.35 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Medium |
| What happened | Invoice Verification (Medium, Medium) took 7.1h vs an expected 3.0h (2.35x). 100% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (100%); High assignee workload that week |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00208; 5 events: EV0001247, EV0001248, EV0001249, EV0001250, EV0001251 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.03,
  "actual_duration_h": 7.12,
  "duration_ratio": 2.35,
  "baseline_p90_h": 4.72,
  "components_actual_vs_expected_h": {
    "queue": [
      0.15,
      0.15
    ],
    "executor_processing": [
      0.65,
      0.65
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.58,
      1.03
    ],
    "dependency_wait": [
      5.73,
      1.07
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
    "assignee_week_expected_effort_h": 15.94,
    "assignee_typical_week_effort_h": 5.0,
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
      6.32,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0036` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00209 (Operations) |
| Severity / classification / confidence | high / rework / high |
| Measured | total_duration_h: observed 3.3, expected 1.22, ratio 2.71 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 3.3h vs an expected 1.2h (2.71x). 75% of the extra time is attributed to: rework after rejection (incorrect category). |
| Most likely reason | Rework after rejection (Incorrect category); preventable by S4 downtime reason coding |
| Ranked candidate causes | Rework after rejection (Incorrect category) (75%); Approval wait at Incharge stage (17%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (6%); Assignment queue delay (3%) |
| SOP reference | SOP-018 band above_p90; rework_trigger RW-CAT |
| Preventable by | S4 downtime reason coding |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00209; 8 events: EV0001252, EV0001253, EV0001254, EV0001255, EV0001256, EV0001257, EV0001258, EV0001259 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.22,
  "actual_duration_h": 3.3,
  "duration_ratio": 2.71,
  "baseline_p90_h": 1.75,
  "components_actual_vs_expected_h": {
    "queue": [
      0.23,
      0.17
    ],
    "executor_processing": [
      0.25,
      0.38
    ],
    "rework": [
      1.77,
      0.0
    ],
    "approval_wait": [
      0.55,
      0.15
    ],
    "dependency_wait": [
      0.5,
      0.37
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
    "assignee_week_expected_effort_h": 9.11,
    "assignee_typical_week_effort_h": 9.11,
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
      1.05,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>

### `DEV-0037` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00228 (HR) |
| Severity / classification / confidence | high / rework / medium |
| Measured | total_duration_h: observed 5.77, expected 1.82, ratio 3.17 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 5.8h vs an expected 1.8h (3.17x). 44% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S2 balance check |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (44%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (23%); Approval wait at Incharge stage (22%); Extended executor processing (11%) |
| SOP reference | SOP-020 band above_p90; rework_trigger RW-AMT |
| Preventable by | S2 balance check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00228; 9 events: EV0001383, EV0001384, EV0001385, EV0001386, EV0001387, EV0001388, EV0001389, EV0001390, EV0001391 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.82,
  "actual_duration_h": 5.77,
  "duration_ratio": 3.17,
  "baseline_p90_h": 2.51,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.12
    ],
    "executor_processing": [
      0.73,
      0.28
    ],
    "rework": [
      1.87,
      0.0
    ],
    "approval_wait": [
      1.08,
      0.15
    ],
    "dependency_wait": [
      2.0,
      1.05
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
    "assignee_week_expected_effort_h": 5.45,
    "assignee_typical_week_effort_h": 7.63,
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
      3.08,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0038` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00262 (Finance) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 4.45, expected 1.97, ratio 2.26 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 4.5h vs an expected 2.0h (2.26x). 59% of the extra time is attributed to: rework after rejection (incorrect category). |
| Most likely reason | Rework after rejection (Incorrect category); preventable by S2 expense category mapping |
| Ranked candidate causes | Rework after rejection (Incorrect category) (59%); Approval wait at Incharge stage (39%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (2%) |
| SOP reference | SOP-016 band above_p90; rework_trigger RW-CAT |
| Preventable by | S2 expense category mapping |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00262; 8 events: EV0001596, EV0001597, EV0001598, EV0001599, EV0001600, EV0001601, EV0001602, EV0001603 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.97,
  "actual_duration_h": 4.45,
  "duration_ratio": 2.26,
  "baseline_p90_h": 3.16,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.13
    ],
    "executor_processing": [
      0.25,
      0.35
    ],
    "rework": [
      1.72,
      0.0
    ],
    "approval_wait": [
      1.25,
      0.13
    ],
    "dependency_wait": [
      1.18,
      1.12
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
    "assignee_week_expected_effort_h": 3.93,
    "assignee_typical_week_effort_h": 5.43,
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
      2.43,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0039` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00277 (Procurement) |
| Severity / classification / confidence | medium / process / low |
| Measured | total_duration_h: observed 6.75, expected 2.73, ratio 2.47 |
| Compared with | BL-v1:L2:BOQ Review:Medium:Low |
| What happened | BOQ Review (Medium, Low) took 6.8h vs an expected 2.7h (2.47x). 38% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (38%); Rework after rejection (Amount mismatch) (32%); Cross-team / dependency wait (18%); Extended executor processing (12%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-013 band within |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00277; 9 events: EV0001688, EV0001689, EV0001690, EV0001691, EV0001692, EV0001693, EV0001694, EV0001695, EV0001696 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.73,
  "actual_duration_h": 6.75,
  "duration_ratio": 2.47,
  "baseline_p90_h": 4.07,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.13
    ],
    "executor_processing": [
      1.13,
      0.67
    ],
    "rework": [
      1.3,
      0.0
    ],
    "approval_wait": [
      2.43,
      0.92
    ],
    "dependency_wait": [
      1.75,
      1.03
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
    "assignee_week_expected_effort_h": 36.82,
    "assignee_typical_week_effort_h": 24.65,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-013",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.89,
    "sop_p10_p90_h": [
      4.57,
      7.21
    ],
    "first_decision_wait_actual_vs_sop_h": [
      4.18,
      3.65
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0040` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00290 (HR) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 5.65, expected 2.7, ratio 2.09 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Low |
| What happened | Employee Document Verification (Medium, Low) took 5.7h vs an expected 2.7h (2.09x). 51% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (51%); Rework after rejection (Incorrect category) (45%); Extended executor processing (4%) |
| SOP reference | SOP-021 band within |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00290; 9 events: EV0001768, EV0001769, EV0001770, EV0001771, EV0001772, EV0001773, EV0001774, EV0001775, EV0001776 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.7,
  "actual_duration_h": 5.65,
  "duration_ratio": 2.09,
  "baseline_p90_h": 3.85,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.12
    ],
    "executor_processing": [
      0.78,
      0.65
    ],
    "rework": [
      1.52,
      0.0
    ],
    "approval_wait": [
      2.37,
      0.68
    ],
    "dependency_wait": [
      0.93,
      1.13
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
    "assignee_week_expected_effort_h": 6.31,
    "assignee_typical_week_effort_h": 6.73,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.3,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0041` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00332 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 7.55, expected 3.0, ratio 2.52 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 7.5h vs an expected 3.0h (2.52x). 94% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (94%); Approval wait at Incharge stage (4%); Assignment queue delay (2%) |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00332; 5 events: EV0002020, EV0002021, EV0002022, EV0002023, EV0002024 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.0,
  "actual_duration_h": 7.55,
  "duration_ratio": 2.52,
  "baseline_p90_h": 5.45,
  "components_actual_vs_expected_h": {
    "queue": [
      0.23,
      0.15
    ],
    "executor_processing": [
      0.62,
      0.65
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.15,
      0.95
    ],
    "dependency_wait": [
      5.55,
      1.17
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
    "assignee_week_expected_effort_h": 6.0,
    "assignee_typical_week_effort_h": 8.02,
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
      6.7,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0042` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00366 (HR) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 4.78, expected 2.7, ratio 1.77 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Low |
| What happened | Employee Document Verification (Medium, Low) took 4.8h vs an expected 2.7h (1.77x). 49% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S5 salary and grade cross-check with offer letter |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (49%); Cross-team / dependency wait (28%); Approval wait at Incharge stage (18%); Assignment queue delay (6%) |
| SOP reference | SOP-021 band within; rework_trigger RW-AMT |
| Preventable by | S5 salary and grade cross-check with offer letter |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00366; 8 events: EV0002227, EV0002228, EV0002229, EV0002230, EV0002231, EV0002232, EV0002233, EV0002234 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.7,
  "actual_duration_h": 4.78,
  "duration_ratio": 1.77,
  "baseline_p90_h": 3.85,
  "components_actual_vs_expected_h": {
    "queue": [
      0.25,
      0.12
    ],
    "executor_processing": [
      0.62,
      0.65
    ],
    "rework": [
      1.08,
      0.0
    ],
    "approval_wait": [
      1.08,
      0.68
    ],
    "dependency_wait": [
      1.75,
      1.13
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
    "assignee_week_expected_effort_h": 5.36,
    "assignee_typical_week_effort_h": 5.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.83,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0043` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00368 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 3.62, expected 1.97, ratio 1.84 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 3.6h vs an expected 2.0h (1.84x). 94% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (94%); Extended executor processing (6%) |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00368; 6 events: EV0002242, EV0002243, EV0002244, EV0002245, EV0002246, EV0002247 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.97,
  "actual_duration_h": 3.62,
  "duration_ratio": 1.84,
  "baseline_p90_h": 3.16,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.13
    ],
    "executor_processing": [
      0.47,
      0.35
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.03,
      0.13
    ],
    "dependency_wait": [
      3.05,
      1.12
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
    "assignee_week_expected_effort_h": 3.93,
    "assignee_typical_week_effort_h": 5.43,
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
      3.08,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0044` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00386 (HR) |
| Severity / classification / confidence | high / process / medium |
| Measured | total_duration_h: observed 4.65, expected 1.82, ratio 2.56 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 4.7h vs an expected 1.8h (2.56x). 50% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (50%); Rework after rejection (Required document missing) (32%); Extended executor processing (18%) |
| SOP reference | SOP-020 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00386; 9 events: EV0002354, EV0002355, EV0002356, EV0002357, EV0002358, EV0002359, EV0002360, EV0002361, EV0002362 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.82,
  "actual_duration_h": 4.65,
  "duration_ratio": 2.56,
  "baseline_p90_h": 2.51,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.12
    ],
    "executor_processing": [
      1.03,
      0.28
    ],
    "rework": [
      1.33,
      0.0
    ],
    "approval_wait": [
      2.22,
      0.15
    ],
    "dependency_wait": [
      0.0,
      1.05
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
    "assignee_week_expected_effort_h": 4.52,
    "assignee_typical_week_effort_h": 7.19,
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
      2.22,
      0.8
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0045` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00399 (Procurement) |
| Severity / classification / confidence | medium / process / low |
| Measured | total_duration_h: observed 11.03, expected 5.97, ratio 1.85 |
| Compared with | BL-v1:L2:Purchase Request:Medium:Low |
| What happened | Purchase Request (Medium, Low) took 11.0h vs an expected 6.0h (1.85x). 38% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (38%); Rework after rejection (Wrong quantity) (35%); Cross-team / dependency wait (26%); Assignment queue delay (0%) |
| SOP reference | SOP-014 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00399; 9 events: EV0002434, EV0002435, EV0002436, EV0002437, EV0002438, EV0002439, EV0002440, EV0002441, EV0002442 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 5.97,
  "actual_duration_h": 11.03,
  "duration_ratio": 1.85,
  "baseline_p90_h": 7.96,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.12
    ],
    "executor_processing": [
      0.52,
      0.67
    ],
    "rework": [
      2.02,
      0.0
    ],
    "approval_wait": [
      5.03,
      2.85
    ],
    "dependency_wait": [
      3.33,
      1.83
    ]
  },
  "context": {
    "task_type": "Purchase Request",
    "complexity": "Medium",
    "priority": "Low",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 25.83,
    "assignee_typical_week_effort_h": 22.28,
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
      5.47,
      3.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0046` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00403 (Finance) |
| Severity / classification / confidence | medium / process / low |
| Measured | total_duration_h: observed 6.48, expected 3.0, ratio 2.16 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 6.5h vs an expected 3.0h (2.16x). 39% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (39%); Rework after rejection (Amount mismatch) (34%); Cross-team / dependency wait (19%); Extended executor processing (8%); High assignee workload that week |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00403; 9 events: EV0002461, EV0002462, EV0002463, EV0002464, EV0002465, EV0002466, EV0002467, EV0002468, EV0002469 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.0,
  "actual_duration_h": 6.48,
  "duration_ratio": 2.16,
  "baseline_p90_h": 5.45,
  "components_actual_vs_expected_h": {
    "queue": [
      0.15,
      0.15
    ],
    "executor_processing": [
      0.93,
      0.65
    ],
    "rework": [
      1.22,
      0.0
    ],
    "approval_wait": [
      2.35,
      0.95
    ],
    "dependency_wait": [
      1.83,
      1.17
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
    "assignee_week_expected_effort_h": 8.0,
    "assignee_typical_week_effort_h": 5.9,
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
      4.18,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0047` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00405 (Operations) |
| Severity / classification / confidence | high / rework / high |
| Measured | total_duration_h: observed 3.28, expected 1.01, ratio 3.26 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.3h vs an expected 1.0h (3.26x). 62% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S3 KPI formula check |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (62%); Approval wait at Incharge stage (36%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (2%); Extended executor processing (0%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; rework_trigger RW-AMT |
| Preventable by | S3 KPI formula check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00405; 8 events: EV0002476, EV0002477, EV0002478, EV0002479, EV0002480, EV0002481, EV0002482, EV0002483 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.01,
  "actual_duration_h": 3.28,
  "duration_ratio": 3.26,
  "baseline_p90_h": 1.86,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.14
    ],
    "executor_processing": [
      0.28,
      0.28
    ],
    "rework": [
      1.48,
      0.0
    ],
    "approval_wait": [
      0.97,
      0.12
    ],
    "dependency_wait": [
      0.43,
      0.38
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
    "assignee_week_expected_effort_h": 26.74,
    "assignee_typical_week_effort_h": 16.05,
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
      1.4,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>

### `DEV-0048` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00410 (Finance) |
| Severity / classification / confidence | high / rework / medium |
| Measured | total_duration_h: observed 5.47, expected 1.95, ratio 2.8 |
| Compared with | BL-v1:L1:Expense Approval:Simple:ALL |
| What happened | Expense Approval (Simple, High) took 5.5h vs an expected 1.9h (2.80x). 52% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S4 computation check |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (52%); Approval wait at Incharge stage (30%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (15%); Extended executor processing (4%) |
| SOP reference | SOP-016 band above_p90; rework_trigger RW-AMT |
| Preventable by | S4 computation check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00410; 8 events: EV0002505, EV0002506, EV0002507, EV0002508, EV0002509, EV0002510, EV0002511, EV0002512 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.95,
  "actual_duration_h": 5.47,
  "duration_ratio": 2.8,
  "baseline_p90_h": 3.14,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.15
    ],
    "executor_processing": [
      0.48,
      0.35
    ],
    "rework": [
      1.98,
      0.0
    ],
    "approval_wait": [
      1.25,
      0.13
    ],
    "dependency_wait": [
      1.72,
      1.17
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
    "assignee_week_expected_effort_h": 1.95,
    "assignee_typical_week_effort_h": 5.9,
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
      2.97,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0049` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00442 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 4.18, expected 1.95, ratio 2.15 |
| Compared with | BL-v1:L1:Expense Approval:Simple:ALL |
| What happened | Expense Approval (Simple, High) took 4.2h vs an expected 1.9h (2.15x). 46% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (46%); Rework after rejection (Required document missing) (36%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (10%); Extended executor processing (4%); Assignment queue delay (4%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00442; 8 events: EV0002715, EV0002716, EV0002717, EV0002718, EV0002719, EV0002720, EV0002721, EV0002722 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.95,
  "actual_duration_h": 4.18,
  "duration_ratio": 2.15,
  "baseline_p90_h": 3.14,
  "components_actual_vs_expected_h": {
    "queue": [
      0.25,
      0.15
    ],
    "executor_processing": [
      0.45,
      0.35
    ],
    "rework": [
      0.85,
      0.0
    ],
    "approval_wait": [
      1.23,
      0.13
    ],
    "dependency_wait": [
      1.4,
      1.17
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
    "assignee_week_expected_effort_h": 14.92,
    "assignee_typical_week_effort_h": 7.97,
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
      2.63,
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
| Entity | T00518 (HR) |
| Severity / classification / confidence | high / rework / medium |
| Measured | total_duration_h: observed 5.53, expected 1.82, ratio 3.05 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Medium |
| What happened | Leave Approval (Simple, Medium) took 5.5h vs an expected 1.8h (3.05x). 50% of the extra time is attributed to: rework after rejection (required document missing). |
| Most likely reason | Rework after rejection (Required document missing); preventable by S2 certificate check |
| Ranked candidate causes | Rework after rejection (Required document missing) (50%); Approval wait at Incharge stage (29%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (21%); Extended executor processing (0%) |
| SOP reference | SOP-020 band above_p90; rework_trigger RW-DOC |
| Preventable by | S2 certificate check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00518; 8 events: EV0003176, EV0003177, EV0003178, EV0003179, EV0003180, EV0003181, EV0003182, EV0003183 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.82,
  "actual_duration_h": 5.53,
  "duration_ratio": 3.05,
  "baseline_p90_h": 2.51,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.12
    ],
    "executor_processing": [
      0.28,
      0.28
    ],
    "rework": [
      1.97,
      0.0
    ],
    "approval_wait": [
      1.32,
      0.15
    ],
    "dependency_wait": [
      1.88,
      1.05
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
    "assignee_week_expected_effort_h": 7.25,
    "assignee_typical_week_effort_h": 7.19,
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
      3.2,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0051` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00519 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 5.48, expected 3.0, ratio 1.83 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 5.5h vs an expected 3.0h (1.83x). 72% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (72%); Rework after rejection (Wrong quantity) (26%); Assignment queue delay (2%); High assignee workload that week |
| SOP reference | SOP-015 band within |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00519; 8 events: EV0003184, EV0003185, EV0003186, EV0003187, EV0003188, EV0003189, EV0003190, EV0003191 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.0,
  "actual_duration_h": 5.48,
  "duration_ratio": 1.83,
  "baseline_p90_h": 5.45,
  "components_actual_vs_expected_h": {
    "queue": [
      0.2,
      0.15
    ],
    "executor_processing": [
      0.5,
      0.65
    ],
    "rework": [
      0.85,
      0.0
    ],
    "approval_wait": [
      0.45,
      0.95
    ],
    "dependency_wait": [
      3.48,
      1.17
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
    "assignee_week_expected_effort_h": 7.96,
    "assignee_typical_week_effort_h": 4.95,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.93,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0052` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00532 (Finance) |
| Severity / classification / confidence | medium / rework / high |
| Measured | total_duration_h: observed 5.5, expected 3.03, ratio 1.81 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Medium |
| What happened | Invoice Verification (Medium, Medium) took 5.5h vs an expected 3.0h (1.81x). 62% of the extra time is attributed to: rework after rejection (incorrect category). |
| Most likely reason | Rework after rejection (Incorrect category); preventable by S4 GL and tax code check |
| Ranked candidate causes | Rework after rejection (Incorrect category) (62%); Cross-team / dependency wait (31%); Approval wait at Incharge stage (6%) |
| SOP reference | SOP-015 band within; rework_trigger RW-CAT |
| Preventable by | S4 GL and tax code check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00532; 8 events: EV0003271, EV0003272, EV0003273, EV0003274, EV0003275, EV0003276, EV0003277, EV0003278 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.03,
  "actual_duration_h": 5.5,
  "duration_ratio": 1.81,
  "baseline_p90_h": 4.72,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.15
    ],
    "executor_processing": [
      0.65,
      0.65
    ],
    "rework": [
      1.63,
      0.0
    ],
    "approval_wait": [
      1.2,
      1.03
    ],
    "dependency_wait": [
      1.88,
      1.07
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
    "assignee_week_expected_effort_h": 3.03,
    "assignee_typical_week_effort_h": 5.0,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.08,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0053` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00566 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 4.93, expected 1.97, ratio 2.51 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 4.9h vs an expected 2.0h (2.51x). 80% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (80%); Extended executor processing (17%); Assignment queue delay (3%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00566; 7 events: EV0003477, EV0003478, EV0003479, EV0003480, EV0003481, EV0003482, EV0003483 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.97,
  "actual_duration_h": 4.93,
  "duration_ratio": 2.51,
  "baseline_p90_h": 3.16,
  "components_actual_vs_expected_h": {
    "queue": [
      0.23,
      0.13
    ],
    "executor_processing": [
      0.9,
      0.35
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.07,
      0.13
    ],
    "dependency_wait": [
      3.73,
      1.12
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
    "assignee_week_expected_effort_h": 8.9,
    "assignee_typical_week_effort_h": 4.95,
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
      3.8,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0054` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00595 (Operations) |
| Severity / classification / confidence | medium / executor_processing / high |
| Measured | total_duration_h: observed 1.87, expected 1.03, ratio 1.81 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 1.9h vs an expected 1.0h (1.81x). 74% of the extra time is attributed to: extended executor processing. |
| Most likely reason | Extended executor processing |
| Ranked candidate causes | Extended executor processing (74%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (14%); Assignment queue delay (10%); Approval wait at Incharge stage (2%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | No individual alert from a single ticket; monitored by the employee-level persistence check. |
| Source records | 1 tickets: T00595; 7 events: EV0003653, EV0003654, EV0003655, EV0003656, EV0003657, EV0003658, EV0003659 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.03,
  "actual_duration_h": 1.87,
  "duration_ratio": 1.81,
  "baseline_p90_h": 1.55,
  "components_actual_vs_expected_h": {
    "queue": [
      0.22,
      0.13
    ],
    "executor_processing": [
      1.0,
      0.38
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.17,
      0.15
    ],
    "dependency_wait": [
      0.48,
      0.37
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
    "assignee_week_expected_effort_h": 18.11,
    "assignee_typical_week_effort_h": 9.11,
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
      0.65,
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
| Entity | T00602 (Finance) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 4.85, expected 1.95, ratio 2.49 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 4.8h vs an expected 1.9h (2.49x). 55% of the extra time is attributed to: rework after rejection (required document missing). |
| Most likely reason | Rework after rejection (Required document missing); preventable by S3 receipt verification |
| Ranked candidate causes | Rework after rejection (Required document missing) (55%); Extended executor processing (27%); Approval wait at Incharge stage (17%); Assignment queue delay (1%) |
| SOP reference | SOP-016 band above_p90; rework_trigger RW-DOC |
| Preventable by | S3 receipt verification |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00602; 10 events: EV0003695, EV0003696, EV0003697, EV0003698, EV0003699, EV0003700, EV0003701, EV0003702, EV0003703, EV0003704 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.95,
  "actual_duration_h": 4.85,
  "duration_ratio": 2.49,
  "baseline_p90_h": 2.99,
  "components_actual_vs_expected_h": {
    "queue": [
      0.18,
      0.16
    ],
    "executor_processing": [
      1.17,
      0.32
    ],
    "rework": [
      1.73,
      0.0
    ],
    "approval_wait": [
      0.7,
      0.17
    ],
    "dependency_wait": [
      1.07,
      1.17
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
    "assignee_week_expected_effort_h": 1.95,
    "assignee_typical_week_effort_h": 5.9,
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
      1.77,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0056` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00612 (Operations) |
| Severity / classification / confidence | high / rework / medium |
| Measured | total_duration_h: observed 3.63, expected 1.01, ratio 3.6 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.6h vs an expected 1.0h (3.60x). 52% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S3 KPI formula check |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (52%); Approval wait at Incharge stage (47%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (1%); Extended executor processing (1%) |
| SOP reference | SOP-018 band above_p90; rework_trigger RW-AMT |
| Preventable by | S3 KPI formula check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00612; 8 events: EV0003765, EV0003766, EV0003767, EV0003768, EV0003769, EV0003770, EV0003771, EV0003772 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.01,
  "actual_duration_h": 3.63,
  "duration_ratio": 3.6,
  "baseline_p90_h": 1.86,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.14
    ],
    "executor_processing": [
      0.3,
      0.28
    ],
    "rework": [
      1.42,
      0.0
    ],
    "approval_wait": [
      1.4,
      0.12
    ],
    "dependency_wait": [
      0.4,
      0.38
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
    "assignee_week_expected_effort_h": 3.26,
    "assignee_typical_week_effort_h": 9.11,
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
      1.8,
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
| Entity | T00636 (Finance) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 5.55, expected 3.03, ratio 1.83 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Medium |
| What happened | Invoice Verification (Medium, Medium) took 5.5h vs an expected 3.0h (1.83x). 49% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S3 three-way match |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (49%); Approval wait at Incharge stage (31%); Cross-team / dependency wait (20%) |
| SOP reference | SOP-015 band within; rework_trigger RW-AMT |
| Preventable by | S3 three-way match |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00636; 8 events: EV0003910, EV0003911, EV0003912, EV0003913, EV0003914, EV0003915, EV0003916, EV0003917 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.03,
  "actual_duration_h": 5.55,
  "duration_ratio": 1.83,
  "baseline_p90_h": 4.72,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.15
    ],
    "executor_processing": [
      0.62,
      0.65
    ],
    "rework": [
      1.35,
      0.0
    ],
    "approval_wait": [
      1.9,
      1.03
    ],
    "dependency_wait": [
      1.62,
      1.07
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
    "assignee_week_expected_effort_h": 3.03,
    "assignee_typical_week_effort_h": 8.02,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.52,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0058` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00637 (HR) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 3.45, expected 1.82, ratio 1.89 |
| Compared with | BL-v1:L1:Leave Approval:Simple:ALL |
| What happened | Leave Approval (Simple, High) took 3.5h vs an expected 1.8h (1.89x). 44% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S2 balance check |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (44%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (34%); Approval wait at Incharge stage (22%); Extended executor processing (1%) |
| SOP reference | SOP-020 band above_p90; rework_trigger RW-AMT |
| Preventable by | S2 balance check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00637; 8 events: EV0003918, EV0003919, EV0003920, EV0003921, EV0003922, EV0003923, EV0003924, EV0003925 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.82,
  "actual_duration_h": 3.45,
  "duration_ratio": 1.89,
  "baseline_p90_h": 2.73,
  "components_actual_vs_expected_h": {
    "queue": [
      0.03,
      0.15
    ],
    "executor_processing": [
      0.32,
      0.3
    ],
    "rework": [
      0.85,
      0.0
    ],
    "approval_wait": [
      0.57,
      0.15
    ],
    "dependency_wait": [
      1.68,
      1.03
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
    "assignee_week_expected_effort_h": 3.64,
    "assignee_typical_week_effort_h": 6.73,
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
      2.25,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0059` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00687 (HR) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 4.85, expected 2.66, ratio 1.82 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Medium |
| What happened | Employee Document Verification (Medium, Medium) took 4.8h vs an expected 2.7h (1.82x). 43% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S5 salary and grade cross-check with offer letter |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (43%); Approval wait at Incharge stage (35%); Cross-team / dependency wait (19%); Assignment queue delay (3%); High assignee workload that week |
| SOP reference | SOP-021 band within; rework_trigger RW-AMT |
| Preventable by | S5 salary and grade cross-check with offer letter |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00687; 9 events: EV0004224, EV0004225, EV0004226, EV0004227, EV0004228, EV0004229, EV0004230, EV0004231, EV0004232 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.66,
  "actual_duration_h": 4.85,
  "duration_ratio": 1.82,
  "baseline_p90_h": 4.28,
  "components_actual_vs_expected_h": {
    "queue": [
      0.22,
      0.15
    ],
    "executor_processing": [
      0.6,
      0.63
    ],
    "rework": [
      0.95,
      0.0
    ],
    "approval_wait": [
      1.6,
      0.81
    ],
    "dependency_wait": [
      1.48,
      1.06
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
    "assignee_week_expected_effort_h": 17.01,
    "assignee_typical_week_effort_h": 7.63,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.08,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0060` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00693 (Operations) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 12.75, expected 7.17, ratio 1.78 |
| Compared with | BL-v1:L2:Incident Review:Complex:High |
| What happened | Incident Review (Complex, High) took 12.8h vs an expected 7.2h (1.78x). 41% of the extra time is attributed to: rework after rejection (required document missing). |
| Most likely reason | Rework after rejection (Required document missing); preventable by S3 evidence checklist |
| Ranked candidate causes | Rework after rejection (Required document missing) (41%); Approval wait at Incharge stage (41%); Cross-team / dependency wait (15%); Extended executor processing (3%) |
| SOP reference | SOP-019 band above_p90; rework_trigger RW-DOC |
| Preventable by | S3 evidence checklist |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00693; 9 events: EV0004263, EV0004264, EV0004265, EV0004266, EV0004267, EV0004268, EV0004269, EV0004270, EV0004271 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 7.17,
  "actual_duration_h": 12.75,
  "duration_ratio": 1.78,
  "baseline_p90_h": 11.72,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.13
    ],
    "executor_processing": [
      1.5,
      1.35
    ],
    "rework": [
      2.07,
      0.0
    ],
    "approval_wait": [
      5.83,
      3.8
    ],
    "dependency_wait": [
      3.28,
      2.55
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
    "assignee_week_expected_effort_h": 9.21,
    "assignee_typical_week_effort_h": 9.11,
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
      6.27,
      4.5
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0061` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00696 (Procurement) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 5.03, expected 2.73, ratio 1.84 |
| Compared with | BL-v1:L2:BOQ Review:Medium:Low |
| What happened | BOQ Review (Medium, Low) took 5.0h vs an expected 2.7h (1.84x). 40% of the extra time is attributed to: rework after rejection (wrong quantity). |
| Most likely reason | Rework after rejection (Wrong quantity); preventable by S3 take-off cross-check |
| Ranked candidate causes | Rework after rejection (Wrong quantity) (40%); Cross-team / dependency wait (35%); Approval wait at Incharge stage (25%) |
| SOP reference | SOP-013 band within; rework_trigger RW-QTY |
| Preventable by | S3 take-off cross-check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00696; 8 events: EV0004283, EV0004284, EV0004285, EV0004286, EV0004287, EV0004288, EV0004289, EV0004290 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.73,
  "actual_duration_h": 5.03,
  "duration_ratio": 1.84,
  "baseline_p90_h": 4.07,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.13
    ],
    "executor_processing": [
      0.67,
      0.67
    ],
    "rework": [
      0.93,
      0.0
    ],
    "approval_wait": [
      1.5,
      0.92
    ],
    "dependency_wait": [
      1.85,
      1.03
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
    "assignee_week_expected_effort_h": 14.44,
    "assignee_typical_week_effort_h": 19.44,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-013",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.89,
    "sop_p10_p90_h": [
      4.57,
      7.21
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.35,
      3.65
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0062` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00762 (Operations) |
| Severity / classification / confidence | high / rework / high |
| Measured | total_duration_h: observed 3.72, expected 1.01, ratio 3.69 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.7h vs an expected 1.0h (3.69x). 60% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S3 KPI formula check |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (60%); Extended executor processing (28%); Approval wait at Incharge stage (10%); Assignment queue delay (2%) |
| SOP reference | SOP-018 band above_p90; rework_trigger RW-AMT |
| Preventable by | S3 KPI formula check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00762; 10 events: EV0004696, EV0004697, EV0004698, EV0004699, EV0004700, EV0004701, EV0004702, EV0004703, EV0004704, EV0004705 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.01,
  "actual_duration_h": 3.72,
  "duration_ratio": 3.69,
  "baseline_p90_h": 1.86,
  "components_actual_vs_expected_h": {
    "queue": [
      0.2,
      0.14
    ],
    "executor_processing": [
      1.08,
      0.28
    ],
    "rework": [
      1.68,
      0.0
    ],
    "approval_wait": [
      0.4,
      0.12
    ],
    "dependency_wait": [
      0.35,
      0.38
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
    "assignee_week_expected_effort_h": 16.64,
    "assignee_typical_week_effort_h": 16.05,
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
      0.75,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>

### `DEV-0063` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00764 (Operations) |
| Severity / classification / confidence | high / rework / high |
| Measured | total_duration_h: observed 3.5, expected 1.22, ratio 2.88 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 3.5h vs an expected 1.2h (2.88x). 67% of the extra time is attributed to: rework after rejection (required document missing). |
| Most likely reason | Rework after rejection (Required document missing); preventable by S2 data completeness check |
| Ranked candidate causes | Rework after rejection (Required document missing) (67%); Approval wait at Incharge stage (29%); Assignment queue delay (3%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; rework_trigger RW-DOC |
| Preventable by | S2 data completeness check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00764; 8 events: EV0004712, EV0004713, EV0004714, EV0004715, EV0004716, EV0004717, EV0004718, EV0004719 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.22,
  "actual_duration_h": 3.5,
  "duration_ratio": 2.88,
  "baseline_p90_h": 1.75,
  "components_actual_vs_expected_h": {
    "queue": [
      0.25,
      0.17
    ],
    "executor_processing": [
      0.25,
      0.38
    ],
    "rework": [
      1.72,
      0.0
    ],
    "approval_wait": [
      0.88,
      0.15
    ],
    "dependency_wait": [
      0.4,
      0.37
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
    "assignee_week_expected_effort_h": 16.5,
    "assignee_typical_week_effort_h": 9.93,
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
      1.28,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>

### `DEV-0064` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00767 (HR) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 4.08, expected 1.79, ratio 2.28 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 4.1h vs an expected 1.8h (2.28x). 51% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S2 balance check |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (51%); Approval wait at Incharge stage (35%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (12%); Assignment queue delay (2%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; rework_trigger RW-AMT |
| Preventable by | S2 balance check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00767; 8 events: EV0004732, EV0004733, EV0004734, EV0004735, EV0004736, EV0004737, EV0004738, EV0004739 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.79,
  "actual_duration_h": 4.08,
  "duration_ratio": 2.28,
  "baseline_p90_h": 2.75,
  "components_actual_vs_expected_h": {
    "queue": [
      0.2,
      0.14
    ],
    "executor_processing": [
      0.25,
      0.3
    ],
    "rework": [
      1.3,
      0.0
    ],
    "approval_wait": [
      1.03,
      0.13
    ],
    "dependency_wait": [
      1.3,
      1.0
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
    "assignee_week_expected_effort_h": 11.67,
    "assignee_typical_week_effort_h": 4.48,
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
      2.33,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0065` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00769 (HR) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 4.85, expected 2.66, ratio 1.82 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Medium |
| What happened | Employee Document Verification (Medium, Medium) took 4.8h vs an expected 2.7h (1.82x). 58% of the extra time is attributed to: rework after rejection (incorrect category). |
| Most likely reason | Rework after rejection (Incorrect category); preventable by S2 document type classification |
| Ranked candidate causes | Rework after rejection (Incorrect category) (58%); Cross-team / dependency wait (36%); Approval wait at Incharge stage (6%); Assignment queue delay (1%) |
| SOP reference | SOP-021 band within; rework_trigger RW-CAT |
| Preventable by | S2 document type classification |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00769; 8 events: EV0004751, EV0004752, EV0004753, EV0004754, EV0004755, EV0004756, EV0004757, EV0004758 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.66,
  "actual_duration_h": 4.85,
  "duration_ratio": 1.82,
  "baseline_p90_h": 4.28,
  "components_actual_vs_expected_h": {
    "queue": [
      0.17,
      0.15
    ],
    "executor_processing": [
      0.52,
      0.63
    ],
    "rework": [
      1.33,
      0.0
    ],
    "approval_wait": [
      0.95,
      0.81
    ],
    "dependency_wait": [
      1.88,
      1.06
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
    "assignee_week_expected_effort_h": 7.15,
    "assignee_typical_week_effort_h": 5.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.83,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0066` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00770 (HR) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 6.2, expected 2.66, ratio 2.33 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Medium |
| What happened | Employee Document Verification (Medium, Medium) took 6.2h vs an expected 2.7h (2.33x). 40% of the extra time is attributed to: rework after rejection (incorrect category). |
| Most likely reason | Rework after rejection (Incorrect category); preventable by S2 document type classification |
| Ranked candidate causes | Rework after rejection (Incorrect category) (40%); Approval wait at Incharge stage (36%); Cross-team / dependency wait (22%); Extended executor processing (2%) |
| SOP reference | SOP-021 band within; rework_trigger RW-CAT |
| Preventable by | S2 document type classification |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00770; 9 events: EV0004759, EV0004760, EV0004761, EV0004762, EV0004763, EV0004764, EV0004765, EV0004766, EV0004767 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.66,
  "actual_duration_h": 6.2,
  "duration_ratio": 2.33,
  "baseline_p90_h": 4.28,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.15
    ],
    "executor_processing": [
      0.72,
      0.63
    ],
    "rework": [
      1.47,
      0.0
    ],
    "approval_wait": [
      2.1,
      0.81
    ],
    "dependency_wait": [
      1.85,
      1.06
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
    "assignee_week_expected_effort_h": 5.32,
    "assignee_typical_week_effort_h": 5.59,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.95,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0067` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00786 (Operations) |
| Severity / classification / confidence | high / rework / high |
| Measured | total_duration_h: observed 3.52, expected 1.22, ratio 2.89 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:High |
| What happened | Daily Operations Report (Simple, High) took 3.5h vs an expected 1.2h (2.89x). 71% of the extra time is attributed to: rework after rejection (required document missing). |
| Most likely reason | Rework after rejection (Required document missing); preventable by S2 data completeness check |
| Ranked candidate causes | Rework after rejection (Required document missing) (71%); Approval wait at Incharge stage (27%); Assignment queue delay (2%) |
| SOP reference | SOP-018 band above_p90; rework_trigger RW-DOC |
| Preventable by | S2 data completeness check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00786; 8 events: EV0004867, EV0004868, EV0004869, EV0004870, EV0004871, EV0004872, EV0004873, EV0004874 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.22,
  "actual_duration_h": 3.52,
  "duration_ratio": 2.89,
  "baseline_p90_h": 1.75,
  "components_actual_vs_expected_h": {
    "queue": [
      0.23,
      0.17
    ],
    "executor_processing": [
      0.25,
      0.38
    ],
    "rework": [
      1.9,
      0.0
    ],
    "approval_wait": [
      0.87,
      0.15
    ],
    "dependency_wait": [
      0.27,
      0.37
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
    "assignee_week_expected_effort_h": 9.11,
    "assignee_typical_week_effort_h": 9.11,
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
      1.13,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>

### `DEV-0068` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00793 (Procurement) |
| Severity / classification / confidence | medium / process / low |
| Measured | total_duration_h: observed 14.43, expected 8.16, ratio 1.77 |
| Compared with | BL-v1:L2:Vendor Onboarding:Complex:Medium |
| What happened | Vendor Onboarding (Complex, Medium) took 14.4h vs an expected 8.2h (1.77x). 33% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (33%); Cross-team / dependency wait (31%); Rework after rejection (Amount mismatch) (27%); Extended executor processing (8%); Assignment queue delay (1%) |
| SOP reference | SOP-017 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00793; 11 events: EV0004910, EV0004911, EV0004912, EV0004913, EV0004914, EV0004915, EV0004916, EV0004917, EV0004918, EV0004919, EV0004920 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 8.16,
  "actual_duration_h": 14.43,
  "duration_ratio": 1.77,
  "baseline_p90_h": 10.66,
  "components_actual_vs_expected_h": {
    "queue": [
      0.2,
      0.16
    ],
    "executor_processing": [
      1.9,
      1.38
    ],
    "rework": [
      1.82,
      0.0
    ],
    "approval_wait": [
      5.55,
      3.38
    ],
    "dependency_wait": [
      4.97,
      2.9
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
    "assignee_week_expected_effort_h": 14.12,
    "assignee_typical_week_effort_h": 22.28,
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
      8.73,
      4.83
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0069` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00838 (HR) |
| Severity / classification / confidence | medium / rework / high |
| Measured | total_duration_h: observed 4.75, expected 2.7, ratio 1.76 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Low |
| What happened | Employee Document Verification (Medium, Low) took 4.8h vs an expected 2.7h (1.76x). 62% of the extra time is attributed to: rework after rejection (wrong quantity). |
| Most likely reason | Rework after rejection (Wrong quantity); preventable by S4 experience duration calculation |
| Ranked candidate causes | Rework after rejection (Wrong quantity) (62%); Approval wait at Incharge stage (38%) |
| SOP reference | SOP-021 band within; rework_trigger RW-QTY |
| Preventable by | S4 experience duration calculation |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00838; 9 events: EV0005191, EV0005192, EV0005193, EV0005194, EV0005195, EV0005196, EV0005197, EV0005198, EV0005199 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.7,
  "actual_duration_h": 4.75,
  "duration_ratio": 1.76,
  "baseline_p90_h": 3.85,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.12
    ],
    "executor_processing": [
      0.6,
      0.65
    ],
    "rework": [
      1.63,
      0.0
    ],
    "approval_wait": [
      1.7,
      0.68
    ],
    "dependency_wait": [
      0.77,
      1.13
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
    "assignee_week_expected_effort_h": 5.4,
    "assignee_typical_week_effort_h": 7.63,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.47,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0070` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00845 (HR) |
| Severity / classification / confidence | medium / rework / high |
| Measured | total_duration_h: observed 3.62, expected 1.79, ratio 2.02 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 3.6h vs an expected 1.8h (2.02x). 75% of the extra time is attributed to: rework after rejection (incorrect category). |
| Most likely reason | Rework after rejection (Incorrect category); preventable by S2 leave type eligibility |
| Ranked candidate causes | Rework after rejection (Incorrect category) (75%); Approval wait at Incharge stage (25%) |
| SOP reference | SOP-020 band above_p90; rework_trigger RW-CAT |
| Preventable by | S2 leave type eligibility |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00845; 8 events: EV0005235, EV0005236, EV0005237, EV0005238, EV0005239, EV0005240, EV0005241, EV0005242 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.79,
  "actual_duration_h": 3.62,
  "duration_ratio": 2.02,
  "baseline_p90_h": 2.75,
  "components_actual_vs_expected_h": {
    "queue": [
      0.08,
      0.14
    ],
    "executor_processing": [
      0.25,
      0.3
    ],
    "rework": [
      1.68,
      0.0
    ],
    "approval_wait": [
      0.7,
      0.13
    ],
    "dependency_wait": [
      0.9,
      1.0
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
    "assignee_week_expected_effort_h": 4.96,
    "assignee_typical_week_effort_h": 4.48,
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
      1.6,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0071` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00852 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 9.12, expected 2.99, ratio 3.05 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:High |
| What happened | Invoice Verification (Medium, High) took 9.1h vs an expected 3.0h (3.05x). 79% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (79%); Rework after rejection (Incorrect category) (16%); Approval wait at Incharge stage (5%); High assignee workload that week |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00852; 8 events: EV0005275, EV0005276, EV0005277, EV0005278, EV0005279, EV0005280, EV0005281, EV0005282 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.99,
  "actual_duration_h": 9.12,
  "duration_ratio": 3.05,
  "baseline_p90_h": 4.84,
  "components_actual_vs_expected_h": {
    "queue": [
      0.12,
      0.14
    ],
    "executor_processing": [
      0.67,
      0.68
    ],
    "rework": [
      0.98,
      0.0
    ],
    "approval_wait": [
      1.22,
      0.9
    ],
    "dependency_wait": [
      6.13,
      1.22
    ]
  },
  "context": {
    "task_type": "Invoice Verification",
    "complexity": "Medium",
    "priority": "High",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 11.89,
    "assignee_typical_week_effort_h": 5.43,
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
      7.35,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0072` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00854 (HR) |
| Severity / classification / confidence | high / rework / low |
| Measured | total_duration_h: observed 4.7, expected 1.82, ratio 2.58 |
| Compared with | BL-v1:L1:Leave Approval:Simple:ALL |
| What happened | Leave Approval (Simple, High) took 4.7h vs an expected 1.8h (2.58x). 33% of the extra time is attributed to: rework after rejection (required document missing). |
| Most likely reason | Rework after rejection (Required document missing); preventable by S2 certificate check |
| Ranked candidate causes | Rework after rejection (Required document missing) (33%); Extended executor processing (23%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (22%); Approval wait at Incharge stage (20%); Assignment queue delay (3%) |
| SOP reference | SOP-020 band above_p90; rework_trigger RW-DOC |
| Preventable by | S2 certificate check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00854; 10 events: EV0005294, EV0005295, EV0005296, EV0005297, EV0005298, EV0005299, EV0005300, EV0005301, EV0005302, EV0005303 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.82,
  "actual_duration_h": 4.7,
  "duration_ratio": 2.58,
  "baseline_p90_h": 2.73,
  "components_actual_vs_expected_h": {
    "queue": [
      0.23,
      0.15
    ],
    "executor_processing": [
      1.0,
      0.3
    ],
    "rework": [
      1.0,
      0.0
    ],
    "approval_wait": [
      0.75,
      0.15
    ],
    "dependency_wait": [
      1.72,
      1.03
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
    "assignee_week_expected_effort_h": 9.04,
    "assignee_typical_week_effort_h": 7.63,
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
      2.47,
      0.8
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0073` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00877 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.13, expected 3.0, ratio 2.04 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 6.1h vs an expected 3.0h (2.04x). 97% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (97%); Assignment queue delay (2%); Extended executor processing (2%); High assignee workload that week |
| SOP reference | SOP-015 band within |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00877; 6 events: EV0005430, EV0005431, EV0005432, EV0005433, EV0005434, EV0005435 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.0,
  "actual_duration_h": 6.13,
  "duration_ratio": 2.04,
  "baseline_p90_h": 5.45,
  "components_actual_vs_expected_h": {
    "queue": [
      0.22,
      0.15
    ],
    "executor_processing": [
      0.72,
      0.65
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.3,
      0.95
    ],
    "dependency_wait": [
      4.9,
      1.17
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
    "assignee_week_expected_effort_h": 13.81,
    "assignee_typical_week_effort_h": 5.43,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      5.2,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0074` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00951 (HR) |
| Severity / classification / confidence | medium / rework / high |
| Measured | total_duration_h: observed 5.02, expected 2.66, ratio 1.89 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Medium |
| What happened | Employee Document Verification (Medium, Medium) took 5.0h vs an expected 2.7h (1.89x). 60% of the extra time is attributed to: rework after rejection (incorrect category). |
| Most likely reason | Rework after rejection (Incorrect category); preventable by S2 document type classification |
| Ranked candidate causes | Rework after rejection (Incorrect category) (60%); Approval wait at Incharge stage (29%); Extended executor processing (11%) |
| SOP reference | SOP-021 band within; rework_trigger RW-CAT |
| Preventable by | S2 document type classification |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00951; 9 events: EV0005870, EV0005871, EV0005872, EV0005873, EV0005874, EV0005875, EV0005876, EV0005877, EV0005878 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.66,
  "actual_duration_h": 5.02,
  "duration_ratio": 1.89,
  "baseline_p90_h": 4.28,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.15
    ],
    "executor_processing": [
      0.95,
      0.63
    ],
    "rework": [
      1.77,
      0.0
    ],
    "approval_wait": [
      1.65,
      0.81
    ],
    "dependency_wait": [
      0.6,
      1.06
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
    "assignee_week_expected_effort_h": 9.79,
    "assignee_typical_week_effort_h": 7.63,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.25,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0075` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00957 (Operations) |
| Severity / classification / confidence | high / rework / medium |
| Measured | total_duration_h: observed 3.03, expected 1.03, ratio 2.94 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Low |
| What happened | Daily Operations Report (Simple, Low) took 3.0h vs an expected 1.0h (2.94x). 56% of the extra time is attributed to: rework after rejection (wrong quantity). |
| Most likely reason | Rework after rejection (Wrong quantity); preventable by S3 reconciliation against plan |
| Ranked candidate causes | Rework after rejection (Wrong quantity) (56%); Approval wait at Incharge stage (33%); Assignment queue delay (5%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (5%); Extended executor processing (1%); High assignee workload that week |
| SOP reference | SOP-018 band above_p90; rework_trigger RW-QTY |
| Preventable by | S3 reconciliation against plan |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00957; 8 events: EV0005915, EV0005916, EV0005917, EV0005918, EV0005919, EV0005920, EV0005921, EV0005922 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.03,
  "actual_duration_h": 3.03,
  "duration_ratio": 2.94,
  "baseline_p90_h": 1.55,
  "components_actual_vs_expected_h": {
    "queue": [
      0.23,
      0.13
    ],
    "executor_processing": [
      0.4,
      0.38
    ],
    "rework": [
      1.12,
      0.0
    ],
    "approval_wait": [
      0.82,
      0.15
    ],
    "dependency_wait": [
      0.47,
      0.37
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
    "assignee_week_expected_effort_h": 24.37,
    "assignee_typical_week_effort_h": 9.93,
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
      1.28,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>

### `DEV-0076` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00964 (Finance) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 5.67, expected 3.0, ratio 1.89 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 5.7h vs an expected 3.0h (1.89x). 50% of the extra time is attributed to: rework after rejection (wrong quantity). |
| Most likely reason | Rework after rejection (Wrong quantity); preventable by S3 three-way match against GRN |
| Ranked candidate causes | Rework after rejection (Wrong quantity) (50%); Cross-team / dependency wait (29%); Approval wait at Incharge stage (17%); Assignment queue delay (2%); Extended executor processing (1%); High assignee workload that week |
| SOP reference | SOP-015 band within; rework_trigger RW-QTY |
| Preventable by | S3 three-way match against GRN |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00964; 8 events: EV0005969, EV0005970, EV0005971, EV0005972, EV0005973, EV0005974, EV0005975, EV0005976 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.0,
  "actual_duration_h": 5.67,
  "duration_ratio": 1.89,
  "baseline_p90_h": 5.45,
  "components_actual_vs_expected_h": {
    "queue": [
      0.22,
      0.15
    ],
    "executor_processing": [
      0.68,
      0.65
    ],
    "rework": [
      1.38,
      0.0
    ],
    "approval_wait": [
      1.42,
      0.95
    ],
    "dependency_wait": [
      1.97,
      1.17
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
    "assignee_week_expected_effort_h": 6.92,
    "assignee_typical_week_effort_h": 5.0,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.38,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0077` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00972 (Procurement) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 5.17, expected 2.88, ratio 1.79 |
| Compared with | BL-v1:L2:BOQ Review:Medium:High |
| What happened | BOQ Review (Medium, High) took 5.2h vs an expected 2.9h (1.79x). 53% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (53%); Rework after rejection (Amount mismatch) (43%); Cross-team / dependency wait (4%) |
| SOP reference | SOP-013 band within |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T00972; 8 events: EV0006016, EV0006017, EV0006018, EV0006019, EV0006020, EV0006021, EV0006022, EV0006023 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.88,
  "actual_duration_h": 5.17,
  "duration_ratio": 1.79,
  "baseline_p90_h": 4.63,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.15
    ],
    "executor_processing": [
      0.53,
      0.67
    ],
    "rework": [
      0.95,
      0.0
    ],
    "approval_wait": [
      2.28,
      1.12
    ],
    "dependency_wait": [
      1.33,
      1.25
    ]
  },
  "context": {
    "task_type": "BOQ Review",
    "complexity": "Medium",
    "priority": "High",
    "dependency_count": 1,
    "rejection_count": 1,
    "reassignment_count": 0,
    "escalation_count": 0,
    "assignee_week_expected_effort_h": 2.88,
    "assignee_typical_week_effort_h": 22.79,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-013",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.89,
    "sop_p10_p90_h": [
      4.57,
      7.21
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.62,
      3.65
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0078` TICKET_DURATION

| field | value |
|---|---|
| Entity | T00991 (Finance) |
| Severity / classification / confidence | high / rework / low |
| Measured | total_duration_h: observed 5.18, expected 1.95, ratio 2.66 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 5.2h vs an expected 1.9h (2.66x). 34% of the extra time is attributed to: rework after rejection (required document missing). |
| Most likely reason | Rework after rejection (Required document missing); preventable by S3 receipt verification |
| Ranked candidate causes | Rework after rejection (Required document missing) (34%); Extended executor processing (23%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (23%); Approval wait at Incharge stage (20%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; rework_trigger RW-DOC |
| Preventable by | S3 receipt verification |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T00991; 10 events: EV0006134, EV0006135, EV0006136, EV0006137, EV0006138, EV0006139, EV0006140, EV0006141, EV0006142, EV0006143 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.95,
  "actual_duration_h": 5.18,
  "duration_ratio": 2.66,
  "baseline_p90_h": 2.99,
  "components_actual_vs_expected_h": {
    "queue": [
      0.17,
      0.16
    ],
    "executor_processing": [
      1.1,
      0.32
    ],
    "rework": [
      1.13,
      0.0
    ],
    "approval_wait": [
      0.85,
      0.17
    ],
    "dependency_wait": [
      1.93,
      1.17
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
    "assignee_week_expected_effort_h": 19.91,
    "assignee_typical_week_effort_h": 7.97,
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
      2.78,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0079` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01026 (Finance) |
| Severity / classification / confidence | medium / rework / high |
| Measured | total_duration_h: observed 3.52, expected 1.97, ratio 1.79 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 3.5h vs an expected 2.0h (1.79x). 62% of the extra time is attributed to: rework after rejection (incorrect category). |
| Most likely reason | Rework after rejection (Incorrect category); preventable by S2 expense category mapping |
| Ranked candidate causes | Rework after rejection (Incorrect category) (62%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (25%); Approval wait at Incharge stage (12%) |
| SOP reference | SOP-016 band above_p90; rework_trigger RW-CAT |
| Preventable by | S2 expense category mapping |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T01026; 8 events: EV0006351, EV0006352, EV0006353, EV0006354, EV0006355, EV0006356, EV0006357, EV0006358 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.97,
  "actual_duration_h": 3.52,
  "duration_ratio": 1.79,
  "baseline_p90_h": 3.16,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.13
    ],
    "executor_processing": [
      0.3,
      0.35
    ],
    "rework": [
      1.18,
      0.0
    ],
    "approval_wait": [
      0.37,
      0.13
    ],
    "dependency_wait": [
      1.6,
      1.12
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
    "assignee_week_expected_effort_h": 3.92,
    "assignee_typical_week_effort_h": 7.97,
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
      1.97,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0080` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01041 (Finance) |
| Severity / classification / confidence | high / process / high |
| Measured | total_duration_h: observed 6.02, expected 1.95, ratio 3.09 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Medium |
| What happened | Expense Approval (Simple, Medium) took 6.0h vs an expected 1.9h (3.09x). 97% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (97%); Extended executor processing (2%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90; C3 undeclared dependency wait (SOP-016 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01041; 6 events: EV0006446, EV0006447, EV0006448, EV0006449, EV0006450, EV0006451 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.95,
  "actual_duration_h": 6.02,
  "duration_ratio": 3.09,
  "baseline_p90_h": 2.99,
  "components_actual_vs_expected_h": {
    "queue": [
      0.22,
      0.16
    ],
    "executor_processing": [
      0.38,
      0.32
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.02,
      0.17
    ],
    "dependency_wait": [
      5.4,
      1.17
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
    "assignee_week_expected_effort_h": 14.9,
    "assignee_typical_week_effort_h": 5.43,
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
      5.42,
      0.89
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0081` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01054 (HR) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 6.38, expected 2.66, ratio 2.4 |
| Compared with | BL-v1:L2:Employee Document Verification:Medium:Medium |
| What happened | Employee Document Verification (Medium, Medium) took 6.4h vs an expected 2.7h (2.40x). 50% of the extra time is attributed to: rework after rejection (wrong quantity). |
| Most likely reason | Rework after rejection (Wrong quantity); preventable by S4 experience duration calculation |
| Ranked candidate causes | Rework after rejection (Wrong quantity) (50%); Approval wait at Incharge stage (42%); Cross-team / dependency wait (9%); High assignee workload that week |
| SOP reference | SOP-021 band within; rework_trigger RW-QTY |
| Preventable by | S4 experience duration calculation |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T01054; 8 events: EV0006521, EV0006522, EV0006523, EV0006524, EV0006525, EV0006526, EV0006527, EV0006528 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.66,
  "actual_duration_h": 6.38,
  "duration_ratio": 2.4,
  "baseline_p90_h": 4.28,
  "components_actual_vs_expected_h": {
    "queue": [
      0.05,
      0.15
    ],
    "executor_processing": [
      0.57,
      0.63
    ],
    "rework": [
      1.93,
      0.0
    ],
    "approval_wait": [
      2.43,
      0.81
    ],
    "dependency_wait": [
      1.4,
      1.06
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
    "assignee_week_expected_effort_h": 8.94,
    "assignee_typical_week_effort_h": 5.89,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-021",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.86,
    "sop_p10_p90_h": [
      4.13,
      7.59
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.83,
      4.07
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0082` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01056 (HR) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 3.4, expected 1.79, ratio 1.9 |
| Compared with | BL-v1:L2:Leave Approval:Simple:Low |
| What happened | Leave Approval (Simple, Low) took 3.4h vs an expected 1.8h (1.90x). 55% of the extra time is attributed to: wait after dependencywait event with no declared dependency (likely reviewer queue). |
| Most likely reason | Wait after DependencyWait event with no declared dependency (likely reviewer queue) |
| Ranked candidate causes | Wait after DependencyWait event with no declared dependency (likely reviewer queue) (55%); Extended executor processing (40%); Approval wait at Incharge stage (5%); Assignment queue delay (0%); High assignee workload that week |
| SOP reference | SOP-020 band above_p90; C3 undeclared dependency wait (SOP-020 declares none) |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01056; 7 events: EV0006534, EV0006535, EV0006536, EV0006537, EV0006538, EV0006539, EV0006540 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.79,
  "actual_duration_h": 3.4,
  "duration_ratio": 1.9,
  "baseline_p90_h": 2.75,
  "components_actual_vs_expected_h": {
    "queue": [
      0.15,
      0.14
    ],
    "executor_processing": [
      1.03,
      0.3
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      0.22,
      0.13
    ],
    "dependency_wait": [
      2.0,
      1.0
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
    "assignee_week_expected_effort_h": 8.98,
    "assignee_typical_week_effort_h": 5.89,
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
      2.22,
      0.8
    ],
    "conformance_fitness": 0.8
  }
}
```
</details>

### `DEV-0083` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01058 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 5.8, expected 3.0, ratio 1.93 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 5.8h vs an expected 3.0h (1.93x). 45% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (45%); Rework after rejection (Incorrect category) (44%); Extended executor processing (11%); High assignee workload that week |
| SOP reference | SOP-015 band within |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01058; 8 events: EV0006546, EV0006547, EV0006548, EV0006549, EV0006550, EV0006551, EV0006552, EV0006553 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.0,
  "actual_duration_h": 5.8,
  "duration_ratio": 1.93,
  "baseline_p90_h": 5.45,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.15
    ],
    "executor_processing": [
      0.97,
      0.65
    ],
    "rework": [
      1.28,
      0.0
    ],
    "approval_wait": [
      2.25,
      0.95
    ],
    "dependency_wait": [
      1.17,
      1.17
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
    "assignee_week_expected_effort_h": 9.03,
    "assignee_typical_week_effort_h": 5.9,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.42,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0084` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01095 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 3.73, expected 1.97, ratio 1.9 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 3.7h vs an expected 2.0h (1.90x). 50% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (50%); Rework after rejection (Incorrect category) (50%); Assignment queue delay (1%); High assignee workload that week |
| SOP reference | SOP-016 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01095; 8 events: EV0006769, EV0006770, EV0006771, EV0006772, EV0006773, EV0006774, EV0006775, EV0006776 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.97,
  "actual_duration_h": 3.73,
  "duration_ratio": 1.9,
  "baseline_p90_h": 3.16,
  "components_actual_vs_expected_h": {
    "queue": [
      0.15,
      0.13
    ],
    "executor_processing": [
      0.25,
      0.35
    ],
    "rework": [
      1.1,
      0.0
    ],
    "approval_wait": [
      1.23,
      0.13
    ],
    "dependency_wait": [
      1.0,
      1.12
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
    "assignee_week_expected_effort_h": 19.91,
    "assignee_typical_week_effort_h": 7.97,
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
      2.23,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0085` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01115 (Finance) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 4.05, expected 1.97, ratio 2.06 |
| Compared with | BL-v1:L2:Expense Approval:Simple:Low |
| What happened | Expense Approval (Simple, Low) took 4.0h vs an expected 2.0h (2.06x). 51% of the extra time is attributed to: rework after rejection (required document missing). |
| Most likely reason | Rework after rejection (Required document missing); preventable by S3 receipt verification |
| Ranked candidate causes | Rework after rejection (Required document missing) (51%); Approval wait at Incharge stage (36%); Extended executor processing (11%); Assignment queue delay (2%) |
| SOP reference | SOP-016 band above_p90; rework_trigger RW-DOC |
| Preventable by | S3 receipt verification |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T01115; 10 events: EV0006889, EV0006890, EV0006891, EV0006892, EV0006893, EV0006894, EV0006895, EV0006896, EV0006897, EV0006898 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.97,
  "actual_duration_h": 4.05,
  "duration_ratio": 2.06,
  "baseline_p90_h": 3.16,
  "components_actual_vs_expected_h": {
    "queue": [
      0.18,
      0.13
    ],
    "executor_processing": [
      0.68,
      0.35
    ],
    "rework": [
      1.53,
      0.0
    ],
    "approval_wait": [
      1.2,
      0.13
    ],
    "dependency_wait": [
      0.45,
      1.12
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
    "assignee_week_expected_effort_h": 4.97,
    "assignee_typical_week_effort_h": 5.0,
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
      1.65,
      0.89
    ],
    "conformance_fitness": 0.8333
  }
}
```
</details>

### `DEV-0086` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01153 (Finance) |
| Severity / classification / confidence | medium / process / medium |
| Measured | total_duration_h: observed 5.3, expected 3.0, ratio 1.77 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 5.3h vs an expected 3.0h (1.77x). 53% of the extra time is attributed to: approval wait at incharge stage. |
| Most likely reason | Approval wait at Incharge stage |
| Ranked candidate causes | Approval wait at Incharge stage (53%); Rework after rejection (Required document missing) (47%); High assignee workload that week |
| SOP reference | SOP-015 band within |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01153; 8 events: EV0007129, EV0007130, EV0007131, EV0007132, EV0007133, EV0007134, EV0007135, EV0007136 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.0,
  "actual_duration_h": 5.3,
  "duration_ratio": 1.77,
  "baseline_p90_h": 5.45,
  "components_actual_vs_expected_h": {
    "queue": [
      0.15,
      0.15
    ],
    "executor_processing": [
      0.62,
      0.65
    ],
    "rework": [
      1.18,
      0.0
    ],
    "approval_wait": [
      2.27,
      0.95
    ],
    "dependency_wait": [
      1.08,
      1.17
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
    "assignee_week_expected_effort_h": 14.95,
    "assignee_typical_week_effort_h": 7.97,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-015",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.12,
    "sop_p10_p90_h": [
      3.78,
      6.46
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.35,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0087` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01159 (Procurement) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 4.95, expected 2.73, ratio 1.81 |
| Compared with | BL-v1:L2:BOQ Review:Medium:Low |
| What happened | BOQ Review (Medium, Low) took 5.0h vs an expected 2.7h (1.81x). 54% of the extra time is attributed to: rework after rejection (amount mismatch). |
| Most likely reason | Rework after rejection (Amount mismatch); preventable by S4 totals formula check |
| Ranked candidate causes | Rework after rejection (Amount mismatch) (54%); Approval wait at Incharge stage (30%); Cross-team / dependency wait (15%); Assignment queue delay (0%) |
| SOP reference | SOP-013 band within; rework_trigger RW-AMT |
| Preventable by | S4 totals formula check |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T01159; 8 events: EV0007169, EV0007170, EV0007171, EV0007172, EV0007173, EV0007174, EV0007175, EV0007176 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.73,
  "actual_duration_h": 4.95,
  "duration_ratio": 1.81,
  "baseline_p90_h": 4.07,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.13
    ],
    "executor_processing": [
      0.6,
      0.67
    ],
    "rework": [
      1.23,
      0.0
    ],
    "approval_wait": [
      1.6,
      0.92
    ],
    "dependency_wait": [
      1.38,
      1.03
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
    "assignee_week_expected_effort_h": 24.72,
    "assignee_typical_week_effort_h": 22.28,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-013",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.89,
    "sop_p10_p90_h": [
      4.57,
      7.21
    ],
    "first_decision_wait_actual_vs_sop_h": [
      2.98,
      3.65
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0088` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01166 (Operations) |
| Severity / classification / confidence | high / rework / high |
| Measured | total_duration_h: observed 3.27, expected 1.01, ratio 3.24 |
| Compared with | BL-v1:L2:Daily Operations Report:Simple:Medium |
| What happened | Daily Operations Report (Simple, Medium) took 3.3h vs an expected 1.0h (3.24x). 78% of the extra time is attributed to: rework after rejection (incorrect category). |
| Most likely reason | Rework after rejection (Incorrect category); preventable by S4 downtime reason coding |
| Ranked candidate causes | Rework after rejection (Incorrect category) (78%); Approval wait at Incharge stage (14%); Wait after DependencyWait event with no declared dependency (likely reviewer queue) (4%); Extended executor processing (2%); Assignment queue delay (1%) |
| SOP reference | SOP-018 band above_p90; rework_trigger RW-CAT |
| Preventable by | S4 downtime reason coding |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T01166; 8 events: EV0007216, EV0007217, EV0007218, EV0007219, EV0007220, EV0007221, EV0007222, EV0007223 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 1.01,
  "actual_duration_h": 3.27,
  "duration_ratio": 3.24,
  "baseline_p90_h": 1.86,
  "components_actual_vs_expected_h": {
    "queue": [
      0.17,
      0.14
    ],
    "executor_processing": [
      0.33,
      0.28
    ],
    "rework": [
      1.83,
      0.0
    ],
    "approval_wait": [
      0.45,
      0.12
    ],
    "dependency_wait": [
      0.48,
      0.38
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
    "assignee_week_expected_effort_h": 8.22,
    "assignee_typical_week_effort_h": 8.56,
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
      0.93,
      0.0
    ],
    "conformance_fitness": 0.6667
  }
}
```
</details>

### `DEV-0089` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01171 (Procurement) |
| Severity / classification / confidence | medium / rework / medium |
| Measured | total_duration_h: observed 5.92, expected 2.73, ratio 2.16 |
| Compared with | BL-v1:L2:BOQ Review:Medium:Low |
| What happened | BOQ Review (Medium, Low) took 5.9h vs an expected 2.7h (2.16x). 55% of the extra time is attributed to: rework after rejection (incorrect category). |
| Most likely reason | Rework after rejection (Incorrect category); preventable by S2 item-code mapping |
| Ranked candidate causes | Rework after rejection (Incorrect category) (55%); Approval wait at Incharge stage (45%); Assignment queue delay (0%); Cross-team / dependency wait (0%) |
| SOP reference | SOP-013 band within; rework_trigger RW-CAT |
| Preventable by | S2 item-code mapping |
| Reason source | baseline+sop |
| Recommended investigation | Review rejection reasons and submission checklist for this task type. |
| Source records | 1 tickets: T01171; 9 events: EV0007244, EV0007245, EV0007246, EV0007247, EV0007248, EV0007249, EV0007250, EV0007251, EV0007252 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 2.73,
  "actual_duration_h": 5.92,
  "duration_ratio": 2.16,
  "baseline_p90_h": 4.07,
  "components_actual_vs_expected_h": {
    "queue": [
      0.13,
      0.13
    ],
    "executor_processing": [
      0.52,
      0.67
    ],
    "rework": [
      1.83,
      0.0
    ],
    "approval_wait": [
      2.4,
      0.92
    ],
    "dependency_wait": [
      1.03,
      1.03
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
    "assignee_week_expected_effort_h": 27.82,
    "assignee_typical_week_effort_h": 22.28,
    "complexity_controlled": "baseline uses same task type, complexity and priority (where n allows)",
    "leave": "leave/absence data not available in this dataset"
  },
  "sop_comparison": {
    "sop_id": "SOP-013",
    "sop_band": "within",
    "sop_expected_elapsed_h": 5.89,
    "sop_p10_p90_h": [
      4.57,
      7.21
    ],
    "first_decision_wait_actual_vs_sop_h": [
      3.43,
      3.65
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>

### `DEV-0090` TICKET_DURATION

| field | value |
|---|---|
| Entity | T01189 (Finance) |
| Severity / classification / confidence | medium / process / high |
| Measured | total_duration_h: observed 6.68, expected 3.0, ratio 2.23 |
| Compared with | BL-v1:L2:Invoice Verification:Medium:Low |
| What happened | Invoice Verification (Medium, Low) took 6.7h vs an expected 3.0h (2.23x). 92% of the extra time is attributed to: cross-team / dependency wait. |
| Most likely reason | Cross-team / dependency wait |
| Ranked candidate causes | Cross-team / dependency wait (92%); Approval wait at Incharge stage (8%) |
| SOP reference | SOP-015 band above_p90 |
| Preventable by | - |
| Reason source | baseline+sop |
| Recommended investigation | Review the approval/dependency queue for this task type; not an executor issue. |
| Source records | 1 tickets: T01189; 5 events: EV0007357, EV0007358, EV0007359, EV0007360, EV0007361 |

<details><summary>Evidence (JSON)</summary>

```json
{
  "expected_duration_h": 3.0,
  "actual_duration_h": 6.68,
  "duration_ratio": 2.23,
  "baseline_p90_h": 5.45,
  "components_actual_vs_expected_h": {
    "queue": [
      0.07,
      0.15
    ],
    "executor_processing": [
      0.5,
      0.65
    ],
    "rework": [
      0.0,
      0.0
    ],
    "approval_wait": [
      1.28,
      0.95
    ],
    "dependency_wait": [
      4.83,
      1.17
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
    "assignee_week_expected_effort_h": 6.0,
    "assignee_typical_week_effort_h": 8.02,
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
      6.12,
      3.4
    ],
    "conformance_fitness": 1.0
  }
}
```
</details>
