#!/usr/bin/env python3
"""Validate the master-vibe-coding skill structure."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []
warnings = []

def check_file(rel, min_chars=200):
    p = ROOT / rel
    if not p.exists():
        errors.append(f"missing: {rel}")
        return ""
    text = p.read_text(encoding="utf-8")
    if len(text) < min_chars:
        errors.append(f"too short: {rel} ({len(text)} chars)")
    return text

def check_dir(rel, expected, label):
    d = ROOT / rel
    if not d.exists():
        errors.append(f"missing dir: {rel}")
        return []
    files = sorted(p.name for p in d.glob("*.md"))
    if len(files) < expected:
        errors.append(f"{label} count {len(files)} below expected {expected}: {files}")
    return files

check_file("SKILL.md", 500)
check_file("README.md", 500)
check_file("CHANGELOG.md", 100)
check_file("VERSION", 3)
check_file("skill.yaml", 50)
agents = check_dir("agents", 20, "agents")
workflows = check_dir("workflows", 22, "workflows")
templates = check_dir("templates", 30, "templates")
github = check_dir("github", 6, "github")
gates = check_dir("quality-gates", 14, "quality gates")
workspace = check_dir("project-workspace", 8, "project workspace")
security_refs = check_dir("security/references", 10, "security references")

for rel in ["SKILL.md"]:
    text = check_file(rel, 1)
    if ";" in text:
        errors.append("SKILL.md must not contain semicolons")
    if "—" in text or "–" in text:
        errors.append("SKILL.md must not contain em or en dashes")

for folder, files in [("agents", agents), ("workflows", workflows), ("quality-gates", gates)]:
    for name in files:
        text = (ROOT / folder / name).read_text(encoding="utf-8")
        if "TODO" in text or "placeholder" in text.lower():
            warnings.append(f"possible placeholder wording in {folder}/{name}")

for name in agents:
    text = (ROOT / "agents" / name).read_text(encoding="utf-8")
    for section in ["Vai trò", "Phạm vi trách nhiệm", "Đầu vào", "Đầu ra", "Quy trình làm việc", "Checklist"]:
        if section not in text:
            errors.append(f"agents/{name} missing section {section}")

for name in workflows:
    text = (ROOT / "workflows" / name).read_text(encoding="utf-8")
    for section in ["Objective", "Deliverables", "Quality Gate", "Failure Handling", "Next Workflow"]:
        if section not in text:
            errors.append(f"workflows/{name} missing section {section}")

# Cross-reference check added in 2.1.0: the first .md file named after
# "Next Workflow" in each workflow file must exist in workflows/.
import re
for name in workflows:
    text = (ROOT / "workflows" / name).read_text(encoding="utf-8")
    m = re.search(r"## Next Workflow\s*\n\s*(\S+\.md)", text)
    if not m:
        errors.append(f"workflows/{name} has no Next Workflow target")
    elif not (ROOT / "workflows" / m.group(1)).exists():
        errors.append(f"workflows/{name} Next Workflow target missing: {m.group(1)}")

# Version check added in 2.1.0: VERSION must match the newest CHANGELOG entry.
version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
if f"## {version} -" not in changelog:
    errors.append(f"VERSION {version} has no matching CHANGELOG entry")

# Broken link check added in 3.0.0: every .md token mentioned in a .md file
# must resolve to a real file. Resolution order: relative to the file, then
# repo root, then templates/ and project-workspace/ for bare template names.
# External paths (http, absolute, home-relative, system skill paths) are skipped.
md_token = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_./-]*\.md")
for p in sorted(ROOT.rglob("*.md")):
    text = p.read_text(encoding="utf-8", errors="ignore")
    for tok in set(md_token.findall(text)):
        if tok.startswith(("http", "/", "~", "workspace/", "opt/")) or "://" in tok:
            continue
        candidates = [p.parent / tok, ROOT / tok]
        if "/" not in tok:
            candidates += [
                ROOT / "templates" / tok,
                ROOT / "project-workspace" / tok,
                ROOT / "agents" / tok,
                ROOT / "workflows" / tok,
                ROOT / "quality-gates" / tok,
                ROOT / "github" / tok,
                ROOT / "docs" / tok,
                ROOT / "security" / "references" / tok,
            ]
        if not any(c.exists() for c in candidates):
            errors.append(f"broken link {tok} in {p.relative_to(ROOT)}")

secret_markers = ["password=", "api_key=", "token=", "-----BEGIN"]
for p in ROOT.rglob("*.md"):
    if "templates" in p.parts or "project-workspace" in p.parts:
        continue
    text = p.read_text(encoding="utf-8", errors="ignore")
    for marker in secret_markers:
        if marker in text:
            errors.append(f"possible secret pattern {marker} in {p.relative_to(ROOT)}")

print(f"agents: {len(agents)}")
print(f"workflows: {len(workflows)}")
print(f"templates: {len(templates)}")
print(f"github: {len(github)}")
print(f"quality gates: {len(gates)}")
print(f"project workspace: {len(workspace)}")
print(f"security references: {len(security_refs)}")
if warnings:
    print("warnings:")
    for w in warnings:
        print(f" - {w}")
if errors:
    print("errors:")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)
print("VALIDATION: PASS")
