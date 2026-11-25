# Git cheat sheet for vibe coders

## Vocabulary

| Term | Plain meaning |
|---|---|
| Repository (repo) | The project folder with its full history |
| Commit | A named save point of the whole project |
| Stage (`add`) | Choose which changes go into the next save point |
| Push / pull | Upload your save points to GitHub / download your team's |
| Branch | A parallel copy to try something without touching the main version |
| `main` | The version everyone agrees works |
| Pull request (PR) | A request to merge your branch into `main`, with a review |
| Revert | A new save point that undoes an earlier one |
| Tag | A label on one save point, for example a version you demonstrated |

## One-time setup

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Existing folder into a repo:

```bash
git init
git add .
git commit -m "Initial commit"
```

Then create an empty repository on GitHub and follow its "push an existing repository" lines.

## Save a checkpoint

```bash
git status                 # what changed?
git diff                   # look at the changes
git add .                  # stage everything
git commit -m "Add hero section with headline and call to action"
git push
```

## Feature branch workflow

```bash
git checkout main
git pull
git checkout -b feature/weekly-challenge
# ... prompt, check, commit, repeat ...
git push -u origin feature/weekly-challenge
# open a pull request on GitHub, review, merge
```

Branch names: `feature/...`, `fix/...`, `design/...`, `docs/...`

## Undo

Not committed yet (throws away all uncommitted changes):

```bash
git checkout -- .
```

Committed, not pushed:

```bash
git reset --soft HEAD~1    # undo the commit, keep the changes
git reset --hard HEAD~1    # undo the commit and discard the changes
```

Already pushed:

```bash
git revert HEAD            # new commit that undoes the last one
```

Look at history, or go back to look at an old version:

```bash
git log --oneline
git checkout <commit-id>   # look around; `git checkout main` to return
```

## Merge conflict

```
<<<<<<< HEAD
your version
=======
your teammate's version
>>>>>>> feature/their-branch
```

Keep what is right, delete the three marker lines, then:

```bash
git add <file>
git commit -m "Resolve merge conflict in navigation"
```

Safe exit: `git merge --abort`

## Tags

```bash
git tag v1-mvp
git push --tags
```

## Never commit

Passwords, API keys, `.env` files. Put them in `.gitignore` before the first commit. If a key was pushed by accident, removing the file is not enough: create a new key and disable the old one.

## Rules to give your AI agent

- Work on a feature branch, never on `main`.
- Commit after each completed task with a descriptive message.
- Do not change files outside the task.
- Never commit secrets.
