# Verification Levels

4-level verification framework for validating implementation completeness. Used by the `verification-agent`.

## Level 1: Exists

**Question**: Do the expected files exist?

- Check every file listed in the plan's `files_modified` and `must_haves.artifacts`
- Verify file is not empty (size > 0)
- **Pass**: All expected files are present and non-empty
- **Fail**: Missing files or empty files

## Level 2: Substantive

**Question**: Does the code contain real implementation, not stubs?

- Scan files for stub indicators (see `stub-indicators.md`)
- Check that functions have real logic, not placeholder returns
- Verify test files have actual assertions, not empty test bodies
- **Pass**: No stub indicators found; code has real logic
- **Fail**: Stub patterns detected (list each one with file and line)

## Level 3: Wired

**Question**: Is the new code connected to the rest of the system?

- Check that new routes are registered in the router
- Check that new components are imported somewhere
- Check that new functions are called from existing code
- Check that new database models are referenced in migrations or seeds
- **Pass**: All new code has at least one integration point
- **Fail**: Orphan code found (exists but nothing references it)

## Level 4: Functional

**Question**: Does it actually work end-to-end?

- Run the plan's `<verify>` commands
- Run existing test suites that touch modified files
- If applicable, trace a user flow from entry point to output
- **Pass**: All verification commands pass, tests pass
- **Fail**: Verification or test failures (list each with output)

## Applying the Levels

Run levels in order. If a level fails, stop — there's no point checking functionality if the code doesn't exist or is stubbed out.

**Minimum verification**: Levels 1-2 (exists + substantive) for every plan.

**Full verification**: Levels 1-4 for milestone boundaries and phase completion.

**Configurable**: The `config.json` `workflow.verifier` toggle enables/disables automated verification. When disabled, verification is manual.
