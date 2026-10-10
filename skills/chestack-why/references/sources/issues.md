# Issues and requirements

**Use when:** testing a product need, acceptance constraint, customer request or incident follow-up as the reason for a change.

**Seed:** linked issue IDs, product terms, symptom, owning project and decision period.

## Search and read

1. Open linked issues and their comments before keyword expansion. Read parent requirements, duplicate-of chains and linked project specifications; a subtask may only describe implementation.
2. If links leave the reason open, search feature names, user-facing symptoms and technical identifiers within the relevant project/period. Record filters and pagination limits.
3. Compare the original scope and acceptance criteria with reopening, edits and closure reasons. Follow linked decisions to determine which requirement applied when the code was introduced.

Labels, milestones and boilerplate are search leads. A closed issue does not prove implementation or release; a current edited description need not represent the original requirement. Stop when the relevant requirement and its link to the change are established, or name the missing link.

## Return

Issue ID/title, parent or canonical issue, author/date, status at the decision when available, the relevant requirement/comment locator and wording, and linked implementation. Include conflicting scope changes, inaccessible attachments and unvisited leads. Preserve query/filter and result status even when no issue matches.
