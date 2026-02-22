# harnais_de_projet

`harnais_de_projet` is a reusable agent workflow harness for running tasks through a four-phase loop:

1. Plan
2. Work
3. Review
4. Compound

It provides phase playbooks, specialized agents, and skills that can be copied into other projects and run locally.

## What this repository contains

- `orchestrator.md` - Main orchestration flow and phase sequencing
- `01_plan/` - Planning phase docs, agents, and skills
- `02_work/` - Implementation phase docs and agents
- `03_review/` - Review phase docs and agents
- `04_compound/` - Documentation/knowledge capture phase docs and skills
- `harness-LOAD-THIS.md` - Onboarding instructions for consuming projects
- `harness-template.md` - Template for wiring the harness into another repo

## Using this harness in another project

1. Open and follow `harness-LOAD-THIS.md`.

