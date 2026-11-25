"""Central configuration: paths, vocabularies, mappings and prototype thresholds.

Every threshold here is a *demonstration* value for synthetic data, not a
production rule. Change them here, never inline in the pipeline code.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
OUTPUT_DIR = ROOT / "outputs"
SOP_DIR = ROOT / "corporate_sops"

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"  # timestamps are naive; assumed single local timezone

REQUIRED_COLUMNS = {
    "employees": ["employee_id", "employee_name", "department", "role", "reporting_to", "active_status"],
    "tickets": [
        "ticket_id", "task_type", "department", "assigned_employee_id", "priority", "complexity",
        "sop_steps", "approval_count", "dependency_count", "created_at", "due_at", "completed_at",
        "final_status",
    ],
    "audit_logs": [
        "event_id", "ticket_id", "employee_id", "action", "timestamp", "stage",
        "previous_status", "new_status", "change_type", "details",
    ],
    "task_types": ["task_type", "department", "complexity", "sop_steps", "approval_count", "dependency_count"],
}

# Hierarchy, lowest to highest.
ROLE_LEVELS = {"Executor": 1, "Incharge": 2, "Lead": 3, "HOD": 4}
COMPLEXITY_LEVELS = ["Simple", "Medium", "Complex"]
PRIORITY_LEVELS = ["Low", "Medium", "High"]
COMPLETED_STATUSES = {"Completed", "Completed_Late"}

# Raw action name (lower-cased, spaces/underscores stripped) -> canonical event type.
# Includes aliases that other platform exports are likely to use.
EVENT_TYPE_MAP = {
    "created": "CREATED",
    "assigned": "ASSIGNED",
    "reassigned": "REASSIGNED",
    "updated": "UPDATED",
    "edit": "UPDATED",
    "submitted": "SUBMITTED",
    "submittedforapproval": "SUBMITTED",
    "resubmitted": "RESUBMITTED",
    "rejected": "REJECTED",
    "sendback": "REJECTED",
    "approved": "APPROVED",
    "approvedbymanager": "APPROVED",
    "dependencywait": "DEPENDENCY_WAIT",
    "escalated": "ESCALATED",
    "reopened": "REOPENED",
    "closed": "CLOSED",
    "cancelled": "CANCELLED",
    "canceled": "CANCELLED",
}
UNKNOWN_EVENT_TYPE = "UNKNOWN"

# ---- SOPs (schema v1.2, see corporate_sops/SOP_SCHEMA.md) --------------------
SOP_SCHEMA_VERSION = "1.2"
SOP_FILE_GLOB = "SOP-*.md"           # legacy SOP-001..012 have no front matter and are listed, not parsed
SLA_HOURS = {"High": 6, "Medium": 12, "Low": 24}
# Fixed rejection vocabulary observed on the platform; rework_triggers.reason must use these strings.
PLATFORM_REJECTION_REASONS = ["Amount mismatch", "Incorrect category", "Required document missing", "Wrong quantity"]

# Complexity score CS-v1 (schema §6). Weights are a hypothesis, tested by Spearman rho each run.
CS_VERSION = "CS-v1"
CS_WEIGHTS = {"steps": 1.0, "appr_base": 2.0, "appr_cond": 1.0, "dep": 2.5, "decision": 1.5,
              "driver": 1.0, "exception": 0.5, "skill": 1.0}
CS_BANDS = (12.0, 20.0)               # < 12 Simple, 12-20 Medium, > 20 Complex
Z_P10_P90 = 1.2816                    # normal quantile for the P10-P90 band

# Effort coverage (schema §8): aggregated only, task type x month
EFFORT_COVERAGE_MIN_N = 20
EFFORT_COVERAGE_HIGH = 1.0            # above: SOP effort exceeds the observed upper bound
EFFORT_COVERAGE_LOW = 0.5             # below: holding includes much non-SOP time

# SOP-log correspondence gate (stage 3b): is the logged process the one the SOP describes?
CORRESPONDENCE_MIN = 0.95             # share of tickets replayable on the SOP model -> corresponds
CORRESPONDENCE_PARTIAL = 0.80         # below this the SOP is excluded from stages 4-6
CORRESPONDENCE_TIME_RANGE = (0.25, 4.0)  # observed median / SOP expected must be the same order of magnitude

# SOP-based process deviations
CONFORMANCE_MIN_SHARE = 0.05          # share of a task type's tickets failing a check
CONFORMANCE_MIN_N = 5
SOP_BAND_TAIL_SHARE = 0.20            # > 20% of tickets above P90 (or below P10); 10% expected
REWORK_SOP_MULTIPLIER = 1.25          # observed rejection rate vs (1 - expected FPY)
REWORK_SOP_MIN_COUNT = 5

# ---- Baselines -------------------------------------------------------------
BASELINE_VERSION = "BL-v1"
MIN_BASELINE_N = 20  # min tickets for a baseline group to be used

# ---- Deviation thresholds (prototype) ---------------------------------------
DURATION_RATIO_THRESHOLD = 1.75       # ticket duration / baseline median
DURATION_RATIO_HIGH = 2.5             # severity = high above this
DOMINANT_SHARE_HIGH_CONF = 0.6        # dominant cause share of excess time -> high confidence
DOMINANT_SHARE_MED_CONF = 0.4

# Persistent employee-level processing deviation (monthly periods)
PERSIST_PERIOD = "M"
PERSIST_MIN_TICKETS_PER_PERIOD = 5
PERSIST_RATIO_THRESHOLD = 1.0         # floor: slower than the typical colleague on the same task type (v2: was
                                      # 1.25, which missed a real 1.4x slowdown from a below-typical start)
PERSIST_P_VALUE = 1e-4               # one-sided Mann-Whitney: window tickets vs own baseline tickets
PERSIST_MIN_VOLUME_SHARE = 0.5        # months with < 50% of the person's median monthly volume are not judged
PERSIST_MIN_PERIODS = 2               # consecutive periods raised, anywhere in the data (v2: was most-recent only)
PERSIST_SELF_CHANGE = 1.2             # period level vs the employee's own previous normal months

# Time-windowed detectors (v2): each series is compared with its OWN previous normal months
WINDOW_BASELINE_PERIODS = 6           # baseline = last 6 unflagged months
WINDOW_MIN_HISTORY_PERIODS = 2        # need at least 2 months of history before anything is flagged
WINDOW_MIN_RUN = 2                    # a process signal must last 2+ consecutive months
WAIT_INCREASE_MIN_N = 15              # tickets per department-month
WAIT_INCREASE_RATIO = 1.5             # monthly median approver wait vs own baseline
WAIT_INCREASE_MIN_H = 0.5             # ... and at least 0.5h longer
SLA_DROP_MIN_N = 20
REWORK_MIN_N = 20                     # tickets per task-type month
REWORK_INCREASE_FACTOR = 2.0          # monthly rejection rate vs own baseline
REWORK_INCREASE_PTS = 0.05            # ... and at least 5 points higher
REWORK_P_VALUE = 1e-4                 # one-sided Fisher exact; ~200 tests per run, so Bonferroni-style
SLA_DROP_PTS = 0.07                   # monthly SLA compliance 7+ points below own baseline

# Context checks used to decide whether a persistent deviation is "explained"
CONTEXT_WORKLOAD_INCREASE = 1.3       # recent expected-effort per period vs own earlier
CONTEXT_REJECTION_INCREASE_PTS = 0.10 # rejection rate increase (absolute)
CONTEXT_COMPLEXITY_SHIFT_PTS = 0.15   # increase in share of Complex tickets (absolute)

# Employee rejection-rate deviation
REJECTION_RATE_MULTIPLIER = 2.0
REJECTION_MIN_COUNT = 4

# Process bottleneck at a decision stage
BOTTLENECK_MIN_N = 20
BOTTLENECK_RATIO_THRESHOLD = 1.3      # dept stage wait vs org-wide wait for same stage & dependency count
BOTTLENECK_HIGH = 2.0
