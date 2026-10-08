# shipping

**Use for:** The user explicitly requests merge or release.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Resolve the exact repository, PR, current head, destination, and authorization scope.
2. Verify required checks, reviews, unresolved threads, mergeability, and dependencies at that head. A stale prior report is insufficient.
3. Merge only the authorized verified change with the forge supported expected-head guard; stop on changed head or unknown gates.
4. Read back merge status and resulting commit. Deploy only if separately authorized; verify the deployed artifact before claiming rollout.

**Principles:** [prove-it-works](../principles/prove-it-works.md), [sequence-verifiable-units](../principles/sequence-verifiable-units.md).

**Done:** Report merged, deployed, and accepted as separate observed states.
