# Lab 02 — Branching and Pull Requests

One **We-do / we do / you do** covering two linked topics:
how a team *branches*, and how changes flow through *pull requests*. They're one
story. A branching strategy is the plan; a pull request is where the plan meets
reality — it's where your branch naming, your review habits, and your merge-style
rules actually get used. So you'll learn both, then exercise both on the same
piece of work.

## What you're working on

The subject of this lab is a small but **real Ignition project**
(`projects/lab-project/`): a Perspective HMI screen (a refrigeration-plant overview)
and two Python script libraries. You don't need prior Ignition experience — the
gateway's admin complexity is abstracted away, and what you edit is approachable (a
small Python function, or a property on a view). The lab is about the **Git
workflow** around those files: how you branch, how you open and review a PR, how you
merge. Gateway config, modules, and deploys are deliberately out of scope — they
arrive in Lab 04.

## Setup (optional but recommended)

You can do every exercise from the files alone. But spinning up the gateway once
makes the project tangible — you can see that `projects/lab-project/` is a real
thing the gateway runs:

```bash
cp .env.example .env
ops/setup.sh          # boots one Ignition gateway, waits for RUNNING
# open http://localhost:8088  → log in with the .env credentials
```

Before opening any PR, run the validator — it's the green/red signal this lab
uses in place of a test suite:

```bash
ops/validate.sh       # checks every project file is valid JSON / parses as Python
```

## Goal

By the end of this lab you should be able to:

- Describe **Git Flow**, **GitHub Flow**, and **trunk-based development**, pick one that fits a team, and capture it in a one-page agreement a new hire could follow
- Open a PR a reviewer enjoys reading: small, scoped, with a clear what / why / how-to-test
- Review someone else's PR with feedback that helps, and choose between approve, request-changes, and comment-only
- Merge cleanly when approved, using the merge style your team agreed on

Read-ahead: [`docs/branching-strategies.md`](../docs/branching-strategies.md) — the three strategies, with diagrams. Optional deep-dive on review craft: [`docs/pr-review-style.md`](../docs/pr-review-style.md).

---

## We-do

### Part A — Branching strategies, side by side

Whiteboard. Same release scenario applied to each strategy:

> *Your team is shipping v2.0 of the product next week. Mid-week, a customer reports a P1 bug in v1.2 that's already in production. You need to ship the v1.2 hotfix today AND keep v2.0 on track.*

For each strategy, the instructor sketches (the diagrams in [`docs/branching-strategies.md`](../docs/branching-strategies.md) mirror these):

1. **Git Flow** — `develop`, `main`, `release/*`, `feature/*`, `hotfix/*`. Where does the hotfix branch off? Where does it merge back to? Why both?
2. **GitHub Flow** — `main` only; feature branches; PRs into `main`; deploy from `main`. Where does v1.2 even live?
3. **Trunk-based** — `main` only; very short-lived branches (≤1 day); feature flags do the heavy lifting. How does the v1.2 hotfix differ?

Pay attention to: branch lifetime, who owns the release, how rollbacks work, and how the graph looks at the end of the week.

### Part B — From strategy to pull request

A branching strategy only comes to life through pull requests — so here's what a
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

Then a quick word on **leaving** review feedback. You don't need a formal system —
just prefix each comment with what kind it is, so the author knows how to react.
Three labels cover almost everything:

- `praise:` — something genuinely good. "praise: nicely focused diff, easy to review."
- `suggestion:` — a specific, optional improvement. "suggestion: collapse these two ifs into one."
- `issue:` — something that should change before merge. "issue: this still throws on a null reading; `format_reading(None, '°C')` errors instead of showing a placeholder."

That's enough to review well today. If you want the fuller toolkit — more labels, tone, and handling disagreement — it's in the optional [`docs/pr-review-style.md`](../docs/pr-review-style.md).

---

## We do

### Part A — Pick a strategy for a real team (pairs)

Pair up.

1. Describe your *partner's* team to them: release cadence, regulatory constraints, team size, how often you ship to production.
2. Together, sketch which strategy fits **their** team best and why. One paragraph.
3. Swap. Defend yours.

> If you've never worked on a multi-engineer team, sketch this for an Ignition team you've consulted with — or use the scenario in `docs/branching-strategies.md` as a stand-in.

### Part B — Review a sample PR together (class)

Back as a class, put the **"bad PR"** from the We-do on the projector. Together:

1. Rewrite its title and description so it's self-describing (What / Why / How to test).
2. Leave a few conventional comments aloud — at least a `praise:`, a `suggestion:`, and an `issue:` — and the instructor types them in.

This is the dry run for the real review you'll do solo in a moment.

---

## You do

Now you'll write your team's branching rules, then actually exercise them: open a
docs PR and a code PR, review a peer's, and merge using the style you chose. By
the end, the agreement you wrote in step 1 is something you *used* in steps 2 and 4
— not just a document.

### 1. Write your branching agreement → open a docs PR

1. From your fork's `main`, branch:
   ```bash
   git switch -c feature/branching-agreement-<your-initials>
   ```
2. Create `docs/branching-strategy.md` (a new file in `docs/`). Write a 1-page team agreement using this structure:
   - **Context** — 2–3 sentences on your team's product, size, and release cadence
   - **Chosen strategy** — Git Flow, GitHub Flow, or trunk-based, and *why*
   - **Branch naming** — `feature/...`, `fix/...`, `release/...`, etc.
   - **Merge style** — fast-forward, `--no-ff`, or rebase + merge. Justify.
   - **Release process** — how a change goes from `main` to production
   - **Hotfix rules** — what's the procedure when v-current is on fire?
3. Commit with a [Conventional Commits](https://www.conventionalcommits.org/) message (e.g., `docs: add team branching agreement`).
4. Push to your fork (`git push -u origin feature/branching-agreement-<your-initials>`).
5. Open a PR with **base = your fork's `main`** using the [PR template](../.github/pull_request_template.md). Fill out **What**, **Why**, **How to test** (for a docs PR, "how to test" is "read the doc"). Drop the link in the cohort chat and tag a peer as reviewer. Don't merge yet.

### 2. Ship a small code change → open a code PR

Now a *code* PR — where "is it scoped?" and "does it break a call site?" actually
bite. Pick **one** target. The script is the main path; the view is a visual
alternative if you'd rather see your change in the gateway UI.

**Option A — the display script (recommended).** `lab.display.format_reading()` in
[`projects/lab-project/ignition/script-python/lab/display/code.py`](../projects/lab-project/ignition/script-python/lab/display/code.py)
formats a tag reading for the HMI — `format_reading(-6.5, "°C")` → `"-6.5 °C"`. But
on a **null reading** (a tag not yet read, or a comms loss) `value` is `None`, and
`"%.1f" % None` throws — so the label shows an error instead of a value. Fix it:
return a clean placeholder like `"-- °C"` for `None` (and other bad input), while
keeping the normal numeric formatting.

**Option B — the Overview view (stretch / visual).** Edit
[`projects/lab-project/com.inductiveautomation.perspective/views/pages/overview/view.json`](../projects/lab-project/com.inductiveautomation.perspective/views/pages/overview/view.json):
change a label's text, or add one. Keep the diff small and the JSON valid. If your
gateway is up, reload it with `docker compose restart` (or, faster, `ops/scan.sh`
if you've set up an API key) and reopen the project to see your change — the
Discharge Temp tile is bound to that script via runScript, too.

Then, whichever you picked:

1. Branch off your fork's `main`, **naming the branch the way your branching agreement says** (e.g. `fix/null-reading-<your-initials>`). This is the first place your agreement bites.
2. Make the change. Run `ops/validate.sh` — green.
3. Commit with a Conventional Commits message (e.g. `fix(display): show placeholder for null readings`).
4. Push and open a PR (**base = your fork's `main`**) using the [PR template](../.github/pull_request_template.md). "How to test" is concrete now: `ops/validate.sh`, plus the behavior you changed. Drop the link in the cohort chat.

> Keep it under ~15 lines of diff. This is the "small, one-concern" PR from the We-do — actually build one.

### 3. Review a peer's code PR

1. Pick a peer's code PR from the cohort chat. (Coordinate so no PR has more than one reviewer for this exercise.)
2. **Read it slowly** — at least 5 minutes before writing anything. Look at:
   - The diff: for a script fix, does it accidentally break the `name`-defaults-to-default case? For a view edit, is the JSON still well-formed and the change scoped?
   - How they verified it: did they run `validate.sh`? Is the "How to test" something you could actually follow?
   - The PR description and commit message.
3. Leave a few genuinely helpful comments — at minimum a `praise:` and a `suggestion:`, plus an `issue:` if something is actually wrong. Quality over quantity; there's no quota.
4. Submit the review:
   - **Request changes** if there's at least one `issue:` comment
   - **Approve** otherwise

> Watch your tone. Conventional comments help, but they're not magic — if you wouldn't say it in person, don't write it in the PR.

### 4. Respond, then merge both PRs

1. On your **code** PR: read every comment and react (`+1` for praise, reply to questions, push a fix-up commit for issues/suggestions you accept, reply with reasoning for ones you decline). Re-request review when ready.
2. Once each is approved, **merge both your docs PR and your code PR** using the merge style your agreement specified — this is where the agreement bites again.
   - If you specified `--no-ff`, squash, or rebase + merge: select it from the dropdown on the merge button. GitHub honors three options here — pick deliberately.
3. Delete each branch after merge (GitHub offers a button; take it).

---

## Stretch challenges `[OPTIONAL]`

- **Migration plan.** Add a section to your branching-agreement doc describing how you'd move your team *from* its current strategy *to* the one you chose over a quarter: one concrete first step (next week), the riskiest change and how you'd de-risk it, and a measurable success criterion. Update the PR. The migration plan is often more interesting than the chosen strategy.
- **Branch protection.** On a repo you own, require PR reviews before merging (1 approval), dismiss stale reviews on new commits, and restrict direct pushes to `main` (no one, including admins). Screenshot the settings and share it with a one-line description of what you protected against. We don't require "passing CI" here because Lab 02 ships no CI — `validate.sh` is something *you* run; Lab 03 turns it into a required status check.

## Debrief

- Which of the three branching strategies surprised you? Which would you adopt tomorrow if it were up to you?
- One thing you saw in someone else's PR that you'll steal for your own work? One habit you want to drop?
- When does a `request-changes` review do more harm than good?
- For your Ignition projects specifically: what's the smallest change you could meaningfully PR? You just did one — a single script function, a single view property. (The smaller the unit, the easier review becomes. Whole-gateway-backup PRs are unreviewable — exactly the problem Lab 04 onward tackles.)
