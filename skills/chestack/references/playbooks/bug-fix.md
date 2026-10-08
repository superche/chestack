# bug-fix

**Use for:** An observed defect.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Capture the failing input and reproduce on the affected surface. If access is missing, preserve the reproducer and report that gap.
2. Trace the earliest incorrect state and its owner; inspect persistent state for restart-related failures.
3. Add a focused failing test when it provides a cheap stable reproducer; avoid manufacturing a large test harness for a small defect.
4. Apply the root-cause fix, rerun the original reproducer, and check related callers and negative cases.

**Principles:** [fix-root-causes](../principles/fix-root-causes.md), [test-behavior-not-implementation](../principles/test-behavior-not-implementation.md), [prove-it-works](../principles/prove-it-works.md).

**Done:** Before/after evidence exists for the original symptom, or the report explicitly remains unverified.
