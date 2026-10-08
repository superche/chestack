# prototype

**Use for:** A factual design uncertainty.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Name the uncertainty, target version/environment, budget, and observation that selects an approach. Reuse the task's acceptance predicates.
2. Build the smallest throwaway experiment that exposes it; isolate it from production code. A single probe can answer one factual question without a candidate competition.
3. For a structural choice, read [candidate comparison](../design/candidates.md), then compare materially different shapes using identical inputs and criteria. Retain commands, outputs, failures, and limits.
4. Recommend a direction, or report that the evidence is inconclusive and name the next discriminating probe. State which prototype assumptions still need production validation; update an existing [design package](../design/package.md) with the result.

**Principles:** [exhaust-the-design-space](../principles/exhaust-the-design-space.md), [experience-first](../principles/experience-first.md).

**Done:** The experiment answers the named uncertainty or identifies the precise unresolved evidence. A prototype is not reported as production-ready.
