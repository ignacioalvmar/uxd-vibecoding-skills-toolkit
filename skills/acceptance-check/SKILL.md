---
name: acceptance-check
description: Checks a vibe-coded build against the acceptance criteria in its PRD. Turns criteria into a test checklist with realistic test data and edge cases, runs the checks where the environment allows or guides the student through them by hand, and reports pass, fail or not checked for each, with fix prompts for failures. Use when a feature or prototype is "done" and someone wants to verify it, test it, check it against requirements, prepare a demo or submission, or decide whether it is ready to ship.
---

# Acceptance check

Answers one question with evidence: does what was built do what the PRD says? Validate against acceptance criteria and test with realistic data, before saving the checkpoint and before every demo.

## Why this skill exists

An AI tool will say "Done! Everything works" whether or not it does. With vibe coding, the designer decides when the quality bar is met, so the designer needs a quick and honest way to check. This skill reports what was verified and what was not. It never reports a pass it did not see.

## Inputs

Ask for what is missing in one short message:

1. **The acceptance criteria**: the PRD or the feature section. If there are none, help write three to five observable criteria for the feature first, and suggest adding them to the PRD.
2. **Access to the build**: can you run it here (project folder, a browser tool, a URL you can open), or will the student test by hand and report back?
3. **Scope**: one feature, or the whole MVP before a demo.

## Step 1: Build the checklist

Turn each criterion into one or more checks that a person can do in under a minute:

| # | Criterion (PRD) | Check: do this | Expected result | Type |
|---|---|---|---|---|

Types: **function**, **content** (exact copy and values), **state** (empty, loading, error), **accessibility**, **responsive**.

Add what the criteria tend to forget, and mark it as an added check:

- **Realistic data**: real-looking names, long texts, special characters, zero and maximum values.
- **Edge cases**: empty input, wrong format, values at the limits, double click, reload in the middle of the flow, back button.
- **Test vectors**: where there is logic, use input and expected output pairs from the PRD. If the PRD has none, ask the student to calculate one expected result by hand. Do not make up the expected value.
- **Accessibility basics**: keyboard only through the main flow, visible focus, labels, contrast, 200 percent zoom.
- **Responsive**: the screen widths named in the PRD.
- **Regression**: one quick check of each feature that worked before.

## Step 2: Run the checks

**If you can run or open the build:** do the checks and record what you observed (actual value, screenshot or output). Use the tool's browser, preview or test runner where available. For logic, write small automated tests if the project supports it, and fix the code and not the test when one fails.

**If you cannot:** hand the checklist to the student as a fill-in table and wait for the results. Do not estimate results from reading the code. Code that looks right is not a passed check.

## Step 3: Report

| # | Check | Result | Evidence or observation |
|---|---|---|---|

Result is exactly one of: **pass** (observed), **fail** (observed, with the actual behavior), **not checked** (with the reason).

Then:

- **Summary**: counts of pass, fail and not checked, and whether the P0 criteria are all met.
- **Failures in order of importance**, each with a one-prompt fix (one change, naming what must stay untouched). For anything unclear, use the `debug-protocol` skill first.
- **Gaps in the PRD**: criteria that were missing or could not be tested as written.
- **Ready?** Say plainly whether the feature meets its criteria. "Not checked" items count against "ready".

## Rules

- Never mark something as pass because the AI builder said so, or because the code suggests it.
- Do not lower a criterion to make it pass. If the criterion is wrong, the student changes the PRD on purpose.
- Passing the acceptance check means the build matches the PRD. It does not mean that users can use it. That needs a test with people.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- Click through the main flow yourself once, as your persona, on a real phone.
- You define "done": is the quality good enough to show, beyond the checklist?
- Fit and finish: alignment, wording, the small details no checklist catches.
- If everything passes, commit and tag this version before you change anything else.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
