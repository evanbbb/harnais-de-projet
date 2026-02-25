---
name: project-setup
description: "Creates .planning/ directory with project definition, requirements, roadmap, state, and configuration. Use after the project-questioner has produced output, or when the user wants to set up project lifecycle management."
---

# Project Setup

This skill creates the `.planning/` directory and populates it with project lifecycle artifacts from templates.

## When to Use This Skill

Use when:
- The project-questioner agent has produced a project understanding summary
- The user wants to set up project lifecycle management for an existing project
- A project needs `.planning/` artifacts created from scratch

Skip when:
- `.planning/` already exists and is populated
- The user only wants task-level workflow (no project lifecycle)

## Core Process

### Step 1: Gather Input

Read the project-questioner output (or brainstorming notes, user description, codebase-mapper report). You need:
- Vision / purpose
- Requirements with acceptance criteria
- Success criteria
- Constraints
- Scope (v1 vs future)

If no questioner output exists, ask the user to describe the project briefly. Minimum needed: what it does, who it's for, what's most important.

### Step 2: Create `.planning/PROJECT.md`

<step number="1" required="true">

Read the template at `templates/PROJECT.md`.

Populate it with:
- Vision from questioner output
- Core value (single most important thing)
- Requirements table — assign REQ-IDs (REQ-001, REQ-002, etc.)
- Constraints from questioner output
- Users and success criteria

**Confirmation gate**: Present the draft PROJECT.md to the user.

```
Here's the project definition. Review it:
[Draft content]

Accept this? (yes / edit / stop)
```

Wait for approval before proceeding.
</step>

### Step 3: Create `.planning/REQUIREMENTS.md`

<step number="2" required="true" depends_on="1">

Read the template at `templates/REQUIREMENTS.md`.

Extract requirements from PROJECT.md and categorize:
- **v1 (Must Have)**: Core requirements for first usable version
- **v2 (Should Have)**: Important but deferrable
- **Out of Scope**: Explicitly excluded

Each requirement gets:
- REQ-ID (consistent with PROJECT.md)
- Category (core / feature / integration)
- Acceptance criteria

**Confirmation gate**: Present the requirements to the user.

```
Here are the categorized requirements. Review:
[Draft content]

Accept this? (yes / edit / stop)
```
</step>

### Step 4: Create `.planning/ROADMAP.md`

<step number="3" required="true" depends_on="2">

Read the template at `templates/ROADMAP.md`.

Break requirements into phases:
- Each phase delivers independently valuable functionality
- 2-5 success criteria per phase (observable, not aspirational)
- Map REQ-IDs to phases
- Note dependencies between phases

**Confirmation gate**: Present the roadmap to the user.

```
Here's the proposed roadmap. Review:
[Draft content]

Accept this? (yes / edit / stop)
```
</step>

### Step 5: Create `.planning/STATE.md` and `.planning/config.json`

<step number="4" required="true" depends_on="3">

Read templates at `templates/STATE.md` and `templates/config.json`.

- STATE.md: Set current position to Phase 01, status "planning"
- config.json: Use defaults unless the user has expressed preferences about workflow toggles

Present config.json options to the user:

```
Default configuration:
- Mode: interactive (confirm before each agent)
- Plan checking: enabled
- Verification: enabled
- Parallelization: disabled
- Git branching: none (commit to current branch)
- Model profile: balanced

Adjust any settings? (accept defaults / customize)
```

If the user wants to customize, walk through each setting.
</step>

### Step 6: Create Directory Structure

<step number="5" required="true" depends_on="4">

Create the supporting directories:

```
.planning/
├── milestones/
├── research/
└── phases/
```

Also ensure `docs/plans/summaries/` exists for work phase summaries.
</step>

## Success Criteria

- [ ] `.planning/PROJECT.md` exists with vision, requirements, constraints
- [ ] `.planning/REQUIREMENTS.md` exists with categorized REQ-IDs
- [ ] `.planning/ROADMAP.md` exists with phased plan and success criteria
- [ ] `.planning/STATE.md` exists with current position set
- [ ] `.planning/config.json` exists with workflow configuration
- [ ] Supporting directories created
- [ ] User has approved each artifact

## Integration

This skill is invoked by:
- `00_init/INIT_PHASE.md` — after project-questioner produces output
- `project-orchestrator.md` — when `.planning/` doesn't exist yet

After completion, the project is ready for the Plan phase (`01_plan/PLAN_PHASE.md`).
