# Source history and review

**Use when:** tracing the introduction or evolution of a behavior, symbol or constraint.

**Seed:** repository/revision, observed paths and symbols, decision period, known commit/PR IDs. Record shallow or snapshot-only coverage before interpreting missing history.

## Establish the lineage

Start with the relevant path and symbols. In a Git checkout, use bounded commands such as `git blame -L START,END -- PATH`, `git log --follow -p -- PATH`, and `git log --format=fuller -- PATH`. Replace the arguments with the observed path/range. Follow rename history and the introduction of the behavior, not only the latest touch. Read related callers/tests and original patches before attributing intent. Use `git log -S 'EXACT_TEXT' -p -- PATH` to locate changes in occurrence count, or `git log -G 'PATTERN' -p -- PATH` for matching changed lines. Inspect the full introducing patch and co-changed files; shallow history, squash merges and missing objects limit the lineage you can establish. See the [Git log manual](https://git-scm.com/docs/git-log) for pickaxe semantics.

If a commit identifies a PR or issue, read its body, discussion, and linked decision records through an authorized connector or CLI. For GitHub, `gh pr view NUMBER --repo OWNER/REPO --json title,body,createdAt,mergedAt,comments,reviews` can retrieve a bounded starting record; check pagination or truncation when missing discussion matters. PR conversation comments and review summaries may omit line-level review discussion. When it matters, read review comments with `gh api --paginate repos/OWNER/REPO/pulls/NUMBER/comments`, following reply context and the relevant diff. See [GitHub review comments](https://docs.github.com/en/rest/pulls/comments). Do not assume git, a remote, or authentication is available. With a source snapshot only, explicitly limit historical conclusions.

## Follow the evidence

Read the introducing change and nearby rationale comments, then callers/tests changed with it. Follow reverts, backports and renames to distinguish origin from later repair. A squash merge may require PR discussion to recover alternatives; a generic commit title is not an explanation. Tests establish expectations, while an explicit contemporary rationale comment can establish stated intent.

## Return

Add to the investigation record: commit and parent, patch location, author/date, PR and review-comment locators, relevant original wording, and whether the item concerns introduction, repair or current behavior. Mark unavailable patches/discussion separately from searches with no matches. Pass linked issue, document or incident IDs as leads rather than inventing their contents.
