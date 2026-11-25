# Process Intelligence - Summary

_What happened in 4,663 tickets (01 Oct to 01 Oct 2026), compared with the company SOPs. Synthetic demo data. Every flag is a **signal to look into, not a judgment of anyone**._

## At a glance

|  | Result |
|---|---|
| Tickets analysed | 4,663 across 4 departments and 9 task types |
| Data quality | 0 errors, 3 warnings: the data can be trusted |
| SOPs that match the logs | 9 of 9 (each log really is the process its SOP describes) |
| Tickets that follow the SOP route exactly | 64% |
| Tickets finished on time (SLA) | 94% |
| Things flagged | 357: 27 about processes or SOPs, 327 slow tickets, 3 about individuals |

## Main findings

1. **An SOP approval step is never recorded.** Platform never logs HOD approvals (0 HOD approval events in all 4663 tickets). Affects Vendor Onboarding.

2. **Approvals given when the SOP does not ask for them.** Daily Operations Report: Incharge approval logged on every ticket although the SOP requires it only when kpi breach or safety event.

3. **Tickets put on hold where the SOP has no waiting step** (913 tickets). Daily Operations Report 58%, Expense Approval 59%, Leave Approval 59%. The SOP says to reject for missing information instead.

4. **SOP time standards look too high.** 24% of tickets finish faster than the SOP's fastest expected time; in 1 of 9 task types most tickets do (Vendor Onboarding 67%).

5. **Slower than the SOP allows:** Daily Operations Report (77% of tickets), Expense Approval (77% of tickets), Invoice Verification (21% of tickets), Leave Approval (71% of tickets), mostly from waiting for the first approval.

6. **More rework than the SOP expects** in 1 task types:

   | Task type | Sent back | SOP expects | Top reason | Check that would prevent it |
   |---|---|---|---|---|
   | Invoice Verification | 14% | 10% | Incorrect category (21) | S4 GL and tax code check |

7. **Approval waits that rose for a few months:**

   - In 2026-08..2026-09, Daily Operations Report tickets waited a median 1.76h for the Incharge decision vs 1.02h in the months before (1.7x). Likely cause: incharge approver queue for daily operations report (only this task type rose and it has no external dependency).
   - In 2026-02..2026-03, Expense Approval tickets waited a median 4.29h for the Incharge decision vs 1.77h in the months before (2.4x). Likely cause: incharge approver queue shared across finance task types (the same wait rose in Invoice Verification in the same months).
   - In 2026-02..2026-03, Invoice Verification tickets waited a median 5.71h for the Incharge decision vs 3.56h in the months before (1.6x). Likely cause: incharge approver queue shared across finance task types (the same wait rose in Expense Approval in the same months).
   - In 2026-01..2026-02, Vendor Onboarding tickets waited a median 10.55h for the Incharge decision vs 5.02h in the months before (2.1x). Likely cause: dependency wait for vendor onboarding (or its incharge approver) (only this task type rose and it declares external dependencies; the log cannot separate the two).
   - In 2026-08..2026-09, Incident Review tickets waited a median 2.44h for the Lead decision vs 1.25h in the months before (2.0x). Likely cause: lead approver queue for incident review (only this task type rose and it has no external dependency).

8. **327 tickets took at least 1.75x their normal time.** Causes: 291 waiting (approvals, holds, dependencies), 26 the work itself, 10 rework after being sent back.

9. **3 signals about 3 individuals.** Not explained by workload or complexity: E1003. Explained by context (e.g. higher workload): E1013, E1015. For a private, supportive conversation with context (leave, other duties, tools), never as a rating.

## Where ticket time goes

About **74% of ticket time is waiting**, mostly for approvals, not working. Speeding up approvals helps more than pushing executors.

| Department | Tickets | Working | Waiting | Sent back | On time |
|---|---|---|---|---|---|
| Finance | 983 | 24% | 74% | 9% | 97% |
| HR | 1066 | 21% | 77% | 9% | 98% |
| Operations | 1108 | 31% | 67% | 9% | 90% |
| Procurement | 1506 | 23% | 75% | 13% | 92% |

## Recommended next steps

1. **Platform team:** confirm whether HOD approval happens outside the system or is skipped, and record it if it happens.
2. **Process owner:** set the approval condition on the platform, or update the SOP if approval on every ticket is wanted.
3. **Approvers:** stop using 'on hold' as a queue; reject with a reason when information is missing.
4. **SOP owners:** review the time standards (a short time study). Do not just edit them to match the data.
5. **Team leads:** tighten the checks listed in the rework table, then re-measure.
6. **Department heads:** check approver availability for the months listed above.

## Keep in mind

- The SOPs took effect after this data period, so the results show how past practice compares with the documented process, not rule breaches.
- SOP time standards and quality targets are illustrative until their owners confirm them.
- Every number can be traced to ticket and event IDs. 10 tickets were re-checked against the raw logs with separate code: 10 of 10 match.

**More detail:** `technical_report.md` (all stages, tables and methods), `deviation_report.md` (every flag with its evidence), and the CSV files in `outputs/`.
