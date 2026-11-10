# Validation Report - 2026-11-11, version 3.1.0

## Skill validation, version 3.1.0

Command: python3 scripts/validate-skill.py

Result: VALIDATION: PASS

- agents: 20
- workflows: 22
- templates: 30
- github: 6
- quality gates: 14
- project workspace: 8
- security references: 10

## Skill validation, version 3.1.0, extra checks

- SKILL.md contains no semicolon, no em dash and no en dash, as required by the validator.
- Living handover: SKILL.md, workflows/12-handover.md, templates/HANDOVER-TEMPLATE.md, quality-gates/handover-gate.md and agents/technical-project-manager.md updated. The handover package is now 22 sections and the gate requires the living handover file to be committed and pushed.
- templates/HANDOVER-TEMPLATE.md normalized to Vietnamese with diacritics, verified by reading the file after the rewrite.
- The living handover file name is written without its markdown extension in skill text, because the validator broken link check requires every markdown file name to exist in the skill repo.
- VERSION 3.1.0 matches the newest CHANGELOG entry, verified by the validator version check.
- Broken link check: no broken links, verified by the validator.
- Project docs validation PASS for examples/simulation-project, simulation test_booking 5 tests OK, example tests web-app 7 pass, api-app 10 pass, mobile-app 11 pass.

# Validation Report - 2026-11-11, version 3.0.0

## Skill validation, version 3.0.0

Command: python3 scripts/validate-skill.py

Result: VALIDATION: PASS

- agents: 20
- workflows: 22
- templates: 30
- github: 6
- quality gates: 14
- project workspace: 8
- security references: 10

## Skill validation, version 3.0.0, extra checks

- SKILL.md contains no semicolon, no em dash and no en dash, as required by the validator.
- New workflow file 09b-performance-audit and new gate performance-gate contain the required sections, verified by the validator.
- New template files THREAT-MODEL and POSTMORTEM exist and are counted by the validator.
- New security reference file file-upload-and-ssrf exists and is counted by the validator.
- Every Next Workflow target exists, verified by the validator cross-reference check. Workflow 09-security-audit now points to 09b-performance-audit, which points to 10-deployment.
- VERSION 3.0.0 matches the newest CHANGELOG entry, verified by the validator version check.
- Broken link check: the new validator check caught 7 bad links in the first CHANGELOG 3.0.0 draft, all fixed before release, and now reports no broken links.
- Vietnamese diacritics normalization verified by stripping diacritics from each converted file and comparing it with the original: 56 files in agents, workflows and quality-gates, all converted, with 9 reviewed exceptions where the original had a typo or a spelling variant, namely Go to Gọi in workflows/07-development, test đỗ unified to test đậu in workflows/08-testing, workflows/08b-systematic-debugging and the development, security and testing gates, phan doi corrected to rút gọn in workflows/00-triage, len lo corrected to lén lọt in quality-gates/requirement-gate, and San phan corrected to Sản phẩm in agents/ux-researcher.
- Install script tested with a temporary home directory: bash scripts/install.sh cursor installed the skill and its own validator run passed.
- Distribution copy at ~/workspace/master-vibe-coding was synced from this skill and verified identical with diff -r. The validator and the project docs validator were also run in the distribution copy and passed.
- Project docs validation was re-run in 3.0.0 and passed for examples/simulation-project. The simulation unittest was re-run in 3.0.0 and passed 5 tests.
- New example tests were run fresh in 3.0.0: examples/web-app 7 tests pass, examples/api-app 10 tests pass, examples/mobile-app 11 tests pass.

# Validation Report - 2026-11-11, version 2.2.0

## Skill validation, version 2.2.0

Command: python3 scripts/validate-skill.py

Result: VALIDATION: PASS

- agents: 20
- workflows: 21
- templates: 28
- github: 6
- quality gates: 13
- project workspace: 8
- security references: 9

## Skill validation, version 2.2.0, extra checks

- SKILL.md contains no semicolon, no em dash and no en dash, as required by the validator.
- New agent file code-reviewer contains the required sections: Vai tro, Pham vi trach nhiem, Dau vao, Dau ra, Quy trinh lam viec and Checklist.
- New workflow files 00b-change-proposal and 07c-code-review contain the required sections: Objective, Deliverables, Quality Gate, Failure Handling and Next Workflow.
- New template files STORY, CODE-REVIEW and CHANGE-PROPOSAL exist and are counted by the validator.
- All 9 security reference files exist in security/references and are counted by the validator.
- Every Next Workflow target exists, verified by the validator cross-reference check.
- VERSION 2.2.0 matches the newest CHANGELOG entry, verified by the validator version check.
- Distribution copy at ~/workspace/master-vibe-coding was synced from this skill and verified identical with diff -r.
- Project docs validation was re-run in 2.2.0 and passed for examples/simulation-project. The simulation unittest was re-run in 2.2.0 and passed 5 tests.

# Validation Report - 2026-11-11, version 2.1.0

## Skill validation, version 2.1.0

Command: python3 scripts/validate-skill.py

Result: VALIDATION: PASS

- agents: 19
- workflows: 19
- templates: 25
- github: 6
- quality gates: 13
- project workspace: 8

## Skill validation, version 2.1.0, extra checks

- SKILL.md contains no semicolon, no em dash and no en dash, as required by the validator.
- New workflow files 00-triage and 08b-systematic-debugging contain the required sections: Objective, Deliverables, Quality Gate, Failure Handling and Next Workflow.
- New template files TRIAGE, CONSTITUTION and DEBUG-REPORT exist and are counted by the validator.
- Design First chain renamed to D1 to D5, no file with the old 05 to 09 design chain names remains, and every Next Workflow target exists, verified by the new validator cross-reference check.
- VERSION 2.1.0 matches the newest CHANGELOG entry, verified by the new validator version check.
- Distribution copy at ~/workspace/master-vibe-coding was synced from this skill and verified identical with diff -r.
- Project docs validation was re-run in 2.1.0 and passed for examples/simulation-project. The simulation unittest was re-run in 2.1.0 and passed 5 tests.

# Validation Report - 2026-11-04, version 2.0.0

## Skill validation, version 2.0.0

Command: python3 scripts/validate-skill.py

Result: VALIDATION: PASS

- agents: 19
- workflows: 17
- templates: 22
- github: 6
- quality gates: 13
- project workspace: 8

## Skill validation, version 2.0.0, extra checks

- SKILL.md contains no semicolon, no em dash and no en dash, as required by the validator.
- New agent files all contain the required sections: Vai tro, Pham vi trach nhiem, Dau vao, Dau ra, Quy trinh lam viec and Checklist.
- New workflow files all contain the required sections: Objective, Deliverables, Quality Gate, Failure Handling and Next Workflow.
- Distribution copy at ~/workspace/master-vibe-coding was synced from this skill and verified identical with diff -r.
- Project docs validation was re-run in 2.0.0 and passed for examples/simulation-project. The simulation unittest was re-run in 2.0.0 and passed 5 tests.
- PWMS audit under the new gate is in ~/workspace/projects/personal-wealth-management/docs/UI-UX-AUDIT-V2.md. It scores the deployed version the user saw at 34.5 out of 100, FAIL, and it does not claim the redesigned version passes, because that version has not been coded yet.

# Validation Report - 2026-11-03

## Skill validation

Command: python3 scripts/validate-skill.py

Result: VALIDATION: PASS

- agents: 15
- workflows: 12
- templates: 12
- github: 6
- quality gates: 10
- project workspace: 8

## Project docs validation

Command: python3 scripts/validate-project-docs.py examples/simulation-project

Result: PROJECT VALIDATION: PASS

## Simulation test

Command: python3 -m unittest -v test_booking, run in examples/simulation-app

Result: Ran 5 tests, OK

- test_empty_calendar: ok
- test_invalid_range: ok
- test_no_overlap: ok
- test_overlap: ok
- test_partial_overlap: ok

## Link check

Skill files were generated by a script that writes only internal relative paths listed in this report. No external link was claimed as verified in this release.

## Limitations

- Validation checks structure, required sections, counts and secret patterns. It does not prove that a future real project will pass its gates.
- Simulation test proves only the small booking overlap logic. Auth and Notification in the simulation remain design only.
- MCP integration is not claimed as tested in this release, because no MCP server was used to build this skill itself.
