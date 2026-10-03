# A practical handoff checklist for a small CSV automation fix

A CSV parser that stops crashing is only part of a finished client job. The handoff should make it clear what was agreed, what changed, which inputs were checked, and what remains unproven. This checklist is free to use in your own work.

This example follows the [self-produced CSV repair demo](../README.md). It is an example, not a claim about paid client work.

## 1. Agree on the boundary before editing

Record these in plain language:

- **Input:** What file or text format arrives? Provide a small synthetic sample with a blank row and a malformed non-empty row.
- **Expected output:** Which rows should be retained, skipped, or rejected?
- **Unchanged behavior:** What must continue to work after the fix?
- **Access:** Who can provide a safe test copy? Do not put credentials or customer data in the issue or handoff.
- **Acceptance check:** What result would let the requester say the job is done?

For the demo, the agreed boundary is narrow: skip blank or whitespace-only rows; still reject a non-empty value that cannot be parsed as an integer.

## 2. Show evidence for each behavior

| Behavior | Example input | Expected result | Evidence |
| --- | --- | --- | --- |
| Original failure is reproducible | `10\\n\\n20\\n30\\n` | Legacy parser raises `ValueError` | `test_legacy_behavior_reproduces_blank_row_crash` |
| Blank rows are skipped | `10\\n\\n  \\n20\\n30\\n` | `[10, 20, 30]` | `test_fixed_behavior_skips_blank_and_whitespace_rows` |
| Bad non-empty data stays visible | `10\\nnope\\n30\\n` | Fixed parser raises `ValueError` | `test_fixed_behavior_preserves_visible_invalid_input` |

Run `python -m unittest -v test_csv_repair.py` from the repository root. Save the command, environment, test output, and date in the handoff. A green test suite proves only the cases it covers; production files and downstream systems need their own checks.

## 3. Leave a usable delivery note

A short note can use this structure:

```text
Change: Skip blank and whitespace-only CSV rows. Keep visible errors for other invalid rows.
Files changed: csv_repair.py, test_csv_repair.py
Verification: python -m unittest -v test_csv_repair.py — 3 tests passed
Known limits: Only integer-row parsing is demonstrated. No production data or downstream integration was tested.
Rollback: Restore the prior parser version and rerun the agreed sample.
Requester action: Test a redacted representative input and confirm the expected output.
```

Before closing, check that the requester can locate the changed source, run the verification, understand the rollback path, and see every untested assumption. Avoid marking a check “passed” when it was not run.

## If you manage several small client jobs

I built a separate [AI Automation Project OS Notion template](https://www.notion.so/marketplace/templates/ai-automation-project-os) to track intake, scope, access readiness, QA evidence, and handoff across projects. It is a **paid $15 template**; this checklist and the demo code are free.
