# Retrospective Format

Template for milestone retrospectives. Used by the `milestone-retrospective` skill.

## Template

```markdown
# Retrospective: [Phase Name]

## What Was Built
[2-5 bullet points describing deliverables in user-facing terms]

## Success Criteria Check
| Criterion (from ROADMAP.md) | Status | Evidence |
|------------------------------|--------|----------|
| [Criterion 1] | met / partial / unmet | [How verified] |
| [Criterion 2] | met / partial / unmet | [How verified] |

## What Worked Well
- [Practice or decision that should continue]
- [Tool or pattern that was effective]

## What Was Inefficient
- [Time sinks or friction points]
- [Avoidable rework or confusion]

## Patterns Discovered
- [New patterns worth reusing]
- [Anti-patterns to avoid in future phases]

## Lessons Learned
- [Key insight for future phases]
- [Adjustment to process or approach]

## Stats
- Plans executed: [N]
- Tasks completed: [N]
- Deviations: [N]
- Time span: [start date] to [end date]

## Recommendations for Next Phase
- [Specific suggestion based on lessons learned]
```

## When to Produce

- At the end of each roadmap phase (when all plans in the phase are complete)
- When a milestone is reached (as defined in ROADMAP.md)
- At project completion (final retrospective covering the whole project)

## Storage

Retrospectives are saved to `.planning/milestones/` in the consuming project:

```
.planning/milestones/XX-phase-name-retrospective.md
```
