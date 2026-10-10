# Design documents

**Use when:** investigating alternatives, architectural constraints or a recorded decision.

**Seed:** linked document IDs, decision/feature names, authors and decision period.

## Search and read

1. Read the linked document body, status and version metadata. Follow alternatives, appendices, superseding records and relevant meeting notes.
2. If the record is incomplete, search technical symbols and product vocabulary in the authorized collection. Read promising bodies rather than relying on search previews.
3. Use the ADR lens: context, decision, status and consequences. Distinguish proposal, acceptance and implementation; locate the version contemporaneous with the change when available.

The ADR lens comes from Michael Nygard's [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions). It does not require creating a new ADR. Predicted consequences are not measured outcomes. If only today's page exists, qualify claims about what it said at the decision date.

## Return

Document/section locator, author/date/version, draft/accepted/superseded status, relevant constraint and rejected alternatives, and links to implementation or replacement decisions. Preserve disagreements with code and limits on older versions; do not silently prefer the most recently edited page.
