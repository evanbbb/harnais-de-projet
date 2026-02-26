# Model Profiles

Recommended model assignments for each harness role. Configured in `.planning/config.json` under `model_profile`.

## Profiles

| Profile | Planning | Execution | Verification | Debugging |
|---------|----------|-----------|--------------|-----------|
| `quality` | Tier 1 | Tier 1 | Tier 2 | Tier 1 |
| `balanced` | Tier 1 | Tier 2 | Tier 2 | Tier 2 |
| `budget` | Tier 2 | Tier 2 | Tier 3 | Tier 2 |

### Default Tier Mapping (Claude)

| Tier | Claude Model |
|------|-------------|
| Tier 1 (flagship) | Opus |
| Tier 2 (balanced) | Sonnet |
| Tier 3 (fast) | Haiku |

For other providers and full tier definitions, see `model-tier-mapping.md`. For multi-provider routing via LiteLLM, see `litellm-config.md`.

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

When `config.json` sets `"provider": "litellm"`, the orchestrator uses tier names (e.g., `tier-1-flagship`) instead of brand-specific model names, enabling multi-provider routing through a LiteLLM proxy.

When no `config.json` exists (standalone task mode), all agents use the inherited model from the parent conversation.
