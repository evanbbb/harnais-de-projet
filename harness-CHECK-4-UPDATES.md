# Harness Check for Updates

Instructions for updating a consuming project's harness copy when harnais_de_projet has new or changed content.

Read this file when the user wants to check for harness updates or when `docs/harness.md` indicates a newer harness version is available. **Every update is optional** — confirm with the user before applying each change.

---

## Prerequisites

- The consuming project has already run harness init (`harness-LOAD-THIS.md`) and has `docs/harness/` with a local copy.
- You have access to the harnais_de_projet source (path on disk, or the repo root).

---

## Step 1: Check if updates exist

Compare the **Harness version** at the top of:
- **Upstream**: `AGENT_SKILL_DIRECTORY.md` in harnais_de_projet
- **Local**: `docs/harness/AGENT_SKILL_DIRECTORY.md` in the consuming project

If the upstream version is newer, or if the user explicitly asked to check for updates, proceed. Otherwise, report: "Harness is up to date (version X)."

---

## Step 2: Identify what changed

Compare the harness source against `docs/harness/` in the consuming project. Categorize each item as:

- **New** — exists in source, not in project
- **Updated** — exists in both, content differs
- **Unchanged** — same in both (skip)

Present a summary to the user before making any changes.

---

## Step 3: Update core harness files (each optional)

For each item below, **ask the user** before copying or overwriting. Do not batch multiple items into a single yes/no — confirm each one.

### 3a. Orchestrator

| Source | Destination | Action |
|--------|-------------|--------|
| `orchestrator.md` | `docs/harness/orchestrator.md` | Overwrite if updated |

**Prompt**: "Overwrite `docs/harness/orchestrator.md` with the latest from the harness? (yes / skip)"

---

### 3b. Phase files

| Source | Destination | Action |
|--------|-------------|--------|
| `01_plan/PLAN_PHASE.md` | `docs/harness/01_plan/PLAN_PHASE.md` | Overwrite if updated |
| `02_work/WORK_PHASE.md` | `docs/harness/02_work/WORK_PHASE.md` | Overwrite if updated |
| `03_review/REVIEW_PHASE.md` | `docs/harness/03_review/REVIEW_PHASE.md` | Overwrite if updated |
| `04_compound/COMPOUND_PHASE.md` | `docs/harness/04_compound/COMPOUND_PHASE.md` | Overwrite if updated |

**Prompt** (per file or as a group, user's choice): "Update phase file(s) X, Y, Z? (yes / skip / list which ones)"

---

### 3c. Agents (new and updated)

For each agent in harnais_de_projet:

- **01_plan/agents/** — `best-practices-researcher.md`, `framework-docs-researcher.md`, `repo-research-analyst.md`, `spec-flow-analyzer.md`
- **02_work/agents/** — `implementation-executor.md`, `test-writer.md`
- **03_review/agents/** — `bug-reproduction-validator.md`, `code-simplicity-reviewer.md`, `pattern-recognition-specialist.md`, `performance-oracle.md`

**If new** (exists in source, missing in project):
- **Prompt**: "Copy new agent `[name].md` to `docs/harness/[phase]/agents/[name].md`? (yes / skip)"

**If updated** (exists in both, content differs):
- **Prompt**: "Overwrite `docs/harness/[phase]/agents/[name].md` with the latest? (yes / skip)"

Confirm each agent separately unless the user says "update all agents."

---

### 3d. Skills (new and updated)

Skills include their folder: `SKILL.md` plus any `assets/`, `references/`, or other subdirectories. Copy or overwrite the **entire skill folder**.

**01_plan/skills/** — `brainstorming/`  
**04_compound/skills/** — `compound-docs/`, `document-review/`

**If new** (skill folder exists in source, missing in project):
- **Prompt**: "Copy new skill `[skill-name]/` (entire folder) to `docs/harness/[phase]/skills/[skill-name]/`? (yes / skip)"

**If updated** (skill folder exists in both, any file differs):
- **Prompt**: "Overwrite skill `[skill-name]/` with the latest? This replaces the whole folder including assets and references. (yes / skip)"

Confirm each skill separately unless the user says "update all skills."

---

### 3e. Agent/skill catalog

| Source | Destination | Action |
|--------|-------------|--------|
| `AGENT_SKILL_DIRECTORY.md` | `docs/harness/AGENT_SKILL_DIRECTORY.md` | Overwrite if updated |

**Prompt**: "Overwrite `docs/harness/AGENT_SKILL_DIRECTORY.md` with the latest catalog? (yes / skip)"

---

### 3f. Design rules

| Source | Destination | Action |
|--------|-------------|--------|
| `design-rules.md` | `docs/design-rules.md` | Overwrite or merge |

**Important**: The project may have customized `docs/design-rules.md`. Options:

1. **Overwrite** — Replace with harness design rules (loses project customizations).
2. **Merge** — Show a diff; user or agent manually merges new harness rules into the project file.
3. **Skip** — Keep the project's current design rules.

**Prompt**: "The harness has updated `design-rules.md`. Your project has `docs/design-rules.md`. Options: (1) Overwrite with harness version, (2) I'll show a diff for manual merge, (3) Skip. Which?"

---

### 3g. Harness config (docs/harness.md)

| Source | Destination | Action |
|--------|-------------|--------|
| `harness-template.md` | `docs/harness.md` | Update version only, or full replace |

The project's `docs/harness.md` may have customizations (e.g. project-specific notes). Recommend:

- **Minimal update**: Only update `last_seen_version` in `docs/harness.md` to match the new harness version. Preserves all other content.
- **Full replace**: Overwrite `docs/harness.md` with the latest `harness-template.md`. Use only if the project has not customized it.

**Prompt**: "Update `docs/harness.md`: (1) Just update `last_seen_version` to [X], (2) Full replace with latest template, (3) Skip. Which?"

---

## Step 4: Post-update

After applying the user's chosen updates:

1. If `AGENT_SKILL_DIRECTORY.md` was updated, ensure `last_seen_version` in `docs/harness.md` matches the new Harness version (so the session-start check stops flagging it).
2. Report what was updated and what was skipped.

---

## Summary

| Category | Source(s) | Confirm before each |
|----------|-----------|---------------------|
| Orchestrator | `orchestrator.md` | yes |
| Phase files | `*_PHASE.md` per phase | yes |
| Agents | `*/agents/*.md` | yes, per agent |
| Skills | `*/skills/*/` (whole folders) | yes, per skill |
| Catalog | `AGENT_SKILL_DIRECTORY.md` | yes |
| Design rules | `design-rules.md` | yes (overwrite / merge / skip) |
| Harness config | `harness-template.md` → `docs/harness.md` | yes (version only / full / skip) |
