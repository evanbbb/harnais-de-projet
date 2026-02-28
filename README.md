# harnais_de_projet

`harnais_de_projet` is a reusable agent workflow harness for AI-driven software engineering. It provides two layers of orchestration.

## Two-Layer Workflow

### Task Level (standalone)

Run a single task through a four-phase loop:

1. **Plan** — Research, brainstorm, produce a plan
2. **Work** — Execute the plan, write code and tests
3. **Review** — Validate quality, catch issues
4. **Compound** — Document solutions for future reference

Entry point: `orchestrator.md`

### Project Level (optional)

Manage a full project lifecycle with phased execution:

1. **Init** — Extract vision, define requirements, create roadmap
2. **For each roadmap phase** — Run task loops (Plan → Work → Review → Compound)
3. **Milestone** — Retrospective, success criteria check, advance to next phase
4. **Complete** — Final retrospective and project wrap-up

Entry point: `project-orchestrator.md` (requires `.planning/` directory)

## What this repository contains

- `orchestrator.md` — Task-level orchestration (Plan → Work → Review → Compound)
- `project-orchestrator.md` — Project-level orchestration (phase sequencing from roadmap)
- `00_init/` — Project initialization: questioning, codebase mapping, project setup
- `01_plan/` — Planning phase: research agents, plan validation, brainstorming
- `02_work/` — Implementation phase: execution, debugging, deviation handling
- `03_review/` — Review phase: verification, simplicity, patterns, performance
- `04_compound/` — Knowledge capture: documentation, retrospectives
- `05_session/` — Cross-session management: pause/resume with context handoff
- `harness-LOAD-THIS.md` — Onboarding instructions for consuming projects
- `harness-template.md` — Template for wiring the harness into another repo
- `harness-CHECK-4-UPDATES.md` — Update instructions for consuming projects

## Using this harness in another project

1. Open and follow `harness-LOAD-THIS.md`.

## Key concepts

- **Agents** — Autonomous prompts for the Task tool (research, analyze, validate)
- **Skills** — Step-by-step processes with templates and decision points
- **References** — Standalone docs that agents and skills point to for methodology
- **`.planning/`** — Optional project lifecycle artifacts (`PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, `config.json`)
