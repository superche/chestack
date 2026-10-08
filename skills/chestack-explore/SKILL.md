---
name: chestack-explore
description: "Explore an unclear problem or approach through bounded investigation and experiments. Deliver a supported proposal, experiment, or demo with unresolved production work; do not treat exploration as a production implementation request."
---

# CheStack Explore

Read the [host contract](../chestack/references/hosts.md). This composition chooses the investigation and experiment needed to make a decision. Its output is a proposal, experiment, or demo; production implementation is a separate outcome requiring corresponding user intent.

## Frame the decision

1. Name the decision, user outcome, constraints, and uncertainty that prevents choosing. Read the [requirements contract](../chestack/references/requirements/contract.md) when intent, scope, acceptance, or ownership is ambiguous. Separate observable facts from product choices. If the direction is already settled and the user wants implementation, route to [Feature](../chestack/references/playbooks/feature.md) within that authorization.
2. Bound effort, experiment side effects, and the stopping condition using the user's constraints and task size. State material assumptions and the evidence that could disprove them. A short question needs a short exploration; a multi-stage inquiry needs explicit phases. A budget ending with an unresolved question is an honest incomplete result.

## Investigate and test

3. Use [How](../chestack-how/SKILL.md) to establish current behavior and [Why](../chestack-why/SKILL.md) when prior decisions constrain the options. Reuse current findings. When source evidence settles the question, deliver the proposal without manufacturing a demo.
4. Compare materially different plausible options against the same criteria using [Compare and Combine](../chestack-compare-and-combine/SKILL.md) when candidate evaluation and synthesis are needed. Include keeping the current approach when it is viable. Eliminate options with evidence; do not invent a second candidate merely to fill a table.
5. For remaining factual uncertainty, follow [Prototype](../chestack/references/playbooks/prototype.md). State the hypothesis and deciding observation before building. Use isolated scratch state, safe fixtures, a bounded run, and the real surface relevant to that question. When reporting measurements, follow the [measurement guide](../chestack/references/measurement.md); a toy workload does not establish production performance.
6. Observe the result, keep or reject the hypothesis, and revise the next experiment accordingly. If a pass comes too easily, check that the probe distinguishes the candidates and did not bypass the uncertain behavior. Keep short decision/evidence notes; for a long inquiry use the [operations guide](../chestack/references/operations.md). Stop when the decision is supported, needs a product choice, or reaches its effort/capability boundary.

## Deliver the appropriate artifact

Return the decision and recommendation, compared options, supporting observations, limitations, and unresolved questions. For an experiment or demo, also give the artifact location, exact launch/use instructions, prerequisites, cleanup, and the paths actually exercised. If it was not run, label it unverified.

Name the production work still required: relevant compatibility, failure handling, security, performance, integration, or rollout checks. Include only applicable gaps. A demo's successful run does not satisfy those checks. Preserve the evidence during cleanup. Readiness to choose a direction and readiness to ship are separate conclusions.

**Done:** the decision has usable evidence or a precise unresolved blocker, and the artifact is labeled at its actual maturity. Do not keep building merely to turn an exploratory result into a production deliverable.
