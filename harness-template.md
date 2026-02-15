## Harness

This project uses harnais_de_projet for its agent workflow.
Harness location: /path/to/harnais_de_projet

### How to use
- Full workflow: Read /path/to/harnais_de_projet/orchestrator.md
- Single phase: Read /path/to/harnais_de_projet/{phase}/PHASE.md
- Specific agent: Read /path/to/harnais_de_projet/{phase}/agents/{name}.md

### Phases
- `01_plan` — Research, brainstorm, produce a plan
- `02_work` — Execute the plan, write code and tests
- `03_review` — Validate quality, catch issues
- `04_compound` — Document solutions for future reference

### On session start

1. **Check for harness updates**: Read `AGENT_SKILL_DIRECTORY.md` from the harness location and compare the `Harness version` at the top against the `last_seen_version` below. If the harness version is newer, tell the user: "Harness updated to version [X]. Read AGENT_SKILL_DIRECTORY.md for what's available." Then update `last_seen_version` here to match.

2. If the user hasn't given a specific task, read `docs/to-do.md` and suggest the highest-priority item that isn't already in progress. Present it as a suggestion, not an action — wait for the user to confirm before starting work.

last_seen_version: 1.0

### Project docs (canonical structure)
- docs/design-rules.md — visual/design rules for this project
- docs/to-do.md — prioritized task list
- docs/memory/ — working memory across sessions
- docs/plans/ — feature plans
- docs/solutions/ — solved problems
- docs/structure/ — repo structure docs
