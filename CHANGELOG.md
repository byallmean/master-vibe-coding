# Changelog

## 3.0.0 - 2026-11-11

- Performance split out: added workflows/09b-performance-audit.md and quality-gates/performance-gate.md with default numeric budgets, LCP at most 2.5 seconds, API p95 at most 500 milliseconds, JavaScript bundle at most 300 KB after compression and slowest query in the main flow at most 200 milliseconds. Workflow 09-security-audit now covers security only and points to 09b as its next workflow. The Performance Engineer agent carries the same budgets and checklist.
- Threat modeling and data classification: Phase 04 now includes a STRIDE threat modeling step with templates/THREAT-MODEL.md, and templates/DATABASE-DESIGN.md has a data classification section stating which data is encrypted at rest and in transit. templates/ARCHITECTURE.md links the threat model summary.
- File upload and SSRF: added security/references/file-upload-and-ssrf.md and a file upload and SSRF audit step in workflow 09-security-audit, covering file type by content, size limit, content scanning, no executable uploads, ownership checks on file access and an allowlist for server-side URL fetches.
- MFA and session management: security/references/authentication.md now covers MFA for admin and sensitive accounts and session management with expiry, remote revocation, revocation on password change and refresh token rotation, tied to Authentik SSO.
- Accessibility and i18n: WCAG 2.1 level AA is now the target for the main flow, recorded in SKILL.md, workflows/D2-visual-design-system.md, templates/DESIGN-SYSTEM.md as appendices and the Accessibility criterion of quality-gates/design-acceptance-gate.md. I18n is done from the start with per-locale language files and locale-based formatting of dates, numbers and currency.
- Postmortem and incident drill: added templates/POSTMORTEM.md. workflows/11-operations.md now requires a postmortem within 3 days of a production incident and periodic incident drills.
- Cost and token budget: SKILL.md, agents/orchestrator.md and project-workspace/PROJECT_STATUS.md now require a cost and token budget before implementation, with a maximum task count per session, a context limit and a model choice per task type, plus a full handover when one account runs out of tokens.
- Real examples: added examples/web-app, a Node.js task list with 7 passing tests, examples/api-app, a Python API with auth, rate limiting and mass assignment protection with 10 passing tests, and examples/mobile-app, a React Native style skeleton with pure logic and 11 passing tests. Each example has its own README with the exact test command.
- One-command install: added scripts/install.sh, which installs the skill to Muse, Claude Code, Cursor or Codex and then runs the validator itself. docs/installation.md now documents the script and the install locations.
- Validator: added a broken link check for every .md file, resolving bare template names against templates and project-workspace. Expectations raised to 20 agents, 22 workflows, 30 templates, 14 quality gates and 10 security references.
- Vietnamese diacritics normalized: all files in agents, workflows and quality-gates are now written in Vietnamese with diacritics, with no logic change. The validator now checks agent section names with diacritics: Vai trò, Phạm vi trách nhiệm, Đầu vào, Đầu ra, Quy trình làm việc and Checklist. Normalization was verified by stripping diacritics from each converted file and comparing it with the original.
- Typo fixes found during normalization: workflows/00-triage.md said 04-architecture at a meaningless level and now says at a shortened level, quality-gates/requirement-gate.md said len lo and now says lén lọt, agents/ux-researcher.md said San phan and now says Sản phẩm, workflows/07-development.md said Go Security Engineer and now says Gọi Security Engineer. The spelling test đỗ was unified to test đậu to match SKILL.md.
- No working version 2.2 component was deleted.

## 2.2.0 - 2026-11-11

- Context management: added templates/STORY.md. Large PRDs and architectures are sharded into self-contained stories at Phase 03, each story carrying its context, acceptance criteria, files to read, files to change, verification command and expected output. Each task goes to a fresh agent when the platform supports it. Work stops when context use passes 70 percent: write a short handover, compact or start a fresh session, then continue. One task changes at most 500 lines.
- Two-stage code review: added agents/code-reviewer.md, workflows/07c-code-review.md and templates/CODE-REVIEW.md. Stage 1 checks spec compliance, stage 2 checks code quality, run separately in that order. The reviewer must not be the agent that wrote the code in the same session when separation is possible. Updated workflows 07-development and github/pull-request-review.md.
- Change proposal for existing apps: added workflows/00b-change-proposal.md and templates/CHANGE-PROPOSAL.md with a propose, apply and archive loop and a delta spec marked ADDED, MODIFIED and REMOVED. The delta is merged into the living spec on archive. Updated SKILL.md and workflows/00-triage.md so triage level M changes on existing apps write a proposal first.
- Remaining gates rewritten: Discovery, Requirement, Architecture, Design, Development, Deployment, Production Acceptance and Handover gates now have concrete criteria tables and CONDITIONAL PASS restrictions modelled on the Design Acceptance Gate. UI Implementation and Visual QA gates were already specific and are unchanged.
- Baseline and worktree: record a baseline of commit, image digest, health status, test results and backup before any change, work on a separate branch or git worktree, and compare the result with the baseline afterwards. Added baseline sections to templates/DEPLOYMENT-CHECKLIST.md and project-workspace/PROJECT_STATUS.md, a worktree section to github/branch-strategy.md, and baseline steps to workflows 07-development and 10-deployment.
- Security references: added security/references with 9 files for the self-hosted stack, secrets-and-env, database-security, authentication, rate-limiting, payments, mobile, ai-integration, deployment and data-access, each with concrete BAD and GOOD patterns. They are loaded lazily, only the file relevant to the real stack, from the Security Engineer, workflow 09-security-audit and SKILL.md. Security negative tests and the leaked secret and accepted risk process from version 2.1 were already in place and are not redone here.
- Validator expectations updated to 20 agents, 21 workflows, 28 templates, 13 quality gates and 9 security references. Validator now also counts the security references directory.
- No working version 2.1 component was deleted.

## 2.1.0 - 2026-11-11

- Lightweight mode: added workflows/00-triage.md and templates/TRIAGE.md. Every request is classified S, M or L before work starts. S is a small fix of 1 to 3 files with no API, database, main UI or auth, payment, secret or user data change. M runs a shortened specify, plan, tasks and implement path. L runs the full 12 phases. The gate list that may be skipped and the gates that must still pass are written in TRIAGE.md.
- Project constitution: added templates/CONSTITUTION.md with 5 to 10 non-negotiable project principles, checked at the start of every major workflow. A step that violates the constitution stops, CONDITIONAL PASS may not be used to bypass it.
- Test-first is now mandatory: no production code without a failing test first. Default coverage threshold is at least 80 percent of lines for new and changed code, adjustable by the Product Owner with a written reason. Security negative tests are required in Phase 08. Updated workflows 07-development and 08-testing, agents QA Engineer and Backend Engineer, templates TEST-PLAN.md and quality-gates/testing-gate.md, which was rewritten with quantified thresholds modelled on the Design Acceptance Gate.
- Systematic debugging: added workflows/08b-systematic-debugging.md and templates/DEBUG-REPORT.md with 4 phases, reproduce, narrow scope, find root cause, fix and re-verify, plus a 5-step Verification Before Completion checklist that must use a freshly run command. Orchestrator, workflows 07, 08 and 09 now route unknown failures to this workflow.
- Design First chain renamed from 05, 06, 07, 08, 09 to D1, D2, D3, D4, D5 so the chain no longer collides with the 12 phase numbers. All references in SKILL.md, README.md, workflows 05, 07 and 08 and agents/orchestrator.md updated. The 12-phase numbering is unchanged.
- Security shift-left: the Security Engineer is called whenever code touches auth, payment, database, API key, secret or user data, not only at Phase 09. Added the Never trust the client rule to SKILL.md and to the Orchestrator, Backend Engineer and Frontend Engineer. Workflows 09-security-audit was rewritten as a 9-step audit adapted from the vibe-security skill for a self-hosted stack, covering secrets, database access control, auth, rate limiting, payments, mobile, AI and LLM, deployment and data access.
- Security Gate rewritten with a criteria table and a hard-fail list modelled on the Design Acceptance Gate. Critical findings, leaked secrets, auth bypass, client-submitted prices and unrotated committed secrets may not use CONDITIONAL PASS. Evidence must include real tool output from gitleaks and dependency scans.
- SECURITY-REPORT template rewritten to the vibe-security output format: file and line, vulnerability name, what an attacker can do, before and after code, severity and retest result, plus a section for deliberately accepted risks with reason, impact and review date.
- Validator expectations updated to 19 agents, 19 workflows, 25 templates and 13 quality gates. Validator now also checks that every Next Workflow target file exists and that VERSION matches the newest CHANGELOG entry.
- No working version 2.0 component was deleted. The old design chain file names are the only names removed, and only because they were renamed to D1 to D5.

## 2.0.0 - 2026-11-04

- Design First upgrade: DESIGN FIRST, USER CENTRIC, FUNCTIONAL EXCELLENCE is now a core rule, not a post-coding decoration step.
- Added 4 specialist agents: Design Director, Product Designer, Visual UI Designer, UX Engineer. Total is now 18 specialists plus the Chief AI Orchestrator, 19 agent files.
- Added a 5-file Design First workflow chain that runs inside existing phases 05, 07 and 08: 05-product-experience-design, 06-visual-design-system, 07-prototype-review, 08-ui-implementation, 09-visual-quality-assurance. The 12-phase numbering is unchanged.
- Added 10 design templates: USER-PERSONA, USER-JOURNEY, INFORMATION-ARCHITECTURE, USER-FLOW, DESIGN-BRIEF, VISUAL-DIRECTION, DESIGN-SYSTEM, SCREEN-SPECIFICATION, DESIGN-REVIEW, UI-UX-AUDIT.
- Added 3 quality gates: design-acceptance-gate (100-point scoring, pass at 85 with no criterion below 70), ui-implementation-gate, visual-qa-gate.
- Added a 20-item Design System standard, a UI Implementation Standard for dashboard, tables and forms, and a JSON and Developer Interface Policy that bans raw JSON for ordinary users.
- Added Visual QA as a mandatory run-and-screenshot process with minimum viewports Desktop 1440 x 900, Laptop 1280 x 800, Tablet 768 x 1024, Mobile 390 x 844.
- Updated the Orchestrator with design authority rules and a Design Director veto, updated Frontend Engineer and UI UX Designer for version 2.0, and linked existing workflows 05, 07 and 08 to the new chain and gates.
- Added an existing-application improvement path: audit, systematic redesign, approval, module-by-module implementation without breaking business logic, API or database, Visual QA to the Design Acceptance Gate, then release.
- Validator expectations updated to 19 agents, 17 workflows, 22 templates and 13 quality gates. No working version 1.0 component was deleted.

## 1.0.0 - 2026-11-03

- Initial release of master-vibe-coding.
- Added Chief AI Orchestrator and 14 specialist agents.
- Added 12 phased workflows from discovery to handover.
- Added 12 project templates, 6 GitHub guides and 10 quality gates.
- Added project workspace templates, validators and a simulation example.
- Added installation, usage, extension and platform adapter guides.
