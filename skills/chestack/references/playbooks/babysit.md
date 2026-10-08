# babysit

**Use for:** Check or drive a PR toward merge readiness.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Choose check (one snapshot), threads-only (review comments), or drive (bounded fix-and-check loop) from the request.
2. Read the [GitHub guide](../github.md). Resolve head SHA, conflicts, draft state, review decision, required checks, and unresolved review threads.
3. Classify findings against the code. Fix authorized issues on the owning branch, batch a coherent push, and re-read state after the new head.
4. Stop at merge-ready, a real user gate, or the run bound. Schedule future checks only when requested and supported.

**Principles:** [fix-root-causes](../principles/fix-root-causes.md), [prove-it-works](../principles/prove-it-works.md).

**Done:** A fresh readiness report distinguishes required blockers from optional checks; this workflow never grants merge authorization.
