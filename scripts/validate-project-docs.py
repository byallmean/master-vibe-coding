#!/usr/bin/env python3
"""Validate one project workspace created from project-workspace templates."""
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("usage: validate-project-docs.py <project-workspace-dir>")
    sys.exit(2)
root = Path(sys.argv[1])
required = ["PROJECT_CONTEXT.md", "PROJECT_STATUS.md", "CURRENT_TASK.md", "DECISIONS.md", "TECHNICAL_DEBT.md", "BLOCKERS.md", "NEXT_STEPS.md", "CHANGELOG.md"]
errors = []
for name in required:
    p = root / name
    if not p.exists():
        errors.append(f"missing: {name}")
        continue
    text = p.read_text(encoding="utf-8")
    if len(text) < 100:
        errors.append(f"too short: {name}")
    if "-----BEGIN" in text or "password=" in text:
        errors.append(f"possible secret in {name}")
status = root / "PROJECT_STATUS.md"
if status.exists():
    text = status.read_text(encoding="utf-8")
    if "Trang thai" not in text and "Status" not in text and "trang thai" not in text.lower():
        errors.append("PROJECT_STATUS.md does not state a status")
if errors:
    print("errors:")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)
print(f"PROJECT VALIDATION: PASS for {root}")
