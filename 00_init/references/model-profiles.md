# Model Profiles

Recommended model assignments for each harness role. Configured in `.planning/config.json` under `model_profile`.

## Profiles

| Profile | Planning | Execution | Verification | Debugging |
|---------|----------|-----------|--------------|-----------|
| `quality` | Opus | Opus | Sonnet | Opus |
| `balanced` | Opus | Sonnet | Sonnet | Sonnet |
| `budget` | Sonnet | Sonnet | Haiku | Sonnet |

## Role Descriptions

- **Planning**: Research agents, plan creation, project-questioner, codebase-mapper
- **Execution**: implementation-executor, test-writer — following plans step by step
- **Verification**: plan-checker, verification-agent, review agents — validating work
- **Debugging**: debugger agent — scientific hypothesis-driven debugging

## When to Use Each

- **quality**: High-stakes projects, complex architectures, greenfield development where planning decisions have lasting impact
- **balanced** (default): Most projects — strong planning with cost-effective execution
- **budget**: Well-defined tasks, maintenance work, projects with tight cost constraints

## How It's Applied

The project-orchestrator reads `model_profile` from `config.json` and passes the appropriate model hint when invoking agents via the Task tool. Agents themselves use `model: inherit` in their frontmatter — the orchestrator controls which model runs.

When no `config.json` exists (standalone task mode), all agents use the inherited model from the parent conversation.
