# Compound Phase

## Purpose

Capture knowledge from the completed work so future sessions benefit. Document solved problems, patterns discovered, and lessons learned.

## Inputs

- Completed, reviewed implementation
- The conversation history (problems encountered, solutions found)
- Existing docs in `docs/solutions/`

## Skills Available

Before running each skill, present it and wait for user approval:

```
Next skill: [skill-name]
Reason: [Why this skill is relevant]

Run this skill? (yes / skip / stop)
```

| Skill | When to use | Path |
|-------|------------|------|
| `compound-docs` | A non-trivial problem was solved during this work — document it for future reference | `skills/compound-docs/SKILL.md` |
| `document-review` | Documentation was created (plan, solution doc) — review it for clarity and completeness | `skills/document-review/SKILL.md` |

## Confirmation Gate

Before each skill invocation, present the skill name and a one-line reason. Wait for the user to approve (yes), skip, or stop the phase entirely.

## When to Compound

Not every task produces documentation. Compound when:
- A non-obvious problem was solved (future sessions would benefit)
- Multiple investigation attempts were needed before finding the solution
- A new pattern or convention was established
- A gotcha or pitfall was discovered

Skip compounding for:
- Trivial fixes (typos, obvious bugs)
- Work that produced no new insights

## Output

- Solution documentation in `docs/solutions/[category]/`
- Updated cross-references between related solutions
- Optionally, new entries in critical patterns

## Next Phase

Return to **Plan** for the next task, or end the session.
