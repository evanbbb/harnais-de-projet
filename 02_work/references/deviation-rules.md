# Deviation Rules

Rules for handling unexpected situations during plan execution. Referenced by the `implementation-executor` agent.

## The 4 Rules

### Rule 1: Auto-Fix Blocking Issues

**When**: Code won't compile, null reference crashes, syntax errors — things that prevent the current step from working.

**Action**: Fix inline. Note the deviation in the step report.

**Examples**:
- Missing semicolon or bracket
- Null reference on an object the plan assumed existed
- Type mismatch between plan expectation and actual code

### Rule 2: Add Missing Critical Elements

**When**: The plan omits something that would make the code unsafe or obviously broken — no password hashing, no error handling on a network call, no input validation on user-facing input.

**Action**: Add the minimal fix. Flag it in the step report as an addition beyond the plan.

**Examples**:
- Plan says "store password" but doesn't mention hashing — add bcrypt
- Plan calls an API but has no error handling — add try/catch with basic error
- Plan accepts user input with no validation — add basic sanitization

### Rule 3: Fix Environmental Blockers

**When**: Something in the environment prevents execution — missing dependency, wrong import path, config file not where expected.

**Action**: Fix immediately. Note in the step report.

**Examples**:
- Package not installed that the plan references
- Import path is wrong (file moved since plan was written)
- Environment variable referenced but not in `.env.example`

### Rule 4: Escalate Architectural Decisions

**When**: The fix would require a design decision the plan didn't anticipate — new database table, framework switch, changing a public API contract, new service dependency.

**Action**: **STOP.** Report to the user with:
- What you encountered
- Why it's beyond auto-fix scope
- 2-3 options with trade-offs

**Examples**:
- Plan assumes a table exists but it doesn't — creating it is a schema decision
- Plan's approach conflicts with a framework constraint — need a different pattern
- Plan requires a third-party service that isn't configured

## Attempt Limits

- **Max 3 auto-fix attempts per task** (Rules 1-3)
- If a task still fails after 3 attempts, escalate to the user regardless of rule
- Each attempt should try a different approach, not repeat the same fix

## Reporting

All deviations (Rules 1-3) must appear in the step completion report:

```
## Deviation Log
- [Rule N]: [What happened] → [What was done]
```

Rule 4 escalations produce a separate report with options for the user.
