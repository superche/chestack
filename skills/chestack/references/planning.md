# Plans with executable acceptance

For a small clear task, state the outcome and a checkable done condition in the task conversation. Create a multi-phase plan when dependencies, ownership, uncertainty, or delivery stages need coordination, or when the user requests one.

For ambiguous intent, multiple acceptance conditions or owners, cross-environment delivery, or changed scope, read the [requirements and acceptance contract](requirements/contract.md). Keep its record inside the plan or link the existing authoritative record. Resolve factual unknowns with bounded probes; expose product choices and blocked work.

## Compatible plan format

Use the following headings for plans checked by `plan-check`. Keep the four phase field labels on their own lines with nonempty values. Additional detail can follow them.

```markdown
# Goal
The observable result and its source of intent.
# Scope
Included requirements and explicit exclusions.
# Constraints
User, repository, capability, ownership, and target-environment constraints.
# Phases
## Phase 1: A bounded unit
Scope: files or behavior owned by this unit; related requirement IDs when used.
Dependencies: none, or named artifacts, decisions, and preceding phases.
Acceptance: observable pass/fail conditions; acceptance IDs when used.
Verification: exact command or user-flow probe, required environment, and evidence to capture.
# Risks
Unresolved facts, choices, or assumptions; their impact, resolver, and blocked work.
# Recovery
How to resume, revert an owned change, or recover partial progress.
```

For larger plans, add the requirement/acceptance mapping under Scope, target and responsibility details under Constraints, and unresolved questions under Risks. Put phase-specific probes and evidence under the corresponding phase. Preserve the six top-level headings and consecutive `## Phase N: title` headings; no new checker syntax is required.

## Review before handoff

1. Trace each in-scope requirement to a scenario and acceptance predicate. Assign every predicate to a phase, including the final cross-phase outcome when component checks are insufficient.
2. Check dependency order, ownership boundaries, available tools, test data, target identity, and recovery. Name the exact condition preventing an infeasible phase from starting.
3. Run `python3 scripts/chestack.py plan-check PATH` from the main skill directory. This validates headings and nonempty fields, not feasibility, coverage, tool access, correctness, or successful execution. Review those separately.
4. Deliver the plan with settled facts, pending decisions, and evidence still needed. A plan request alone does not authorize executing the plan. Use implementation authorization already provided without asking again.

When requirements change or results arrive, apply the contract's change and closure rules to the affected phases. Keep planned checks distinct from observed results.
