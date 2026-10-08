# runtime-forensics

**Use for:** A live resource leak, spin, hang, or intermittent failure.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Identify the actual target process, revision, environment, and symptom.
2. Capture a bounded profile, heap snapshot, or trace using an available authorized control tool.
3. Reduce the artifact to a hot path, ownership chain, or state transition; test a competing explanation.
4. Return the diagnosis and evidence; implement a fix only if the user requested one.

**Principles:** [fix-root-causes](../principles/fix-root-causes.md), [guard-the-context-window](../principles/guard-the-context-window.md).

**Done:** The diagnosis points to concrete runtime evidence and states unresolved causality.
