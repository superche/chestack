# orchestrate

**Use for:** A multi-track program outlives one worker session.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Define countable completion, units, dependencies, exclusive ownership, and a budget. Collapse to a simpler workflow if one session suffices.
2. Read the delegation guide and create a task-local ledger of units, heads, evidence, blockers, and standing constraints.
3. Pilot one unit through build and independent verification before expanding the work. Spawn only through supported authorized host tools.
4. Drain compact completion reports, reconcile them with live artifacts, and update the ledger. Carry standing constraints into every handoff.
5. Stop spawning in time to consolidate results. Report completed, pending, failed, and user-gated units separately.

**Principles:** [guard-the-context-window](../principles/guard-the-context-window.md), [separate-before-serializing-shared-state](../principles/separate-before-serializing-shared-state.md), [encode-lessons-in-structure](../principles/encode-lessons-in-structure.md).

**Done:** Every claimed completed unit has current evidence; the ledger is bookkeeping, not a scheduler.
