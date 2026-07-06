# Lab 02: Branching and Pull Requests

One **we-do / you-do** covering two linked topics:
how a team *branches*, and how changes flow through *pull requests*. They're one
story. A branching strategy is the plan; a pull request is where the plan meets
reality, where your branch naming, your review habits, and your merge-style rules
actually get used. So you'll learn both, then live them: you'll run the release-week
hotfix scenario through Git Flow on a real Ignition project, end to end.

## What you're working on

The subject of this lab is a small but **real Ignition project**
(`projects/lab-project/`): a Perspective HMI screen (the Oatmakers Site 04
oat-line overview, the client from Lab 01) and two Python script libraries. You don't need prior Ignition experience: the
gateway's admin complexity is abstracted away, and what you edit is approachable (a
small Python function, or a new view). The lab is about the **Git workflow** around
those files: how you branch, how you open and review a PR, how you merge. Gateway
config, modules, and deploys are deliberately out of scope; they arrive in Lab 04.

## Setup (optional but recommended)

You can do every exercise from the files alone. But spinning up the gateway once
makes the project tangible, and lets you see your new v2.0 view go live:

```bash
cp .env.example .env
scripts/setup.sh          # boots one Ignition gateway, waits for RUNNING
# open http://localhost:8088  → log in with the .env credentials
```

Before opening any PR, run the validator. It's the green/red signal this lab uses
in place of a test suite:

```bash
scripts/validate.sh       # checks every project file is valid JSON / parses as Python
```

## Goal

By the end of this lab you should be able to:

- Describe **Git Flow**, **GitHub Flow**, and **trunk-based development**, and pick one that fits a team
- Run a **Git Flow hotfix** end to end: branch off production, fix, and merge back to both `main` and `develop` (with a version tag)
- Open a PR a reviewer enjoys reading: small, scoped, with a clear what / why / how-to-test
- Review someone else's PR with feedback that helps, and choose between approve, request-changes, and comment-only
- Merge cleanly and in the right order when approved, and open a cross-fork PR upstream

Read-ahead: [`docs/branching-strategies.md`](../docs/branching-strategies.md) covers the three strategies, with diagrams. Optional deep-dive on review craft: [`docs/pr-review-style.md`](../docs/pr-review-style.md).

---

## We-do

### Part A: from strategy to pull request

A branching strategy only comes to life through pull requests, so here is what a
good one looks like. Two PRs side by side on the projector:

| Bad PR | Good PR |
|---|---|
| Title: "update stuff" | Title: "fix(display): handle null readings without crashing" |
| 800-line diff across 12 files | 6-line diff in one file |
| No description | Clear What / Why / How to test |
| Mixes a rename, a bugfix, and a feature | One concern only |
| Leaves `validate.sh` red | `validate.sh` green |

The good column is the whole lesson. A PR is easy to review when it's **small**,
does **one thing**, is **self-describing** (What / Why / How to test), and shows
**how it was verified**. If you catch yourself writing "and" in the title, split
the PR.

### Part B: leaving review feedback

You don't need a formal system, just prefix each comment with what kind it is, so
the author knows how to react. Three labels cover almost everything:

- `praise:` something genuinely good. "praise: nicely focused diff, easy to review."
- `suggestion:` a specific, optional improvement. "suggestion: collapse these two ifs into one."
- `issue:` something that should change before merge. "issue: this still throws on a null reading; `format_reading(None, '°C')` errors instead of showing a placeholder."

That's enough to review well today. If you want the fuller toolkit (more labels,
tone, and handling disagreement) it's in the optional
[`docs/pr-review-style.md`](../docs/pr-review-style.md).

---

## You do

You'll live the release-week scenario from the teaching deck, for real, on your own
fork. Ship a v2.0 feature, get ambushed by a P1 bug in production, and thread both
through **Git Flow**, exactly the way Chapter 1 drew it. Then your peers review your
PRs, you merge in the right order, and you send one PR back upstream.

Do the whole thing in your breakout room, sharing your screen. Open PRs early and
drop every link in the cohort chat: the review step needs a peer's PR to exist, and
merging needs a peer to have reviewed yours.

### 1. Discuss: which strategy fits your team? (breakout room)

Talk it through out loud, no writing. Each person sketches their own team or
project (release cadence, regulatory constraints, team size, how often production
ships), and the room argues which of Git Flow, GitHub Flow, or trunk-based fits
**their** reality, and why. Disagreement is the point.

You'll run step 2 in **Git Flow** regardless. Knowing which one you'd actually pick
is what makes feeling the difference land in the stretch.

> Never worked on a multi-engineer team? Argue it for an Ignition team you've
> consulted with, or use the scenario in `docs/branching-strategies.md` as a stand-in.

### 2. Run the release-week scenario in Git Flow

`v1.2` is live in production. You start the v2.0 feature, and mid-work a P1 bug in
production ambushes you. You thread both through Git Flow.

**Step 1: set up the Git Flow world.** On your fork, make sure `main` exists and
create `develop` off it, the two long-lived branches Git Flow needs. Then tag what's
live as `v1.2` on `main`, and push both the branch and the tag.

```bash
git switch main
git switch -c develop
git push -u origin develop

git switch main
git tag v1.2
git push origin v1.2      # "production" is v1.2
```

Mental model: `main` = production, `develop` = the next release in progress,
`v1.2` = the exact commit customers are running.

**Step 2: ship the v2.0 feature (a new Perspective view).** Branch off `develop`
(features target the next release, not `main`), named per your discussion, e.g.
`feature/v2-<view-name>-<your-initials>`. Add a new view: the easiest path is to
copy the `overview` resource folder to a new name under `views/pages/`, edit its
`view.json` title, and register the page in `page-config/config.json` so it's
reachable. Run `scripts/validate.sh` (green), commit with a
[Conventional Commits](https://www.conventionalcommits.org/) message, push, and open
a PR with **base = `develop`**. Drop the link in chat, tag a peer, and **leave it
open**: the ambush comes before you merge.

> Gateway up? `scripts/scan.sh` (or `docker compose restart`), then open the project.
> Your new page is there. That's the "it goes live" moment.

**Step 3: the P1 ambush, hotfixed the Git Flow way.** Your feature is still open when
a customer hits the null-reading crash in v1.2, live. It can't wait for v2.0.

1. Branch the hotfix off **production** (`main` / the `v1.2` tag), **not** `develop`:
   `hotfix/null-reading-<your-initials>`. Your v2.0 work isn't in production, so it
   must not ride along.
2. The bug: `lab.display.format_reading()` in
   [`projects/lab-project/ignition/script-python/lab/display/code.py`](../projects/lab-project/ignition/script-python/lab/display/code.py)
   does `"%.1f" % None` on a null reading (a tag not yet read, or a comms loss) and
   throws, so the label shows an error instead of a value. Fix it: return a clean
   placeholder like `"-- °C"` for `None` (and other bad input), while keeping the
   normal numeric formatting. Remember `0` is a valid reading and must still format as
   `"0.0 °C"`. Run `scripts/validate.sh` (green).
3. **Merge it twice**, the Git Flow move: into `main` (production gets the fix), tag
   `v1.2.1`, **and** into `develop` (so v2.0 doesn't regress it). Do both via PRs so
   your peers can review.
4. Now finish the feature: pull the hotfix down into your feature branch
   (`git merge develop`), so its PR into `develop` stays clean.

```bash
git switch main
git switch -c hotfix/null-reading-<ini>
# fix format_reading(), then:
scripts/validate.sh
git commit -am "fix(display): placeholder for null readings"
# PR 1: hotfix -> main    (then tag v1.2.1)
# PR 2: hotfix -> develop
git switch feature/v2-<view-name>-<ini>
git merge develop         # pick up the hotfix
```

> The whole lesson: a hotfix that only lands on `main` reappears next release,
> because `develop` never got it. Git Flow's "merge twice" is annoying *and* exactly
> why it exists. You just felt both.

### 3. Review a peer's PR, then merge yours

You each have a hotfix PR and a feature PR open. Coordinate in chat so each PR gets
one reviewer.

1. Pick a peer's PR from the chat. The **hotfix** is the richest to review.
2. **Read it slowly**, at least 5 minutes before writing anything. For the hotfix:
   - Do valid readings still format? `format_reading(162.0, "°C")` must return
     `"162.0 °C"`, and `format_reading(0, "°C")` must return `"0.0 °C"` (zero is a
     valid reading, not "missing").
   - Git Flow check: did it branch off **production**, not `develop`?
   - Did they run `validate.sh`? Is the "How to test" something you could follow?
   For the feature PR: is the JSON well-formed, the page registered, the change scoped?
3. Leave a few genuinely helpful comments: at minimum a `praise:` and a `suggestion:`,
   plus an `issue:` if something is actually wrong. Quality over quantity, no quota.
4. Submit the review: **Request changes** if you left at least one `issue:`,
   **Approve** otherwise.

> Watch your tone. Conventional comments help, but they're not magic. If you
> wouldn't say it in person, don't write it in the PR.

Then respond and merge, in Git Flow order:

1. On your PRs, react to every comment (`+1` for praise, reply to questions, push a
   fix-up commit for what you accept, reply with reasoning for what you decline).
   Additive commits, no force-push during review. Re-request review when ready.
2. Merge in order: the two hotfix PRs first (into `main`, tag `v1.2.1`, then into
   `develop`), then the feature PR into `develop`.
3. Delete each branch after merge (GitHub offers a button; take it).

### 4. Send one PR back upstream (open source)

Every PR so far had base = your fork. Now open one with **base = the upstream repo**
(`mustry-academy/cicd-lab-02-branching-and-prs`), head = your fork's branch. GitHub
calls this a cross-fork PR. Pick your cleanest branch (the hotfix is ideal), and
write the description for a stranger: the maintainer has none of your context, so the
What / Why / How to test is all they get.

Fork, branch, PR back to the original repo is the entire open-source contribution
model. Linux, Python, Ignition modules on GitHub, all of it is this loop at scale.
We won't merge cohort PRs into the course repo; the point is *doing* the cross-fork
PR, not landing it.

---

## Stretch challenges `[OPTIONAL]`

- **Now do it in GitHub Flow.** Same scenario, one long-lived branch. Reset to
  GitHub Flow (one `main`, no `develop`, no `release/*`), and run the same two changes:
  the v2.0 view on a `feature/*` branch, the null-reading fix on a `fix/*` branch,
  both PR'd straight into `main`. Notice the difference: the hotfix merges **once**,
  not twice. But where does `v1.2` live? If production were an older release, GitHub
  Flow has nowhere to put the fix. That's the whole trade-off, in your hands. Git
  Flow's double-merge felt like bureaucracy until you ask GitHub Flow to patch an
  *old* version and it can't. You now know both from the inside.
- **Branch protection.** On a repo you own, require PR reviews before merging
  (1 approval), dismiss stale reviews on new commits, and restrict direct pushes to
  `main` (no one, including admins). Screenshot the settings and share it with a
  one-line description of what you protected against. We don't require "passing CI"
  here because Lab 02 ships no CI: `validate.sh` is something *you* run, and Lab 03
  turns it into a required status check.

## Debrief

- Did the double-merge feel worth it? When does Git Flow's ceremony earn its keep, and when is it just merge work?
- Which of the three branching strategies surprised you? Which would you adopt tomorrow if it were up to you?
- One thing you saw in someone else's PR that you'll steal for your own work? One habit you want to drop?
- When does a `request-changes` review do more harm than good?
- For your Ignition projects specifically: what's the smallest change you could meaningfully PR? You just did one: a single script function, a single new view. (The smaller the unit, the easier review becomes. Whole-gateway-backup PRs are unreviewable, exactly the problem Lab 04 onward tackles.)
