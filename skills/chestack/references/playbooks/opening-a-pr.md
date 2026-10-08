# opening-a-pr

**Use for:** Prepare a reviewable GitHub change.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Confirm the requested owner and repository with gh, inspect git status, and select an isolated existing branch or worktree.
2. Read repository contribution guidance, review the scoped diff, and run required checks on the intended commit.
3. Commit with repository-local identity, push the authorized branch, and create a PR with problem, behavior change, and actual validation evidence. Use --body-file for multiline text.
4. Attach the created PR through the host artifact tool when available. Report the URL, head SHA, CI state, and remaining gates.

**Principles:** [sequence-verifiable-units](../principles/sequence-verifiable-units.md), [prove-it-works](../principles/prove-it-works.md).

**Done:** The PR exists at the reported SHA; opening it does not imply CI, merge, or deployment completion.
