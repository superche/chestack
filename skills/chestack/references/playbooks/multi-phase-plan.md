# multi-phase-plan

**Use for:** A requested plan spanning phases or PRs.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. State outcome, non-goals, constraints, and observable acceptance criteria.
2. Resolve factual unknowns with bounded read-only probes; leave genuine product decisions explicit.
3. Write ordered phases with scope, dependencies, implementation shape, verification, risks, and rollback or recovery.
4. Read the planning guide and run the structural plan checker if shell is available. Review semantic feasibility separately.
5. Deliver the plan; implement only when the user also authorized implementation.

**Principles:** [foundational-thinking](../principles/foundational-thinking.md), [sequence-verifiable-units](../principles/sequence-verifiable-units.md).

**Done:** Every phase has a feasible verification method and no placeholder decision is hidden as certainty.
