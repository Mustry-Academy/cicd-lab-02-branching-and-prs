# Lab 02 — instructor answer key

> **Do not read this before you've attempted the You-do solo.** The point of this
> lab is the *process* — writing the team agreement, and reviewing well — not
> getting the "right" strategy or the "right" comments.

The lab is one I-do / we-do / you-do flow covering two topics. This key is grouped
by topic to match — [`exercises/lab.md`](../exercises/lab.md) for the flow itself.

---

# Branching strategies

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

## Stretch — migration plan rubric

Migration plans are often more interesting than the chosen strategy. Evaluate against:

- **Concrete first step** — what happens next *Monday*? "Adopt GitHub Flow" is not a step; "Add a PR template to the repo and require reviews for merging" is.
- **Riskiest change called out** — long-lived branches don't disappear overnight. A serious migration plan acknowledges the messiest case and de-risks it.
- **Success criterion** — a measurable, time-bounded outcome. "Cycle time from PR open to merge drops below 24 hours by end of Q3."

A participant who can write a migration plan probably can run a migration. One who can't, will probably keep doing whatever they're doing.

## Branching-strategy debrief crib

- *"Which strategy surprised you?"* — Most non-developers are surprised by **trunk-based**. It looks chaotic but works in mature teams. Worth contrasting with Git Flow, which looks rigorous but mostly creates merge work.
- *"Which would you adopt tomorrow?"* — Push for a one-sentence reason. "GitHub Flow because we're a 4-person team and continuous deploy" is a good answer. "GitHub Flow because it's simple" without a fit-to-team reason is shallow.
- *"What makes branching harder for Ignition teams?"* — Three honest answers:
  1. Project export format makes diffs noisy
  2. Multi-gateway state means "what's in production" is plural
  3. Hotfix-via-Designer is still a thing in many shops, and it bypasses Git entirely
- Foreshadow Lab 04: most of what we've discussed assumes a clean text-file diff. Ignition projects test that assumption — and this lab's `projects/lab-project/` is a first, deliberately gentle look at what those text files are.

---

# Pull requests

## The code PR (reference solution)

The main path has participants fix `lab.greeting.greet()` so a whitespace-only
name falls back to the default instead of returning `Hello,    !`. A clean
solution:

```python
DEFAULT_NAME = "world"


def greet(name=None):
    if name is not None:
        name = name.strip()
    if not name:
        name = DEFAULT_NAME
    return "Hello, %s!" % name
```

What to look for / push on:

- **The default still works.** `greet()` and `greet("")` must still return `Hello, world!`. A naive fix like `name = name.strip()` *without* the `is not None` guard throws `AttributeError` on `greet()` (None has no `.strip()`). If `validate.sh` is green but the no-arg case now breaks, that's an `issue:` — and a great teaching moment that "parses cleanly" is not "works."
- **Whitespace, not just empty.** The whole point is `"   "`. A change that only re-handles `""` (already handled) hasn't fixed anything.
- **One concern, small diff.** If the PR also renames things or reformats the module, it's no longer the small scoped PR the block is teaching — call it out.

> **On testing.** This lab's green/red signal is `scripts/validate.sh`, which checks
> that JSON is valid and Python parses — *not* behavior. That's deliberate: automated
> behavior tests (and a real "tests pass" gate in CI) arrive in Lab 03. So in the
> review, "is it tested?" becomes "did they verify it, and is the verification
> something I could repeat?" If a participant *wants* to prove the behavior, the
> honest manual check is the gateway's **Script Console** (`lab.greeting.greet("  ")`),
> but that's optional and not required to pass the exercise.

**Option B (view edit).** Some participants edit the Overview `view.json` instead.
A good one is a small, scoped text/label change with valid JSON. Watch for: a
copy-paste that breaks the JSON (validate.sh catches it), or a sprawling redesign
that's no longer a "small PR." Either is fair review fodder.

## What "good" looks like for the peer review

The You-do asks for a few genuinely helpful comments — at minimum a `praise:` and a `suggestion:`, plus an `issue:` when something's actually wrong. There's no quota: a thoughtful 3-comment review beats six box-ticking ones. The lab keeps participants to three labels on purpose; the fuller set (`question`, `nitpick`, `thought`, `chore`) lives in the optional `docs/pr-review-style.md` for anyone who wants it, and you should feel free to model those richer labels in your own review comments.

### A reference review skeleton

For most greeting-fix PRs, a strong review will include something like:

- **One `praise:`** — something genuinely good. A focused diff, or keeping the `None` guard. Praise is not throwaway — it tells the author what's working.
- **At least one `question:`** — there's almost always something genuinely unclear. "question: should a whitespace name fall back to `world`, or be rejected outright? What does the product want?" Questions surface assumptions the author didn't realize they had.
- **At least one `suggestion:`** — a specific change the author could make. Not a vague "this could be better" — a concrete alternative. "suggestion: collapse the two ifs — `name = (name or '').strip() or DEFAULT_NAME`."
- **Optionally `nitpick:`** — for small style things. PEP8, the docstring wording, `is None` vs `== None`. Always non-blocking.
- **`issue:` only when you mean it.** If the fix breaks the no-arg default (`AttributeError` on `greet()`), that's a real issue. Don't use `issue:` for taste differences.

> The **We-do** rehearses reviewing on a sample PR, and each author's *tagged peer* handles the **branching-agreement doc PR** — that's where doc-style comments (Context clarity, hotfix specificity, branch-naming concreteness) belong. The you-do's *solo* review (step 3) is on the **code PR**, where "does it break a call site?" actually has teeth.

### Tone — what to flag

Watch reviews for:

- **Sarcasm or condescension.** "Why didn't you just strip it?" reads as judgmental. Better: "question: any reason to keep the two separate ifs over a single `(name or '').strip()`?"
- **Vague criticism.** "This isn't very specific" is not actionable. Better: "suggestion: 'feature branches' is generic — would you commit to a specific pattern like `feature/<ticket-id>-<slug>`?"
- **Drive-by comments without context.** A single `?` or `huh?` is unhelpful. Push them to expand.
- **Blocker comments dressed as nitpicks.** If the comment would prevent merge, it shouldn't be labeled `nitpick:` — that's misleading the author.

If you spot any of these, model the rewrite in your own review comment on the same PR (or in the debrief). The label vocabulary is most of the lesson, but tone is where it actually lands.

## What "good" looks like for the author's response (you-do step 4)

Authors should:

- React to every comment with *something* (a reply, a reaction, or a fix-up commit).
- For `suggestion:` and `issue:` comments: explicit accept/decline with reasoning. Silent ignores are a smell.
- For `question:` comments: an answer, even if short.
- Re-request review after substantive changes.

Common author mistakes:

- **Marking conversations as resolved without responding.** Push back: even a `+1` reply is more communicative than silent resolution.
- **Accepting every suggestion without thinking.** Authors are not obligated to agree. A `decline: I think the two explicit ifs read clearer here` is a valid response.
- **Force-pushing over fix-ups.** A force-push during review nukes the reviewer's context. Prefer additive commits during review; squash on merge if you must.

## Merge style (you-do step 4)

Participants merge **both** PRs — their code PR and their branching-agreement PR — using the style their agreement specified. GitHub's merge dropdown gives three options:

| Option | Effect | Use when |
|---|---|---|
| **Create a merge commit** | `--no-ff`; preserves branch shape | Team agreement specifies `--no-ff` |
| **Squash and merge** | One commit on `main` representing the entire PR | Small PRs, team prefers linear history |
| **Rebase and merge** | Replays commits onto `main` linearly; no merge commit | Trunk-based, very clean linear-history teams |

Participants should pick the one their team agreement specified — that's the whole point of writing it.

If GitHub doesn't show all three: the repo has restricted them in Settings → Branches → Merge button options. Worth surfacing as a procedural point.

## Stretch — branch protection

Acceptable settings vary by team. Look for at least:

- "Require pull request reviews before merging" — usually 1 approval
- "Dismiss stale pull request approvals when new commits are pushed" — fights against approve-and-then-force-push
- "Do not allow bypassing the above settings" — applies the rules even to admins

We deliberately don't require "passing CI" here because Lab 02 has no CI — `validate.sh` is a local convenience, not an enforced gate. Lab 03 introduces CI; when participants set up branch protection then, they should layer "require status checks" on top.

## Pull-request debrief crib

- *"One thing you'll steal?"* — Push for specifics. "I liked their PR description" is shallow. "I liked that they linked to the ticket and quoted the customer's report" is real.
- *"One habit to drop?"* — The honest answers are often: "writing PRs too big," "not verifying my own change before opening," "leaving lots of nitpicks instead of one suggestion."
- *"When does request-changes do more harm than good?"* — Three common cases:
  1. When the only issues are nitpicks (use approve + nitpick comments instead).
  2. When the reviewer is the second of two and the first already approved (use comment-only).
  3. When the timing matters and the author is offline (consider a synchronous chat instead of a blocking review).
- *"Smallest meaningful Ignition PR?"* — They just shipped one: a single script function or a single view property. The point is to seed the idea that PR-sized changes are *possible* for Ignition, even though many shops currently PR whole gateway backups.

End the lab with one explicit foreshadowing line: **"Tomorrow we add the CI safety net — turning `validate.sh` into a gate no one can merge past — that makes all of this scale."**
