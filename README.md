# Lab 02 — Branching and Pull Requests

Day 1, Blocks C and D of the [CI/CD for Ignition Masterclass](https://github.com/mustry-academy/cicd-masterclass).

> Compare branching strategies side by side, and learn to write a pull request a reviewer actually enjoys reading.

This is the second lab in the course. Like Lab 01, it deliberately stays out of Ignition territory — the demo stack is a tiny Flask + Redis web app, used as the subject of our branching and PR exercises. Ignition-specific deployments arrive in Lab 04.

## Prerequisites

- Completed [Lab 01](https://github.com/mustry-academy/cicd-lab-01-git-fundamentals)
- Pass [`cicd-preflight`](https://github.com/mustry-academy/cicd-preflight)

## Working model: fork and PR

Blocks C and D have you open real PRs, review your peers', and merge your own when
approved — so everyone needs merge rights on the repo they're PRing into. The clean
way to get that without handing a whole cohort write access to one repo: **work in
your own fork, and open PRs inside it.**

1. **Fork + clone** (sets `origin` to your fork, `upstream` to the lab repo):
   ```bash
   gh repo fork mustry-academy/cicd-lab-02-branching-and-prs --clone
   cd cicd-lab-02-branching-and-prs
   ```
2. Branch and push to **your** fork (`git push -u origin <branch>`).
3. Open PRs with **base = your fork's `main`**, compare = your branch.
4. **Share each PR link in the cohort chat** so peers can find and review it.
5. You own your fork, so you can merge your own PRs once they're approved.

## Quick start

```bash
cp .env.example .env
docker compose up -d
# Then:
curl http://localhost:5050/health         # → {"status":"ok"}
curl "http://localhost:5050/greet?name=Ada"
```

To run the tests locally without Docker:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r sample-app/requirements-dev.txt
pytest sample-app/tests -q
```

## Lab structure

| Block | Topic | Exercise |
|---|---|---|
| C | Branching strategies compared: Git Flow vs GitHub Flow vs trunk-based | [`exercises/block-c.md`](./exercises/block-c.md) |
| D | Pull requests done right: scope, review, and merge hygiene | [`exercises/block-d.md`](./exercises/block-d.md) |

## Checkpoints

```bash
git fetch --tags
git checkout block-c-start
git checkout block-c-end
git checkout block-d-start
git checkout block-d-end
```

## Repo layout

```
cicd-lab-02-branching-and-prs/
├── README.md
├── docker-compose.yml            ← Flask + redis dev stack
├── .env.example                  ← copy to .env before running
├── .github/
│   └── pull_request_template.md
├── exercises/
│   ├── block-c.md
│   └── block-d.md
├── docs/                         ← reference reading
│   ├── branching-strategies.md
│   └── pr-review-style.md
├── instructor-notes/             ← answer keys (read after solo work)
│   ├── block-c-key.md
│   └── block-d-key.md
└── sample-app/                   ← Flask + redis web app, subject of the exercises
    ├── app.py
    ├── Dockerfile
    ├── .dockerignore
    ├── requirements.txt           ← runtime deps (flask, redis)
    ├── requirements-dev.txt       ← + pytest, fakeredis for local testing
    ├── tests/
    │   └── test_app.py
    └── README.md
```

## The Compose stack

A two-service development stack: a tiny Flask app and a Redis sidecar. The app exposes `/health` and `/greet?name=<name>`; `/greet` increments a per-name counter in Redis so the redis service has something to do.

```yaml
services:
  app:
    build: ./sample-app
    ports: ["5050:5050"]
    environment:
      REDIS_URL: "redis://redis:6379/0"
    depends_on:
      redis: { condition: service_healthy }

  redis:
    image: redis:7-alpine   # no published port; reached over the compose network
```

> **No CI in this lab.** We deliberately ship no `.github/workflows/`. CI is introduced from scratch in Lab 03 — having pre-built CI here would muddy that narrative.

## License

Apache 2.0 — see [`LICENSE`](./LICENSE).
