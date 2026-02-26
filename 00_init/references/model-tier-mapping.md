# Model Tier Mapping

Provider-agnostic model tiers for the harness. Update this table as new models are released.

See `model-profiles.md` for how tiers map to harness roles, and `litellm-config.md` for routing configuration.

---

## Tier Definitions

| Tier | Capability Level | Typical Use in Harness |
|------|-----------------|----------------------|
| **Tier 1 (flagship)** | Complex reasoning, architecture, multi-step planning | Planning agents, debugger, plan-checker |
| **Tier 2 (balanced)** | Solid implementation, code review, structured tasks | Implementation-executor, test-writer, review agents |
| **Tier 3 (fast)** | Quick verification, simple checks, formatting | Verification-agent, simple lookups |

---

## Provider Model Mapping

| Tier | Claude (Anthropic) | OpenAI | Kimi (Moonshot) | Google (Gemini) |
|------|-------------------|--------|-----------------|-----------------|
| **Tier 1** (flagship) | Opus 4 | GPT-4o | K2.5 | Gemini 2.5 Pro |
| **Tier 2** (balanced) | Sonnet 4 | GPT-4o-mini | K2 | Gemini 2.0 Pro |
| **Tier 3** (fast) | Haiku 3.5 | — | — | Gemini 2.0 Flash |

### Notes

- **Claude** is the primary, fully-tested provider. Other providers are supported via LiteLLM routing.
- **Tier 3** has limited options outside Anthropic and Google. If no Tier 3 model is available for your provider, the tier falls back to Tier 2.
- Model names in this table are shorthand. See `litellm-config.md` for full model identifiers used in LiteLLM configuration.
- **Google (Gemini CLI)**: Gemini CLI users access these models directly via the `-m` flag without LiteLLM.
- This table reflects models available as of early 2026. Update entries as providers release new models.

---

## How to Update This Table

When a new model is released:

1. Determine which tier it fits based on the capability descriptions above
2. Add it to the appropriate row in the Provider Model Mapping table
3. If using LiteLLM, add a corresponding entry to your `litellm_config.yaml`
4. Test the model on a few representative tasks before relying on it for production work
