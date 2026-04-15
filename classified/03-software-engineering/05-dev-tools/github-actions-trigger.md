---
name: github-actions-trigger
description: Trigger GitHub Actions workflows from Claude Code. Auto-run tests, deploy, or validate when skills like run-pre-commit-checks complete.
kind: reference
category: dev/tools
status: active
tags: [actions, claude-code, dev, github, tools, trigger]
related_skills: [run-pre-commit-checks]
---

# GitHub Actions Trigger — CI/CD Bridge

You are a **GitHub Actions integration bridge**. You trigger workflows, monitor runs, and report results back to Claude Code.

## Setup

```
GH_TOKEN = "ghp_YOUR_TOKEN"
GH_OWNER = "your-username"
GH_REPO  = "your-repo"
```
Save: `/context-memory save gh_token=<token> gh_repo=owner/repo`

## Trigger a Workflow

```
/github-actions-trigger run workflow_file=ci.yml
/github-actions-trigger run workflow_file=deploy.yml branch=main
/github-actions-trigger run workflow_file=test.yml inputs='{"env":"staging"}'
```

## Monitor Run Status

```
/github-actions-trigger status run_id=12345678
/github-actions-trigger latest workflow=ci.yml
/github-actions-trigger logs run_id=12345678
```

## Pre-built Integration Flows

### After /run-pre-commit-checks passes:
```
/github-actions-trigger run workflow=ci.yml
→ Monitor status every 30s
→ Report pass/fail back
```

### After /code-review approves:
```
/github-actions-trigger run workflow=deploy-staging.yml
→ Get deployment URL
→ Send to /discord-webhook
```

### After /run-e2e-tests completes:
```
/github-actions-trigger run workflow=deploy-prod.yml
→ Requires all tests passed
→ Notify via /telegram-bot
```

## API Functions

```python
import requests

class GitHubActions:
    BASE = "https://api.github.com"

    def __init__(self, token, owner, repo):
        self.headers = {"Authorization": f"token {token}",
                        "Accept": "application/vnd.github+json"}
        self.url = f"{self.BASE}/repos/{owner}/{repo}"

    def trigger(self, workflow_id: str, ref: str = "main", inputs: dict = {}):
        endpoint = f"{self.url}/actions/workflows/{workflow_id}/dispatches"
        return requests.post(endpoint, headers=self.headers,
                             json={"ref": ref, "inputs": inputs})

    def get_runs(self, workflow_id: str):
        endpoint = f"{self.url}/actions/workflows/{workflow_id}/runs"
        return requests.get(endpoint, headers=self.headers).json()

    def get_logs(self, run_id: int):
        endpoint = f"{self.url}/actions/runs/{run_id}/logs"
        return requests.get(endpoint, headers=self.headers)
```

## Status Output Format

```
GitHub Actions Run #12345678
─────────────────────────────
Workflow:  ci.yml
Branch:    main
Status:    ✅ completed → success
Duration:  2m 34s
Triggered: 2026-03-18 09:15 UTC

Jobs:
  ✅ lint        (12s)
  ✅ test        (1m 45s)
  ✅ build       (37s)
```
