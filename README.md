# Lab 02 — Branching and Pull Requests

Day 1, Blocks C and D of the [CI/CD for Ignition Masterclass](https://github.com/mustry-academy/cicd-masterclass).

> Compare branching strategies side by side, and learn to write a pull request a reviewer actually enjoys reading.

This is the second lab in the course. Like Lab 01, it deliberately stays out of Ignition territory — the demo stack is a tiny Flask + Redis web app, used as the subject of our branching and PR exercises. Ignition-specific deployments arrive in Lab 04.

## Prerequisites

- Completed [Lab 01](https://github.com/mustry-academy/cicd-lab-01-git-fundamentals)
- Pass [`cicd-preflight`](https://github.com/mustry-academy/cicd-preflight)

## Quick start

```bash
gh repo clone mustry-academy/cicd-lab-02-branching-and-prs
cd cicd-lab-02-branching-and-prs
cp .env.example .env
docker compose up -d
# Then:
curl http://localhost:5050/health         # → {"status":"ok"}
curl "http://localhost:5050/greet?name=Ada"
```

To run the tests locally without Docker:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r sample-app/requirements.txt
pytest sample-app/tests -q
```

The lab also runs in [GitHub Codespaces](https://github.com/features/codespaces) — see [`.devcontainer/devcontainer.json`](./.devcontainer/devcontainer.json).

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
├── PLAN.md                       ← design doc for this lab
├── docker-compose.yml            ← Flask + redis dev stack
├── .env.example                  ← copy to .env before running
├── .devcontainer/                ← Codespaces fallback config
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
    ├── requirements.txt
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
    image: redis:7-alpine
    ports: ["6379:6379"]
```

> **No CI in this lab.** We deliberately ship no `.github/workflows/`. CI is introduced from scratch in Lab 03 — having pre-built CI here would muddy that narrative.

## Licence

Apache 2.0 — see [`LICENSE`](./LICENSE).
