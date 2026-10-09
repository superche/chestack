# Choose the reader's task

Use the dominant reader need to choose the structure. The checks below are completion criteria, not required headings.

| Type | Reader goal | Include | Done when |
|---|---|---|---|
| Tutorial | Learn by completing a first successful example | Starting state, prerequisites, a bounded result, steps with observable checkpoints, cleanup where needed | A learner can follow the chosen path and recognize the result without unstated knowledge |
| How-to | Complete a known task | Conditions, direct actions, meaningful branches, expected result, recovery for likely failures | A competent reader can choose the applicable path and verify success |
| Reference | Look up an exact contract | Inputs, types, defaults, outputs, errors, side effects, limits, version or platform scope where relevant | Each requested item is traceable to the implementation or authoritative source; unknowns are marked |
| Explanation | Understand a mechanism or tradeoff | A plain definition, concrete input-to-result example, causal sequence, constraints, alternatives, uncertainty | The account explains both the observed behavior and the limits of the stated rationale |

## Tutorial and how-to

Select a safe, small example. Put a prerequisite or warning before the step that needs it. Show the working directory, exact command, and expected observable result where ambiguity would prevent execution. Distinguish literal arguments from placeholders. Give a useful recovery action for a likely failure instead of telling the reader to repeat the same step.

For tutorials, keep one reliable route and introduce terms when the learner needs them. For how-to guides, assume the stated prior knowledge and allow branches that solve the reader's actual task. Keep long explanations and full option tables behind links.

Execute documented commands in an authorized isolated workspace when possible. Compare actual output and files with the claimed checkpoints. If execution is unavailable, mark the procedure unverified and name the missing capability. A plausible command is not a tested procedure.

## Reference

Inspect source, schemas, help output, or authoritative documentation before stating defaults and guarantees. Keep terminology consistent with the interface. Explicitly distinguish omitted values, empty values, and invalid values when behavior differs. An example illustrates a contract; it does not establish a guarantee.

Test the relevant boundary where feasible, such as an invalid option or missing input. State scope instead of extrapolating one observed case to every platform or version.

## Explanation and teaching

For source investigation, read [How](../../../chestack-how/SKILL.md) to trace current behavior and [Why](../../../chestack-why/SKILL.md) when the explanation needs historical rationale. Reuse current findings instead of repeating their investigation. Choose depth from the reader's task: onboarding, modifying, debugging, or reviewing. Build the mechanism from evidence, then distinguish recorded rationale from your own inference. Preserve uncertainty about intent even when the implementation is clear.

Start with the smallest complete answer, then add the detail needed for the request. In conversation, let follow-up questions guide further depth; deliver a requested standalone document in full. Use a traced example to connect actions with effects. Use a diagram only when relationships become easier to follow visually, and match its size to the question.

A useful understanding check is whether the explanation predicts a concrete edge case. Include that edge case when it clarifies the mechanism; do not turn every explanation into a quiz.

## One feature, different outputs

For a hypothetical tool that validates a configuration file:

- A tutorial creates a minimal valid file, runs the validator, and shows the successful result.
- A how-to explains how to locate and repair a rejected field in an existing file.
- A reference lists accepted fields, defaults, validation errors, and exit codes supported by the source.
- An explanation traces validation before execution and explains what that ordering protects, with any inferred rationale labeled.

Reuse the verified facts across these artifacts. Change the path through them to match the reader's goal.
