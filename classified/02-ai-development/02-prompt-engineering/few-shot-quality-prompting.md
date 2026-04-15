---
name: few-shot-quality-prompting
description: Master guide for crafting prompts that make AI models produce professional-quality code and UI consistently. Trigger whenever the user asks about prompt engineering, improving AI output quality, building system prompts, few-shot examples, making AI write better code, prompt optimization, or says "how to prompt", "better results", "improve output", "stop getting slop". Covers system prompt architecture, few-shot patterns, negative examples, chain-of-thought, output formatting, and evaluation-driven iteration.
kind: reference
category: ai/prompting
status: active
tags: [few, prompting, quality, shot]
related_skills: [writing-hookify-rules]
---

# Few-Shot Quality Prompting Skill — Engineering AI Output Excellence

## Identity
You are a prompt engineering specialist who knows that the difference between
mediocre and exceptional AI output is 90% prompt design and 10% model capability.
You design prompts as carefully as you design code — with structure, testing, and iteration.

---

## CORE INSIGHT

> **The model is a mirror. It reflects the quality level you demonstrate in your prompt.**
>
> Show it amateur code → get amateur code.
> Show it senior-engineer code → get senior-engineer code.
> Show it nothing → get generic defaults.

---

## SYSTEM PROMPT ARCHITECTURE

### The 7-Layer System Prompt

```
┌─────────────────────────────────────┐
│ LAYER 1: IDENTITY                   │  Who is the AI? (role, expertise level)
├─────────────────────────────────────┤
│ LAYER 2: CONTEXT                    │  What's the project? (stack, constraints)
├─────────────────────────────────────┤
│ LAYER 3: SKILLS                     │  Domain knowledge (loaded dynamically)
├─────────────────────────────────────┤
│ LAYER 4: GOLDEN EXAMPLES            │  2-3 examples of perfect output
├─────────────────────────────────────┤
│ LAYER 5: ANTI-PATTERNS              │  Explicit "NEVER do this" list
├─────────────────────────────────────┤
│ LAYER 6: OUTPUT FORMAT              │  Exact structure of response
├─────────────────────────────────────┤
│ LAYER 7: QUALITY GATES              │  Self-check before responding
└─────────────────────────────────────┘
```

### Layer-by-Layer Construction

#### Layer 1: Identity
```
WEAK: "You are a helpful coding assistant."
STRONG: "You are a senior frontend engineer at a design-focused studio
        with 10 years of experience shipping production React applications.
        You have strong opinions about clean architecture and refuse to
        write code you wouldn't approve in a code review."
```

The identity sets the quality floor. "Senior engineer at Stripe" produces better code than "helpful assistant" because the model activates different knowledge distributions.

#### Layer 2: Context
```
WEAK: "Help me with my React app."
STRONG: "Project: SaaS dashboard for analytics.
        Stack: React 18 + TypeScript + Tailwind + shadcn/ui
        Architecture: Feature-based modules, custom hooks for state
        Target: Production deployment, needs responsive + accessible
        Existing code style: [paste 20-line example from codebase]"
```

#### Layer 3: Skills (Dynamic)
```
Load the relevant skill markdown based on task type.
Keep total skill injection under 5K tokens.
If multiple skills needed, extract only the relevant sections.
```

#### Layer 4: Golden Examples (THE MOST IMPORTANT LAYER)
```
PATTERN: Show 2-3 complete input→output examples at the quality level you expect.

Example for a React component task:

---BEGIN EXAMPLE---
USER: Create a stat card showing monthly revenue with trend indicator.

ASSISTANT:
```tsx
import { TrendingUp, TrendingDown } from 'lucide-react';

interface StatCardProps {
  label: string;
  value: string;
  trend: number;
  period?: string;
}

export default function StatCard({
  label,
  value,
  trend,
  period = 'vs last month'
}: StatCardProps) {
  const isPositive = trend >= 0;

  return (
    <div className="group relative rounded-xl border border-zinc-200
                    bg-white p-6 transition-all duration-200
                    hover:shadow-md hover:border-zinc-300">
      <p className="text-sm font-medium text-zinc-500 tracking-wide">
        {label}
      </p>
      <p className="mt-2 text-3xl font-semibold text-zinc-900 tabular-nums">
        {value}
      </p>
      <div className="mt-3 flex items-center gap-1.5">
        {isPositive ? (
          <TrendingUp className="h-4 w-4 text-emerald-500" />
        ) : (
          <TrendingDown className="h-4 w-4 text-red-500" />
        )}
        <span className={`text-sm font-medium ${
          isPositive ? 'text-emerald-600' : 'text-red-600'
        }`}>
          {isPositive ? '+' : ''}{trend}%
        </span>
        <span className="text-sm text-zinc-400">{period}</span>
      </div>
    </div>
  );
}
` ` `
---END EXAMPLE---

WHY THIS WORKS:
  - Shows exact import style
  - Shows TypeScript interface pattern
  - Shows Tailwind class organization (responsive, spacing, color)
  - Shows hover state handling
  - Shows proper default props
  - Sets the quality bar: real data, polished transitions, proper types
```

#### Layer 5: Anti-Patterns
```
## FORBIDDEN — Never Do These

- Do NOT use `any` type in TypeScript
- Do NOT use inline styles when Tailwind classes exist
- Do NOT hardcode colors (use design tokens / Tailwind palette)
- Do NOT use placeholder text like "Lorem ipsum" or "Item 1"
- Do NOT omit hover/focus/active states on interactive elements
- Do NOT skip error handling
- Do NOT use console.log in production code
- Do NOT create functions longer than 25 lines
- Do NOT use generic variable names (data, item, thing, obj)
- Do NOT import from relative paths deeper than 2 levels (../../..)
```

#### Layer 6: Output Format
```
OPTION A — Code Only:
  "Respond with ONLY the complete code file. No explanations,
   no markdown wrapping, no commentary before or after."

OPTION B — Structured Response:
  "Respond in this exact format:
   ## Approach (2-3 sentences)
   ## Code
   ```language
   [complete file]
   ```
   ## Key Decisions (bullet list, max 4 items)"

OPTION C — JSON Structured:
  "Respond with ONLY a JSON object:
   {
     'files': [{'path': '...', 'content': '...'}],
     'commands': ['npm install ...'],
     'notes': '...'
   }"
```

#### Layer 7: Quality Gates
```
## Self-Check Before Responding

Before outputting your response, verify:
□ All imports are present and correct
□ No TypeScript `any` types
□ All interactive elements have hover + focus states
□ Error states handled (loading, error, empty)
□ Responsive on mobile (min 375px)
□ Color contrast meets WCAG AA (4.5:1)
□ Code runs as-is without modification
□ No TODO or placeholder comments

If any check fails, fix it before responding.
```

---

## FEW-SHOT PATTERNS

### Pattern 1: Input-Output Pairs (Most Effective)
```
Show 2-3 complete examples of:
  Input: [user request]
  Output: [perfect response]

The model pattern-matches against your examples.
More examples = more consistent output.
2 examples is the sweet spot (enough to show pattern, not too much context).
```

### Pattern 2: Good vs Bad Comparison
```
GOOD EXAMPLE:
```tsx
<button
  className="inline-flex items-center gap-2 rounded-lg bg-indigo-600 px-4 py-2.5
             text-sm font-medium text-white transition-colors
             hover:bg-indigo-700 focus:outline-none focus:ring-2
             focus:ring-indigo-500 focus:ring-offset-2
             disabled:opacity-50 disabled:cursor-not-allowed"
  disabled={isLoading}
>
  {isLoading ? <Spinner className="h-4 w-4 animate-spin" /> : <Plus className="h-4 w-4" />}
  {isLoading ? 'Creating...' : 'Create Project'}
</button>
` ` `

BAD EXAMPLE (Do NOT produce this):
```tsx
<button style={{background: 'blue', color: 'white'}} onClick={handleClick}>
  Submit
</button>
` ` `

The bad example explicitly shows what to avoid. Models learn from negative examples.
```

### Pattern 3: Progressive Complexity
```
Example 1: Simple (establishes baseline quality)
Example 2: Medium (shows how to handle edge cases)
Example 3: Complex (shows the ceiling)

Each example builds on the previous, showing how quality scales with complexity.
```

### Pattern 4: Domain-Specific Templates
```
For each type of output (component, API endpoint, test file, etc.),
provide a template that shows the expected structure:

REACT COMPONENT TEMPLATE:
  1. Imports (external, then internal, then types)
  2. Interface/Types
  3. Sub-components (if small enough to colocate)
  4. Main component with default export
  5. Hooks at top, handlers in middle, render at bottom

This template acts as a structural few-shot — even without full examples.
```

---

## PROMPT OPTIMIZATION TECHNIQUES

### Technique 1: Prompt Refinement Loop
```
Step 1: Write initial prompt
Step 2: Generate 5 outputs
Step 3: Score each (1-10) on: correctness, style, completeness
Step 4: Identify failure patterns
Step 5: Add specific rules/examples to fix failures
Step 6: Repeat until average score > 8

TRACK:
  Prompt version | Avg score | Worst failure | Fix applied
  v1            | 5.2       | Missing types  | Added TypeScript rule
  v2            | 6.8       | No hover states| Added CSS interaction example
  v3            | 8.1       | Inconsistent   | Added 2nd few-shot example
  v4            | 8.7       | Edge cases     | Added anti-pattern list
```

### Technique 2: Temperature & Sampling Control
```
CODE GENERATION:     temperature=0.0 to 0.3 (deterministic, correct)
CREATIVE UI DESIGN:  temperature=0.5 to 0.7 (some variation, still coherent)
BRAINSTORMING:       temperature=0.8 to 1.0 (diverse ideas)
NAMING/COPY:         temperature=0.4 to 0.6

For agents: Use temperature=0 for tool calls, 0.3 for code, 0.5 for explanations
```

### Technique 3: Structured Output Enforcement
```python
# Force JSON output with schema validation
system = """Respond ONLY with valid JSON matching this schema. 
No markdown, no backticks, no explanation.

Schema:
{
  "component_name": "string",
  "imports": ["string"],
  "props": [{"name": "string", "type": "string", "required": "boolean"}],
  "code": "string"
}"""

# Parse response
import json
response_text = response.content[0].text
# Strip any accidental markdown fencing
clean = response_text.strip().removeprefix("```json").removesuffix("```").strip()
data = json.loads(clean)
```

### Technique 4: Chain-of-Thought for Complex Tasks
```
"Before writing code, think through:
1. What are the inputs and outputs?
2. What edge cases exist?
3. What's the simplest correct implementation?
4. What could go wrong?

Write your thinking in a <planning> block, then provide the code."

This produces measurably better code for complex tasks (20%+ improvement on benchmarks).
```

### Technique 5: Role-Specific Personas
```
DIFFERENT ROLES ACTIVATE DIFFERENT KNOWLEDGE:

"You are a security engineer" → Finds injection vulnerabilities, checks auth
"You are a performance engineer" → Spots N+1 queries, unnecessary re-renders
"You are a UX designer who codes" → Better component APIs, accessibility, states
"You are a senior at [specific company]" → Mimics that company's coding patterns

USE: Rotate personas for different review passes on the same code.
```

---

## EVALUATION FRAMEWORK

### Scoring Rubric for Code Output
```
CORRECTNESS (0-3):
  0: Doesn't run
  1: Runs but has bugs
  2: Works for happy path
  3: Handles edge cases correctly

COMPLETENESS (0-3):
  0: Missing major features
  1: Core feature works, missing states (loading/error/empty)
  2: All states handled, missing polish
  3: Complete with all states, transitions, responsive

STYLE (0-2):
  0: Inconsistent, messy
  1: Consistent but generic
  2: Clean, idiomatic, follows design system

UI QUALITY (0-2):
  0: Unstyled or broken layout
  1: Functional but generic
  2: Polished, professional, memorable

TOTAL: /10 — Target ≥ 8 for production use
```

### A/B Testing Prompts
```python
def evaluate_prompt(prompt_version: str, test_cases: list[str], n_trials: int = 5) -> dict:
    """Run test cases against a prompt and score results."""
    scores = []
    for test in test_cases:
        for _ in range(n_trials):
            output = call_llm(system=prompt_version, user=test)
            score = score_output(output)  # Your scoring function
            scores.append(score)

    return {
        "mean": sum(scores) / len(scores),
        "min": min(scores),
        "max": max(scores),
        "std": (sum((s - sum(scores)/len(scores))**2 for s in scores) / len(scores)) ** 0.5,
        "pass_rate": sum(1 for s in scores if s >= 8) / len(scores)
    }
```

---

## COMPLETE SYSTEM PROMPT TEMPLATE

```
You are a [ROLE] with expertise in [DOMAINS].

## Project Context
- Stack: [TECHNOLOGIES]
- Architecture: [PATTERNS]
- Style: [CONVENTIONS]

## Active Skills
[DYNAMICALLY LOADED SKILL CONTENT]

## Golden Examples

### Example 1
USER: [simple request]
RESPONSE:
[complete, high-quality output]

### Example 2
USER: [complex request]
RESPONSE:
[complete, high-quality output showing how to handle complexity]

## Anti-Patterns — NEVER Do These
- [specific bad pattern 1]
- [specific bad pattern 2]
- [specific bad pattern 3]

## Output Format
[exact structure expected]

## Quality Checklist (Verify Before Responding)
□ [check 1]
□ [check 2]
□ [check 3]
□ [check 4]

If any check fails, fix it before outputting your response.
```

---

## KEY METRICS TO TRACK

```
1. FIRST-TRY SUCCESS RATE: % of outputs that need zero fixes
   Target: > 70% for well-prompted agents

2. AVERAGE ITERATIONS TO SUCCESS: How many generate→fix cycles
   Target: < 3 for most tasks

3. QUALITY SCORE: Average score on your rubric
   Target: > 8/10 consistently

4. CONTEXT EFFICIENCY: Useful output tokens / total tokens consumed
   Target: > 30% (rest is reasoning and tool calls)

5. COST PER TASK: Total API cost for a completed task
   Track this to optimize prompt length and model selection
```
