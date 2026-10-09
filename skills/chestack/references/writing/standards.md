# Choose a standard for the requested document

Use the user's or repository's required standard first. Record the requested language, audience, document type, applicable version, and what a conformance claim would require. A style preference, an information architecture, and a controlled-language standard answer different questions.

| Need | Basis | Apply it to |
|---|---|---|
| Separate learning, task execution, lookup, and understanding | [Diátaxis](https://diataxis.fr/start-here/) | Choose the document's purpose and navigation; it is not a sentence checker |
| Write an English technical procedure under a controlled-language requirement | [ASD-STE100 official information](https://www.asd-ste100.org/about_STE.html) and the specified edition | Review both writing rules and the controlled dictionary, including permitted project terminology |
| Write ordinary developer documentation | [Google developer documentation style guide](https://developers.google.com/style/) plus repository conventions | Resolve recurring presentation and language questions without overriding the reader's task |
| Document an API or CLI | The actual schema, source, and help output at the target version | Establish facts; a style guide cannot establish behavior |

## Procedures and controlled language

ASD-STE100 is an English controlled-language standard with writing rules and a dictionary. Short sentences alone do not establish conformance. If formal conformance is requested, obtain the specified edition and applicable terminology, check both parts, and report checks and exceptions. If those resources are unavailable, provide a limited editorial review and leave conformance unverified. Do not reproduce the standard or its dictionary as a bundled checklist.

For ordinary procedures, apply this house procedure profile: make actions explicit, keep terminology stable, state conditions before actions, and separate actions from expected results. Use one independently verifiable action per numbered step unless tightly coupled actions are clearer together. Put a hazard or irreversible consequence before the action it governs. Show prerequisites, success checks, and a bounded recovery path.

For Chinese documents, use those clarity principles with natural Chinese syntax. Do not convert English word limits into Chinese character quotas or describe Chinese output as ASD-STE100 compliant. The examples in this bundle follow a house style; they are not certified or fully assessed against that standard.

## Artifact acceptance

- Tutorial: a beginner can reach the promised artifact from the stated starting state and recognize each checkpoint.
- How-to: a competent reader can select the applicable branch, perform the task, verify success, and respond to a likely failure.
- Reference: the scoped contract is searchable and source-backed, including relevant errors and limits.
- Explanation: a concrete example connects mechanism, constraints, and tradeoffs; historical intent retains its evidence level.

Use the [worked examples](examples.md) as examples of these outcomes, not mandatory templates. Use the [review checklist](review-checklist.md) to inspect an actual draft. Following the layout of an example does not prove correctness.
