# Block D — Pull requests done right

**Duration:** ~90 minutes
* 20 min demo
* 15 min we-do
* 40 min you-do
* 10 min debrief
* ~5 min buffer

## Goal

You should leave this block able to:

- Open a PR a reviewer enjoys reading: small, scoped, with a clear what/why and a how-to-test
- Review someone else's PR with [conventional comments](https://conventionalcomments.org/) — useful feedback that doesn't read as criticism
- Decide between approve, request-changes, and "comment-only" on a real PR
- Merge cleanly when approved, choosing the merge style your team agreed on

## Pre-flight

```bash
git fetch --tags
git checkout block-d-start
```

If you'd like to read ahead: [`docs/pr-review-style.md`](../docs/pr-review-style.md).

## I do (20 min)

Two PRs side by side on the projector:

| Bad PR | Good PR |
|---|---|
| Title: "update stuff" | Title: "fix(greet): handle empty-string name without crashing" |
| 800-line diff across 12 files | 12-line diff in one file |
| No description | Clear What / Why / How to test |
| Mixes a rename, a bugfix, and a feature | One concern only |
| No tests | One regression test added |

Then a tour of **conventional comments** with examples:

- `praise:` — "praise: this is a nicely focused diff, easy to review"
- `nitpick:` — "nitpick: prefer `is None` over `== None` for PEP8"
- `suggestion:` — "suggestion: extract this into a helper; it's used three times"
- `issue:` — "issue: this swallows the exception; the caller can't handle it"
- `question:` — "question: why don't we close the redis connection here?"
- `thought:` — "thought: this might be a good place to add metrics later"
- `chore:` — "chore: rebase onto main before merging"

The labels do three things at once: signal *severity*, frame the tone, and let the author scan the review by category.

## We do (15 min)

Together, review one volunteer's branching-agreement PR from Block C using conventional comments. Class suggests comments aloud; instructor types them into the PR. Aim for at least one of each: `praise`, `suggestion`, `question`, and `nitpick`.

## You do (40 min)

### Part 1 — Review a peer's PR (20 min)

1. Pick a peer's PR from Block C. (Coordinate with your cohort so no PR has more than one reviewer for this exercise.)
2. **Read it slowly** — at least 5 minutes before writing anything. Look at:
   - The diff
   - The PR description (does it answer *what* and *why*?)
   - The commit messages
3. Leave **≥ 4 conventional comments**, spanning at least **3 of**: `praise`, `suggestion`, `question`, `nitpick`, `issue`.
4. Submit the review:
   - **Request changes** if there's at least one `issue:` comment
   - **Approve** otherwise

> Watch your tone. Conventional comments help, but they're not magic — if you wouldn't say it in person, don't write it in the PR.

### Part 2 — Address feedback on your own PR (15 min)

1. Read every comment on your PR (the one you opened in Block C).
2. For each: react (`+1` for praise, reply to questions, push a fix-up commit for issues/suggestions you accept, reply with reasoning for ones you decline).
3. Re-request review when you're ready.

### Part 3 — Merge cleanly (5 min)

1. Once approved, merge using the style your team agreement specified.
2. If you specified `--no-ff` or rebase + merge: select it from the dropdown on the merge button. GitHub honors three options here — pick deliberately.
3. Delete the branch after merge (GitHub offers a button; take it).

## Stretch challenge `[OPTIONAL]`

Set up **branch protection** on a repo you own. Configure:

- Require pull request reviews before merging (1 approval)
- Dismiss stale reviews when new commits are pushed
- Restrict who can push directly to `main` (no one, including admins, ideally)

Take a screenshot of the settings page; share it in your cohort chat with a one-line description of what you protected against.

> We deliberately don't require "passing CI" here because Lab 02 ships no CI. Lab 03 introduces it; you'll come back to branch protection then.

## Debrief (10 min)

- One thing you saw in someone else's PR that you'll steal for your own work?
- One habit you want to drop from your own PR-writing or reviewing?
- When does a `request-changes` review do more harm than good?
- For your Ignition projects specifically: what's the smallest change you could meaningfully PR? (Hint: the smaller the unit, the easier review becomes. Whole-gateway-backup PRs are unreviewable.)
