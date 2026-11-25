# Corporate SOP Dataset

Synthetic SOP documents for the Process Intelligence prototype. They are not actual corporate policy.

| Files | Format | Used by the pipeline |
|---|---|---|
| `SOP_SCHEMA.md` | Schema v1.2 specification | Reference for authors and code |
| `SOP-013` … `SOP-021` | YAML front matter + ISO 9001 body (schema v1.2) | **Yes.** One per task type: parsed, validated, parameterised and used for conformance checks |
| `SOP-001` … `SOP-012` | Legacy free text | **No.** Kept unchanged for reference. SOP-002/003/004 are superseded by SOP-014/015/016 |

The legacy SOPs share identical body text apart from their titles, so they carry no task-specific
information. All standard times and quality targets in SOP-013..021 are illustrative values for
synthetic data (`standard_time_source: illustrative_expert_estimate`, `quality_targets_source: unconfirmed`).
