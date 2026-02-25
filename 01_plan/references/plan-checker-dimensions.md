# Plan Checker Dimensions

8 dimensions for validating plan quality. Used by the `plan-checker` agent.

## 1. Requirement Coverage

Does the plan address all REQ-IDs listed in its frontmatter?

- Every requirement in `requirements:` must map to at least one task
- No task should address requirements not listed in the frontmatter
- **Pass**: All listed REQ-IDs are covered by tasks
- **Fail**: Missing coverage or phantom requirements

## 2. Task Completeness

Is each task well-defined enough to execute without guessing?

- Every `<task>` has `name`, `files`, `action`, `verify`, and `done`
- `action` is specific — not vague ("implement the feature") but concrete ("add a POST /api/login endpoint that accepts email and password")
- `files` lists actual paths, not placeholders
- **Pass**: All tasks have complete, specific fields
- **Fail**: Missing fields or vague instructions

## 3. Dependency Correctness

Are `depends_on` and task ordering consistent?

- Tasks that read output from other tasks must depend on them
- No circular dependencies
- `depends_on` in frontmatter matches actual data flow between plans
- **Pass**: Dependencies reflect real execution order
- **Fail**: Missing dependency, circular reference, or unnecessary dependency

## 4. Key Links

Are critical connections between components identified?

- `must_haves.key_links` lists connections that could break if either side changes
- Examples: API endpoint ↔ client call, DB schema ↔ model, route ↔ handler
- **Pass**: Key integration points are identified
- **Fail**: Obvious connections missing from key_links

## 5. Scope

Is the plan appropriately sized?

- Ideal: 2-3 tasks per plan
- Acceptable: 1-5 tasks
- **Pass**: Plan has 1-5 focused tasks
- **Fail**: Plan has 0 tasks, or 6+ tasks that should be split

## 6. Must-Haves Derivation

Are must_haves observable and derived from requirements?

- `truths` describe user-visible behaviors ("user can log in with email and password")
- `artifacts` are files that must exist ("src/routes/auth.ts", "tests/auth.test.ts")
- Neither field contains implementation details — they describe outcomes
- **Pass**: Must-haves are observable, not implementation-prescriptive
- **Fail**: Must-haves are vague, unverifiable, or describe internal implementation

## 7. Context Compliance

Does the plan respect project constraints and conventions?

- Check against `.planning/PROJECT.md` constraints (if present)
- Check against `docs/design-rules.md` (if relevant)
- Check against existing codebase patterns (naming, file organization)
- **Pass**: Plan aligns with documented constraints and conventions
- **Fail**: Plan contradicts stated constraints or ignores conventions

## 8. Nyquist Validation

Does every task have an automated verification step?

Named after the Nyquist sampling theorem — you need to measure at least as often as things can go wrong. Every task must have a `<verify>` command that:

- Runs in under 60 seconds
- Returns a clear pass/fail signal (exit code 0 = pass)
- Actually tests the task's completion, not something unrelated
- **Pass**: Every task has a meaningful, fast verify command
- **Fail**: Missing verify, verify takes too long, or verify doesn't test what the task does

## Scoring

Each dimension is **pass** or **fail** with specific issues listed. The plan-checker agent should:

1. Evaluate all 8 dimensions
2. Report pass/fail per dimension with specific issues
3. Suggest fixes for each failure
4. Allow up to 3 revision iterations
5. Escalate to user if plan still fails after 3 iterations
