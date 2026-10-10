---
name: chestack-why
description: "Investigate historical rationale, design decisions, thresholds, regressions, and tradeoffs using source history and authorized records. Separate documented intent from inference and missing evidence."
---

# CheStack Why

Read the [host contract](../chestack/references/hosts.md). Investigate read-only. Treat the user's proposed reason as a hypothesis, not a conclusion. Current code establishes behavior; it does not establish historical intent.

## Anchor the question

1. Name the decision or behavior being explained, its current code/symbol or artifact, and the relevant period. Use [How](../chestack-how/SKILL.md) only if the current mechanism is unclear; narrow its question and reuse an existing current trace.
2. Follow the change lineage through source history, renames, related tests, PRs, and linked records. Read [source investigation](references/sources.md) for the concrete search procedure and source-coverage contract.
3. Record which evidence categories could settle the question and which are available. Search the relevant categories, follow linked evidence, and record empty results, unavailable sources, and justified exclusions. For multiple sources, contested findings or delegated investigation, read [investigation and synthesis roles](references/investigation.md). A small explicit rationale may settle a narrow question; widen when it leaves an important alternative unexplained.
4. Build the chronology and test competing explanations. Distinguish introduction, later repair, and present behavior; a recent edit need not explain the original decision. Preserve contradictions and identify evidence that would distinguish the remaining hypotheses.
5. Calibrate each conclusion against its source. Use the confidence distinctions below and verify material citations before handing off. Stop when the requested rationale is supported or the remaining gap and next discriminating source are clear.

## Confidence and output

Use **Direct / Supported / Inferred / Speculative / Unknown** per claim. Read [confidence and synthesis](references/synthesis.md) before finalizing; it defines the distinctions, citation checks, and reusable evidence contract. A short answer can express these distinctions naturally without five sections.

Lead with the strongest supported answer. Include the chronology only where it explains the decision, then conflicting explanations, gaps, and a compact source-coverage account. Preserve uncertainty when another skill reuses the result. Never turn an absence of records into proof that no constraint existed.

When this investigation informs a change, translate findings into **preserve / change candidate / avoid / unresolved risk**, with supporting records. This is a planning input, not authorization to implement or contact people.

**Done:** each claimed motivation has appropriately qualified evidence; unanswered parts remain explicit. A user-suggested explanation is accepted only if the record supports it.
