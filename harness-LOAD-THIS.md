# Harness Init

Step-by-step instructions for onboarding a consuming project to use harnais_de_projet.

Read this file when setting up a new project with the harness. Follow each step in order, confirming with the user before making changes.

---

## Step 1: Audit

Read the consuming project's current file structure to understand what exists.

**Project lifecycle question**: Does this project need project-level lifecycle management (roadmap, requirements traceability, phased execution)? Ask the user:

```
Does this project need project lifecycle management?

1. Yes — Set up .planning/ with project definition, requirements, roadmap, and phased execution
2. No — Use task-level workflow only (Plan → Work → Review → Compound per task)

Which? (1 / 2)
```

If **yes**: After completing all steps below, run `docs/harness/00_init/INIT_PHASE.md` to create `.planning/`.

If **no**: Proceed with the standard setup below. The project lifecycle can be added later.

**CLI question**: Which AI coding CLI are you using?

```
1. Claude Code (recommended — full feature support)
2. Antigravity (Google — agent-first IDE, closest structural fit to harness)
3. Codex (OpenAI — native multi-agent support)
4. Gemini CLI (Google — native MCP, 1M context)
5. Cursor
6. Aider
7. Cline
8. Other
```

If not Claude Code: See `00_init/references/cli-compatibility.md` after completing setup for tool equivalents, agent dispatch guidance, and MCP fallbacks. Codex users should also set up `.codex/config.toml` with harness agent roles — see the Codex section in that doc.

- Check for existing `docs/` directory
- Identify which root-level project entry point exists (any one of `CLAUDE.md`, `PROJECT.md`, `README.md`, `.cursorrules`, or similar). Only one is needed — do not flag missing alternatives as issues.
- Note any existing documentation files (ARCHITECTURE.md, CONTRIBUTING.md, etc.)
- Note any existing plans, solutions, or memory files in non-standard locations

Report findings to the user before proceeding.

---

## Step 2: Scaffold

Create the canonical `docs/` structure:

```bash
mkdir -p docs/memory docs/plans docs/solutions docs/structure
```

Create empty template files where they don't already exist:

**docs/design-rules.md** (only if it doesn't already exist):

Ask the user to choose:

1. **Use harness design rules** — Copy `design-rules.md` from harnais_de_projet to `docs/design-rules.md`. The harness provides layout, typography, colors, cards, and other UI conventions.
2. **Use blank template** — Create `docs/design-rules.md` with:

```markdown
# Design Rules

<!-- Project-specific visual and design rules go here -->
<!-- Update this file when design components change -->
```

**docs/to-do.md**:
```markdown
# To Do

## P1 (Critical)

## P2 (Important)

## P3 (Nice to Have)
```

---

## Step 2b: Link harness

Create a symlink from `docs/harness` to the harnais_de_projet directory. This makes all harness content immediately available and always current — no copying or manual updates needed.

**Source**: The absolute path to harnais_de_projet on this machine (the user must provide this, or it may be known from context).

```bash
ln -s /path/to/harnais_de_projet docs/harness
```

Confirm the path with the user before running. After creating the symlink, verify it resolves correctly:

```bash
ls docs/harness/orchestrator.md
```

**Note**: This symlink is machine-local. It works perfectly for a single developer on one machine. If the project ever needs to run on another machine or in CI, the symlink will be broken there — use a copy or git submodule instead for those scenarios.

**If project lifecycle was selected in Step 1**: No additional steps — all files (including `project-orchestrator.md`, `00_init/`, and `05_session/`) are available through the symlink automatically.

---

## Step 3: Merge Existing Files

Only move files that clearly belong in the `docs/` subdirectories. Do not touch root-level project files like `PROJECT.md`, `README.md`, or `package.json` — these belong at the root and are not part of the harness structure.

Do not create any files beyond the scaffold templates in Step 2 and the harness config in Step 4. If existing files don't map to the docs structure, leave them where they are.

### 3a: Check for conflicts with harness files

Compare the project's existing files against what the harness provides (AGENT_PROCESS.md, AGENT_SKILL_DIRECTORY.md, orchestrator.md, phase files, agent definitions, etc.). If a project file covers the same topic as a harness file, flag it:

```
Conflict: [project file path]
Overlaps with harness file: [harness file name]
Summary: [brief description of what differs]

Options:
  1. Keep yours — leave the project file as-is; harness version is accessed separately
  2. Use harness — archive the project file to docs/memory/ and rely on the harness version
  3. Merge manually — keep both for now; you'll reconcile them later
```

Wait for the user's decision on each conflict before proceeding.

### 3b: Relocate documentation files

If the project has documentation in other locations that belongs in the `docs/` subdirectories, present each potential move to the user for confirmation:

Common mappings:
- `ARCHITECTURE.md` → `docs/structure/architecture.md`
- `docs/adr/` or `docs/decisions/` → `docs/structure/decisions/`
- Existing bug notes or troubleshooting docs → `docs/solutions/`
- Existing feature specs or plans → `docs/plans/`

For each file:
```
Found: [source path]
Proposed: Move to [destination path]

Move this file? (yes / skip / other location)
```

For files that don't map cleanly, skip them. Do not invent new locations or create new files to accommodate them.

---

## Step 4: Configure

Create `docs/harness.md` using the template from `harness-template.md` in harnais_de_projet. The template points to the harness symlink at `docs/harness`; no path replacement is needed.

If the project uses Claude Code and wants `get-shit-done` commands, ensure `.claude/settings.local.json` includes this permission:

```json
"Bash(npx get-shit-done-cc@latest:*)"
```

If `.claude/settings.local.json` does not exist yet, create it with a minimal allow-list and include the permission above.

---

## Step 5: Ensure Something Points to the Harness

Check whether any root-level file (found in Step 1) already references `docs/harness.md`. If so, this step is done.

If nothing points to the harness, suggest that the user add the following line to an existing project entry point (`PROJECT.md`, `CLAUDE.md`, `README.md`, etc.):

```
Read docs/harness.md for agent workflow instructions.
```

If no suitable file exists at all, suggest creating a `PROJECT.md` with a brief project description and the harness reference. Confirm with the user before creating it.

The harness does not dictate which file this goes in — that depends on the user's tools and preferences.

---

## Verification

After completing all steps, confirm:
- [ ] `docs/` directory exists with all subdirectories
- [ ] `docs/design-rules.md` exists (harness design rules, blank template, or already present)
- [ ] `docs/harness` is a symlink pointing to harnais_de_projet, and `docs/harness/orchestrator.md` resolves correctly
- [ ] `docs/harness.md` exists and points to the harness at `docs/harness`
- [ ] No files were moved without user confirmation
- [ ] Existing documentation was preserved (moved, not deleted)
- [ ] If using Claude Code + `get-shit-done`, `.claude/settings.local.json` allows `Bash(npx get-shit-done-cc@latest:*)`

**If project lifecycle was selected:**
- [ ] `docs/harness/project-orchestrator.md`, `docs/harness/00_init/`, `docs/harness/05_session/` are accessible via the symlink
- [ ] `.planning/` exists with PROJECT.md, REQUIREMENTS.md, ROADMAP.md, STATE.md, config.json (created by running 00_init)

Report the final state to the user.
