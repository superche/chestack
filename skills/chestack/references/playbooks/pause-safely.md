# pause-safely

**Use for:** The user asks to stop or pause.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Stop starting new work. Interrupt owned workers if supported and requested scope requires it.
2. Preserve local changes, active process identities, branches, current heads, evidence paths, and pending gates.
3. Pause only schedules within the user request and verify their state.
4. Write a short resume brief with the last verified state and next safe step.

**Principles:** [prove-it-works](../principles/prove-it-works.md).

**Done:** The work is recoverable and no owned autonomous continuation contradicts the pause request.
