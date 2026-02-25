# Summary Format

Template for SUMMARY.md produced after plan execution. Saved alongside the plan in `docs/plans/summaries/`.

## Template

```markdown
# Summary: [Plan Name]

## Status
[completed | partial | blocked]

## Duration
Started: YYYY-MM-DD HH:MM
Finished: YYYY-MM-DD HH:MM

## Tasks Completed
- [x] Task 1 name
- [x] Task 2 name
- [ ] Task 3 name (blocked — reason)

## What Was Built
[2-3 sentence description of the deliverable in plain language. What can the user do now that they couldn't before?]

## Deviations
[List any Rule 1-3 deviations from deviation-rules.md, or "None"]
- [Rule N]: [Description] → [Action taken]

## Files Changed
| File | Action | Description |
|------|--------|-------------|
| `src/path/file.ts` | created | New auth endpoint |
| `src/path/other.ts` | modified | Added login route |

## Key Decisions
[Decisions made during execution that weren't in the plan]
- [Decision]: [Rationale]

## Metrics
- Tests passing: [X/Y or N/A]
- Verify commands: [X/Y passed]

## Next Steps
[What should happen next — remaining work, follow-up tasks, or "None — plan fully complete"]
```

## When to Produce

- After every plan execution (complete or partial)
- After a plan is abandoned or blocked (note why)

## File Naming

`docs/plans/summaries/[plan-name]-summary.md`

Match the plan name from `docs/plans/[plan-name].md`.
