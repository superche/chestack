# Decision trails and continuation

For long or unattended work, keep task-local records with outcome, reason, evidence pointer, result, timestamp, and relevant commit. Use the bundled `log` command with an explicit path. Keep secrets, raw tokens, private unrelated transcripts, and full customer payloads out of the record.

Store current units, owner, branch, head, acceptance result, and blockers in a simple task-local table when coordination needs it. Keep one writer per file. Derive aggregate status from evidence, and checkpoint the next safe step before stopping. The bundled logger is not a concurrent queue, scheduler, or orchestration service.

For requested recurring work, discover the native automation tool and use its current schema. Preserve the user's cadence, time zone, destination, and notification intent. Notify on meaningful change, completion, failure, or required action unless the user requests periodic updates. Verify creation before saying a future run is scheduled. If no scheduling tool exists, save the prompt and state that it is not scheduled.

For pauses, stop owned work and preserve recoverable state within the requested scope. For resumption, revalidate claims against live artifacts before continuing.
