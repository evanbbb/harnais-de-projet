## Harness

This project uses harnais_de_projet for its agent workflow.
Harness location: docs/harness (local copy)

### How to use
- Full task workflow: Read docs/harness/orchestrator.md
- Project lifecycle: Read docs/harness/project-orchestrator.md (requires .planning/)
- Single phase: Read the phase entry point for the phase you need:
  - Init: docs/harness/00_init/INIT_PHASE.md (project setup)
  - Plan: docs/harness/01_plan/PLAN_PHASE.md
  - Work: docs/harness/02_work/WORK_PHASE.md
  - Review: docs/harness/03_review/REVIEW_PHASE.md
  - Compound: docs/harness/04_compound/COMPOUND_PHASE.md
- Session management: Read docs/harness/05_session/SESSION_MANAGEMENT.md
- Specific agent: Read docs/harness/{phase}/agents/{name}.md (e.g. docs/harness/01_plan/agents/best-practices-researcher.md)

### Phases
- `00_init` — Project lifecycle setup (optional — creates .planning/)
- `01_plan` — Research, brainstorm, produce a plan
- `02_work` — Execute the plan, write code and tests
- `03_review` — Validate quality, catch issues
- `04_compound` — Document solutions for future reference
- `05_session` — Cross-session management (pause/resume)

### On session start

1. **Check for harness updates**: If docs/harness/AGENT_SKILL_DIRECTORY.md exists, read it and compare the `Harness version` at the top against the `last_seen_version` below. If the harness version is newer, tell the user: "Harness updated to version [X]. Read AGENT_SKILL_DIRECTORY.md for what's available. For update instructions, read harness-CHECK-4-UPDATES.md in the harness repo." Then update `last_seen_version` here to match.

2. If the user hasn't given a specific task, read `docs/to-do.md` and suggest the highest-priority item that isn't already in progress. Present it as a suggestion, not an action — wait for the user to confirm before starting work.

last_seen_version: 1.5

### Project docs (canonical structure)
- docs/design-rules.md — visual/design rules for this project
- docs/to-do.md — prioritized task list
- docs/memory/ — working memory across sessions (includes continue-here files)
- docs/plans/ — feature plans
- docs/plans/summaries/ — completion summaries from work phase
- docs/solutions/ — solved problems
- docs/structure/ — repo structure docs

### Project lifecycle (optional)
- .planning/PROJECT.md — project vision, requirements, constraints
- .planning/REQUIREMENTS.md — categorized requirements with REQ-IDs
- .planning/ROADMAP.md — phased execution plan with success criteria
- .planning/STATE.md — current project position and metrics
- .planning/config.json — workflow configuration (gates, parallelization, model profile)
