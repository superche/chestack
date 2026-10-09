# Investigate decision records

Read only the categories needed to settle the question. Start from linked identifiers, then widen with symbols, product vocabulary and the decision period if links do not settle material alternatives. Use available authorized tools; vendor names are not capability requirements.

## Issues and requirements

Open linked issues including comments, parent requirements and duplicate-of chains. Compare original scope, later edits, acceptance criteria and closure reason with the introducing change. Labels and generic template text are leads, not explicit rationale. Record which requirement applied at the decision date; a reopened ticket may describe a different problem.

## Design documents

Fetch the relevant content and linked alternatives, not only titles/previews. Identify author, date, status and superseding decisions. Distinguish a proposal from an accepted decision and from its implementation. If only the latest text is available, qualify claims about what it said before the code landed.

Use the established ADR lens: context, decision, status and consequences. An accepted decision can explain intent; its predicted consequences still need observation. See Michael Nygard's [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions). This is a reading lens, not a requirement to create an ADR.

## Team discussion

Search exact PR/issue URLs, symbols, feature vocabulary and error strings in relevant authorized channels and dates. Read replies and linked follow-ups: an early suggestion, joke or rejected option is not the final decision. Retain author, timestamp, permalink and context for any attributed reason. Note inaccessible threads, private messages outside scope and retention limits; an empty public-channel search does not cover them.

## Return evidence

For each useful record, preserve the specific constraint or alternative it supports, its locator/date/status, contrary passages, and leads not yet followed. Several records repeating one PR are one origin, not independent corroboration. If the record says why but current code differs, hand the mismatch to source verification rather than silently rewriting either account.
