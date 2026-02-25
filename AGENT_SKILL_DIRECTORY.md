**Harness version: 1.5**

## Overview

**Init → Plan → Work → Review → Compound → Repeat**

### Two-Layer Model

- **Task level**: `orchestrator.md` runs Plan → Work → Review → Compound for a single task. Works standalone.
- **Project level**: `project-orchestrator.md` sequences roadmap phases, each containing multiple task loops. Requires `.planning/`.

### Agents vs Skills

- **Agents** are autonomous prompts for the Task tool. They research, analyze, or validate independently given a goal.
- **Skills** are step-by-step processes with supporting assets (templates, schemas, references). They guide Claude through structured workflows with decision points.

## 00 Init

### Agents

| Agent | Description |
|-------|-------------|
| `project-questioner` | Dream extraction — conversational exploration of project vision, requirements, and success criteria |
| `codebase-mapper` | 4-lens codebase analysis (technology, architecture, quality, concerns) for project planning |

### Skills

| Skill | Description |
|-------|-------------|
| `project-setup` | Creates `.planning/` directory with PROJECT.md, REQUIREMENTS.md, ROADMAP.md, STATE.md, config.json |

## 01 Plan

### Agents

| Agent | Description |
|-------|-------------|
| `best-practices-researcher` | Gather external best practices and examples |
| `framework-docs-researcher` | Research framework documentation and best practices |
| `plan-checker` | Validate plans across 8 quality dimensions before execution |
| `repo-research-analyst` | Research repository structure and conventions |
| `research-synthesizer` | Combine outputs from multiple research agents into prioritized synthesis |
| `spec-flow-analyzer` | Analyze user flows and identify gaps in specifications |

### Skills

| Skill | Description |
|-------|-------------|
| `brainstorming` | Explore requirements and approaches through collaborative dialogue |

## 02 Work

### Agents

| Agent | Description |
|-------|-------------|
| `debugger` | Scientific hypothesis-driven debugging (observe → hypothesize → experiment → conclude) |
| `implementation-executor` | Execute a plan step by step with XML task parsing, deviation rules, and completion summaries |
| `test-writer` | Write tests matching the project's existing test patterns |

## 03 Review

### Agents

| Agent | Description |
|-------|-------------|
| `bug-reproduction-validator` | Systematically reproduce and validate bug reports |
| `code-simplicity-reviewer` | Final pass for simplicity and minimalism |
| `pattern-recognition-specialist` | Analyze code for patterns and anti-patterns |
| `performance-oracle` | Performance analysis and optimization |
| `verification-agent` | 4-level verification (exists, substantive, wired, functional) with stub detection — recommended first reviewer |

## 04 Compound

### Skills

| Skill | Description |
|-------|-------------|
| `compound-docs` | Capture solved problems as categorized documentation |
| `document-review` | Improve documents through structured self-review |
| `milestone-retrospective` | Phase-end retrospective — review accomplishments, check success criteria, capture lessons |

## 05 Session

### References

| Reference | Description |
|-----------|-------------|
| `SESSION_MANAGEMENT.md` | Guidelines for pausing and resuming work across sessions |
| `continue-here-format.md` | Template for session handoff files |
