# Project Orchestrator

Drives the full project lifecycle across roadmap phases. Wraps `orchestrator.md` (task loop) with phase sequencing, state management, and milestone tracking.

## When to Use

Use this orchestrator when:
- `.planning/` exists with ROADMAP.md and STATE.md
- The user wants to work through a project phase by phase
- Multi-phase, multi-plan work needs coordination

Use `orchestrator.md` directly when:
- No `.planning/` exists
- The user wants to run a single task through Plan → Work → Review → Compound
- Standalone task-level work

## Process

### 1. Check for `.planning/`

If `.planning/` does not exist:
- Ask the user: "No project lifecycle found. Would you like to set one up?"
- If yes: Run `00_init/INIT_PHASE.md`
- If no: Fall through to `orchestrator.md` for task-level work

### 2. Load Project State

Read:
- `.planning/STATE.md` — current position, blockers, metrics
- `.planning/ROADMAP.md` — phase structure, success criteria, progress
- `.planning/config.json` — workflow toggles, parallelization, confirmation gates

Extract model routing from `config.json`:
- `model_profile` (default: `"balanced"` if absent)
- `model_routing.provider` (default: `"anthropic"` if absent)

Resolve model names for this session using the profile:

| Role | quality | balanced | budget |
|------|---------|----------|--------|
| planning | opus | opus | sonnet |
| execution | opus | sonnet | sonnet |
| verification | sonnet | sonnet | haiku |
| debugging | opus | sonnet | sonnet |

Store as named references used throughout this session:
- **M_PLAN** = resolved model for planning role
- **M_EXEC** = resolved model for execution role
- **M_VERIFY** = resolved model for verification role
- **M_DEBUG** = resolved model for debugging role

If `model_routing.provider = "litellm"`:
- The Task tool still receives `opus`/`sonnet`/`haiku` — the LiteLLM proxy maps these to configured providers
- Check that `ANTHROPIC_BASE_URL=http://localhost:4000` is set; if not, warn the user before running any agents

Report current state to the user:

```
## Project Status

Phase: [current phase name]
Status: [planning / executing / reviewing / blocked]
Progress: [X/Y phases complete]

Next action: [what should happen next based on state]

Proceed? (yes / adjust / stop)
```

### 3. Phase Execution

For each task/plan in the current phase:

#### Sequential Mode (default)

For each plan in the phase:
1. Read the plan from `docs/plans/`
2. If `config.json` has `workflow.plan_check: true`, run `plan-checker` agent (model: M_VERIFY)
3. Invoke `orchestrator.md` to run the task loop (Plan → Work → Review → Compound)
4. After task loop completes, update `.planning/STATE.md` with progress

#### Parallel Mode (opt-in via `config.json`)

When `parallelization.enabled: true`:
1. Group plans by `wave` field in their frontmatter
2. Within a wave, run plans concurrently (skip per-agent confirmation gates within the wave)
3. Gate once per wave completion — present results and confirm before next wave
4. Requires at least `parallelization.min_plans_for_parallel` plans to activate

### 4. Phase Verification

After all plans in a phase are complete:

1. If `config.json` has `workflow.verifier: true`, run `verification-agent` at Levels 1-4 (model: M_VERIFY)
2. Check ROADMAP.md success criteria for the phase — are they met?
3. Update `.planning/STATE.md` — mark phase status

Present results:

```
## Phase [XX] Verification

Success criteria:
- [Criterion 1]: met / unmet
- [Criterion 2]: met / unmet

Verification: [passed / failed at level N]

[If all met]: Ready for milestone retrospective and next phase.
[If unmet]: These criteria need attention: [list]

Proceed? (retrospective / fix issues / stop)
```

### 5. Milestone Retrospective

If `config.json` has `confirmation_gates.phase_verification: true`:

1. Run `milestone-retrospective` skill from `04_compound/skills/milestone-retrospective/SKILL.md`
2. Archive phase artifacts if desired
3. Update ROADMAP.md progress table

### 6. Advance to Next Phase

1. Read ROADMAP.md for the next phase
2. Check dependencies — is the next phase unblocked?
3. Update STATE.md — set new active phase
4. Present the next phase to the user:

```
## Next Phase: [Phase Name]

Goal: [Phase goal from ROADMAP.md]
Requirements: [REQ-IDs addressed]
Success criteria:
- [Criterion 1]
- [Criterion 2]

Begin this phase? (yes / skip to phase N / stop)
```

5. If yes, return to Step 3 (Phase Execution)

### 7. Project Complete

When all roadmap phases are done:

1. Run final retrospective covering the whole project
2. Update STATE.md with final metrics
3. Create MILESTONE.md entry for the completed project

```
## Project Complete

All [N] phases finished.
Total plans executed: [N]
Total tasks completed: [N]

Final retrospective saved to .planning/milestones/

Congratulations!
```

## Confirmation Gates

Configurable via `config.json`. When enabled:

| Gate | When | Default |
|------|------|---------|
| `project_confirmation` | Before starting project execution | on |
| `phase_verification` | After phase completion, before retrospective | on |
| `roadmap_approval` | Before advancing to next phase | on |
| `plan_execution_review` | After each plan's task loop | on |
| `transition_confirmation` | Before major state transitions | on |

When `auto_advance: true` in config, confirmation gates are skipped (except `project_confirmation` which always requires approval).

## Session Management

If a session needs to pause mid-phase:
- Create a continue-here file per `05_session/SESSION_MANAGEMENT.md`
- Update STATE.md with current position
- On resume, read continue-here file and STATE.md to pick up where left off

## Important Rules

- Never modify ROADMAP.md success criteria during execution — they were approved during Init
- Always update STATE.md after completing a plan or phase
- Respect config.json toggles — don't run plan-checker if `plan_check: false`
- The task loop (`orchestrator.md`) handles individual plans; this orchestrator handles phase sequencing
- Projects can always drop back to task-level by ignoring `.planning/` — nothing breaks
