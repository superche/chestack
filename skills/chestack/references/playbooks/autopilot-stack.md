# autopilot-stack

**Use for:** A root owner manages an ordered stack.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Write the stack order, per-PR scope, dependencies, and acceptance gates.
2. Keep one root owner for stack topology. Build and verify each slice before adding dependent work.
3. Check the lowest unmerged frontier first; batch upper-stack observations without repeatedly restarting the frontier.
4. Use babysit for readiness and shipping for authorized landing. Re-verify affected slices after any restack.

**Principles:** [sequence-verifiable-units](../principles/sequence-verifiable-units.md), [prove-it-works](../principles/prove-it-works.md).

**Done:** The contiguous verified frontier is explicit and no upper change silently collapses its review boundary.
