# autopilot-full

**Use for:** Several independently owned PR lifecycles.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Define the units, dependency graph, exclusive branches, acceptance gates, and run bound.
2. Read the delegation guide. Assign an owner and independent verifier per unit when supported and authorized; otherwise execute units sequentially.
3. Each owner builds, verifies, pushes, opens a PR, and reports the current head with evidence. Track completion in a durable ledger.
4. Recheck readiness centrally. Land only when the user authorized it, in dependency order, and record the final state of each unit.

**Principles:** [separate-before-serializing-shared-state](../principles/separate-before-serializing-shared-state.md), [sequence-verifiable-units](../principles/sequence-verifiable-units.md), [prove-it-works](../principles/prove-it-works.md).

**Done:** Each unit has an exact head, verification result, and separately recorded merge state.
