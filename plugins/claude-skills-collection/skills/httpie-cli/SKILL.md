---
name: httpie-cli
description: >
  HTTPie — human-friendly CLI HTTP client for APIs, debugging, testing and scripting.
  USE FOR: "httpie", "http cli", "api testing", "http request terminal", "curl alternative",
  "test API from command line", "send HTTP request", "REST client CLI", "debug API",
  "http post json cli", "download file cli", "http auth cli", "http session", "http proxy".
kind: tool
category: dev/tools
status: active
related_skills: [firecrawl, stripe-best-practices, debug-failing-test]
tags: [http, api, cli, rest, debugging, testing]
repo: https://github.com/httpie/cli
---

# HTTPie CLI — Complete Reference

> "curl for humans" — expressive syntax, colorized output, built-in JSON support.

## Installation

```bash
# Universal
pip install httpie

# macOS
brew install httpie

# Windows
choco install httpie

# Upgrade
pip install --upgrade httpie
```

---

## Core Syntax

```
http [flags] [METHOD] URL [ITEM...]
https [flags] [METHOD] URL [ITEM...]  # forces HTTPS
```

**Method defaults:** GET if no body, POST if body present.

---

## Request Items — Key Operators

| Operator | Type | Example |
|----------|------|---------|
| `:` | Header | `X-Token:abc123` |
| `==` | URL query param | `page==2` |
| `=` | JSON / form string field | `name=John` |
| `:=` | Raw JSON (non-string) | `age:=29` |
| `@` | File upload | `photo@~/pic.jpg` |
| `=@` | String from file | `body=@note.txt` |
| `:=@` | Raw JSON from file | `data:=@payload.json` |

---

## Common Examples

```bash
# Simple GET
http httpie.io/hello
https api.github.com/repos/httpie/cli

# POST JSON (auto Content-Type: application/json)
http POST api.example.com name=John age:=29 married:=false

# Nested JSON
http POST api.example.com platform[name]=HTTPie platform[stars]:=54000

# PUT with header + data
http PUT pie.dev/put X-API-Token:123 name=John

# Query params
http https://api.github.com/search/repositories q==httpie per_page==1

# Localhost shortcut
http :3000/api          # → http://localhost:3000/api
http :/health           # → http://localhost/health
```

---

## Authentication

```bash
# Basic auth
http -a username:password api.example.com

# Digest auth
http -A digest -a user:pass api.example.com

# Bearer token
http -A bearer -a mytoken api.example.com

# GitHub API example
http -a USERNAME POST https://api.github.com/repos/owner/repo/issues/1/comments body='text'
```

---

## Forms & File Uploads

```bash
# URL-encoded form
http --form POST api.example.com name='John Smith' email=john@example.com

# Multipart file upload
http -f POST api.example.com name='John' cv@~/resume.pdf photo@~/pic.jpg
```

---

## Output Control

```bash
http -h api.example.com          # headers only
http -b api.example.com          # body only
http -v api.example.com          # full verbose (request + response)
http -m api.example.com          # metadata + timing
http -q api.example.com          # quiet (no output)
http -p Hh api.example.com       # custom: request headers + response headers
http --offline POST api.example.com data=test  # build request without sending
```

---

## Downloads

```bash
http --download https://example.com/file.zip
http -d https://example.com/file.zip -o myfile.zip   # custom filename
http -dc https://example.com/file.zip                # resume interrupted download
```

---

## Sessions (Persist Cookies + Auth)

```bash
# Named session (saved to ~/.config/httpie/sessions/)
http --session=myapp -a user:pass api.example.com/login
http --session=myapp api.example.com/profile   # reuses cookies + auth

# Anonymous session (one-off)
http --session=/tmp/session.json api.example.com
```

---

## Raw Body & Stdin

```bash
# From stdin
echo '{"key":"value"}' | http POST api.example.com
cat data.json | http PUT api.example.com

# From file (auto Content-Type detection)
http PUT api.example.com @data.xml

# Raw flag
http --raw '{"data":"test"}' POST api.example.com
```

---

## HTTPS / SSL

```bash
http --verify=no https://example.org              # skip SSL verification
http --verify=/path/to/ca-bundle.pem https://...  # custom CA
http --cert=client.pem --cert-key=key.pem https://...  # client cert
http --ssl=tls1.2 https://example.org             # force TLS version
```

---

## Proxies

```bash
http --proxy=http:http://10.10.1.10:3128 example.org
http --proxy=https:socks5://user:pass@host:port example.org

# Or via env vars:
export HTTP_PROXY=http://proxy:8080
export HTTPS_PROXY=http://proxy:8080
export NO_PROXY=localhost,127.0.0.1
```

---

## Redirects

```bash
http --follow pie.dev/redirect/3              # follow redirects
http --follow --all pie.dev/redirect/3        # show all intermediate responses
http --max-redirects=5 pie.dev/redirect/10
```

---

## Streaming & Chunked

```bash
http --stream pie.dev/stream/100              # stream response
http --chunked POST api.example.com @large.xml  # chunked upload
http --compress POST api.example.com @data.xml  # deflate compression
```

---

## Scripting Best Practices

```bash
# Non-interactive script — always use these flags:
http --check-status --ignore-stdin --timeout=2.5 HEAD pie.dev/get

# Exit codes:
# 2 = connection timeout
# 3 = 3xx not followed
# 4 = 4xx client error
# 5 = 5xx server error
```

---

## Plugins

```bash
httpie cli plugins install httpie-aws-auth
httpie cli plugins install httpie-oauth
httpie cli plugins install httpie-jwt-auth
httpie cli plugins list
httpie cli plugins upgrade httpie-aws-auth
httpie cli plugins uninstall httpie-aws-auth
httpie cli check-updates
```

---

## Config File

`~/.config/httpie/config.json` (Linux/macOS)
`%APPDATA%\httpie\config.json` (Windows)

```json
{
  "default_options": ["--style=fruity", "--verify=no"],
  "plugins_dir": "~/.config/httpie/plugins"
}
```

Unset any option per-request: `--no-OPTION` (e.g. `--no-verify`, `--no-style`)

---

## Quick Cheat Sheet

```bash
# Test if API is alive
http HEAD api.example.com

# GET with auth + query params
http -a user:pass api.example.com/data page==1 limit==20

# POST JSON with nested object
http POST api.example.com user[name]=John user[age]:=30 tags:='["vip","new"]'

# Upload + form field
http -f POST api.example.com title="My Doc" file@doc.pdf

# Full verbose debug
http -v POST api.example.com Authorization:"Bearer token" data=test

# Download with progress
http --download https://files.example.com/large.tar.gz

# Offline request preview
http --offline DELETE api.example.com/resource/42 Authorization:"Bearer token"
```
