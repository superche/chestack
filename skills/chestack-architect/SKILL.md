---
name: chestack-architect
description: "Design caller-facing interfaces, data ownership, types, and state transitions before implementation; deliver an implementable design package and revise it when implementation disproves its assumptions."
---

# CheStack Architect

Read the [host contract](../chestack/references/hosts.md). Own the structural design and its consistency with caller behavior. A design request produces a sketch and rationale; implementation proceeds only within the user's requested outcome. For a known local change, a caller example, invariant, and acceptance probe are enough.

## Establish the design boundary

1. Consume the existing task's goal, scope, acceptance predicates, target revision/environment, owners, dependencies, evidence, and open questions. Use the [requirements contract](../chestack/references/requirements/contract.md) for missing or conflicting inputs; preserve its identifiers rather than defining another requirements format.
2. Reuse current [How](../chestack-how/SKILL.md) findings or read that skill to trace the affected caller-to-result and failure paths. Use [Why](../chestack-why/SKILL.md) when an existing ownership boundary, defensive behavior, or historical decision constrains the design. Retain their evidence limits; do not repeat an already current investigation.
3. State preserved invariants and the boundary allowed to change. For greenfield work, inspect integration constraints. If observed behavior already meets the goal, recommend no implementation change with evidence. Resolve a missing fact or product choice before it determines a consequential structural decision.

## Derive the shape from use

4. Write the caller's usage first: input, operation, result, and meaningful failure/recovery. Include another consumer when its needs differ. For UI or operational work, use the equivalent action-to-result flow.
5. Derive the data structures, signatures, module ownership, validation boundaries, and state transitions. Trace dominant access patterns through them. Mark sketches as unimplemented and keep them outside production code unless scaffolding is part of the request.
6. Screen the design for callers coordinating internal stages, leaked representation details, duplicated state or policy, pass-through layers, and manually synchronized facts. Explain necessary exceptions. Prefer an interface that hides substantial policy while leaving callers a small coherent operation.
7. For a consequential structural fork, use [Arena](../chestack-arena/SKILL.md) with the grounded task and caller examples. Compare different ownership, representation, or boundary choices, including the current approach when viable. For one factual uncertainty use [Prototype](../chestack/references/playbooks/prototype.md); use [Explore](../chestack-explore/SKILL.md) when choosing the problem direction itself remains the work. When producing one candidate for an enclosing Arena run, return that candidate without starting another comparison; the enclosing run owns alternatives and synthesis. Avoid creating alternatives solely to fill a table.

## Deliver and maintain the design

8. Produce a proportional [design package](references/package.md): caller usage and shape must agree, each accepted tradeoff has a reason, and the first implementation step has a pass predicate. An explicit user checkpoint remains pending; otherwise continue authorized implementation after the choice is supported.
9. At a changed public boundary or failed acceptance check, compare the implementation with the package. Classify deviations as local refinement, contract change, or structural contradiction using the package's revision procedure. Repeated workarounds or a disproved hard premise trigger renewed grounding and design, not silent compatibility layers.

**Done:** The design makes callers, ownership, invariants, decisive evidence, remaining risks, and the next verifiable step explicit. Design completion is distinct from implemented or accepted behavior.
