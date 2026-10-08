# Revise against meaning and evidence

Run these passes on the requested artifact. Scale the depth to the change; a sentence rewrite does not require a repository investigation.

1. **Preserve the claim.** For a restatement, compare actors, actions, conditions, quantities, negations, and confidence with the source. Keep uncertainty that reflects missing evidence. Resolve ambiguity from context or flag it instead of inventing intent.
2. **Check the facts.** For newly authored technical claims, trace material behavior to code or an authoritative source. Verify identifiers, links, commands, defaults, and counts at the relevant version. Remove unsupported assurances; label assumptions and unrun checks.
3. **Walk the reader's path.** Apply the selected artifact's completion criteria. In a procedure, execute the safe path and a relevant failure case when authorized, then inspect the actual outputs. In an explanation, trace a concrete example. In a proposal, check that alternatives use the same criteria.
4. **Edit for clarity.** Replace vague praise with behavior or evidence, name the actor when it matters, put conditions before actions, and keep one name for each concept. Split sentences that require rereading while preserving necessary qualifications. Remove repetition and generic conclusions.
5. **Check delivery.** Review the rendered structure when layout matters. Confirm headings, lists, code blocks, and links serve the reader. Compare the revised text with the original again for changed meaning. Return the artifact and only material evidence gaps or editorial notes the user needs.

Use natural sentence rhythm and the user's language. Punctuation, sentence length, passive voice, and formatting are tools, not universal bans or quotas. Preserve established technical terms when they are more precise than a replacement. Explain unfamiliar terms once rather than cycling through synonyms.

## Before and after

These examples are invented to illustrate the checks; they are not product guarantees. Each pair assumes that the concrete actor, behavior, condition, and measurements in the revision are available in verified source context. Without that context, preserve the narrower claim or flag what is missing.

| Problem | Before | After | What changed |
|---|---|---|---|
| Missing action and actor | Configuration validation is performed prior to execution. | The runner validates the configuration before starting the job. | Names the actor and ordering |
| Hidden condition | Delete the cache and restart if the cache is corrupt. | If the cache is corrupt, delete it, then restart the service. | Limits both actions to the condition |
| Unsupported praise | The update significantly improves performance. | In the local 100-request sample, median latency fell from 80 ms to 60 ms. | Uses supplied measurements and their scope; omit the numbers if no such evidence exists |
| Lost uncertainty | The timeout may be caused by a stalled worker. | A stalled worker may explain the timeout. | Preserves the hypothesis instead of turning it into a diagnosis |
| Dense terminology | The persistence subsystem facilitates state restoration. | The app saves the draft and reloads it when the editor opens. | Replaces abstraction with the supplied behavior |

## Small repeatable checks

For a command guide, start from the documented initial state in a temporary directory, run each command, compare exit status and generated files with the text, and record any mismatch. Repeat a meaningful failure case. Keep the execution transcript in review evidence, not the published guide.

For a restatement, use a source containing a condition, a negation, and uncertainty. Check that all three survive the rewrite. For an RFC or PR, include one unrun test in the source facts and confirm that the output still labels it unrun. These checks expose semantic drift that spelling checks cannot catch.

A wording checklist cannot prove technical correctness or reader comprehension. Distinguish command execution, your own editorial review, and an independent reader evaluation when reporting evidence.
