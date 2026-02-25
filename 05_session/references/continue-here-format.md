# Continue-Here Format

Template for session handoff files. Created when pausing work so the next session can resume efficiently.

## Template

```markdown
# Continue Here — YYYY-MM-DD

## Current State
[One paragraph: what phase/plan/task is active, what's been accomplished this session]

## What Was In Progress
- [Specific task or action that was underway when the session paused]
- [Any partially completed steps]

## Next Steps
1. [Immediate next action — be specific enough to resume without re-reading everything]
2. [Following action]
3. [etc.]

## Blockers
[List any blockers that prevented further progress, or "None"]
- [Blocker]: [What's needed to unblock]

## Key Context
[Any non-obvious context the next session needs — decisions made, gotchas encountered, important findings]

## Files to Review
[Files the next session should read to get up to speed]
- `path/to/file` — [why]
```

## When to Create

- User says "stop", "pause", "let's pick this up later"
- Context is getting long and a fresh session would be more effective
- Natural stopping point between phases or plans
- End of a work session

## File Location

```
docs/memory/continue-here-YYYY-MM-DD.md
```

If multiple sessions happen on the same day, append a sequence number:
```
docs/memory/continue-here-YYYY-MM-DD-02.md
```

## How to Resume

1. Read the most recent `continue-here-*.md` file in `docs/memory/`
2. Summarize the current state to the user
3. Confirm the next action before proceeding
4. Archive or delete the continue-here file once work resumes (optional — user preference)
