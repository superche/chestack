# hillclimb

**Use for:** Repeated optimization toward a measured target.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Define the target, time or iteration budget, regression gates, and stop rule.
2. Build and validate a sensitive measurement harness; freeze the workload and preserve baseline samples.
3. Run one hypothesis per isolated candidate. Keep or revert after measurement and correctness checks; log every decision.
4. On a plateau test a different premise. Stop at the agreed bound and report the best verified candidate plus rejected hypotheses.

**Principles:** [build-the-lever](../principles/build-the-lever.md), [explain-the-number](../principles/explain-the-number.md), [attack-the-premise](../principles/attack-the-premise.md).

**Done:** A retained candidate is repeatably measured, regression-safe, and tied to its exact revision.
