# Write a tutorial

Use [Diátaxis tutorials](https://diataxis.fr/tutorials/) as the structural basis. Serve a beginner learning through a successful practical experience. Name the artifact they will produce; select one reliable path with an early visible result. Introduce concepts when needed and link extended explanation outside the steps.

State prerequisites, starting directory, literal values versus placeholders, checkpoints, and cleanup. Execute the commands in an authorized isolated workspace and compare output with the promised result. Review with the [editorial workflow](revision.md).

**Done:** a reader at the stated starting level can reach and recognize the promised result without unexplained choices. Unrun platform checks remain explicit.

## Worked example

The following Chinese sample uses the actual CheStack CLI. Adapt facts and prerequisites to the target product; do not copy this structure mechanically.

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
