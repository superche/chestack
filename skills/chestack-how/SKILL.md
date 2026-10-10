---
name: chestack-how
description: "Trace current behavior and architecture from source when asked how a subsystem, API, state transition, or code path works. Distinguish source-derived behavior from runtime observations."
---

# CheStack How

Read the [host contract](../chestack/references/hosts.md). Keep an explanation request read-only. Inherit the current model; a separate explorer is optional and follows the [delegation contract](../chestack/references/delegation.md).

## Trace the behavior

1. Pin the question, target revision/runtime, entry point, and depth needed by the caller. For one function, stay local. For a subsystem, partition by actual responsibility and interface; naming directories alone is not an architecture model. For cross-module paths, disputed findings, or runtime/source mismatch, read [boundary tracing](references/trace.md). Stay on the local path when it settles the question.
2. Follow one representative input from its public entry to the result. Read implementations and callers, data shapes, state owners, persistence, and relevant configuration. Track transformations and transitions; distinguish who owns data from who happens to pass it along.
3. Trace a meaningful failure or alternate path that changes the answer: rejection, cancellation, retry, cleanup, or unavailable dependency. Inspect the tests as evidence of intended behavior; a test name is not evidence of execution.
4. Resolve uncertain connections with the smallest authorized observation. Label source analysis separately from an actual run and identify the observed target. If a call crosses unavailable code or a private service, name the unresolved edge instead of guessing.
5. Reconcile conflicting findings against source and target identity. Stop when the path and relevant failure boundary are accounted for, or return the exact gap that prevents doing so.

## Return a usable model

Lead with what the system does. Explain the causal sequence, the few domain objects and owners needed to follow it, and the result/failure boundary. Link the supporting files or runtime evidence near each material claim. Add a small diagram only when it clarifies relationships; avoid a catalog of every function.

For reuse by another skill, retain the question, target, traced path, ownership, observations versus source deductions, citations, and unresolved edges. This can remain in the current response; a separate document is optional.

Historical motivation belongs to [Why](../chestack-why/SKILL.md). Route there only when the question needs intent; plausible implementation benefits do not establish why an author chose it.

**Done:** the explanation accounts for the requested behavior and material failure paths with source pointers and honest observation limits. It does not imply code changes or production acceptance.
