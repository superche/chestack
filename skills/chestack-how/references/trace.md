# Trace across boundaries

Use this procedure when a local reading cannot account for the requested behavior. Work sequentially unless authorized delegation earns its cost; each slice uses the same evidence contract.

## Establish the target

Record checkout/revision and relevant uncommitted changes. If reporting a run, identify the actual executable/build, process or service, configuration and input. A checked-out branch does not identify an already-running process. If runtime identity is unavailable, retain the observation but leave its connection to the source unverified.

Partition by responsibility: request validation, scheduling, state ownership, persistence, execution, or presentation as applicable. Assign each boundary once and reconcile shared interfaces. Directory names and identical type names do not prove ownership or a connection.

## Follow one input

For each material boundary, retain:

| Field | Evidence to collect |
|---|---|
| Trigger and input | Public caller, concrete input values/shape, applicable configuration |
| Transformation | Implementation/symbol and how values or state change |
| Owner | Who creates, mutates, persists and disposes the state; distinguish a proxy or view |
| Output and next edge | Return/event/write, consumer, correlation identifier or adapter connecting them |
| Failure | Propagation, retry/cancellation, cleanup and partial state visible to the caller |
| Evidence | Revision + file/symbol/lines, or command/observation + actual runtime identity |
| Open edge | Missing implementation, ambiguous dispatch, inaccessible dependency or unexecuted branch |

Inspect both sides of dispatch/serialization boundaries. A producer and a consumer with similar names are insufficient: check routing, registration, version/configuration and data conversion. Trace only failure/alternate branches that affect the user's question. Tests describe expected behavior until an actual run demonstrates it.

## Reconcile before explaining

When findings disagree, reopen the exact caller, implementation and configuration at the claimed revision. Separate different versions, feature flags, runtime targets and success/failure paths before treating findings as contradictory. Recheck a disputed edge against original source; counting agreeing summaries does not resolve it. If a relevant connection remains inaccessible, show the unresolved edge in the explanation.

Return one causal model, with evidence close to each consequential claim. Carry target identity, boundary ownership, observed versus source-derived behavior, unresolved edges and the next discriminating check into any Teach or Why handoff. A narrow answer may use a paragraph; the table is a collection aid, not a mandatory final format.
