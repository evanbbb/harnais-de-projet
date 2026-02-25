# Plan Format

Reference for plan file structure when used with the project lifecycle.

## Frontmatter

Plans should include YAML frontmatter when managed by the project orchestrator:

```yaml
---
phase: XX-name
plan: NN
wave: N
depends_on: []
files_modified: []
requirements: [REQ-IDs]
must_haves:
  truths: []      # Observable user behaviors that prove correctness
  artifacts: []   # Files that must exist after completion
  key_links: []   # Critical connections between components
---
```

**Field descriptions:**
- **phase**: The roadmap phase this plan belongs to (e.g., `01-authentication`)
- **plan**: Sequential plan number within the phase
- **wave**: Execution wave for parallel scheduling (plans in the same wave can run concurrently)
- **depends_on**: List of plan numbers that must complete before this one
- **files_modified**: Expected files to create or change
- **requirements**: REQ-IDs from `.planning/REQUIREMENTS.md` that this plan addresses
- **must_haves**: Observable proof of completion — not aspirational, but verifiable

## XML Task Format

Each plan contains tasks in XML format for structured parsing by executors:

```xml
<task type="auto">
  <name>Task Name</name>
  <files>src/path/to/file.ts</files>
  <action>Specific implementation instructions</action>
  <verify>Automated command proving completion (60 sec max)</verify>
  <done>Measurable acceptance criteria</done>
</task>
```

**Task type values:**
- `auto` — Fully automated, no human input needed
- `human-verify` — Automated execution, but human must verify the result
- `decision` — Requires a human decision before proceeding
- `human-action` — Requires a human to perform an action outside the agent (e.g., configure a service, approve access)

## Checkpoint Types

Insert checkpoints between tasks when human involvement is needed:

```xml
<checkpoint type="human-verify">
  <description>Verify the login page renders correctly</description>
</checkpoint>

<checkpoint type="decision">
  <description>Choose between OAuth and JWT for session management</description>
  <options>
    <option>OAuth — delegated auth, better for third-party integrations</option>
    <option>JWT — self-contained tokens, simpler infrastructure</option>
  </options>
</checkpoint>

<checkpoint type="human-action">
  <description>Create the Stripe account and add API keys to .env</description>
</checkpoint>
```

## Plan Sizing

Ideal plan size: **2-3 tasks per plan**. This keeps plans focused, reviewable, and easy to re-run if something fails. If a plan has more than 5 tasks, consider splitting it.

## Standalone vs Project-Managed

- **Standalone** (no `.planning/`): Plans omit frontmatter. Task format is optional but recommended.
- **Project-managed** (`.planning/` exists): Plans include frontmatter. Task format is required. REQ-IDs trace back to REQUIREMENTS.md.
