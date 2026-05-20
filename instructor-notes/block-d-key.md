# Block D — instructor answer key

> **Do not read this before you've attempted the You-do solo.** This block is mostly about doing the review well, not knowing the "right" comments. Read this after you've reviewed your peer's PR.

## What "good" looks like for the peer review

The You-do requires ≥ 4 conventional comments spanning ≥ 3 labels from `praise / suggestion / question / nitpick / issue`. Aim higher: a serious review of a one-page docs PR is usually 5–8 comments.

### A reference review skeleton

For most branching-agreement PRs from Block C, a strong review will include something like:

- **One `praise:`** — something genuinely good. The clarity of the Context section, or the specificity of the hotfix rule. Praise is not throwaway — it tells the author what's working.
- **At least one `question:`** — there's almost always something genuinely unclear. "question: when you say 'we deploy when ready,' how do you decide *who* presses the button?" Questions surface assumptions the author didn't realize they had.
- **At least one `suggestion:`** — a specific change the author could make. Not a vague "this could be better" — a concrete alternative. "suggestion: rename `feature/*` to `feat/*` to match Conventional Commits."
- **Optionally `nitpick:`** — for small style things. PEP8, capitalization, ordering. Always non-blocking.
- **`issue:` only when you mean it.** If the team agreement contradicts itself, or violates something the participant called out as a constraint, that's a real issue. If the strategy doesn't fit the context, that's a real issue. Don't use `issue:` for taste differences.

### Tone — what to flag

Watch reviews for:

- **Sarcasm or condescension.** "Why didn't you just pick GitHub Flow?" reads as judgmental. Better: "question: I'm curious what made Git Flow feel right over GitHub Flow for this team — was it the regulatory step?"
- **Vague criticism.** "This isn't very specific" is not actionable. Better: "suggestion: 'feature branches' is generic — would you commit to a specific pattern like `feature/<ticket-id>-<slug>`?"
- **Drive-by comments without context.** A single `?` or `huh?` is unhelpful. Push them to expand.
- **Blocker comments dressed as nitpicks.** If the comment would prevent merge, it shouldn't be labeled `nitpick:` — that's misleading the author.

If you spot any of these, model the rewrite in your own review comment on the same PR (or in the debrief). The label vocabulary is most of the lesson, but tone is where it actually lands.

## What "good" looks like for the response (Part 2)

Authors should:

- React to every comment with *something* (a reply, a reaction, or a fix-up commit).
- For `suggestion:` and `issue:` comments: explicit accept/decline with reasoning. Silent ignores are a smell.
- For `question:` comments: an answer, even if short.
- Re-request review after substantive changes.

Common author mistakes:

- **Marking conversations as resolved without responding.** Push back: even a `+1` reply is more communicative than silent resolution.
- **Accepting every suggestion without thinking.** Authors are not obligated to agree. A `decline: I think keeping the longer name is clearer here` is a valid response.
- **Force-pushing over fix-ups.** A force-push during review nukes the reviewer's context. Prefer additive commits during review; squash on merge if you must.

## Merge style (Part 3)

GitHub's merge dropdown gives three options:

| Option | Effect | Use when |
|---|---|---|
| **Create a merge commit** | `--no-ff`; preserves branch shape | Team agreement specifies `--no-ff` |
| **Squash and merge** | One commit on `main` representing the entire PR | Small PRs, team prefers linear history |
| **Rebase and merge** | Replays commits onto `main` linearly; no merge commit | Trunk-based, very clean linear-history teams |

Participants should pick the one their Block C team agreement specified — that's the whole point of writing it.

If GitHub doesn't show all three: the repo has restricted them in Settings → Branches → Merge button options. Worth surfacing as a procedural point.

## Stretch — branch protection

Acceptable settings vary by team. Look for at least:

- "Require pull request reviews before merging" — usually 1 approval
- "Dismiss stale pull request approvals when new commits are pushed" — fights against approve-and-then-force-push
- "Do not allow bypassing the above settings" — applies the rules even to admins

We deliberately don't require "passing CI" here because Lab 02 has no CI. Lab 03 introduces it; when participants set up branch protection then, they should layer "require status checks" on top.

## Debrief crib

- *"One thing you'll steal?"* — Push for specifics. "I liked their PR description" is shallow. "I liked that they linked to the ticket and quoted the customer's report" is real.
- *"One habit to drop?"* — The honest answers are often: "writing PRs too big," "not testing my own change before opening," "leaving lots of nitpicks instead of one suggestion."
- *"When does request-changes do more harm than good?"* — Three common cases:
  1. When the only issues are nitpicks (use approve + nitpick comments instead).
  2. When the reviewer is the second of two and the first already approved (use comment-only).
  3. When the timing matters and the author is offline (consider a synchronous chat instead of a blocking review).
- *"Smallest meaningful Ignition PR?"* — Honest answers range widely: a single Perspective property change, a single tag historian config change, a single script function rewrite. The point is to seed the idea that PR-sized changes are *possible* for Ignition, even though many shops currently PR whole gateway backups.

End the block with one explicit foreshadowing line: **"Tomorrow we add the CI safety net that makes all of this scale."**
