# Worked examples for four reader needs

Read the section matching the requested document. The Chinese samples use the real CheStack `plan-check` interface; instructions outside the samples explain how to adapt and review them. They are examples, not a universal page template. For a different product, replace the source facts and rerun the relevant checks. These examples do not claim ASD-STE100 conformance.

## Tutorial sample: create and check a first plan

### 检查你的第一份计划

你将创建一份最小计划，并确认它具备检查器要求的结构。检查器不会执行计划，也不会判断任务是否可行。

准备 Python 3.10 或更高版本，以及一份包含 `skills/chestack/scripts/chestack.py` 的 CheStack 源码。以下命令适用于提供 `sh`、`mktemp` 和 `cat` 的 macOS 或 Linux 终端。从 CheStack 源码根目录开始。

1. 创建独立练习目录，并记录检查器位置。

   ```sh
   chestack_cli="$PWD/skills/chestack/scripts/chestack.py"
   writing_example_dir=$(mktemp -d)
   cd "$writing_example_dir"
   ```

   练习文件将保存在临时目录中。

2. 创建 `plan.md`。

   ```sh
   cat > plan.md <<'PLAN'
   # Goal
   创建一份本地文本报告。
   # Scope
   只处理 report.txt。
   # Constraints
   不覆盖已有文件。
   # Phases
   ## Phase 1: 创建报告
   Scope: 写入 report.txt。
   Dependencies: 无。
   Acceptance: report.txt 包含一行“完成”。
   Verification: 读取 report.txt 并核对内容。
   # Risks
   目标文件可能已存在。
   # Recovery
   删除本次新建的 report.txt。
   PLAN
   ```

   现在目录中有一份包含目标、范围和阶段信息的计划。

3. 检查计划结构。

   ```sh
   python3 "$chestack_cli" plan-check plan.md
   ```

   预期退出码为 `0`。输出中的 `valid_structure` 为 `true`，`errors` 是空数组。目录中不会因此出现 `report.txt`，因为这个命令只读取并检查计划。

   如果出现 `missing or empty` 错误，根据错误中的名称检查相应标题或字段是否为空，再运行同一命令。保留示例中的英文标题与字段名，内容可以使用中文。

4. 完成练习后，删除练习文件并退出临时目录。

   ```sh
   rm plan.md
   cd ..
   rmdir "$writing_example_dir"
   ```

   如果目录非空，`rmdir` 会拒绝删除。检查剩余文件，不要为了清理练习而递归删除未知内容。

Author review: run the exact shell blocks in sequence from a fresh checkout-root shell. Inspect the JSON and directory contents. Check the prerequisites on the target platform; a macOS run does not establish Linux execution.

## How-to sample: repair a missing acceptance field

### 修复计划中的 Acceptance 缺失错误

适用情况：运行 `plan-check` 后，输出包含 `Phase 1: missing or empty Acceptance`，命令退出码为 `1`。你需要知道第一阶段的预期结果；如果结果尚未确定，先确定结果，再修改计划。

以下命令从 CheStack 源码根目录运行，假设待修复文件为该目录中的 `plan.md`。如果使用其他文件，替换命令中的路径。修改前保存原内容，以便恢复。

1. 在 `plan.md` 中找到 `# Phases` 下的 `## Phase 1:` 段落。
2. 在该阶段正文中添加或补全 `Acceptance:` 行。填写可以检查的结果，例如：

   ```text
   Acceptance: report.txt 包含一行“完成”。
   ```

   仅当这个结果符合实际任务时使用该内容。字段必须在代码块外，不能只写在示例中。

3. 重新检查文件。

   ```sh
   python3 skills/chestack/scripts/chestack.py plan-check plan.md
   ```

   如果输出为 `valid_structure: true` 且退出码为 `0`，结构检查通过。如果仍有错误，按 `errors` 中的项目继续修正。

如果填写了错误的验收条件，恢复保存的原内容，再与任务要求核对。结构检查通过后，还需要按计划执行验证，才能确认任务结果。

Author review: create a plan with an empty Acceptance line, observe the reported error, perform the repair, and rerun. Also place the field only in a fenced example and confirm that this does not satisfy the field requirement.

## Reference sample: look up the checker contract

### `plan-check` 命令参考

范围：CheStack 的计划结构检查器。下表描述该命令，不覆盖其他子命令。

```text
python3 skills/chestack/scripts/chestack.py plan-check PATH
```

| 项目 | 契约 |
|---|---|
| `PATH` | 必填的位置参数，指向 UTF-8 文本文件；没有默认路径 |
| 工作目录 | 相对路径以进程当前工作目录为基准 |
| 必需一级标题 | `Goal`、`Scope`、`Constraints`、`Phases`、`Risks`、`Recovery`；各节必须有内容 |
| 阶段 | `Phases` 内至少有一个 `## Phase N: title`；编号从 1 连续递增 |
| 阶段字段 | `Scope:`、`Dependencies:`、`Acceptance:`、`Verification:`；各字段的同行值必须非空 |
| 代码块 | 代码块中的模板不作为已填写的计划内容；未闭合代码块属于结构错误 |
| 占位符 | 代码块外的 `TODO`、`TBD`、`FIXME` 单词或尖括号占位内容会触发错误 |
| 标准输出 | 可读取的输入返回 JSON，包含 `valid_structure`、`errors`、`scope` |
| 退出码 `0` | 结构检查通过 |
| 退出码 `1` | 文件已读取，但结构检查失败 |
| 退出码 `2` | 参数解析错误，或文件读取/解码等处理失败；参数错误为终端诊断，捕获的文件错误为标准错误上的 JSON |
| 副作用 | 此命令不执行计划，不创建计划中的产物，也不改写计划文件 |
| 限制 | 不判断验收条件是否合理、计划能否执行或实现是否正确 |

空文件产生结构错误，不等于缺少 `PATH` 参数。不存在的文件产生读取错误，不等于计划的结构错误。

Author review: compare entries against the current CLI parser and checker implementation. Exercise valid, empty, missing-file, and missing-argument inputs. Do not infer all exit-code behavior from one successful run.

## Explanation sample: understand the validation boundary

### 为什么结构检查通过后，仍要验证执行结果

`plan-check` 检查计划是否提供了约定的栏目和阶段字段。它不执行这些字段中的指令。

例如，计划可以写明创建 `report.txt`，并要求文件中包含“完成”。检查器读取计划文本，排除代码块中的示例，再检查标题、阶段编号、必需字段和占位内容。字段满足结构要求时，它返回通过。

这个过程没有创建报告，也没有读取报告来确认内容。因此，结构通过只说明计划提供了检查器要求的内容。即使 `Acceptance:` 写了一个非空但无法衡量的目标，结构检查也可能通过。

这条边界让我们区分两项工作：结构检查帮助发现遗漏；执行后的验证确认结果是否满足要求。两者回答不同的问题。若目标是确认报告已经生成，需要实际创建报告，再读取文件核对内容。

从当前实现可以确认检查器的范围有限。把这种设计解释为减少执行副作用，是对当前机制的分析；没有历史决策记录时，不能声称这就是作者最初选择该设计的原因。

Author review: trace the implementation and one valid input. Then use a nonempty but unmeasurable Acceptance value to demonstrate the boundary. Verify that no report file is created; do not treat that observation as evidence of historical intent.
