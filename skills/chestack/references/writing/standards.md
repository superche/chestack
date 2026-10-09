# Choose a standard for the requested document

Use the user's or repository's required standard first. Record the requested language, audience, document type, applicable version, and what a conformance claim would require. A style preference, an information architecture, and a controlled-language standard answer different questions.

| Need | Basis | Apply it to |
|---|---|---|
| Separate learning, task execution, lookup, and understanding | [Diátaxis](https://diataxis.fr/start-here/) | Choose the document's purpose and navigation; it is not a sentence checker |
| Write or review an English technical procedure | [ASD-STE100 official information](https://www.asd-ste100.org/about_STE.html) and the specified edition | Review both writing rules and the controlled dictionary, including permitted project terminology |
| Write ordinary developer documentation | [Google developer documentation style guide](https://developers.google.com/style/) plus repository conventions | Resolve recurring presentation and language questions without overriding the reader's task |
| Document an API or CLI | The actual schema, source, and help output at the target version | Establish facts; a style guide cannot establish behavior |

## Procedures and controlled language

ASD-STE100 is an English controlled-language standard with writing rules and a dictionary. Short sentences alone do not establish conformance. If formal conformance is requested, obtain the specified edition and applicable terminology, check both parts, and report checks and exceptions. If those resources are unavailable, provide a limited editorial review and leave conformance unverified. Do not reproduce the standard or its dictionary as a bundled checklist.

For how-to guides, apply the [procedure rules](how-to.md) directly, using the official ASD-STE100 Issue 9 rule references. For English standard-based review, also check the controlled dictionary, approved parts of speech and meanings, technical terminology, verb rules, and word-count rules in the specified edition. This bundle links the standard; it does not replace its full requirements.

For Chinese documents, use those clarity principles with natural Chinese syntax. Do not convert English word limits into Chinese character quotas or describe Chinese output as ASD-STE100 compliant. The Chinese examples adapt applicable procedure principles; they are not English conformance specimens. If no edition is specified for an English procedure, use Issue 9 (2025-01-15) as the baseline and state that choice. A user-specified edition takes precedence.

## Artifact acceptance

- Tutorial: a beginner can reach the promised artifact from the stated starting state and recognize each checkpoint.
- How-to: a competent reader can select the applicable branch, perform the task, verify success, and respond to a likely failure.
- Reference: the scoped contract is searchable and source-backed, including relevant errors and limits.
- Explanation: a concrete example connects mechanism, constraints, and tradeoffs; historical intent retains its evidence level.

Read the matching [document-type guide](document-types.md) for its worked example, not a mandatory template. Use the [review checklist](review-checklist.md) to inspect an actual draft. Following the layout of an example does not prove correctness.
