---
name: chestack-deslop
description: "Remove unnecessary code introduced by the current change while preserving behavior and repository conventions."
---

# CheStack Deslop

1. Read the [host contract](../chestack/references/hosts.md). Resolve the intended base and current diff; preserve unrelated user changes. Use the repository's actual default branch or the user-provided base.
2. Read surrounding code before editing. Find additions that increase complexity without serving the requested behavior: redundant comments, unnecessary wrappers, repeated guards inside trusted boundaries, broad catch blocks hiding defects, unsafe type assertions, and avoidable nesting.
3. Remove or simplify only changes supported by the local contract. Keep validation at trust boundaries, recovery behavior, public API documentation, legal notices, and verified external constraints. A defensive check is not redundant merely because it looks verbose.
4. Prefer focused edits and early returns where local style supports them. If cleanup would change behavior, separate that finding and obtain the authorization required for the behavior change.
5. Review the resulting diff and run checks appropriate to the affected contract. For runtime behavior use [verification](../chestack/references/verification.md). Stop when further edits would be speculative or outside scope.

Return a concise result: what complexity was removed, behavior checks, and remaining concrete issues. Avoid a narrated editing history.
