---
name: youtube-video-to-knowledge
description: Extract knowledge from YouTube videos — transcripts, keyframes, metadata, AI-powered analysis, and AUTOMATIC skill integration. When a YouTube URL is shared, extract the content AND route the knowledge to related existing skills in parallel. Use this skill whenever the user shares a YouTube URL or asks to summarize/analyze/extract notes from a YouTube video. Also trigger for "youtube transcript", "video notes", "watch and summarize", "video summary", "extract from youtube", "youtube to text", "video knowledge", "NoteGPT", "summarize this video", "what does this video say", "video flashcards", "add to skills", or any request involving YouTube content extraction and analysis. After extraction, always identify and update related skills with the new knowledge. Works for any YouTube video with or without subtitles.
kind: tool
category: data/media
status: active
tags: [data, knowledge, media, video, youtube]
---

# YouTube Video to Knowledge Extractor

Transform any YouTube video into structured knowledge — transcripts, visual keyframes, AI-powered summaries, flashcards, mind maps, and more.

## When to Use This Skill

Trigger whenever:
- User shares a YouTube URL (youtube.com/watch, youtu.be, shorts)
- User asks to "summarize a video", "extract notes", "what does this video say"
- User wants transcripts, captions, or subtitles from YouTube
- User asks for flashcards, mind maps, or blog posts from video content
- User mentions "NoteGPT", "video notes", "video to text"
- User asks to analyze visual content (slides, diagrams) from a video
- User wants to extract knowledge from a playlist or channel

## Architecture Overview

```
YouTube URL
    │
    ├── [1] Metadata Extraction (yt-dlp) — title, channel, chapters, tags
    │
    ├── [2] Transcript Extraction (3-tier fallback):
    │       ├── youtube-transcript-api (fastest, no download)
    │       ├── yt-dlp subtitle download (VTT parse)
    │       └── Whisper local transcription (audio download + ASR)
    │
    ├── [3] Visual Extraction (optional):
    │       ├── Scene-change keyframes (OpenCV histogram diff)
    │       ├── Interval-based frames (fixed time steps)
    │       └── FFmpeg scene detection
    │
    ├── [4] Knowledge Synthesis (Claude):
    │       ├── Comprehensive Notes
    │       ├── Executive Summary
    │       ├── Flashcards
    │       ├── Mind Map (Mermaid)
    │       ├── Blog Article
    │       ├── Technical Analysis
    │       └── Visual Analysis (with keyframe images)
    │
    └── [5] Skill Routing (PARALLEL — always do this):
            ├── Identify related skills from video topic
            ├── Update existing skills with new knowledge
            └── Cross-reference between skills
```

## CRITICAL: Parallel Skill Integration (Always Do This)

After extracting and summarizing a YouTube video, you MUST do two things **in parallel**:

1. **Present the summary** to the user
2. **Route the knowledge to related skills** — find and update existing skills

### How Skill Routing Works

**Step A — Identify related skills (during synthesis):**
While reading the transcript, identify the video's domain topics. Match against existing skills:
- Trading concepts (BOS, CHoCH, liquidity, etc.) → market-structure-bos-choch, ict-smart-money, smc-beginner-pro-guide, etc.
- Strategy types → backtesting-sim, price-action, session-scalping, etc.
- Risk/portfolio → risk-and-portfolio, risk-and-portfolio, drawdown-playbook, etc.
- Technical analysis → technical-analysis, chart-pattern-scanner, fibonacci-strategy-engine, etc.
- Any other domain → match by keyword from skill descriptions

**Step B — Update skills in parallel:**
Use the Agent tool to spawn parallel subagents that:
1. Read each related skill's SKILL.md
2. Add the new knowledge (rules, methods, concepts, Python code) as a new section
3. Add source attribution: `> Source: "Video Title" by Channel (Date)`
4. Add cross-references to other updated skills
5. Update the skill's description if new trigger terms are needed

**Step C — Report to user:**
After both the summary and skill updates complete, tell the user:
```
Updated X related skills:
- skill-name-1: added [concept] section
- skill-name-2: added cross-reference to [concept]
```

### Skill Update Rules

- Add new knowledge as a clearly marked section with source attribution
- Include Python implementations when the video teaches a quantifiable/automatable method
- Add new trigger terms to the skill description if the video introduces new terminology
- Cross-link updated skills to each other
- Never remove existing content — only add or enhance
- If no related skill exists, note this to the user (they may want to create one)

## Quick Start — Step by Step

### Step 0: Install Dependencies

```bash
pip install yt-dlp youtube-transcript-api webvtt-py --break-system-packages -q
```

These are lightweight. OpenCV and FFmpeg are pre-installed in the environment.

### Step 1: Extract Content

Read and execute the extraction script:

```bash
python3 /path/to/scripts/youtube_extractor.py "YOUTUBE_URL" \
  --work-dir /home/claude/yt_work \
  --output /home/claude/yt_work/video_knowledge.md
```

**Common options:**
| Flag | Purpose | Default |
|------|---------|---------|
| `--frames` | Extract keyframe images | Off |
| `--frame-method` | `scene` / `interval` / `ffmpeg` | `scene` |
| `--max-frames` | Max keyframes to extract | 15 |
| `--languages en ar` | Preferred transcript languages | en + 9 others |
| `--whisper` | Enable Whisper fallback (slow) | Off |
| `--whisper-model` | `tiny`/`base`/`small`/`medium` | `base` |

### Step 2: Read the Extracted Content

After extraction, you'll have:
- `*_knowledge.md` — Human-readable knowledge document
- `*_raw.json` — Structured data for programmatic use
- `keyframes/` directory (if `--frames` was used)

Read the markdown to understand the content, then proceed to analysis.

### Step 3: Analyze with Claude (this is YOU)

You ARE Claude. After extracting the transcript, you have the full content in context. Now analyze it directly based on what the user wants:

**If user wants notes/summary:** Read the transcript and produce structured notes yourself.
**If user wants flashcards:** Generate Q&A pairs from the content.
**If user wants a mind map:** Create a Mermaid diagram showing concept relationships.
**If user wants visual analysis + `--frames` was used:** Use the `view` tool to look at the extracted keyframe images, then describe what's shown at each timestamp.

The `scripts/knowledge_synthesizer.py` script exists for API-based synthesis (useful in artifacts or automated pipelines), but in most cases you should just analyze the transcript content directly.

## Detailed Workflows

### Workflow A: Quick Transcript + Summary (Most Common)

This is the 80% case — user shares a URL and wants to know what the video says.

```python
# In your Python execution:
import sys
sys.path.insert(0, '/path/to/scripts')
from youtube_extractor import extract_video_id, get_video_metadata, extract_transcript_api

video_id = extract_video_id(url)
metadata = get_video_metadata(url)
transcript = extract_transcript_api(video_id)

# Now you have metadata['title'], transcript['text'], transcript['segments']
# Analyze directly in your response
```

Or use the CLI:
```bash
python3 scripts/youtube_extractor.py "URL" --work-dir /home/claude/yt_work
cat /home/claude/yt_work/*_knowledge.md
```

### Workflow B: Visual Content Analysis

For tutorial videos, presentations, or demos where slides/screens matter:

```bash
python3 scripts/youtube_extractor.py "URL" \
  --frames --frame-method scene --max-frames 15 \
  --work-dir /home/claude/yt_work
```

Then use the `view` tool to examine each keyframe image, correlating what's shown with the transcript timestamps.

### Workflow C: No Subtitles Available

Some videos have no captions at all. Enable Whisper fallback:

```bash
python3 scripts/youtube_extractor.py "URL" \
  --whisper --whisper-model base \
  --work-dir /home/claude/yt_work
```

**Warning:** Whisper downloads a model (~140MB for base) and transcribes the full audio. This is slow (real-time ratio ~0.3x on CPU). Only use when subtitles are unavailable.

### Workflow D: Non-English Videos

Specify preferred languages:

```bash
python3 scripts/youtube_extractor.py "URL" \
  --languages ar en fr \
  --work-dir /home/claude/yt_work
```

The transcript API tries each language in order. Arabic (`ar`) is supported for auto-generated captions on most videos.

### Workflow E: Batch / Playlist Processing

For multiple videos, loop over URLs:

```python
urls = ["URL1", "URL2", "URL3"]
for i, url in enumerate(urls):
    result = extract_youtube_knowledge(
        url=url,
        work_dir=f'/home/claude/yt_work/video_{i}',
    )
    # Process each result
```

## Output Types for Knowledge Synthesis

When using `scripts/knowledge_synthesizer.py` or when the user asks for a specific format:

| Type | Description | Best For |
|------|-------------|----------|
| `comprehensive_notes` | Full structured notes with all details | Study, reference |
| `executive_summary` | Concise 500-word summary | Busy professionals |
| `flashcards` | 15-25 Anki-style Q&A cards | Learning/review |
| `mindmap` | Mermaid mindmap diagram | Concept overview |
| `blog_article` | Rewritten as blog post | Content repurposing |
| `technical_analysis` | Deep technical breakdown | Engineering/research |
| `visual_analysis` | Analysis of slides/screens | Presentation videos |

## Important Considerations

### Network Access
- `youtube-transcript-api` needs access to YouTube's servers
- `yt-dlp` needs access to YouTube for downloads
- In restricted environments, the transcript API is the lightest option (no video download)

### Rate Limits & Errors
- YouTube may rate-limit transcript requests — add small delays for batch processing
- Some videos block embedding/subtitles — the 3-tier fallback handles most cases
- Age-restricted or private videos require authentication (not supported in this skill)

### File Sizes
- Transcripts: typically 10-50 KB text
- Keyframes: ~50-200 KB each (JPEG, 360p resolution)
- Audio (for Whisper): ~1 MB/minute at 128kbps
- Video (for frames): ~2-5 MB/minute at 360p

### Cleanup
Always clean up working directories after extraction:
```bash
rm -rf /home/claude/yt_work
```

## Error Handling Checklist

| Error | Cause | Fix |
|-------|-------|-----|
| "Could not extract video ID" | Malformed URL | Ask user to verify URL |
| "Transcripts disabled" | Channel disabled captions | Use `--whisper` fallback |
| "Video unavailable" | Private/deleted/geo-blocked | Inform user, cannot extract |
| "No subtitles available" | No captions in any language | Use `--whisper` fallback |
| OpenCV can't open video | Download failed or corrupt | Try `--frame-method ffmpeg` |
| Whisper OOM | Video too long for memory | Use `--whisper-model tiny` |

## Script Locations

After installing this skill, scripts are at:
```
youtube-video-to-knowledge/
├── SKILL.md                          ← You are here
├── scripts/
│   ├── youtube_extractor.py          ← Main extraction pipeline
│   └── knowledge_synthesizer.py      ← Claude API synthesis (for artifacts)
├── references/
│   └── prompt_templates.md           ← Customizable prompt templates
└── assets/
    └── (empty — for user templates)
```

## Tips for Best Results

1. **Always extract metadata first** — chapters and description give you a roadmap of the content.
2. **Prefer transcript API over yt-dlp** — it's faster and doesn't download anything.
3. **Use `--frames` for tutorial/presentation videos** — slides contain info not in speech.
4. **For long videos (>1 hour)**, consider extracting chapters and summarizing per-chapter.
5. **Arabic videos**: Most have auto-generated Arabic captions. Use `--languages ar en`.
6. **Keyframe scene detection** works best on videos with clear scene changes (presentations, cuts). For talking-head videos, use `--frame-method interval --frame-interval 60`.
