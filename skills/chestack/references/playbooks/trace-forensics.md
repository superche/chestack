# trace-forensics

**Use for:** A supplied trace, profile, heap, or log artifact.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Identify artifact format, capture conditions, and the question it can actually answer.
2. Parse the artifact with suitable tools, keeping raw data out of the main context when a targeted query suffices.
3. Connect the significant frames or events to the matching code revision.
4. Report findings, capture limitations, and the next discriminating measurement.

**Principles:** [guard-the-context-window](../principles/guard-the-context-window.md), [explain-the-number](../principles/explain-the-number.md).

**Done:** Every finding has an artifact location and is bounded by the capture conditions.
