# Design and candidate comparison

Scale design work to the decision. For a local change with a known shape, state the caller's outcome, affected invariant, and acceptance probe, then implement. A competition or separate design document is optional for that path.

For a material change to ownership, interfaces, persistence, or system structure:

1. Consume the existing task's goal, scope, acceptance predicates, version/environment, responsibility boundaries, dependencies, evidence, and unresolved questions. Reference their source; preserve identifiers and mark missing facts or conflicts. This guide does not define a replacement requirements format. Resolve a gap before it determines an irreversible choice; continue independent investigation meanwhile.
2. Before choosing a shape, read [Grounding](design/grounding.md). Trace current behavior and distinguish known rationale from inference. For greenfield work, investigate integration boundaries and mark the absent implementation explicitly.
3. Read [Candidates and decision](design/candidates.md). Write caller usage before interfaces, compare structurally different options against shared criteria, and test only decisive uncertainties.
4. Preserve the chosen sketch and rationale using [Design package and revision](design/package.md). Keep the record proportional to the change and connect implementation evidence back to its acceptance predicates.
5. Implement within the authorized scope. Honor an explicit design checkpoint; otherwise proceed when the choice is supported. Revisit disproved premises using the revision conditions in the package guide.

Use the [delegation contract](delegation.md) only when separate workers are useful and permitted. Inherit the current model. Sequential candidate and evaluation passes are valid; label them accurately rather than claiming an independent panel.

**Done:** The caller's path, chosen shape, decisive evidence, remaining risks, and next implementation or verification step are clear. A sketch is not a tested implementation.
