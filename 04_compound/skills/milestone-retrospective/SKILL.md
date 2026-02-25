---
name: milestone-retrospective
description: "Conducts a retrospective at phase or milestone completion. Reviews what was built, checks success criteria, captures lessons learned. Use when a roadmap phase is complete or a milestone is reached."
---

# Milestone Retrospective

This skill conducts a structured retrospective when a roadmap phase is complete or a significant milestone is reached.

## When to Use This Skill

Use when:
- All plans in a roadmap phase are complete
- A milestone boundary is reached (as defined in ROADMAP.md)
- The project is complete (final retrospective)

Skip when:
- Mid-phase work (wait until the phase is done)
- No `.planning/` exists (task-level work doesn't have milestones)

## Reference

Read `references/retrospective-format.md` for the output template.

## Core Process

### Step 1: Gather Phase Accomplishments

<step number="1" required="true">

Read:
- `.planning/STATE.md` — metrics, decisions, blockers encountered
- `.planning/ROADMAP.md` — success criteria for the completed phase
- `docs/plans/summaries/` — completion summaries from executed plans
- Recent git log for the phase's time span

Compile a list of everything that was built, changed, or delivered.
</step>

### Step 2: Check Success Criteria

<step number="2" required="true" depends_on="1">

For each success criterion in ROADMAP.md for this phase:

| Criterion | Status | Evidence |
|-----------|--------|----------|
| [From ROADMAP.md] | met / partial / unmet | [How verified — test output, file exists, user confirmed] |

If any criteria are unmet, flag them:

```
These success criteria are not fully met:
- [Criterion]: [What's missing]

Options:
1. Mark phase complete anyway (criteria were aspirational)
2. Address remaining items before closing the phase
3. Carry forward to next phase

Which? (1 / 2 / 3)
```

Wait for user decision.
</step>

### Step 3: Run Retrospective

<step number="3" required="true" depends_on="2">

Analyze the phase execution for patterns:

**What worked well** — Practices, tools, decisions that should continue
**What was inefficient** — Time sinks, friction, avoidable rework
**Patterns discovered** — New patterns worth reusing, anti-patterns to avoid
**Lessons learned** — Key insights for future phases

Present the retrospective to the user for review and additions.
</step>

### Step 4: Update State

<step number="4" required="true" depends_on="3">

Update `.planning/STATE.md`:
- Mark current phase as complete
- Update performance metrics
- Record any accumulated decisions

Update `.planning/ROADMAP.md`:
- Set phase status to "done" with completion date
</step>

### Step 5: Archive and Advance

<step number="5" required="false" depends_on="4">

Save the retrospective to `.planning/milestones/`:
```
.planning/milestones/XX-phase-name-retrospective.md
```

Ask the user:
```
Phase [XX] retrospective complete.

Options:
1. View next phase and continue
2. Pause here (create continue-here file)
3. End project orchestration

Which?
```
</step>

## Success Criteria

- [ ] All phase success criteria evaluated with evidence
- [ ] Retrospective document produced with all sections
- [ ] STATE.md updated with phase completion
- [ ] ROADMAP.md progress table updated
- [ ] Retrospective archived to `.planning/milestones/`

## Integration

This skill is invoked by:
- `project-orchestrator.md` — after phase verification passes
- `04_compound/COMPOUND_PHASE.md` — when a roadmap phase boundary is reached
- Directly by the user at any time
