# worktree-cleanup

**Use for:** Inspect or clean development worktrees.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Inventory worktrees through git and record paths, branch, dirty state, merge status, and active task or process ownership.
2. Classify candidates with evidence; unknown ownership or uncommitted work requires preservation.
3. Present destructive deletions for the authorization required by the current session. Use the host managed-worktree archive API for host-created worktrees.
4. Remove only the approved inactive targets and verify both repository state and recovered space.

**Principles:** [prove-it-works](../principles/prove-it-works.md), [build-the-lever](../principles/build-the-lever.md).

**Done:** Only authorized inactive worktrees were removed; evidence and recovery paths remain available.
