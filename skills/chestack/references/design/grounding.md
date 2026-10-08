# Ground the design

Read this before a material design choice. Use the [explanation guide](../explain.md) for how/why investigations; retain the design-relevant findings here rather than duplicating the full explanation.

1. Anchor observations to the target revision and environment. Locate an actual caller or user entry point, domain types, state owners, dependencies, and externally visible result. Read implementations and relevant tests, not just filenames or signatures.
2. Trace one representative input across the affected boundaries: who validates it, changes state, invokes dependencies, and returns the result? Trace a relevant failure or recovery path as well. Record concrete file/symbol pointers and any untraced edge. Distinguish source-inferred behavior from executed observations.
3. When changing an existing boundary or defensive behavior, investigate its rationale using history and available authorized records. Mark each material constraint as documented, inferred, or unknown, with its source. Current code demonstrates mechanics; it does not establish original intent. Keep conflicting sources visible. Record unavailable sources and the consequence of the gap instead of inventing a reason.
4. Write the caller's desired usage before internal types: inputs, operation, result, and how failure is handled. Include the dominant path and a meaningful adverse case; add a second consumer when it would reveal conflicting needs. For UI or operational work, use the equivalent action-to-result flow.
5. Identify what must stay stable, what may change, and who owns each affected state or decision. Expose compatibility, migration, permission, and external dependency constraints that can eliminate a candidate.

If observed behavior already satisfies the requested outcome, report that evidence and recommend no implementation change. Resolve any remaining semantic difference before designing an extra interface.

**Ready to sketch:** A reader can trace the caller to the result, locate each affected owner, and distinguish verified facts from assumptions. An unresolved question names the candidate or acceptance predicate it may invalidate and the next evidence needed. For a new system, integration constraints serve as the baseline.
