---
name: chestack-verify
description: "Verify real behavior, create a project-local verification skill and feature map, or maintain an existing verification harness against source and live behavior."
---

# CheStack Verify

Read the [host contract](../chestack/references/hosts.md) and [verification standard](../chestack/references/verification.md). Identify the target revision, requested outcome, and available execution surface.

Choose the requested mode; ordinary verification does not authorize installing or rewriting a skill:

| Request | Procedure |
|---|---|
| Prove a change or reproduce a behavior | Use the verification standard and the project's existing recipe. Select checks for the claim and report uncovered entry points. |
| Create a reusable verification skill or fill a missing harness | Read [Create](references/create.md), then the [feature-map contract](references/feature-map.md). |
| Audit or update an existing verification skill | Read [Maintain](references/maintain.md), then the feature-map contract. |

For numerical comparisons, read the [measurement guide](../chestack/references/measurement.md). A source walkthrough, an executed check, and complete feature coverage are separate evidence states.
