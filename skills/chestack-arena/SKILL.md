---
name: chestack-arena
description: "Compare candidate designs, implementations, or artifacts under shared criteria; choose a coherent base, synthesize useful alternatives, and verify the resulting artifact."
---

# CheStack Arena

Read the [host contract](../chestack/references/hosts.md). Own comparison and synthesis, not the decision to expand product scope. Accept existing candidates or generate bounded alternatives. Inherit the current model; use separate workers only when useful and permitted by the [delegation contract](../chestack/references/delegation.md). Sequential passes are valid and must be labeled as such.

## Frame and isolate

1. Pin the requested artifact, task contract, target/environment, common inputs, permitted side effects, and effort boundary. Reuse [requirements](../chestack/references/requirements/contract.md) and supplied grounding. Freeze the comparison criteria before seeing results: hard acceptance gates first, then a small set of observable preferences. Tie each criterion to a check or source, not a holistic impression.
2. Give candidates the same task and constraints, with separate output locations and exclusive write ownership. Use separate worktrees for code when appropriate or scratch directories for sketches. Prefer materially different approaches; for design compare ownership, representation, or boundaries, using [Architect](../chestack-architect/SKILL.md) for design production. Reuse supplied candidates after checking their target and task compatibility. A single viable result is not evidence of a successful comparison.
3. Produce or inspect each candidate with its rationale, assumptions, evidence, and rejected alternatives. Keep candidate outputs separate until evaluation. Record dropouts and incomplete runs; obtain decisive missing evidence or make the selection provisional. Do not reward the only candidate that happened to finish.

## Evaluate and synthesize

4. Read every completed artifact. Apply identical inputs and checks, recording pass, fail, or unknown for hard gates and evidence-backed tradeoffs for preferences. A hard-gate failure cannot be offset by a preference score. Unknown decisive evidence stays unresolved. If authorized independent review is useful, start it after artifacts stabilize and provide the criteria and artifacts without a preferred verdict; otherwise perform a labeled sequential review.
5. Select a coherent base and explain the decisive evidence. Resolve reviewer disagreement against sources and checks. If candidates interpreted the task differently, reframe before combining them. If all candidates fail, return the failed predicates and the next discriminating change rather than declaring a winner.
6. Revisit the alternatives for useful parts. Record what is adopted and rejected and why. Integrate by reconciling assumptions and ownership, not mechanically merging outputs. Convergence may justify keeping the base unchanged; synthesis does not require a graft.
7. Treat a synthesized artifact as a new candidate. Rerun all hard gates and checks affected by the graft on the actual final artifact. Use the [verification guide](../chestack/references/verification.md) for evidence and [measurement](../chestack/references/measurement.md) for numerical claims. If only sketches were reviewed, report design-level support and unexecuted runtime checks. A failed final check returns to the responsible assumption or integration choice.

## Return the decision

Deliver the final artifact or its path plus the shared criteria, candidate outcomes, base, adopted/rejected parts, missing candidates, final verification, and evidence that would overturn the choice. Preserve the task's acceptance identifiers. For a design, this record belongs in Architect's existing package; other artifacts use a compact synthesis note. Do not create a separate record merely to duplicate one.

**Done:** The selected or synthesized artifact has evidence at the requested level, or the exact unresolved gates are reported. Candidate quality, synthesis verification, and independent review are separate claims.
