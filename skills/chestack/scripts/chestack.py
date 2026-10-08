#!/usr/bin/env python3
"""Small, bounded evidence helpers. No background execution or network writes."""

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def doctor():
    return {
        "python": sys.version.split()[0],
        "executables": {name: shutil.which(name) for name in ("git", "gh", "codex")},
        "scope": "Local executable presence only; no authentication or host-tool checks.",
        "model_policy": "inherit-current-session",
        "capabilities_requiring_session_inspection": [
            "subagents", "browser-control", "connectors", "automation", "write-permissions"
        ],
    }


def plan_errors(text):
    # Exclude examples: a template inside a code fence is not a completed plan.
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    clean = "\n".join(lines)
    errors = []
    if fence:
        errors.append("Unclosed code fence")
    sections = {}
    matches = list(re.finditer(r"^# ([^\n]+)\s*$", clean, re.MULTILINE))
    for i, match in enumerate(matches):
        key = match.group(1).strip().lower()
        if key in sections:
            errors.append(f"Duplicate section: {key}")
        end = matches[i + 1].start() if i + 1 < len(matches) else len(clean)
        sections[key] = clean[match.end():end].strip()
    for name in ("goal", "scope", "constraints", "phases", "risks", "recovery"):
        if not sections.get(name):
            errors.append(f"Missing or empty section: {name}")
    phases = sections.get("phases", "")
    starts = list(re.finditer(r"^## Phase (\d+):\s*(\S[^\n]*)$", phases, re.MULTILINE))
    if not starts:
        errors.append("Phases must contain at least one '## Phase N: title'")
    for i, match in enumerate(starts):
        number = int(match.group(1))
        if number != i + 1:
            errors.append("Phase numbers must be consecutive starting at 1")
        end = starts[i + 1].start() if i + 1 < len(starts) else len(phases)
        body = phases[match.end():end]
        for field in ("Scope", "Dependencies", "Acceptance", "Verification"):
            if not re.search(rf"^{field}:[ \t]*\S[^\n]*$", body, re.MULTILINE):
                errors.append(f"Phase {number}: missing or empty {field}")
    if re.search(r"\b(TODO|TBD|FIXME)\b|<[^>\n]+>", clean):
        errors.append("Unresolved placeholder outside code fences")
    return errors


def append_log(path, decision, reason, evidence, result):
    path = Path(path)
    if not all(value.strip() for value in (decision, reason, evidence, result)):
        raise ValueError("Decision, reason, evidence, and result must be nonempty")
    # Detect corrupt input instead of extending a file that consumers cannot read.
    if path.exists():
        raw = path.read_text(encoding="utf-8")
        if raw and not raw.endswith("\n"):
            raise ValueError("Existing log must end with a newline")
        for number, line in enumerate(raw.splitlines(), 1):
            try:
                entry = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at line {number}") from exc
            if not isinstance(entry, dict):
                raise ValueError(f"Expected an object at line {number}")
    path.parent.mkdir(parents=True, exist_ok=True)
    entry = dict(timestamp=now(), decision=decision, reason=reason, evidence=evidence, result=result)
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry


def run_json(argv, runner=subprocess.run, accepted_exit_codes=(0,)):
    try:
        completed = runner(argv, capture_output=True, text=True, timeout=30, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"ok": False, "error": type(exc).__name__}
    try:
        data = json.loads(completed.stdout)
    except json.JSONDecodeError:
        data = None
    # Do not include arbitrary stderr, URLs, environment variables, or auth material.
    return {"ok": completed.returncode in accepted_exit_codes and data is not None,
            "exit_code": completed.returncode, "data": data}


def pr_status(repo, number, runner=subprocess.run):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo) or number < 1:
        raise ValueError("Use OWNER/REPO and a positive PR number")
    common = [str(number), "--repo", repo]
    metadata = run_json(["gh", "pr", "view", *common, "--json",
                         "url,number,state,isDraft,headRefOid,baseRefName,mergeable,mergeStateStatus,reviewDecision"], runner)
    # gh uses 1 for failing checks and 8 for pending checks even with valid data.
    checks = run_json(["gh", "pr", "checks", *common, "--required", "--json",
                       "name,state,bucket,link"], runner, accepted_exit_codes=(0, 1, 8))
    if not isinstance(metadata.get("data"), dict):
        metadata["ok"] = False
    if not isinstance(checks.get("data"), list):
        checks["ok"] = False
    return {
        "captured_at": now(), "repo": repo, "pr": number,
        "metadata": metadata, "required_checks": checks,
        "readiness": "not-evaluated",
        "remaining_evidence": ["unresolved-review-threads", "branch-protection-and-user-gates",
                               "head-freshness-before-action", "stack-dependencies"],
        "scope": "Read-only snapshot. No polling, review certification, or merge.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("doctor", help="Inspect executable presence, not host permissions")
    plan = commands.add_parser("plan-check", help="Validate plan structure, not correctness")
    plan.add_argument("path", type=Path)
    log = commands.add_parser("log", help="Append one decision to a single-writer JSONL")
    log.add_argument("--path", type=Path, required=True)
    for field in ("decision", "reason", "evidence", "result"):
        log.add_argument("--" + field, required=True)
    pr = commands.add_parser("pr-status", help="Read a bounded GitHub PR snapshot")
    pr.add_argument("--repo", required=True)
    pr.add_argument("--pr", type=int, required=True)
    args = parser.parse_args(argv)
    try:
        code = 0
        if args.command == "doctor":
            output = doctor()
        elif args.command == "plan-check":
            errors = plan_errors(args.path.read_text(encoding="utf-8"))
            output = {"valid_structure": not errors, "errors": errors,
                      "scope": "Structural check only; execution and feasibility are unverified."}
            code = int(bool(errors))
        elif args.command == "log":
            output = append_log(args.path, args.decision, args.reason, args.evidence, args.result)
        else:
            output = pr_status(args.repo, args.pr)
            code = int(not output["metadata"]["ok"] or not output["required_checks"]["ok"])
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return code
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
