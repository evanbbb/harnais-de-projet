## Overview

**Plan → Work → Review → Compound → Repeat**

harnais_de_projet is a collection of agent specs and skills that implement a compound engineering workflow. It lives separate from any project repo. When applying the harness to a project, the onboarding process creates a symlink from `docs/harness` to harnais_de_projet; the project then references that path via `docs/harness.md`.

### Two-Layer Orchestration

The harness operates at two levels:

1. **Task Level** (existing) — `orchestrator.md` runs Plan → Work → Review → Compound for a single unit of work. This works standalone without any project artifacts.

2. **Project Level** (optional) — `project-orchestrator.md` wraps the task loop with phase sequencing from a ROADMAP.md. It manages `.planning/` artifacts, milestone tracking, and cross-phase coordination.

```
PROJECT LIFECYCLE (project-orchestrator.md)
  00_init/  →  project setup, questioning, codebase mapping
  ↓
  For each ROADMAP phase:
    TASK LOOP (orchestrator.md)
      01_plan/ → 02_work/ → 03_review/ → 04_compound/
    ↓
  Milestone retrospective
  ↓
  Next phase or PROJECT COMPLETE
```

Projects can enter at either level — the task loop works standalone without `.planning/`.

### Philosophy

Each unit of engineering work should make subsequent units easier, not harder.

Traditional development accumulates technical debt — every feature adds complexity and the codebase becomes harder to work with over time. Compound engineering inverts this. 80% of effort goes to planning and review, 20% to execution:

- **Plan** thoroughly before writing code
- **Work** by following the plan, not freestyling
- **Review** to catch issues and capture learnings
- **Compound** knowledge so it's reusable

### How Consuming Projects Integrate

1. Run the onboarding process described in `harness-LOAD-THIS.md` (harness init).
2. Onboarding creates `docs/harness` as a symlink to harnais_de_projet, and creates `docs/harness.md` pointing to that symlink.
3. The project's `CLAUDE.md` (or similar) includes: `Read docs/harness.md for agent workflow instructions`.
4. Agents and skills are invoked by reading the relevant `.md` file from `docs/harness/` (e.g. `docs/harness/orchestrator.md`, `docs/harness/01_plan/agents/...`).
5. If the project uses Claude Code with `get-shit-done` commands, ensure `.claude/settings.local.json` allows `Bash(npx get-shit-done-cc@latest:*)` in that consuming repo.

To update the harness in a consuming project, follow `harness-CHECK-4-UPDATES.md` — it covers symlink migrations, template refreshes, and Claude Code permission checks for optional `get-shit-done` usage.

See `harness-LOAD-THIS.md` for full onboarding steps.

## CLI Compatibility

This harness is optimized for Claude Code but works with other AI CLIs. See `00_init/references/cli-compatibility.md` for tool equivalents and per-CLI guides. Agent files contain Claude-specific elements (`<commentary>` tags, named tool references) that are safely ignored by other CLIs.

## Folder Structure

```
harnais_de_projet/
├── orchestrator.md              # Task-level loop — Plan→Work→Review→Compound
├── project-orchestrator.md      # Project-level loop — phase sequencing from ROADMAP.md
├── harness-LOAD-THIS.md         # Onboarding instructions for new projects
├── harness-template.md          # Template for consuming project's docs/harness.md
├── 00_init/                     # Project lifecycle initialization (optional)
│   ├── INIT_PHASE.md
│   ├── agents/                  # project-questioner, codebase-mapper
│   ├── skills/                  # project-setup (creates .planning/)
│   └── references/              # questioning-methodology
├── 01_plan/                     # Planning phase — research, brainstorm, spec out work
│   ├── PLAN_PHASE.md
│   ├── agents/                  # Research agents + plan-checker, research-synthesizer
│   ├── skills/                  # brainstorming
│   └── references/              # plan-format, plan-checker-dimensions
├── 02_work/                     # Work phase — execute plans, write code and tests
│   ├── WORK_PHASE.md
│   ├── agents/                  # implementation-executor, test-writer, debugger
│   └── references/              # deviation-rules, summary-format, git-conventions
├── 03_review/                   # Review phase — validate quality, catch issues
│   ├── REVIEW_PHASE.md
│   ├── agents/                  # Review agents + verification-agent
│   └── references/              # verification-levels, stub-indicators
├── 04_compound/                 # Compound phase — capture knowledge for reuse
│   ├── COMPOUND_PHASE.md
│   ├── skills/                  # compound-docs, document-review, milestone-retrospective
│   └── references/              # retrospective-format
└── 05_session/                  # Cross-session management
    ├── SESSION_MANAGEMENT.md
    └── references/              # continue-here-format
```

### Agents vs Skills

- **Agents** are autonomous prompts designed for the Task tool. Give them a goal and they research, analyze, or validate independently.
- **Skills** are step-by-step processes with assets (templates, schemas). They guide Claude through a structured workflow with decision points.

## Consuming Project Structure

Projects that use harnais_de_projet should have the following docs structure. The `harness-LOAD-THIS.md` onboarding process creates this automatically (including linking `docs/harness` to harnais_de_projet):

```
project-root/
├── .planning/                    # Project lifecycle (optional — created by 00_init)
│   ├── PROJECT.md
│   ├── REQUIREMENTS.md
│   ├── ROADMAP.md
│   ├── STATE.md
│   ├── config.json
│   ├── milestones/               # Archived milestone retrospectives
│   ├── research/                 # Domain research outputs
│   └── phases/                   # Per-phase artifacts
├── docs/
│   ├── harness.md                # Points to local docs/harness/
│   ├── harness/                  # Symlink to harnais_de_projet
│   │   ├── orchestrator.md
│   │   ├── project-orchestrator.md
│   │   ├── 00_init/              # Project initialization (optional)
│   │   ├── 01_plan/              # Plan phase (agents, skills, references)
│   │   ├── 02_work/              # Work phase (agents, references)
│   │   ├── 03_review/            # Review phase (agents, references)
│   │   ├── 04_compound/          # Compound phase (skills, references)
│   │   ├── 05_session/           # Session management
│   │   └── AGENT_SKILL_DIRECTORY.md
│   ├── design-rules.md
│   ├── to-do.md
│   ├── memory/                   # Cross-session memory + continue-here files
│   ├── plans/
│   │   └── summaries/            # Completion summaries from work phase
│   ├── solutions/
│   └── structure/
```

When `.planning/` exists, the `project-orchestrator.md` drives phase-by-phase execution. When it doesn't, `orchestrator.md` runs standalone task loops. See `config.json` template in `00_init/skills/project-setup/templates/` for workflow configuration options.

### File Descriptions

- **harness.md** — The bridge between the project and the harness. Points to the symlinked harness path at `docs/harness/` and explains how to invoke agents and skills.
- **design-rules.md** — Design rules for the project. Updated when visual components change.
- **to-do.md** — Loose to-do list organized by priority (P1, P2, etc.).
- **memory/** — Working memory between context windows. Used during bug investigations or multi-session tasks. After a bug is solved, the solution moves to `solutions/`.
- **plans/** — Feature plans generated by AI agents during the Plan phase.
- **solutions/** — Compounded knowledge. Solved bugs and problems are documented here for future agents to reference.
- **structure/** — Documents the repo's structure at the project, component, and feature level.
