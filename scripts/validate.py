#!/usr/bin/env python3
"""Validate local package inventory, metadata, references, and portability."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors = []
    catalog = json.loads((root / "catalog.json").read_text())
    manifest = json.loads((root / "plugin.json").read_text())
    if manifest["name"] != "chestack" or manifest["version"] != catalog["version"]:
        errors.append("Manifest identity/version mismatch")
    overlay = json.loads((root / ".codex-plugin/plugin.json").read_text())
    presentation = manifest["extensions"]["com.openai"]["interface"]
    if presentation.get("displayName") != "CheStack":
        errors.append("Plugin display name must be CheStack")
    if (overlay.get("interface") != presentation or
            overlay.get("name") != manifest["name"] or
            overlay.get("version") != manifest["version"]):
        errors.append("Codex compatibility manifest differs from portable metadata")
    onboarding = manifest["extensions"]["com.openai"]["onboardingSkill"]
    if not (root / onboarding).is_file():
        errors.append("Missing onboarding skill")
    market = json.loads((root / ".agents/plugins/marketplace.json").read_text())
    for plugin in market["plugins"]:
        if not (root / plugin["source"]["path"] / "plugin.json").is_file():
            errors.append("Marketplace source does not resolve to a plugin")
    core = root / "skills/chestack"
    groups = [(root / "skills", "*/SKILL.md", "skills"),
              (core / "references/principles", "*.md", "principles"),
              (core / "references/playbooks", "*.md", "playbooks")]
    for directory, pattern, key in groups:
        found = {p.parent.name if key == "skills" else p.stem for p in directory.glob(pattern)}
        if found != set(catalog[key]) or len(catalog[key]) != len(found):
            errors.append(f"Catalog mismatch: {key}")
    implicit = catalog.get("implicit_skills", [])
    if len(implicit) != len(set(implicit)) or not set(implicit).issubset(catalog["skills"]):
        errors.append("Invalid implicit skill inventory")
    for name in catalog["skills"]:
        skill = root / "skills" / name
        text = (skill / "SKILL.md").read_text()
        if not re.match(r"^---\nname: " + re.escape(name) + r"\ndescription: .+\n---\n", text):
            errors.append(f"Invalid skill frontmatter: {name}")
        yaml = (skill / "agents/openai.yaml").read_text()
        policy = re.findall(r"^  allow_implicit_invocation: (true|false)$", yaml, re.MULTILINE)
        expected_policy = "true" if name in implicit else "false"
        if policy != [expected_policy] or "$" + name not in yaml:
            errors.append(f"Missing invocation policy or prompt: {name}")
        if not re.search(r'display_name: "CheStack(?: |")', yaml):
            errors.append(f"Skill display name must start with CheStack: {name}")
    # Core execution must not depend on another vendor's host API or model IDs.
    banned = re.compile(r"\.cursor/|\.claude/|subagent_type|disable-model-invocation|grok-\d|claude-opus|cursor-team-kit")
    for path in (root / "skills").rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml", ".py"}:
            if banned.search(path.read_text()):
                errors.append(f"Foreign host dependency: {path.relative_to(root)}")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text()
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"^[a-z]+://|^#", target):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f"Broken or external local link: {path.relative_to(root)} -> {target}")
    return errors


if __name__ == "__main__":
    try:
        errors = validate()
    except (OSError, ValueError, KeyError) as exc:
        errors = [str(exc)]
    print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
    sys.exit(int(bool(errors)))
