# Block C — instructor answer key

> **Do not read this before you've attempted the You-do solo.** The point of Block C is the *process* of writing the team agreement, not getting the "right" strategy.

## What "good" looks like for the team-agreement doc

There's no single correct strategy. Evaluate participants' `docs/branching-strategy.md` against four criteria:

### 1. The chosen strategy fits the described context

Look at the **Context** section, then the **Chosen strategy** section. Does the strategy match?

| If Context describes… | Then strategy should usually be… |
|---|---|
| Single SaaS, 2–10 engineers, continuous deploy | GitHub Flow |
| Multiple supported product versions in production | Git Flow (or GitHub Flow + version tags) |
| Regulated environment, formal release validation | Git Flow |
| Small high-trust team with feature flags | Trunk-based |
| Ignition shop with multi-gateway customers | GitHub Flow + per-customer tags (Lab 05 territory) |

If a participant picks **trunk-based** for a team that has no feature-flag system, push back in the review: where do in-progress features live in production?

If a participant picks **Git Flow** for a single-product SaaS that deploys continuously, push back: what is the `develop` branch buying you?

### 2. Branch naming is specific

Acceptable:
- `feature/<jira-id>-short-slug`
- `fix/<short-slug>`
- `release/v<major.minor>` (Git Flow only)
- `hotfix/<short-slug>` (Git Flow only)

Not acceptable:
- "use descriptive names" with no concrete pattern
- `dev`, `test`, `prod` as branch names (these should be tags/environments, not branches)

### 3. Merge style is justified

The doc should pick one of: fast-forward only, `--no-ff` merge commits, or rebase + merge. And it should *say why*.

Best answer: "We use `--no-ff` because we want the branch shape preserved in `git log --graph` — it makes 'what shipped in v1.2' visible without tags."

Worst answer: "We use rebase because it's clean." Why is clean better than informative? Push them.

### 4. Hotfix rules are concrete

Concrete: "Branch from the production tag (`v1.2`), fix, cherry-pick into `main` or merge into `release/v1.2`, tag as `v1.2.1`, deploy."

Vague: "Hotfix as needed." This is not a rule, it's a hope.

## Common pitfalls in participant docs

- **Strategy + reality mismatch.** A team has been doing trunk-based informally and writes "Git Flow" because it sounds more sophisticated. Probe: "what's the smallest change you'd actually move to Git Flow for?"
- **Hand-waved hotfix process.** Especially for Ignition teams — what does "hotfix the gateway" mean? Is it a deploy of the whole project, or a config-only change, or a single tag value? They'll figure this out in Lab 04, but mention it now.
- **No mention of who merges.** Who has merge rights? The PR author? A reviewer? Anyone with approval? Worth asking.
- **No mention of release cadence.** "We ship when ready" is not a cadence. Push for at least a rough rhythm.

## What to do in your peer review (You-do step 5)

You'll be the second reviewer on many of these PRs. Aim to leave at least one comment per criterion above. Conventional comments are introduced formally in Block D, but feel free to use them already here — the participants haven't seen them yet, so it's a soft introduction.

## Stretch — migration plan rubric

Migration plans are often more interesting than the chosen strategy. Evaluate against:

- **Concrete first step** — what happens next *Monday*? "Adopt GitHub Flow" is not a step; "Add a PR template to the repo and require reviews for merging" is.
- **Riskiest change called out** — long-lived branches don't disappear overnight. A serious migration plan acknowledges the messiest case and de-risks it.
- **Success criterion** — a measurable, time-bounded outcome. "Cycle time from PR open to merge drops below 24 hours by end of Q3."

A participant who can write a migration plan probably can run a migration. One who can't, will probably keep doing whatever they're doing.

## Debrief crib

- *"Which strategy surprised you?"* — Most non-developers are surprised by **trunk-based**. It looks chaotic but works in mature teams. Worth contrasting with Git Flow, which looks rigorous but mostly creates merge work.
- *"Which would you adopt tomorrow?"* — Push for a one-sentence reason. "GitHub Flow because we're a 4-person team and continuous deploy" is a good answer. "GitHub Flow because it's simple" without a fit-to-team reason is shallow.
- *"What makes branching harder for Ignition teams?"* — Three honest answers:
  1. Project export format makes diffs noisy
  2. Multi-gateway state means "what's in production" is plural
  3. Hotfix-via-Designer is still a thing in many shops, and it bypasses Git entirely
- Foreshadow Lab 04: most of what we've discussed assumes a clean text-file diff. Ignition projects test that assumption.
