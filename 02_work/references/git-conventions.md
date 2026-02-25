# Git Conventions

Commit and branching conventions for work executed through the harness.

## Commit Format

Atomic, per-task commits using conventional commit format:

```
{type}({phase}-{plan}): {description}
```

**Types:**
| Type | When |
|------|------|
| `feat` | New feature or capability |
| `fix` | Bug fix |
| `test` | Adding or updating tests |
| `refactor` | Code change that doesn't add features or fix bugs |
| `perf` | Performance improvement |
| `chore` | Build process, dependencies, tooling |
| `docs` | Documentation only |

**Examples:**
```
feat(01-03): add login endpoint with JWT
test(01-03): add auth integration tests
fix(02-01): correct null check on user lookup
docs(01-03): add auth API documentation
```

The `{phase}-{plan}` scope is optional for standalone (non-project-managed) work. In that case, use a descriptive scope:

```
feat(auth): add login endpoint
```

## Atomic Commits

One commit per completed task. This means:
- Each task in a plan gets its own commit
- If a task touches 5 files, all 5 go in one commit
- Don't combine multiple tasks into one commit
- Don't split one task across multiple commits

## When to Commit

- After each task's `<verify>` command passes
- After completing a deviation fix (Rules 1-3)
- Before escalating (Rule 4) — commit what works so far

## Branching Strategy

Configured in `.planning/config.json` under `git.branching_strategy`:

- `none` — Commit directly to current branch (default)
- `feature` — Create feature branches per phase: `phase/XX-name`
- `plan` — Create branches per plan: `plan/XX-NN`

When no `.planning/config.json` exists, commit to the current branch.
