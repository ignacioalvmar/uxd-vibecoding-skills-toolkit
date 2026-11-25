---
name: checkpoint-coach
description: Coaches designers through version control while vibe coding. Sets up a Git repository, saves checkpoints (commits) after each AI task, works on branches, opens pull requests, and rolls back safely when the AI breaks something. Explains each step in plain language and can run the git commands where the environment allows. Use when someone asks how to save their progress, undo what the AI did, go back to a working version, set up GitHub for a project, resolve a merge conflict, or work on a vibe coding project as a team.
---

# Checkpoint coach

CHECKPOINTS is one of the five vibe coding skills: always save your work incrementally, because things will break. This skill makes saving and undoing routine for people who are new to Git.

## Why this skill exists

AI tools change many files in seconds. Without a save point, one bad prompt can cost an afternoon. With a commit after every working step, the worst case is losing the last ten minutes. Designers often avoid Git because it looks like a programmer's tool. It is closer to version history in Figma, only more deliberate.

## First find out where the student is

Ask, in one short message:

1. Which tool are they building in, and does the project live in a folder on their computer, or only inside a browser tool (Lovable, Replit)?
2. Is there a Git repository already? Is it connected to GitHub?
3. Solo or team?
4. What do they want right now: set up, save, undo, branch, share, or fix a conflict?

Browser builders have their own version history and usually a GitHub connection. Use the built-in checkpoints there, and explain how to connect GitHub if the student wants a durable copy. Do not walk through terminal commands that do not apply.

## How to coach

- One step at a time. Give the command, say in one plain sentence what it does, and say what the student should see afterwards.
- If you can run commands in this environment, offer to run them. Always show `git status` before and after, so the student sees what changed.
- If the student would rather click than type, describe the same step in their editor's source control panel or in GitHub Desktop.
- Use the vocabulary in `references/git-cheatsheet.md`. It also has the commands for each situation below.

## Situations

**Set up.** Create the repository (on GitHub first is easiest for beginners), clone or initialize, set name and email once, make the first commit. Check that a `.gitignore` exists and that files with secrets (`.env`, API keys) are in it before the first push.

**Save a checkpoint.** After every AI task that works: look at what changed (`git status`, `git diff`), stage, commit with a message that says what was done, push. A good message names the feature: "Add weekly challenge section with pledge checkboxes". "update" tells nobody anything.

**Work on a branch.** One feature per branch. Start from an up-to-date `main`, create `feature/<name>`, commit there, push, open a pull request, merge after the check passes. Tell AI agents to work on a branch and to commit after every iteration.

**Undo.** First find out which case applies. The right command depends on it:

| State | What to do |
|---|---|
| Changes not committed yet | Discard them and return to the last commit |
| Committed, not pushed | Undo the last commit (keep or drop the changes) |
| Already pushed or shared | Revert with a new commit. Never rewrite shared history |

Before any command that throws work away (`git checkout -- .`, `git reset --hard`), say exactly what will be lost and ask for confirmation. Never run a destructive command on your own initiative.

**Team.** Agree on branch names, never push directly to `main`, review each other's pull requests, split work so that people do not edit the same files, and say in the pull request which changes were AI-generated.

**Merge conflict.** Explain the conflict markers, help decide which version to keep for each conflict, then stage and commit. If the student is lost, the safe exit is to abort the merge and ask a teammate.

**Tag a milestone.** Tag versions that were demonstrated or submitted (`v1-wireframe`, `v2-mvp`), so they can be found again.

## Make it a habit

Suggest this rhythm for every build session: pull, branch, prompt, check, commit, repeat, then push and open a pull request at the end. Also suggest adding the rule to the project's AGENTS.md: "Work on a feature branch. Commit after each completed task with a descriptive message. Never push to main." The `project-context-files` skill writes that file.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- Look at the diff before you commit. Did the AI change files you did not expect?
- Commit only states that work. A checkpoint of a broken app is not a safe place to return to.
- Check that no passwords or API keys are in the commit.
- Write the commit message yourself. It is your record of the design decisions.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
