# Process Intelligence - Summary

_What happened in 1,200 tickets (01 Jun to 25 Sep 2026), compared with the company SOPs. Synthetic demo data. Every flag is a **signal to look into, not a judgment of anyone**._

## At a glance

|  | Result |
|---|---|
| Tickets analysed | 1,200 across 4 departments and 9 task types |
| Data quality | 0 errors, 3 warnings: the data can be trusted |
| SOPs that match the logs | 9 of 9 (each log really is the process its SOP describes) |
| Tickets that follow the SOP route exactly | 58% |
| Tickets finished on time (SLA) | 96% |
| Things flagged | 90: 30 about processes or SOPs, 59 slow tickets, 1 about individuals |

## Main findings

1. **An SOP approval step is never recorded.** Platform never logs HOD approvals (0 HOD approval events in all 1200 tickets). Affects Vendor Onboarding.

2. **Approvals given when the SOP does not ask for them.** Daily Operations Report: Incharge approval logged on every ticket although the SOP requires it only when kpi breach or safety event.

3. **Tickets put on hold where the SOP has no waiting step** (358 tickets). Daily Operations Report 96%, Expense Approval 93%, Leave Approval 96%. The SOP says to reject for missing information instead.

4. **SOP time standards look too high.** 59% of tickets finish faster than the SOP's fastest expected time; in 6 of 9 task types most tickets do (BOQ Review 94%, Employee Document Verification 87%, Incident Review 80%, Invoice Verification 79%, Vendor Onboarding 74%, Daily Operations Report 58%).

5. **Slower than the SOP allows:** Expense Approval (36% of tickets), Leave Approval (52% of tickets), mostly from waiting for the first approval.

6. **More rework than the SOP expects** in 5 task types:

   | Task type | Sent back | SOP expects | Top reason | Check that would prevent it |
   |---|---|---|---|---|
   | Invoice Verification | 13% | 10% | Incorrect category (7) | S4 GL and tax code check |
   | Expense Approval | 8% | 5% | Required document missing (4) | S3 receipt verification |
   | Daily Operations Report | 7% | 5% | Amount mismatch (3) | S3 KPI formula check |
   | Leave Approval | 7% | 5% | Required document missing (4) | S2 certificate check |
   | Employee Document Verification | 14% | 10% | Incorrect category (8) | S2 document type classification |

7. **Approval queues:** Finance tickets wait 1.5x the company average for the Incharge decision (1.4h vs 0.9h); HR tickets wait 1.4x the company average for the Incharge decision (1.3h vs 0.9h). This is a process issue, not the executors'.

8. **On-time delivery is falling.** Operations SLA compliance fell for 3 consecutive months: 96.3% -> 94.3% -> 93.8% -> 88.7%.

9. **59 tickets took at least 1.75x their normal time.** Causes: 36 rework after being sent back, 22 waiting (approvals, holds, dependencies), 1 the work itself.

10. **1 signals about 1 individuals.** Not explained by workload or complexity: E1002. For a private, supportive conversation with context (leave, other duties, tools), never as a rating.

## Where ticket time goes

About **71% of ticket time is waiting**, mostly for approvals, not working. Speeding up approvals helps more than pushing executors.

| Department | Tickets | Working | Waiting | Sent back | On time |
|---|---|---|---|---|---|
| Finance | 279 | 27% | 67% | 10% | 99% |
| HR | 261 | 29% | 65% | 11% | 100% |
| Operations | 257 | 26% | 70% | 12% | 93% |
| Procurement | 403 | 19% | 78% | 11% | 93% |

## Recommended next steps

1. **Platform team:** confirm whether HOD approval happens outside the system or is skipped, and record it if it happens.
2. **Process owner:** set the approval condition on the platform, or update the SOP if approval on every ticket is wanted.
3. **Approvers:** stop using 'on hold' as a queue; reject with a reason when information is missing.
4. **SOP owners:** review the time standards (a short time study). Do not just edit them to match the data.
5. **Team leads:** tighten the checks listed in the rework table, then re-measure.
6. **Department heads:** review approver turnaround in Finance and HR.
7. **Operations head:** review the late tickets together with the queue and individual signals above.

## Keep in mind

- The SOPs took effect after this data period, so the results show how past practice compares with the documented process, not rule breaches.
- SOP time standards and quality targets are illustrative until their owners confirm them.
- Every number can be traced to ticket and event IDs. 10 tickets were re-checked against the raw logs with separate code: 10 of 10 match.

**More detail:** `technical_report.md` (all stages, tables and methods), `deviation_report.md` (every flag with its evidence), and the CSV files in `outputs/`.
