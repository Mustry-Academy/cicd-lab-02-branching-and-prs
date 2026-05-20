# Block C — Branching strategies compared

**Duration:** ~90 minutes 
* 20 min demo
* 15 min we-do
* 35 min you-do
* 10 min debrief
* ~10 min buffer

## Goal

You should leave this block able to:

- Describe **Git Flow**, **GitHub Flow**, and **trunk-based development** in your own words
- Pick a strategy that fits your team's release cadence and constraints, and defend the choice
- Translate the choice into a one-page written team agreement that a new hire could follow

## Pre-flight

```bash
git fetch --tags
git checkout block-c-start
```

If you'd like to read ahead: [`docs/branching-strategies.md`](../docs/branching-strategies.md).

## I do (20 min)

Whiteboard. Same release scenario applied to each strategy:

> *Your team is shipping v2.0 of the product next week. Mid-week, a customer reports a P1 bug in v1.2 that's already in production. You need to ship the v1.2 hotfix today AND keep v2.0 on track.*

For each strategy, the instructor sketches:

1. **Git Flow** — `develop`, `main`, `release/*`, `feature/*`, `hotfix/*`. Where does the hotfix branch off? Where does it merge back to? Why both?
2. **GitHub Flow** — `main` only; feature branches; PRs into `main`; deploy from `main`. Where does v1.2 even live?
3. **Trunk-based** — `main` only; very short-lived branches (≤1 day); feature flags do the heavy lifting. How does the v1.2 hotfix differ?

Pay attention to: branch lifetime, who owns the release, how rollbacks work, and how the graph looks at the end of the week.

## We do (15 min)

Pair up.

1. Describe your *partner's* team to them: release cadence, regulatory constraints, team size, how often you ship to production.
2. Together, sketch which strategy fits **their** team best and why. One paragraph.
3. Swap. Defend yours.

> If you've never worked on a multi-engineer team, sketch this for an Ignition team you've consulted with — or use the scenario in `docs/branching-strategies.md` as a stand-in.

## You do (35 min)

Open a real PR proposing a branching strategy for your own team.

1. From `block-c-start`, branch:
   ```bash
   git switch -c feature/branching-agreement-<your-initials>
   ```
2. Create `docs/branching-strategy.md` (yes, a new file in the `docs/` directory). Write a 1-page team agreement using this structure:
   - **Context** — 2–3 sentences on your team's product, size, and release cadence
   - **Chosen strategy** — Git Flow, GitHub Flow, or trunk-based, and *why*
   - **Branch naming** — `feature/...`, `fix/...`, `release/...`, etc.
   - **Merge style** — fast-forward, `--no-ff`, or rebase + merge. Justify.
   - **Release process** — how a change goes from `main` to production
   - **Hotfix rules** — what's the procedure when v-current is on fire?
3. Commit with a message that follows [Conventional Commits](https://www.conventionalcommits.org/) (e.g., `docs: add team branching agreement`).
4. Push the branch.
5. Open a PR against `main` of this lab repo using the [PR template](../.github/pull_request_template.md). Fill out **What**, **Why**, **How to test** (yes — for a docs PR, "how to test" is "read the doc").
6. Tag one of your peers as reviewer. Don't merge yet — Block D will use this PR.

> Stuck on which strategy to pick? See `docs/branching-strategies.md` for a decision matrix.

## Stretch challenge `[OPTIONAL]`

Add a **migration plan** section to your team-agreement doc. Describe how you would move your team *from* its current strategy *to* the one you chose, over the next quarter. Include:

- One concrete first step (next week)
- The riskiest change and how you'd de-risk it
- A success criterion you'd measure at the end of the quarter

Update the PR. The migration plan is often more interesting than the chosen strategy.

## Debrief (10 min)

- Which of the three strategies surprised you in some way?
- Which would you adopt tomorrow if it were entirely up to you?
- For Ignition teams specifically: what makes branching harder than for typical web/app teams? (Hint: gateway state, project export format, multi-gateway deploys — all of which we'll wrestle with from Day 3 onward.)
