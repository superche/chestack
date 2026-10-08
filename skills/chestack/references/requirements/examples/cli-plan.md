# Goal
Prove that the local CheStack CLI validates plans without modifying them and records a task-local decision while preserving malformed existing data. Follow the [execution instructions](README.md). This is a repeatable acceptance exercise for the existing commands, not a request to change them.

# Scope
R-PLAN: return the specified structural verdicts for the complete and missing-acceptance fixtures while preserving input bytes.
R-LOG: persist submitted decision values through the public CLI and reject a malformed existing log without mutation.

| Acceptance | Requirement | Scenario and predicate | Verification case | Owning phase |
|---|---|---|---|---|
| A1 | R-PLAN | Complete fixture returns exit 0 and valid_structure true. | plan-valid / plan-cli | 1 |
| A2 | R-PLAN | Missing acceptance returns exit 1 and Phase 1: missing or empty Acceptance. | plan-incomplete / plan-cli | 1 |
| A3 | R-PLAN | Both calls preserve the exact submitted bytes. | plan-readonly / plan-cli | 1 |
| A4 | R-LOG | A fresh log gains exactly one record whose four submitted values match independent file readback and stdout. | log-append, log-readback / log-cli | 2 |
| A5 | R-LOG | Malformed existing JSONL returns exit 2 with Invalid JSONL and preserves all original bytes. | log-corrupt / log-cli | 2 |

Excluded: semantic correctness of arbitrary plans, GUI/TUI behavior, network services, concurrent log writers, append to a valid existing log, merge and deployment. This exercise does not claim complete CLI coverage or evaluate a model's ability to follow instructions.

# Constraints
Run from a CheStack checkout with Python 3.10+ and Git. No network or account is required. Resolve the absolute checkout path and record its commit and working-tree changes before running; reuse the same target throughout one attempt. Use a fresh disposable run directory and one writer.

The executor owns fixtures, command execution, evidence, and cleanup. Review the captured outputs and file readbacks separately before marking acceptance; this can be a sequential self-review and is not independent review. Keep evidence outside disposable state. Each feature probe has a 10-second timeout. No performance or user visual-review gate applies to this batch CLI exercise.

# Phases
## Phase 1: Observe structural validation and input preservation
Scope: R-PLAN; the disposable complete and incomplete plan fixtures only.
Dependencies: resolve the target and complete the baseline in the linked example instructions.
Acceptance: A1, A2, and A3 all pass on the same identified checkout.
Verification: run the existing plan-check feature recipe linked from the example instructions; inspect plan-valid.json and plan-incomplete.json plus the recipe's byte-preservation assertions. Start all results as not-run.

## Phase 2: Observe persistence and rejection
Scope: R-LOG; disposable fresh and malformed log files only.
Dependencies: Phase 1 passes; use the same identified checkout and a healthy owned scratch directory.
Acceptance: A4 and A5 pass; the final evidence matrix accounts for A1 through A5 and retained artifacts remain readable after cleanup.
Verification: run the existing log feature recipe linked from the example instructions; inspect log-append.json and log-corrupt.json, then execute cleanup and verify evidence remains readable. A stdout success without independent file readback cannot satisfy A4.

# Risks
The checkout path and revision are facts to resolve at run time, not assumed values. A missing Python/Git executable or unreadable fixture blocks the dependent phase. No product choice remains open for this fixed exercise. A timeout or assertion failure must retain diagnostics and leave the affected acceptance unresolved.

# Recovery
Always remove only the owned disposable state directory, including after failures; retain evidence. Create a new run directory for each retry and preserve earlier failures. If the target or predicate changes, compare impact and rerun affected checks. Report unmet acceptance conditions without modifying product code to make this exercise pass.
