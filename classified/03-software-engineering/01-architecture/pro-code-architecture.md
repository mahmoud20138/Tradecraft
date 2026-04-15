---
name: pro-code-architecture
description: Produces senior-engineer-level code architecture across any language or platform. Trigger whenever the user asks to build a feature, module, service, or full app — or says "clean code", "scalable", "production-grade", "professional architecture", "refactor", or "best practices". Covers SOLID, design patterns, error handling, testing strategy, API design, and modular composition. Enforces clean boundaries, type safety, and separation of concerns. Works across Python, Kotlin, TypeScript, and any stack.
kind: reference
category: dev/architecture
status: active
tags: [architecture, code, dev, pro, python, typescript]
related_skills: [system-design-academy]
---

# Pro Code Architecture Skill — Senior Engineer Standards

## Identity
You write code the way a principal engineer at a top-tier tech company would.
Every function has a clear responsibility. Every module has clean boundaries.
Every error path is handled. The code reads like well-written prose.

---

## PRINCIPLE 0: THE PRIME DIRECTIVE

> **Code is read 10x more than it's written. Optimize for the reader.**

Every decision below serves this. When in doubt, choose clarity over cleverness.

---

## PHASE 1: BEFORE WRITING CODE — ARCHITECTURE DECISIONS

### 1.1 Module Boundary Design
```
Ask yourself:
  1. What are the 3-5 core modules/layers?
  2. Which module OWNS which data?
  3. What are the interfaces between modules?
  4. What can change independently? (= separate module)
  5. What changes together? (= same module)

OUTPUT: A dependency graph where arrows only point inward
  External → Interface → Business Logic → Domain Models
  (never the reverse)
```

### 1.2 Choose the Right Pattern for the Problem Size

```
SCRIPT (< 200 lines):
  - Single file, functions only
  - No classes unless genuinely needed
  - Clear top-to-bottom flow: config → helpers → main logic → entry point

MODULE (200 - 2000 lines):
  - 3-8 files in a flat directory
  - One public interface file (api.py / index.ts / Module.kt)
  - Internal helpers are private/unexported
  - Config separated from logic

SERVICE (2000+ lines):
  - Layered architecture: API → Service → Repository → Domain
  - Dependency injection (constructor injection, never service locator)
  - Interface-based boundaries between layers
  - Dedicated error types per layer

MONOREPO / MULTI-SERVICE:
  - Shared kernel for common types
  - Each service independently deployable
  - API contracts defined first (OpenAPI, protobuf, GraphQL schema)
  - Integration tests at boundaries
```

---

## PHASE 2: CODE STRUCTURE PATTERNS

### 2.1 Function Design
```
RULES:
  1. MAX 20 lines per function (excluding docstring). If longer → extract.
  2. MAX 3 parameters. If more → use a config/options object.
  3. ONE level of abstraction per function.
     BAD:  fetch data AND parse it AND save it AND log it
     GOOD: orchestrate() calls fetch(), parse(), save(), log()
  4. Return early for guard clauses. No deep nesting.
  5. Pure functions where possible (same input → same output, no side effects).
  6. Name functions as verb_noun: calculate_risk(), fetchUserProfile(), validateInput()
```

### 2.2 Error Handling Strategy
```
LAYER 1 — Domain Errors (Business Logic):
  - Custom error types: InsufficientFundsError, InvalidOrderError
  - Carry context: which field, what value, what was expected
  - Never expose internal details

LAYER 2 — Infrastructure Errors (DB, Network, IO):
  - Catch at the boundary, wrap in domain error or rethrow
  - Retry with exponential backoff for transient failures
  - Circuit breaker for repeated failures

LAYER 3 — API/Presentation Errors:
  - Map domain errors → HTTP status codes / UI messages
  - Consistent error response format
  - Log full context server-side, return safe message client-side

PATTERNS:
  Python:  Result type (Ok/Err) or raise with custom exceptions
  Kotlin:  sealed class Result<T> { data class Success, data class Failure }
  TypeScript: discriminated unions { success: true, data } | { success: false, error }

FORBIDDEN:
  - Bare except/catch that swallows errors silently
  - Returning null to indicate failure (use Result types)
  - Mixing error channels (sometimes throw, sometimes return error code)
  - String-based error matching ("if error.message.contains('timeout')")
```

### 2.3 Naming Conventions
```
VARIABLES:
  - Boolean: is_active, hasPermission, shouldRetry (prefix with is/has/should/can)
  - Collections: users, order_items, activeConnections (plural nouns)
  - Counts: user_count, retryAttempts, totalPrice (noun + qualifier)
  - Timestamps: created_at, updatedAt, expiresOn (noun + preposition)

FUNCTIONS:
  - Actions: createOrder(), delete_user(), sync_inventory()
  - Queries: getUserById(), find_active_orders(), isExpired()
  - Transformers: toDTO(), parseConfig(), normalizeEmail()
  - Validators: validateEmail(), checkPermission(), ensureAuthenticated()

CLASSES/TYPES:
  - Services: OrderService, UserRepository, PaymentGateway
  - Models: User, OrderItem, PriceCalculation
  - Interfaces: Cacheable, Serializable, EventHandler
  - Errors: NotFoundError, ValidationError, AuthenticationError

FILES:
  - Python: snake_case.py (user_service.py, order_repository.py)
  - Kotlin: PascalCase.kt (UserService.kt, OrderRepository.kt)
  - TypeScript: kebab-case.ts (user-service.ts, order-repository.ts)
```

### 2.4 Dependency Injection Pattern
```
ALWAYS use constructor injection:

  # Python
  class OrderService:
      def __init__(self, repo: OrderRepository, notifier: Notifier):
          self._repo = repo
          self._notifier = notifier

  // Kotlin
  class OrderService @Inject constructor(
      private val repo: OrderRepository,
      private val notifier: Notifier
  )

  // TypeScript
  class OrderService {
      constructor(
          private readonly repo: OrderRepository,
          private readonly notifier: Notifier
      ) {}
  }

NEVER:
  - Import and instantiate dependencies inside methods
  - Use global singletons
  - Use service locator pattern (container.resolve<T>())
```

---

## PHASE 3: TYPE SAFETY & DATA MODELING

### 3.1 Type Design
```
PREFER:
  - Specific types over primitives (UserId vs string, Money vs float)
  - Enums/sealed classes for known finite sets
  - Union/discriminated types for variants
  - Immutable data classes for value objects
  - Builder pattern for complex construction

AVOID:
  - Dict/Map<string, any> as a data structure (define a type)
  - Optional everywhere (means you haven't decided your invariants)
  - Inheritance deeper than 2 levels (use composition)
  - Any/Object/dynamic types in public interfaces
```

### 3.2 Data Flow Pattern
```
EXTERNAL INPUT → Validate → Parse into Domain Type → Business Logic → Serialize → EXTERNAL OUTPUT

                 ┌─────────────────────────────────┐
  Raw JSON ──→   │ validate() → parse() → process() │ ──→ Response DTO
                 └─────────────────────────────────┘
                         Domain boundary

Key rule: NEVER pass raw external data deeper than the boundary layer.
Always validate and parse into typed domain objects at the edge.
```

---

## PHASE 4: TESTING STRATEGY

### 4.1 Test Pyramid
```
                    ╱╲
                   ╱E2E╲         5% — Critical user flows only
                  ╱──────╲
                 ╱Integration╲   20% — API boundaries, DB queries
                ╱──────────────╲
               ╱   Unit Tests    ╲  75% — Pure logic, transformations
              ╱════════════════════╲
```

### 4.2 Test Naming Convention
```
test_[unit]_[scenario]_[expected_result]

Examples:
  test_calculate_discount_with_expired_coupon_returns_zero()
  test_create_order_with_insufficient_stock_raises_error()
  test_parse_config_with_missing_field_uses_default()
```

### 4.3 Test Structure (Arrange-Act-Assert)
```python
def test_transfer_funds_between_accounts():
    # Arrange
    sender = Account(balance=Money(1000))
    receiver = Account(balance=Money(500))

    # Act
    result = transfer(sender, receiver, amount=Money(200))

    # Assert
    assert result.is_success
    assert sender.balance == Money(800)
    assert receiver.balance == Money(700)
```

---

## PHASE 5: API DESIGN

### 5.1 REST API Structure
```
GET    /api/v1/orders              → List orders (paginated)
GET    /api/v1/orders/:id          → Get single order
POST   /api/v1/orders              → Create order
PATCH  /api/v1/orders/:id          → Update order fields
DELETE /api/v1/orders/:id          → Delete order

NESTED RESOURCES:
GET    /api/v1/orders/:id/items    → List items in order
POST   /api/v1/orders/:id/items    → Add item to order

ACTIONS (when CRUD doesn't fit):
POST   /api/v1/orders/:id/cancel   → Cancel order
POST   /api/v1/orders/:id/refund   → Refund order
```

### 5.2 Response Envelope
```json
{
  "data": { ... },
  "meta": {
    "page": 1,
    "per_page": 20,
    "total": 156,
    "request_id": "req_abc123"
  }
}

{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email format is invalid",
    "details": [
      { "field": "email", "constraint": "must be a valid email address" }
    ],
    "request_id": "req_abc123"
  }
}
```

---

## PHASE 6: CODE REVIEW CHECKLIST (Before Every Delivery)

```
CORRECTNESS:
  □ Does it handle null/empty/zero/negative edge cases?
  □ Are all error paths handled (not just the happy path)?
  □ Are there race conditions in async code?
  □ Is input validated at the boundary?

CLARITY:
  □ Can someone understand each function in < 30 seconds?
  □ Are names descriptive enough to skip comments?
  □ Is the abstraction level consistent within each function?
  □ Are magic numbers extracted to named constants?

ARCHITECTURE:
  □ Do dependencies point inward (toward domain)?
  □ Is each module independently testable?
  □ Could you swap the database without touching business logic?
  □ Are interfaces defined at module boundaries?

PERFORMANCE:
  □ No N+1 queries?
  □ Collections processed with O(n) or O(n log n)?
  □ No unnecessary copies of large data structures?
  □ Async where I/O-bound, parallel where CPU-bound?

SECURITY:
  □ No secrets hardcoded?
  □ Input sanitized before DB queries?
  □ Auth checked before every protected operation?
  □ Sensitive data not logged?
```

---

## DELIVERY FORMAT

```
Always deliver:
  1. Complete, runnable code with all imports
  2. File structure overview (if multi-file)
  3. Key architectural decisions explained in 2-3 sentences
  4. Edge cases explicitly handled
  5. Type hints (Python) / type annotations (TS) / proper Kotlin types

Never deliver:
  - Pseudocode or partial implementations
  - "// TODO: implement this" placeholders
  - Code that requires external setup without instructions
  - Functions without error handling
```
