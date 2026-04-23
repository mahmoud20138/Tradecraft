---
name: system-design-academy
description: >
  Real-world system design case studies from 40+ major tech companies + 114 concepts.
  USE FOR: system design, design Twitter, design YouTube, design Uber, design Netflix,
  design WhatsApp, design Slack, design Instagram, URL shortener, payment system,
  distributed systems, scalability, microservices, caching patterns, consistent hashing,
  rate limiting, system design interview, architecture patterns, database scaling.
kind: reference
category: dev/architecture
repo: https://github.com/systemdesign42/system-design-academy
tags: [system-design, architecture, scalability, distributed-systems, interviews]
status: active
related_skills: [pro-code-architecture]
---

# System Design Academy

> Case studies from 40+ companies + 114 system design concepts.

## Company Case Studies

| Company | Topics |
|---------|--------|
| Amazon / AWS | S3 architecture, Prime Video microservices, scaling |
| Netflix | Microservices, chaos engineering |
| Uber | ETA computation, nearby drivers, payments |
| WhatsApp | Messaging at billions scale |
| Slack | Messaging architecture |
| Stripe | Rate limiting, idempotent APIs |
| Instagram | Infrastructure scaling to billions |
| YouTube | Scalability, Vitess MySQL |
| Google | Search engine, Docs real-time editing |
| Discord | Performance optimization, messaging |
| Figma | PostgreSQL scaling |
| Shopify | Flash sales handling |
| Zoom | Video conferencing |
| Facebook | Live video streaming |
| Tinder | Swipe architecture |
| LinkedIn | Scalability patterns |
| Reddit | Architecture |
| Dropbox | File sync and growth |
| Canva | Real-time collaboration |
| Stripe / Razorpay / PayPal | Payment gateways |
| Zapier | Automation platform |
| Bluesky | Decentralized social network |
| Disney+ Hotstar | 25M concurrent users, emoji delivery |

## Core Concepts (114 total)

| Concept | Key Points |
|---------|-----------|
| API Gateway | Auth, routing, rate limiting, aggregation |
| Caching | Write-through, write-behind, cache-aside, eviction |
| Consistent Hashing | Virtual nodes, minimal rehashing on scale |
| Load Balancing | Round-robin, least-connections, IP-hash |
| Rate Limiting | Token bucket, sliding window, fixed window |
| Message Queues | Kafka, RabbitMQ, pub/sub patterns |
| DB Scaling | Sharding, replication, SQL vs NoSQL trade-offs |
| CDN | Edge caching, origin pull vs push |
| Bloom Filters | Probabilistic membership, space efficient |
| Gossip Protocol | Distributed state propagation |
| Cell Architecture | Blast radius isolation |
| Chaos Engineering | Netflix Simian Army approach |
| Actor Model | Concurrent, message-passing systems |
| Real-time | WebSocket vs SSE vs long-polling |

## Back-of-Envelope Numbers
- 1M req/day = ~12 req/sec
- 1B req/day = ~12,000 req/sec
- MySQL write ~1,000 QPS; Redis read ~100,000 QPS
- Typical read:write ratio = 10:1 to 100:1

## 7 Interview Failure Patterns
1. Not clarifying requirements first
2. Skipping scale estimation
3. Ignoring failure modes
4. Not discussing trade-offs
5. Over-engineering for current scale
6. Missing data consistency requirements
7. Forgetting monitoring and observability
