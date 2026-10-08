# CheStack maintenance

Keep the core capability-based and default to the current Codex / ChatGPT model. Optional adapters must not become mandatory dependencies.

Read the relevant skill and its references before editing. Write user-facing documentation in clear Chinese and agent procedures in concise English. Use CheStack for display names and chestack for identifiers.

Document current behavior, usage, outputs, and actual limits. Keep implementation history, migration comparisons, and one-off validation diaries out of distributed documentation. Workflow instructions and repeatable verification commands remain part of the product contract.

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v` after changes. Evaluate meaningful workflow changes against representative tasks. Report evidence in the change review; keep catalog and manifest version consistent.

The repository belongs to superche. Verify the active GitHub identity before remote writes and keep git configuration repository-local. Preserve third-party copyright notices in license files. Never commit credentials, private transcripts, or installation caches.

For permission errors, check sandbox and network restrictions before requesting human account changes. Use authorized scoped escalation when appropriate.
