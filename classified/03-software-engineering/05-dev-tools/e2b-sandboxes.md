---
name: e2b-sandboxes
description: >
  E2B open-source cloud sandboxes for executing AI-generated code securely.
  USE FOR: run code in sandbox, e2b, code interpreter, execute AI code,
  secure code execution, isolated environment, AI coding agent execution,
  run untrusted code, cloud sandbox, code execution API, python sandbox cloud,
  AI agent code runner, safe code execution, jupyter sandbox.
kind: tool
category: dev/tools
repo: https://github.com/e2b-dev/E2B
tags: [sandbox, code-execution, ai, cloud, security]
status: active
---

# E2B Code Interpreter Sandboxes

> Secure isolated cloud VMs for executing AI-generated code. Open-source.

## Installation
```bash
pip install e2b-code-interpreter
npm i @e2b/code-interpreter
export E2B_API_KEY=your_key_here   # get at https://e2b.dev/dashboard
```

## Python Usage
```python
from e2b_code_interpreter import Sandbox

# Basic execution
with Sandbox() as sandbox:
    result = sandbox.run_code("x = 1 + 1; print(x)")
    print(result.logs.stdout)   # ["2"]

# Stateful multi-step session
with Sandbox() as sandbox:
    sandbox.run_code("data = [1, 2, 3]")
    r = sandbox.run_code("print(sum(data))")
    print(r.logs.stdout)        # ["6"]
```

## TypeScript Usage
```typescript
import { Sandbox } from "@e2b/code-interpreter"

const sandbox = await Sandbox.create()
const result = await sandbox.runCode("print(1 + 1)")
console.log(result.logs.stdout)
await sandbox.kill()
```

## Use With Claude AI Agent
```python
from anthropic import Anthropic
from e2b_code_interpreter import Sandbox

client = Anthropic()
sandbox = Sandbox()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Write Python to compute fibonacci(10)"}]
)
code = response.content[0].text
result = sandbox.run_code(code)
print(result.logs.stdout)
sandbox.kill()
```

## Key Features
| Feature | Detail |
|---------|--------|
| Isolation | Each sandbox = fresh cloud VM |
| Stateful | Variables persist within session |
| Languages | Python, JavaScript/TypeScript |
| Outputs | stdout, stderr, rich results (plots, tables) |
| Self-hostable | GCP (prod-ready), AWS (in progress), Azure (planned) |

## Self-Hosting
```bash
# GCP (production-ready)
terraform apply -var-file=gcp.tfvars
```

---
