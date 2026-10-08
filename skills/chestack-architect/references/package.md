# Design package and revision

Use this record for a material design handoff or when implementation challenges a chosen shape. Keep it next to the task's existing design artifacts, at an authorized path. A short inline record is sufficient for a small decision; omit inapplicable sections with a reason rather than filling boilerplate.

## Package contents

- **Task anchor:** Link the existing goal/scope and acceptance predicates, target revision/environment, responsibility boundaries, dependencies, evidence, and unresolved questions. Reuse their identifiers; record assumption changes at their source when authorized.
- **Grounded behavior:** Caller-to-result trace, affected state owners, preserved invariants, and documented versus inferred constraints, with source pointers.
- **Caller usage:** The operation, expected result, and relevant failure/recovery examples written before the internal sketch.
- **Shape:** Data structures, signatures, module ownership, transitions, validation boundaries, and dependencies. Explain what the interface hides and what callers still need to know. Mark sketches as unimplemented.
- **Decision:** Candidates, shared criteria, gate outcomes and evidence, selected base, adopted ideas, rejected ideas, and accepted tradeoffs. Label provisional choices and absent or failed evaluations.
- **Delivery boundary:** Consumer migration, compatibility and rollback needs, implementation order, and the first verifiable step. Identify the owner of work outside this task's scope without silently assigning it.
- **Open evidence:** Remaining questions and risks, their effect on acceptance, and the observation that resolves each. Separate tests run from source inspection and proposed checks.

**Handoff complete:** Another implementer can derive the first change and its pass predicate without guessing ownership or caller semantics. This is a design completion condition, not production acceptance.

## Implementation feedback

Compare implementation against the package at a changed public boundary or a failed acceptance check. Record a meaningful deviation with the original assumption, new evidence, affected callers/invariants, and decision:

- **Local refinement:** The change preserves the contract and ownership. Update the sketch and rerun affected acceptance checks.
- **Contract or dependency change:** Update the relevant task source within authority, or return the unresolved decision to its owner. Keep dependent work pending while progressing independent work.
- **Structural contradiction:** Stop extending the affected shape and revisit its grounding and candidates.

Repeated workarounds across unrelated callers, multiple writers where one owner was assumed, callers depending on hidden ordering, or types repeatedly escaping their invariants are redesign signals. A directly disproved hard premise is sufficient on its own; ordinary edge cases need judgment, not an automatic restart.

For redesign, trace the implemented behavior again, treat the newly discovered constraint as a starting assumption, and compare a simpler replacement with the cost of preserving the current shape. Bound migration and rollback before replacing working code. Update the decision and invalidate evidence tied to the old revision or assumptions; rerun the relevant probes on the new shape.
