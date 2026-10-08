# perf-issue

**Use for:** An observed latency, throughput, CPU, or memory regression.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Define the metric and reproduce the slow case with a representative workload.
2. Read the measurement guide; record baseline samples, errors, work count, environment, and the suspected limiter.
3. Use a trace to select one cause, change one variable, and compare interleaved baseline/candidate samples.
4. Retain a change only if correctness holds and the measured effect exceeds noise.

**Principles:** [explain-the-number](../principles/explain-the-number.md), [fix-root-causes](../principles/fix-root-causes.md), [prove-it-works](../principles/prove-it-works.md).

**Done:** The claim includes comparable samples and correctness evidence, not only a faster-looking diff.
