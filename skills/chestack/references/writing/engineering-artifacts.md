# Write for an engineering decision

Use the repository's template when present. Include only the sections needed for the decision; the criteria below do not require a fixed outline.

## Pull request

The reviewer needs to understand the final problem, behavior change, evidence, and risk. Inspect the final diff before writing. Use a concrete trigger and before/after behavior when that makes the change clear. Explain a surprising implementation choice only when it helps review.

Report checks actually run and their scope. Separate local checks, CI, review, merge, deployment, and client acceptance. Link lengthy evidence instead of pasting a work log. State material compatibility or rollout limits and any unverified behavior. Replace stale descriptions when the final scope changes.

Done means the description matches the current diff and gives the reviewer enough evidence to assess it. Writing a body does not authorize publishing it. For authorized delivery, follow [GitHub guidance](../github.md); use a body file or structured arguments for multiline prose.

## RFC

The reader must make a decision that is still open. State the decision sought, the problem, relevant constraints, and success criteria. Describe the proposed behavior, credible alternatives including keeping the current behavior when viable, and the tradeoff behind the recommendation.

Separate observed facts, assumptions, and estimates. Identify unresolved questions that could change the choice and how to resolve them. Include compatibility, adoption, rollback, and validation plans when the proposal changes those concerns. Present planned tests as plans, not results. A prototype supports only the properties it actually exercised.

Done means the reader can compare alternatives against the same criteria and knows what remains undecided. A recommendation is not an approved decision.

## Decision record

Record an actual decision, its status, constraints, rationale, and consequences. Cite the decision source when available. If approval is unknown, label the record proposed or unconfirmed instead of inventing agreement. Link an RFC for extended alternatives rather than duplicating it.

Done means a later reader can identify what was decided, why, and the conditions that would justify reconsidering it.

## Commit message

State the specific change and its reason at the scale of the commit. Add a body when the motivation or compatibility consequence is not clear from the diff. Follow local conventions and keep validation claims proportional to evidence. A commit message is not the PR's full review packet.

## Example: preserve the evidence state

Hypothetical source facts: a patch rejects negative timeouts; a local unit test passes; CI has not run.

Before:

> This comprehensive hardening guarantees reliable timeout handling and is fully verified for production.

After, for a PR:

> Reject negative timeouts before starting the request. The local unit test covers rejection of `-1`; CI and deployment have not been verified.

For an RFC on the same idea, use proposal language and define the intended check:

> Reject negative timeouts before starting the request. Validate this behavior with a boundary test for `-1` and confirm that zero retains its current behavior before adoption.

The PR describes a change and observed evidence. The RFC asks for a decision and names future validation.
