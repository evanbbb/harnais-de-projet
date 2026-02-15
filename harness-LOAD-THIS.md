# Harness Init

Step-by-step instructions for onboarding a consuming project to use harnais_de_projet.

Read this file when setting up a new project with the harness. Follow each step in order, confirming with the user before making changes.

---

## Step 1: Audit

Read the consuming project's current file structure to understand what exists.

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

**docs/design-rules.md**:
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

Create `docs/harness.md` using the template from `harness-template.md` in harnais_de_projet.

Replace the placeholder path with the actual absolute path to harnais_de_projet on this machine.

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
- [ ] `docs/harness.md` exists and points to the correct harnais_de_projet path
- [ ] No files were moved without user confirmation
- [ ] Existing documentation was preserved (moved, not deleted)

Report the final state to the user.
