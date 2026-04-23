---
name: ip-rotation
description: >
  Rotate IP addresses when sessions are rate-limited or blocked by YouTube or other services.
  USE FOR: ip rotation, rate limit, proxy, tor, blocked, 429 error, youtube block.
related_skills:
  - youtube-video-to-knowledge
tags:
  - utility
  - ip-rotation
  - proxy
  - tor
  - rate-limit
skill_level: intermediate
kind: tool
category: dev/tools
status: active
---
> **Skill:** Ip Rotation  |  **Domain:** utils  |  **Category:** utility  |  **Level:** intermediate
> **Tags:** `utility`, `ip-rotation`, `proxy`, `tor`, `rate-limit`


# IP Rotation Skill

Rotate IP addresses when sessions are rate-limited or blocked.

## Tools Referenced

- **Tor IP Changer**: https://github.com/isPique/Tor-IP-Changer
- **gr33n37 IP Changer**: https://github.com/gr33n37/gr33n37-ip-changer

## When to Use

- News/market data API rate limits hit
- IP-based blocking on external services
- Session limits from data providers
- Brave Search or other web scraping getting 429/403 errors

## Setup

```bash
# Install Tor IP Changer
git clone https://github.com/isPique/Tor-IP-Changer
cd Tor-IP-Changer
pip install -r requirements.txt

# Or install gr33n37
git clone https://github.com/gr33n37/gr33n37-ip-changer
cd gr33n37-ip-changer
python setup.py install
```

## Usage Pattern

```python
from tor_ip_changer import TorIpChanger

# Rotate IP before retry
changer = TorIpChanger()
changer.get_new_ip()
# Then retry request with new IP
```

## Integration

Wrap external API calls with IP rotation:
1. Attempt request
2. If 429/403 received, rotate IP
3. Retry with exponential backoff
4. Log rotation for debugging

## Priority

Low/Medium — only activate when external services actively block.

---

## Related Skills

- [Youtube Video To Knowledge](../youtube-video-to-knowledge.md)
