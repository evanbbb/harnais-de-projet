# Harness Init

Step-by-step instructions for onboarding a consuming project to use harnais_de_projet.

Read this file when setting up a new project with the harness. Follow each step in order, confirming with the user before making changes.

---

## Step 1: Audit

Read the consuming project's current file structure to understand what exists.

- Check for existing `docs/` directory
- Check for `CLAUDE.md`
- Note any existing documentation files (README, ARCHITECTURE.md, CONTRIBUTING.md, etc.)
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

If the project already has documentation in other locations, present each potential move to the user for confirmation:

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

For files that don't map cleanly, ask the user where they belong.

---

## Step 4: Configure

Create `docs/harness.md` using the template from `harness-template.md` in harnais_de_projet.

Replace the placeholder path with the actual absolute path to harnais_de_projet on this machine.

---

## Step 5: Update CLAUDE.md

Add the following line to the project's `CLAUDE.md` (create the file if it doesn't exist):

```
Read docs/harness.md for agent workflow instructions.
```

If `CLAUDE.md` already exists, append this line in an appropriate location (near other documentation references if they exist).

---

## Verification

After completing all steps, confirm:
- [ ] `docs/` directory exists with all subdirectories
- [ ] `docs/harness.md` exists and points to the correct harnais_de_projet path
- [ ] `CLAUDE.md` references `docs/harness.md`
- [ ] No files were moved without user confirmation
- [ ] Existing documentation was preserved (moved, not deleted)

Report the final state to the user.
