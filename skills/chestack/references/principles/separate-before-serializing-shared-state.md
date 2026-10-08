# separate-before-serializing-shared-state

**Trigger:** Concurrent workers may mutate one resource.

Give each writer its own branch, worktree, file, or key. Coordinate only the resource whose single ownership is a real invariant.

**Evidence:** Name each writer and its exclusive scope before parallel execution.
