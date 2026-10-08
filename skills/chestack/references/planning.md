# Plans with executable acceptance

Use the following headings for plans checked by `plan-check`:

```markdown
# Goal
The observable result.
# Scope
Included work and explicit exclusions.
# Constraints
User, repository, capability, and rollout constraints.
# Phases
## Phase 1: A bounded unit
Scope: files or behavior owned by this unit.
Dependencies: none, or named preceding phases.
Acceptance: observable pass/fail condition.
Verification: exact command or user-flow probe and required environment.
# Risks
Unresolved assumptions and the probes that will settle them.
# Recovery
How to resume, revert an owned change, or recover partial progress.
```

Run `python3 scripts/chestack.py plan-check PATH` from the main skill directory. This validates headings and nonempty fields, not feasibility, tool access, correctness, or successful execution. Review those separately. A plan request alone does not authorize executing the plan.
