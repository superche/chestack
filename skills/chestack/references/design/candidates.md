# Compare candidates and make a decision

Read this for a consequential structural fork or an explicit candidate comparison. Work sequentially unless delegation is both useful and allowed by the [delegation contract](../delegation.md).

## Frame a fair comparison

Use the same task contract, grounded sources, environment, representative inputs, and effort boundary for every candidate. Separate hard acceptance gates from preferences before evaluating results. Choose a small set of criteria that can discriminate this decision, such as:

- Caller correctness: normal, invalid, retry, and recovery behavior required by the task.
- Ownership and invariants: where validation and state transitions live; whether two actors can disagree.
- Interface depth: how much policy the interface hides, and what callers must still coordinate or know.
- Change cost: affected consumers, migration/rollback boundary, dependencies, and operational cost.
- Performance or resource limits only where required, measured with the same method.

For each criterion name an observable check or source. Hard-gate failure disqualifies a candidate regardless of preference scores. Unknown decisive evidence remains unknown; an attractive sketch cannot earn a measured result.

## Sketch and probe

Produce at least two structurally different shapes for a material fork: different ownership, data representation, boundary, or execution model, not renamed wrappers around the same design. Include the current approach or a smaller change when viable. If constraints force one viable shape, record the concrete alternative eliminated by those constraints.

For each option derive types, signatures, state transitions, and a module map from caller usage. State which invariants the structure enforces and which need runtime checks. Keep sketches separate from production code; mark incomplete bodies explicitly.

Screen for caller orchestration of internal stages, leaked storage/transport details, duplicated state ownership or policy, pass-through layers, and manually synchronized facts. Explain any necessary exception. Prefer a boundary that lets a maintainer change one policy without coordinating unrelated callers.

Use a [bounded prototype](../playbooks/prototype.md) when a decisive fact cannot be settled by inspection. Name the hypothesis, pass/fail observation, inputs, and budget first. Preserve results and scope limits. A failed or missing candidate run is a gap, not a vote for the survivor; obtain the missing evidence or make the decision explicitly provisional.

## Synthesize

Read every completed candidate and compare criterion by criterion. Record pass, fail, or unknown for hard gates and evidence-backed tradeoffs for preferences. Resolve disagreements against evidence; if they reveal incompatible task interpretations, reframe the brief before combining designs.

Select one coherent base. Record useful ideas adopted from each alternative and those rejected, with reasons. A hybrid is a new candidate: reconcile its ownership and caller contract, then rerun affected checks and all hard acceptance gates before treating it as validated. If options converge, record that and avoid a gratuitous hybrid.

Return the decision in a [design package](package.md), including the evidence that would overturn it. Distinguish your sequential evaluation from any actually executed independent review.
