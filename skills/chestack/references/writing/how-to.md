# Write a how-to guide

Use [Diátaxis how-to guides](https://diataxis.fr/how-to-guides/) for structure: address a competent reader's specific task, name that task in the title, and include meaningful branches. Keep background and full lookup tables in linked documents.

Use [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) as the procedure-language basis. Apply these rule references when drafting and reviewing:

| Rule | Review action |
|---|---|
| 5.1 | For English procedural sentences, check the 20-word ceiling with the counting rules in section 8 |
| 5.2 | Separate instructions into sentences; retain the exception for simultaneous actions |
| 5.3 | Give actions as direct commands |
| 5.4 | Put a prerequisite condition before its command, separated by a comma in English |
| 5.5 | Keep notes informational; move instructions, requirements, and limits into the procedure |
| 7.1–7.3 | Where a real hazard exists, identify its level; begin the safety instruction with its preventive command or condition, then explain the risk or result |

Consult [standards and language scope](standards.md) for dictionary checks and formal English conformance. For Chinese, apply the procedure principles in natural Chinese; do not substitute character quotas for English word counts. Preserve code and interface identifiers. A style adaptation does not establish full ASD-STE100 conformance.

State the initial state, dependencies, ordered actions, expected observations, relevant recovery, and stop conditions. Execute the authorized safe path and a meaningful failure path. Review each action and result separately through the [editorial workflow](revision.md).

**Done:** a competent reader can choose the correct branch, complete the task, recognize success, and handle the documented failure without guessing.

## Worked example

The following Chinese procedure applies the structural and applicable language principles above; it is not a formal English conformance example.

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
