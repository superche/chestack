# multi-phase-plan

**Use for:** A requested plan spanning phases or PRs.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Read the [planning guide](../planning.md). Scale the plan to the task; for a small clear request, give a short outcome and done condition.
2. For ambiguous intent, multiple acceptance conditions or owners, cross-environment delivery, or changed scope, read the [requirements and acceptance contract](../requirements/contract.md). Establish intent, scenarios, scope/non-goals, target, responsibility boundaries, dependencies, and unresolved questions in the existing task or plan.
3. Resolve factual unknowns with bounded read-only probes or an authorized isolated experiment. Record observed results and limits. Keep product decisions explicit and continue work independent of pending decisions.
4. Write ordered phases with scope, dependencies, implementation shape, acceptance predicates, verification, risks, and recovery. Map requirements to acceptance conditions and their owning phases; include proof of the final outcome across phase boundaries.
5. Run the structural plan checker if shell is available. Review coverage and semantic feasibility separately. Mark missing prerequisites and dependent work explicitly; checker success is not an execution result.
6. Deliver the plan and evidence limits. Implement only when the user also authorized implementation. During execution or scope changes, maintain acceptance links and evidence validity using the contract.

**Principles:** [foundational-thinking](../principles/foundational-thinking.md), [sequence-verifiable-units](../principles/sequence-verifiable-units.md).

**Done:** Every in-scope requirement has an observable acceptance condition and an owning phase with a feasible probe or an explicit blocker. Unresolved facts and product decisions stay visible. Plan delivery and implementation completion are separate outcomes.
