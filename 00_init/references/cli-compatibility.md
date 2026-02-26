# CLI Compatibility

This harness is optimized for Claude Code but works with other AI coding CLIs. This document maps harness concepts to each CLI's equivalents and provides quick-start guidance.

---

## Feature Matrix

| Harness Concept | Claude Code | Cursor | Aider | Cline | Codex | Gemini CLI | Antigravity |
|----------------|-------------|--------|-------|-------|-------|------------|-------------|
| **Agent dispatch** | Task tool (launches subagent) | `@file` to inject agent `.md` into context | `/read` to load agent `.md` into context | Context injection via file reference | `[agents.<role>]` with `config_file` | Load `.md` via `GEMINI.md` or `--include-directories` | Skills in `.agents/skills/` + Agent Manager |
| **File search** | Glob tool | Built-in file search | Built-in file search | Built-in file search | Built-in file search | Built-in file search | Built-in file search |
| **File read** | Read tool | Built-in file read | Built-in file read | Built-in file read | Built-in file read | Built-in file read | Built-in file read |
| **Content search** | Grep tool | Built-in code search | Built-in code search | Built-in code search | Built-in code search | Built-in code search + Google Search grounding | Built-in code search + browser subagent |
| **MCP (Context7)** | Native MCP support | Use web search or direct docs URLs | Use web search or direct docs URLs | MCP support (varies by version) | Use web search or direct docs URLs | Native MCP support via `settings.json` | Use web search or direct docs URLs |
| **`model: inherit`** | Orchestrator controls model | Ignored (uses configured model) | Ignored (uses configured model) | Ignored (uses configured model) | Override via `model` in role `.toml` | Ignored (uses `-m` flag model) | Per-conversation model dropdown |
| **`<commentary>` tags** | Rendered as agent thinking | Ignored (harmless) | Ignored (harmless) | Ignored (harmless) | Ignored (harmless) | Ignored (harmless) | Ignored (harmless) |
| **Named tool refs** | Exact tool names (Edit, Write, etc.) | CLI uses its own tool names | CLI uses its own tool names | CLI uses its own tool names | CLI uses its own tool names | CLI uses its own tool names | CLI uses its own tool names |

---

## Agent Dispatch Without the Task Tool

In Claude Code, the orchestrator uses the Task tool to launch agents as independent subprocesses. Codex and Antigravity both have native multi-agent systems that map closely (see their sections below). Other CLIs don't have this mechanism, but the agents still work:

**The prompt IS the agent.** Each agent `.md` file is a self-contained prompt. To "dispatch" an agent in any CLI:

1. Load the agent file into your context (method varies by CLI — see below)
2. Provide the agent with its required inputs (described in the agent file's header)
3. The agent's instructions guide the model through the task

The main difference: in Claude Code, agents run in isolated context windows. In other CLIs, agents share your main context, which means you may hit context limits sooner on complex multi-agent workflows.

---

## MCP Fallback

Some agents reference Context7 (an MCP server) for fetching live framework documentation. If your CLI doesn't support MCP:

- **Use web search**: Most CLIs have web search capabilities. Search for the same documentation the agent would fetch via Context7.
- **Use direct URLs**: Paste documentation URLs directly into your context.
- **Pre-fetch docs**: Download relevant documentation pages and load them as local files.

Context7 references in agent files are non-blocking — agents will work without them, just with less up-to-date framework documentation.

---

## Per-CLI Quick Start

### Cursor

Cursor works well with the harness since it can inject files directly into context using `@file` references.

To use an agent: type `@docs/harness/01_plan/agents/repo-research-analyst.md` in the chat to load the agent prompt, then describe your task. For the orchestrator workflow, load `@docs/harness/orchestrator.md` and follow its instructions manually — Cursor will handle the file operations using its built-in tools. Set your preferred model in Cursor's settings; `model: inherit` lines in agent frontmatter are ignored.

### Aider

Aider can load harness files using the `/read` command, which adds files to the chat context without marking them for editing.

To use an agent: run `/read docs/harness/01_plan/agents/repo-research-analyst.md` to load the agent, then describe your task. For multi-agent workflows, load the orchestrator with `/read docs/harness/orchestrator.md` and step through phases manually. Aider's `--model` flag controls which model runs; agent frontmatter model hints are ignored. Use `--openai-api-base` to point at a LiteLLM proxy for multi-provider routing (see `litellm-config.md`).

### Cline

Cline supports context injection through its file reference mechanism and has growing MCP support.

To use an agent: reference the agent `.md` file in your prompt to inject it into context. Cline will follow the agent's instructions using its built-in file and terminal tools. For the orchestrator workflow, reference `docs/harness/orchestrator.md` and follow the phase sequence. Cline manages its own tool naming, so references to Claude-specific tool names (Read, Write, Grep, etc.) in agent files are automatically mapped to Cline's equivalents.

### Gemini CLI

Gemini CLI is Google's open-source AI agent for the terminal. It has native MCP support, Google Search grounding, and a 1M token context window — making it one of the more capable non-Claude options for the harness.

**Setup**: Create a `GEMINI.md` file in your project root (Gemini's equivalent of `CLAUDE.md`) that points to the harness:

```markdown
Read docs/harness.md for agent workflow instructions.
```

To use an agent: ask Gemini to read the agent `.md` file (e.g., "Read `docs/harness/01_plan/agents/repo-research-analyst.md` and follow its instructions for this task"). For loading the full harness context, use `--include-directories docs/harness` when launching. Model selection is via the `-m` flag (e.g., `gemini -m gemini-2.5-pro`); `model: inherit` in agent frontmatter is ignored.

**MCP**: Gemini CLI supports MCP natively. Configure Context7 in `~/.gemini/settings.json` the same way you would any MCP server — no fallback to web search needed.

**Model profile mapping for Gemini CLI**:

| Harness Tier | Gemini Model |
|-------------|-------------|
| Tier 1 (flagship) | `gemini-2.5-pro` |
| Tier 2 (balanced) | `gemini-2.0-pro` |
| Tier 3 (fast) | `gemini-2.0-flash` |

**Orchestrator compatibility**: The `project-orchestrator.md` can be used manually — load it into context and step through phases. Gemini CLI does not yet have multi-agent dispatch (sub-agent support is in development), so agents share the main context window. The 1M token context helps offset this limitation.

**What works well**:
- Native MCP support (Context7 works without fallback)
- Google Search grounding for documentation lookups
- Large context window (1M tokens) — less pressure from shared context
- `GEMINI.md` provides a natural harness entry point

**Limitations**:
- No multi-agent dispatch yet — agents run in the main context, not isolated subprocesses
- No per-agent model selection within a session
- Gemini models only (no LiteLLM routing unless using Gemini CLI with a proxy)

### Codex

Codex (OpenAI's CLI agent) has native multi-agent support that maps well to the harness. Unlike other non-Claude CLIs, Codex can dispatch sub-agents with per-role model selection and isolated execution — the closest equivalent to Claude Code's Task tool.

**Setup**: Define harness agent roles in `.codex/config.toml` (or `~/.codex/config.toml` for global config). Each role points to a `.toml` config file with `developer_instructions` derived from the agent `.md` content.

Example `.codex/config.toml`:

```toml
[agents]
max_threads = 3
max_depth = 1

[agents.researcher]
description = "Research agent for planning phase."
config_file = "agents/researcher.toml"

[agents.implementer]
description = "Implementation executor — follows plans step by step."
config_file = "agents/implementer.toml"

[agents.reviewer]
description = "Code review and verification agent."
config_file = "agents/reviewer.toml"

[agents.explorer]
description = "Fast codebase explorer for read-heavy tasks."
config_file = "agents/explorer.toml"

[agents.debugger]
description = "Scientific hypothesis-driven debugging."
config_file = "agents/debugger.toml"
```

Example `.codex/agents/researcher.toml`:

```toml
model = "o3"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
developer_instructions = """
You are a research agent. Read docs/harness/01_plan/agents/repo-research-analyst.md
and follow its instructions. Focus on thorough codebase analysis and produce
structured research findings.
"""
```

Example `.codex/agents/explorer.toml`:

```toml
model = "codex-mini"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
You are a fast codebase explorer. Read docs/harness/01_plan/agents/spec-flow-analyzer.md
and follow its instructions. Optimized for quick file search and code reading.
"""
```

**Model profile mapping for Codex**:

| Harness Tier | Codex Model | Reasoning Effort |
|-------------|-------------|-----------------|
| Tier 1 (flagship) | `o3` | `high` |
| Tier 2 (balanced) | `o3` | `medium` |
| Tier 3 (fast) | `codex-mini` | `medium` |

**Orchestrator compatibility**: The `project-orchestrator.md` workflow can run in Codex with one adjustment — set `auto_advance: true` in `config.json` to skip interactive confirmation gates, since Codex sub-agents are non-interactive. The parent Codex session remains interactive for top-level confirmations.

**What works well**:
- Parallel agent dispatch (Codex spawns multiple sub-agents concurrently)
- Per-agent model selection via role `.toml` files
- Isolated execution (sub-agents inherit sandbox policy)
- The orchestrator can spawn researcher, implementer, and reviewer agents

**Limitations**:
- Sub-agents are non-interactive — they can't pause for user confirmation mid-task
- `agents.max_depth` defaults to 1 (no agent-spawns-agent chains)
- Sub-agents that need approvals beyond the parent's sandbox policy will fail
- No MCP support — use web search for documentation lookups

### Antigravity

Google Antigravity is an agent-first IDE (with a `agy` CLI) that maps almost structurally identically to the harness. Its skill system (`SKILL.md` + `references/`, `assets/`, `scripts/`) mirrors the harness skill format exactly. This is the best non-Claude fit for the harness architecture.

**The key insight**: harness agent `.md` files become Antigravity Skills, harness skills become Antigravity Workflows, and the orchestrator phases become Antigravity Workflows triggered with `/`.

**Setup**: Create `.agents/` in your project root:

```
.agents/
├── rules/              # Behavioral guidelines (replaces CLAUDE.md harness ref)
│   └── harness.md      # Point to docs/harness/ and describe workflow
├── skills/             # Harness agents as Antigravity skills
│   ├── researcher/
│   │   └── SKILL.md
│   ├── implementer/
│   │   └── SKILL.md
│   ├── reviewer/
│   │   └── SKILL.md
│   └── debugger/
│       └── SKILL.md
└── workflows/          # Orchestrator phases as saved prompts
    ├── plan.md         # /plan — triggers Plan phase
    ├── work.md         # /work — triggers Work phase
    ├── review.md       # /review — triggers Review phase
    └── compound.md     # /compound — triggers Compound phase
```

**`.agents/rules/harness.md`** (replaces `CLAUDE.md` harness reference):
```markdown
Read docs/harness.md for agent workflow instructions.
Follow the Plan → Work → Review → Compound cycle for all engineering tasks.
Use harness skills for specialized tasks (researcher, implementer, reviewer, debugger).
```

**Example `.agents/skills/researcher/SKILL.md`**:
```markdown
---
name: researcher
description: Research agent for planning phase — analyzes codebase and gathers context
---

Read docs/harness/01_plan/agents/repo-research-analyst.md and follow its instructions.
Focus on thorough codebase analysis and produce structured research findings.
```

**Example `.agents/workflows/plan.md`** (triggered with `/plan`):
```markdown
Begin the Plan phase. Read docs/harness/01_plan/PLAN_PHASE.md and follow its instructions
for this task. Use the researcher skill for codebase analysis if needed.
```

**Agent Manager**: Use Antigravity's Manager Surface to spawn multiple harness agents in parallel — equivalent to Claude Code's parallel Task tool calls. Set Planning mode to `Planning` for complex tasks (research, debugging) and `Fast` for straightforward execution.

**What works exceptionally well**:
- Skill system is structurally identical to harness skills
- Agent Manager dispatches parallel agents (equivalent to Task tool)
- Artifact review system maps to harness plan review gates
- Rules/workflows/skills separation mirrors harness reference/skill/agent separation
- Browser subagent useful for Context7-style documentation fetching

**Limitations**:
- Public preview as of early 2026 — quota limits and occasional instability
- No MCP support yet — use browser subagent for documentation lookups
- Model selection (Gemini 3 Pro) available per conversation, not per agent
- `agents.max_depth` equivalent not documented — agent nesting depth unclear

---

## What You Can Ignore

The following Claude Code-specific elements appear in agent files and are **safely ignored** by other CLIs:

- **`model: inherit`** in frontmatter — tells Claude Code's Task tool to use the parent model
- **`<commentary>` tags** — structured thinking output; treated as regular text by other CLIs
- **Task tool references** — instructions like "launch via Task tool" just mean "run this agent"
- **`.claude/` path references** — Claude Code's settings directory; Glob/Read calls to these paths return nothing on other CLIs (harmless)
