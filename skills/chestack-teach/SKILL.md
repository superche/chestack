---
name: chestack-teach
description: "Teach a subsystem, change, or concept by combining grounded how and why findings into an explanation matched to the reader. Use for onboarding and requests to really understand, not to implement."
---

# CheStack Teach

Read the [host contract](../chestack/references/hosts.md). This composition combines [How](../chestack-how/SKILL.md), [Why](../chestack-why/SKILL.md), and the [writing guide](../chestack/references/writing.md). Read the needed skill files and execute their procedures with current capabilities; references do not require nested tool invocation or separate agents.

1. Infer the reader's purpose and existing knowledge from the request: changing, reviewing, debugging, or learning. Choose the few things they need to understand. Ask only when a missing audience or goal would materially change the explanation; do not quiz them before helping.
2. Build or reuse a current How trace. Use Why for the decisions and tradeoffs needed to explain it. A small mechanical change may need only How; a historical question may need primarily Why. Preserve citations, target, and confidence when reusing findings. Neither path requires an exhaustive unrelated investigation.
3. Explain the thing in familiar terms, then walk one concrete input through the system. Introduce domain terms at the point they become useful. Connect the mechanism to the problem it solves; distinguish a verified historical reason from a present-day benefit you infer.
4. Layer detail around the reader's question. Use a diagram or before/after example when it reduces effort, adding complexity only as needed. A list of symbols is reference material, not an explanation of their relationships.
5. Answer at the requested depth. In conversation, give a complete first layer and follow the reader's next question; in a requested standalone tutorial, finish the tutorial rather than artificially stopping. Preserve meaningful uncertainty and link paths for deeper inspection.

**Return:** the explanation itself, with a concrete example, necessary tradeoffs, and material gaps. Do not return a report about running How and Why. Do not claim understanding was demonstrated unless the reader actually demonstrated it.

**Done:** the requested concept can be followed from input to outcome, at the intended depth, without replacing uncertain rationale with a tidy story. Teaching does not authorize implementation.
