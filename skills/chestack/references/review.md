# Review changes and their effects

1. Fix the review boundary: base revision, head revision, touched files, and intended behavior. Preserve local user changes.
2. Trace changed contracts into callers, configuration, persisted data, authorization boundaries, and recovery paths. A small diff can have a large impact outside itself.
3. For each suspected defect, establish a reachable trigger and a concrete bad outcome. Prefer a reproducer or focused probe; label unexecuted reasoning.
4. Check whether tests exercise actual behavior and would detect the defect. Distinguish a correctness requirement from stylistic preference.
5. Recheck the relevant source before returning findings. Report severity, exact location, trigger, consequence, and evidence. Do not invent findings to fill a quota.

## Focused lenses

- **Adversarial review:** choose different failure hypotheses such as API compatibility, state concurrency, user behavior, and test blind spots. Independent reviewers follow [delegation](delegation.md). The lead verifies findings and resolves disagreements against source or experiments.
- **Blast radius:** inspect importers, callers, serialized formats, flags, and deployment order beyond the diff. Prove the safety assumption that makes the change bounded.
- **Comments:** keep legal notices, public contracts, and verified non-obvious external constraints. Convert misleading internal narration into clearer names or structure only within the authorized scope. A comment-only review does not authorize rewriting application code.
- **Types:** parse external data, model legal states, exhaust variants, derive schemas, and examine assertions that suppress real uncertainty.

If no actionable findings remain, say so and give the reviewed scope plus any untested boundary. A review verdict is neither passing CI nor merge authorization.
