# Init Phase

## Purpose

Initialize a project for lifecycle management. This phase creates the `.planning/` directory with project definition, requirements, roadmap, and configuration. It only runs once per project — after that, work flows through the Plan → Work → Review → Compound loop.

## Two Modes

### New Project

Start from scratch with dream extraction and requirement discovery.

1. Run `project-questioner` agent — conversational exploration of vision, users, constraints, success criteria
2. Optionally run `codebase-mapper` agent — if there's existing code to build on
3. Run `project-setup` skill — creates `.planning/` artifacts from questioner output

### Adopt Existing

Bring an existing codebase under project lifecycle management.

1. Run `codebase-mapper` agent — analyze current state through 4 lenses
2. Run `project-questioner` agent — understand what comes next (shorter session, focused on future work)
3. Run `project-setup` skill — creates `.planning/` artifacts incorporating existing state

## Agents Available

Before running each agent, present it and wait for user approval:

```
Next agent: [agent-name]
Reason: [Why this agent is relevant]

Run this agent? (yes / skip / stop)
```

| Agent | When to use | Path |
|-------|------------|------|
| `project-questioner` | Starting a new project or defining future direction for an existing one | `agents/project-questioner.md` |
| `codebase-mapper` | Existing code needs to be understood for planning | `agents/codebase-mapper.md` |

## Skills Available

| Skill | When to use | Path |
|-------|------------|------|
| `project-setup` | Questioner output is ready and `.planning/` needs to be created | `skills/project-setup/SKILL.md` |

## Confirmation Gate

Before each agent or skill invocation, present the name and a one-line reason. Wait for the user to approve (yes), skip, or stop.

## Per-Agent Completion Gate

After each agent runs and produces output, ask the user if they want to refine or proceed before moving to the next agent or skill.

## Skipping This Phase

This phase is optional. Projects can use the task-level loop (Plan → Work → Review → Compound) without project lifecycle management. If the user declines project setup, proceed directly to `01_plan/PLAN_PHASE.md`.

## Output

- `.planning/PROJECT.md` — Vision, requirements, constraints
- `.planning/REQUIREMENTS.md` — Categorized requirements with REQ-IDs
- `.planning/ROADMAP.md` — Phased execution plan with success criteria
- `.planning/STATE.md` — Current position tracker
- `.planning/config.json` — Workflow configuration

## Next Phase

**Plan** (`01_plan/PLAN_PHASE.md`) — Create plans for the first roadmap phase.
