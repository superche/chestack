# Write an explanation

Use [Diátaxis explanation](https://diataxis.fr/explanation/) as the structural basis. Answer a bounded understanding question with context, relationships, constraints, and relevant alternatives. Let the reader's question determine depth.

For technical behavior, read [How](../../../chestack-how/SKILL.md); for historical intent, read [Why](../../../chestack-why/SKILL.md). Reuse current findings with their target, evidence, and confidence. Start with a plain definition, then connect one concrete input to its outcome and a relevant edge case. Use a diagram when it clarifies relationships. Keep historical rationale distinct from present-day benefits you infer.

Deliver a requested standalone explanation in full. For conversational teaching, layer detail around the reader's questions without forcing quizzes or artificial pauses. Apply the [editorial workflow](revision.md), especially causal claims and uncertainty.

**Done:** the reader can follow the requested mechanism and tradeoffs from the explanation; do not claim demonstrated comprehension without reader evidence.

## Worked example

This sample uses the actual CheStack checker to explain a boundary, without claiming to reconstruct its author's intent.

### 为什么结构检查通过后，仍要验证执行结果

`plan-check` 检查计划是否提供了约定的栏目和阶段字段。它不执行这些字段中的指令。

例如，计划可以写明创建 `report.txt`，并要求文件中包含“完成”。检查器读取计划文本，排除代码块中的示例，再检查标题、阶段编号、必需字段和占位内容。字段满足结构要求时，它返回通过。

这个过程没有创建报告，也没有读取报告来确认内容。因此，结构通过只说明计划提供了检查器要求的内容。即使 `Acceptance:` 写了一个非空但无法衡量的目标，结构检查也可能通过。

这条边界让我们区分两项工作：结构检查帮助发现遗漏；执行后的验证确认结果是否满足要求。两者回答不同的问题。若目标是确认报告已经生成，需要实际创建报告，再读取文件核对内容。

从当前实现可以确认检查器的范围有限。把这种设计解释为减少执行副作用，是对当前机制的分析；没有历史决策记录时，不能声称这就是作者最初选择该设计的原因。

Author review: trace the implementation and one valid input. Then use a nonempty but unmeasurable Acceptance value to demonstrate the boundary. Verify that no report file is created; do not treat that observation as evidence of historical intent.
