# Confidence calibration examples

Use the tier definitions in [synthesis](synthesis.md). These fictional examples show how evidence changes the claim; cite real originals in actual answers. Grade the specific claim, not the number of documents. Unknown is the answerability state of a question and can coexist with a speculative candidate.

## Explicit motive, unmeasured outcome

材料：同期 PR 写“采用队列，避免发送失败时丢失请求”；没有上线或效果记录。

可说：“PR 明确把保留失败请求列为动机（Direct）。实际是否降低丢失率，现有材料无法判断（Unknown）。”

不能把“作者想解决”合并成“已经解决”。后续实测若确认效果，只提升效果主张，不改变原始意图记录的性质。

## Supported versus Inferred

材料：同期独立事故记录显示上传内存耗尽；关联需求列出内存预算；补丁将整批读取改为流式读取，并新增对应峰值内存测试。没有一句话明确说出整体选型理由，也未发现其他动机线索。

可说：“事故、需求与实现变化共同指向控制内存占用（Supported）；这是对多种证据的综合判断，非作者原话。”三者各贡献故障、约束和响应，仍应说明检索范围及未排除的替代解释。

若只有流式代码和一项测试，可说：“这一实现可能用于减少峰值内存（Inferred），但缺少把实现与历史决策连接起来的记录。”若只有一个名称相似的函数，连这条推断也不足；只能作为待查线索。

## Inferred versus Speculative, with Unknown

材料：超时上限从 8 秒改为 12 秒；同日关联事故显示请求在 9–11 秒完成，没有明确选值说明。

可说：“延长上限可能是为了容纳当时较慢的请求（Inferred），时间与现象支持这一解释，但决策联系未被明确记录。为何恰好取 12 秒仍 Unknown。”

若仅有 `timeout = 12`，可说：“可能留了余量（Speculative），但没有区分经验值、上游限制等解释的证据。”不需要列出无助于用户决定的所有猜测。

## Repeated origins and conflicting Direct records

材料：一条评审写“为降低延迟”；发布摘要与周报都转述它。另一份同期已接受设计写“为失败恢复”；没有替代决定。

可说：“降低延迟是评审中的明确说法，失败恢复是设计中的明确说法（各自 Direct）。转述不增加独立支持；不能据文档数量或最近日期选出唯一动机（Unknown）。”

找到正式替代决定后，可以解释哪项意图在何时生效；仍不能据此证明性能收益。

## Correlation, later repair and measurement changes

材料：后续修复发布后错误数下降，同时采样率降低、错误分组发生变化。

可说：“图表记录的数量下降了，但无法据此确认故障减少或修复有效（Unknown）；需要一致口径的事件/请求分母及发布关联。”

修复 PR 明说“防止重复发送”可作为这次修复意图的 Direct 证据，不能拿来解释两年前为什么最初选择队列。

## Empty, partial and unavailable

材料：一个完整的限定 issue 查询返回零条；聊天无权限；日志只保留最近七天，问题发生于上月。

可说：“该 issue 查询没有找到记录；聊天及目标时段日志不可用。因此不能确定当时没有事故或约束。”如果 issue 结果只有第一页，改为 partial，不能写成完整搜索的空结果。用户给的查询导出需注明为提供的材料，而非本次亲自执行。
