# LiteLLM Configuration

LiteLLM is an open-source proxy that provides a unified OpenAI-compatible API across 100+ LLM providers. Using LiteLLM with the harness enables multi-provider model routing, cost optimization, and provider fallbacks.

---

## Why LiteLLM

- **Cost savings**: Route fast/simple tasks to cheaper models (Haiku, GPT-4o-mini) while reserving flagship models for planning and debugging
- **Provider fallbacks**: If one provider is down or rate-limited, automatically fall back to another
- **Unified API**: All CLIs connect to one endpoint regardless of which provider actually serves the request
- **Budget controls**: Set spend limits per model, per day, or per project

---

## Recommended Configuration

Create a `litellm_config.yaml` with tier-based model groups that match the harness model profiles (see `model-tier-mapping.md`):

```yaml
model_list:
  # Tier 1 — Flagship: complex reasoning, planning, debugging
  - model_name: "tier-1-flagship"
    litellm_params:
      model: "anthropic/claude-opus-4"
      api_key: "os.environ/ANTHROPIC_API_KEY"
  - model_name: "tier-1-flagship"
    litellm_params:
      model: "openai/gpt-4o"
      api_key: "os.environ/OPENAI_API_KEY"
  - model_name: "tier-1-flagship"
    litellm_params:
      model: "openai/kimi-k2.5"
      api_base: "https://api.moonshot.cn/v1"
      api_key: "os.environ/MOONSHOT_API_KEY"

  # Tier 2 — Balanced: implementation, reviews
  - model_name: "tier-2-balanced"
    litellm_params:
      model: "anthropic/claude-sonnet-4"
      api_key: "os.environ/ANTHROPIC_API_KEY"
  - model_name: "tier-2-balanced"
    litellm_params:
      model: "openai/gpt-4o-mini"
      api_key: "os.environ/OPENAI_API_KEY"

  # Tier 3 — Fast: verification, quick checks
  - model_name: "tier-3-fast"
    litellm_params:
      model: "anthropic/claude-haiku-4-5"
      api_key: "os.environ/ANTHROPIC_API_KEY"
  - model_name: "tier-3-fast"
    litellm_params:
      model: "google/gemini-2.0-flash"
      api_key: "os.environ/GOOGLE_API_KEY"

# Fallback chain: if tier-1 fails, try tier-2, then tier-3
router_settings:
  routing_strategy: "cost-based-routing"  # cheapest available model first
  num_retries: 2
  fallbacks:
    - tier-1-flagship: ["tier-2-balanced"]
    - tier-2-balanced: ["tier-3-fast"]
```

---

## Running the Proxy

```bash
# Install
pip install litellm[proxy]

# Start the proxy server
litellm --config litellm_config.yaml --port 4000
```

The proxy runs at `http://localhost:4000` and accepts OpenAI-compatible API calls.

---

## Per-CLI Connection

### Claude Code

```bash
# Set the base URL to point at LiteLLM
export ANTHROPIC_BASE_URL=http://localhost:4000
```

Note: Claude Code expects Anthropic-format requests. LiteLLM handles the translation, but verify compatibility with your LiteLLM version.

### Cursor

In Cursor settings, configure the OpenAI-compatible endpoint:
- API Base URL: `http://localhost:4000`
- Model name: `tier-2-balanced` (or whichever tier you want as default)

### Aider

```bash
aider --openai-api-base http://localhost:4000 --openai-api-key "any-string" --model tier-2-balanced
```

### Cline

Configure the OpenAI-compatible provider in Cline's settings:
- Base URL: `http://localhost:4000`
- Model: `tier-2-balanced`

---

## Cost Comparison (Approximate)

Prices are per 1M tokens (input/output). Check provider pricing pages for current rates.

| Tier | Model | Input | Output |
|------|-------|-------|--------|
| **Tier 1** | Claude Opus 4 | $15 | $75 |
| **Tier 1** | GPT-4o | $2.50 | $10 |
| **Tier 1** | Kimi K2.5 | ~$2 | ~$8 |
| **Tier 2** | Claude Sonnet 4 | $3 | $15 |
| **Tier 2** | GPT-4o-mini | $0.15 | $0.60 |
| **Tier 3** | Claude Haiku 3.5 | $0.80 | $4 |
| **Tier 3** | Gemini Flash | $0.075 | $0.30 |

With cost-based routing, LiteLLM automatically selects the cheapest available model within a tier, potentially reducing costs significantly for Tier 1 and Tier 2 tasks.

---

## Integration with Harness Model Profiles

The harness `model_profile` setting in `config.json` maps roles to tiers:

| Profile | Planning | Execution | Verification | Debugging |
|---------|----------|-----------|--------------|-----------|
| `quality` | Tier 1 | Tier 1 | Tier 2 | Tier 1 |
| `balanced` | Tier 1 | Tier 2 | Tier 2 | Tier 2 |
| `budget` | Tier 2 | Tier 2 | Tier 3 | Tier 2 |

When `config.json` sets `"provider": "litellm"`, the orchestrator uses tier names (e.g., `tier-1-flagship`) instead of brand-specific model names. See `model-profiles.md` and `model-tier-mapping.md` for the full mapping.
