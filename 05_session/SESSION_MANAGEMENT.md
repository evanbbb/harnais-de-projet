# Session Management

Guidelines for pausing and resuming work across sessions.

## When to Pause

- The user says "stop", "pause", "let's pick this up later", or similar
- The conversation context is getting long and a fresh session would be more effective
- A natural stopping point between phases or plans
- End of a work session

## How to Pause

### 1. Save Current State

If `.planning/` exists:
- Update `.planning/STATE.md` with current position (active phase, plan, task)
- Record any in-flight decisions or blockers

### 2. Create Continue-Here File

Create a session handoff file following the template in `references/continue-here-format.md`:

```
docs/memory/continue-here-YYYY-MM-DD.md
```

Include:
- Current state (what's active, what's been done this session)
- What was in progress when pausing
- Next steps (specific enough to resume without re-reading everything)
- Blockers (if any)
- Key context the next session needs
- Files to review on resume

### 3. Confirm with User

```
Session paused. State saved to:
- .planning/STATE.md (updated)
- docs/memory/continue-here-YYYY-MM-DD.md (created)

To resume: Read docs/memory/continue-here-YYYY-MM-DD.md
```

## How to Resume

### 1. Find the Latest Continue-Here File

Look for the most recent `docs/memory/continue-here-*.md` file.

### 2. Read and Summarize

Read the continue-here file and present a summary:

```
## Resuming from [date]

Last session state:
- [Current state summary]
- [What was in progress]

Suggested next action:
- [First next step from the continue-here file]

Continue with this? (yes / different task / review context first)
```

### 3. Load Project State

If `.planning/` exists:
- Read `.planning/STATE.md` for project position
- Read `.planning/ROADMAP.md` for phase context
- Verify state matches the continue-here file

### 4. Resume Work

Based on user confirmation, either:
- Continue from where the last session left off
- Start a different task
- Review more context before deciding

## Reference

See `references/continue-here-format.md` for the full template.
