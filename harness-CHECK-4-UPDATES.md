# Harness Check for Updates

The harness is linked via symlink (`docs/harness → harnais_de_projet`), so the consuming project always reads the current harness files directly. There is nothing to copy or diff.

If the project has an older harness setup, follow the relevant migration section first:
- **Copy-based** (`docs/harness/` is a real directory): see "Migrating from a copy-based harness"
- **Absolute-path reference** (no `docs/harness` at all — `harness.md` points directly to harnais_de_projet by full path): see "Migrating from an absolute-path harness"

---

## Migrating from a copy-based harness

Run this if `docs/harness` is a directory of copied files rather than a symlink. Check:

```bash
ls -la docs/harness
```

If the first column shows `d` (directory) rather than `l` (symlink), follow these steps.

**Step 1: Confirm the harnais_de_projet path**

The user must confirm the absolute path to harnais_de_projet on this machine before proceeding.

**Step 2: Remove the stale copy**

```bash
rm -rf docs/harness
```

Confirm with the user before running this — it deletes the entire copied harness directory.

**Step 3: Create the symlink**

```bash
ln -s /path/to/harnais_de_projet docs/harness
```

**Step 4: Verify the symlink resolves**

```bash
ls docs/harness/orchestrator.md
```

If this fails, the path is wrong — go back to Step 1.

**Step 5: Update docs/harness.md**

The project's `docs/harness.md` was generated from an older template. It needs two changes:

1. **Location line** — change:
   ```
   Harness location: docs/harness (local copy)
   ```
   to:
   ```
   Harness location: docs/harness (symlink → harnais_de_projet)
   ```

2. **Session-start section** — replace the old version-check block (the one with `last_seen_version`) with:
   ```
   1. **Check harness symlink**: Verify `docs/harness/orchestrator.md` is accessible. If not, the symlink to harnais_de_projet may be broken — tell the user: "The harness symlink at docs/harness is not resolving. Check that harnais_de_projet is still at the expected path." To update the harness, run `git pull` in harnais_de_projet.
   ```
   Remove the `last_seen_version:` line entirely.

3. **How to use section** — if the old `harness.md` is missing entries for project lifecycle, session management, or per-agent paths, compare it against `harness-template.md` in harnais_de_projet and add what's missing. Preserve any project-specific content.

After these changes the migration is complete. The project now reads directly from harnais_de_projet on every session.

---

## Migrating from an absolute-path harness

Run this if `docs/harness` does not exist and `docs/harness.md` references harnais_de_projet by its full absolute path (e.g. `Harness location: /Users/you/code/harnais_de_projet`). Check:

```bash
ls -la docs/harness 2>/dev/null || echo "no docs/harness"
```

If this prints "no docs/harness", follow these steps.

**Step 1: Confirm the harnais_de_projet path**

Read `docs/harness.md` — the absolute path is in the `Harness location:` line. Confirm with the user that it is still correct.

**Step 2: Create the symlink**

No removal needed — `docs/harness` doesn't exist yet.

```bash
ln -s /path/to/harnais_de_projet docs/harness
```

**Step 3: Verify the symlink resolves**

```bash
ls docs/harness/orchestrator.md
```

If this fails, the path is wrong — go back to Step 1.

**Step 4: Update docs/harness.md**

1. **Location line** — change the absolute path line to:
   ```
   Harness location: docs/harness (symlink → harnais_de_projet)
   ```

2. **How to use section** — replace all absolute paths with `docs/harness/`-relative paths. Compare against `harness-template.md` in harnais_de_projet and bring the section up to date (the old version likely has placeholder paths like `{phase}/PHASE.md` rather than the real filenames).

3. **Session-start section** — replace the old version-check block (the one with `last_seen_version`) with:
   ```
   1. **Check harness symlink**: Verify `docs/harness/orchestrator.md` is accessible. If not, the symlink to harnais_de_projet may be broken — tell the user: "The harness symlink at docs/harness is not resolving. Check that harnais_de_projet is still at the expected path." To update the harness, run `git pull` in harnais_de_projet.
   ```
   Remove the `last_seen_version:` line entirely.

After these changes the migration is complete.

---

## To update the harness

Pull the latest changes in harnais_de_projet:

```bash
cd /path/to/harnais_de_projet && git pull
```

That's it. All projects with the symlink immediately see the updated files.

---

## If docs/harness.md needs refreshing

`docs/harness.md` lives in the consuming project and is not part of the symlink. It is generated once from `harness-template.md` and may drift if the template changes significantly.

To refresh it:

1. Read `harness-template.md` from harnais_de_projet
2. Compare it to `docs/harness.md` in the consuming project
3. Apply any structural changes (new sections, updated instructions) — preserve project-specific customizations

This is only needed when the template itself has meaningful structural changes, not for routine harness updates.

---

## If using Claude Code + get-shit-done

`get-shit-done` commands run via `npx` and need explicit Claude Code permission in each consuming repo.

Check:

```bash
rg -n "Bash\\(npx get-shit-done-cc@latest:\\*\\)" .claude/settings.local.json
```

If missing, add this allow entry under `.claude/settings.local.json`:

```json
"Bash(npx get-shit-done-cc@latest:*)"
```

This permission is repo-local. Adding it in harnais_de_projet does not automatically grant it in other repos.

---

## If the symlink is broken

If `docs/harness/orchestrator.md` is not accessible, the symlink may be pointing to a path that no longer exists (e.g., harnais_de_projet was moved).

Fix it:

```bash
# Remove the broken symlink
rm docs/harness

# Re-create with the correct path
ln -s /new/path/to/harnais_de_projet docs/harness
```

Verify:

```bash
ls docs/harness/orchestrator.md
```
