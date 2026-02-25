# Plan Phase

## Purpose

Research, brainstorm, and produce a written plan before any code is written. The plan becomes the source of truth for the Work phase.

## Inputs

- A task description or goal from the user
- Access to the project codebase
- Optionally, existing docs in `docs/structure/` and `docs/solutions/`

## Agents Available

Before running each agent, present it and wait for user approval:

```
Next agent: [agent-name]
Reason: [Why this agent is relevant to the current task]

Run this agent? (yes / skip / stop)
```

| Agent | When to use | Path |
|-------|------------|------|
| `repo-research-analyst` | Unfamiliar with the codebase or area being modified | `agents/repo-research-analyst.md` |
| `best-practices-researcher` | Need external patterns, examples, or prior art | `agents/best-practices-researcher.md` |
| `framework-docs-researcher` | Working with a framework/library — need official docs or source exploration | `agents/framework-docs-researcher.md` |
| `spec-flow-analyzer` | Need to map user flows, identify spec gaps, or trace data through the system | `agents/spec-flow-analyzer.md` |
| `plan-checker` | A plan has been drafted — validate across 8 quality dimensions | `agents/plan-checker.md` |
| `research-synthesizer` | Multiple research agents ran — combine their outputs into prioritized synthesis | `agents/research-synthesizer.md` |

### Skills

| Skill | When to use | Path |
|-------|------------|------|
| `brainstorming` | Open-ended problem that benefits from exploring multiple approaches | `skills/brainstorming/SKILL.md` |

Not every agent runs every time. Select based on what the task needs.

## Confirmation Gate

Before each agent invocation, present the agent name and a one-line reason. Wait for the user to approve (yes), skip, or stop the phase entirely.

## Per-Agent Completion Gate

After each agent runs and produces actionable output (findings, recommendations, gaps to address), ask the user if they want to incorporate or act on those items before moving to the next agent. Do not advance until they have done so or explicitly skipped.

## Plan Format

When managed by the project lifecycle (`.planning/` exists), plans should include YAML frontmatter and XML task format. See `references/plan-format.md` for the full specification.

For standalone plans (no `.planning/`), frontmatter and XML tasks are optional but recommended.

## Output

A plan file saved to `docs/plans/` in the consuming project. The plan should include:
- Clear goal statement
- Step-by-step implementation approach (XML `<task>` blocks when project-managed)
- Files to create or modify
- Acceptance criteria
- Any open questions or risks
- YAML frontmatter with REQ-IDs and must_haves (when project-managed)

## Next Phase

**Work** (`02_work/WORK_PHASE.md`) — Execute the plan.
