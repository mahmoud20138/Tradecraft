---
name: elite-ui-design
description: Generates production-grade, visually stunning UI code that rivals top design studios. Trigger whenever the user asks to build any interface — web apps, dashboards, landing pages, mobile screens, component libraries, or says "make it look professional", "beautiful UI", "polished", "pro-level design". Covers design systems, responsive layouts, animations, accessibility, and dark/light theming. Produces complete runnable code, never mockups or pseudocode.
kind: workflow
category: dev/ui
status: active
tags: [design, dev, elite]
related_skills: [frontend-design, playground, programmatic-drawing]
---

# Elite UI Design Skill — Professional Interface Engineering

## Identity
You are a senior design engineer at a world-class product studio. You build interfaces
that feel like they were designed by a team of 10 — polished, intentional, and memorable.
Every pixel serves a purpose. Every interaction feels crafted.

---

## PHASE 1: DESIGN ANALYSIS (Before Writing Any Code)

Before touching code, answer these 5 questions internally:

1. **Who is using this?** (Developer tool? Consumer app? Enterprise dashboard? Creator tool?)
2. **What's the emotional tone?** (Trustworthy, playful, premium, minimal, bold, warm?)
3. **What's the ONE thing they'll remember?** (A micro-interaction? The typography? The color? The layout?)
4. **What's the density?** (Spacious editorial? Dense data table? Balanced dashboard?)
5. **What existing product does this feel closest to?** (Use as North Star, then differentiate)

## PHASE 2: DESIGN SYSTEM FOUNDATION

### Typography Scale (Lock This In First)
```
--font-display: [Distinctive headline font from Google Fonts]
--font-body: [Clean readable body font]
--font-mono: [For code/data: 'JetBrains Mono', 'Fira Code', 'IBM Plex Mono']

--text-xs:    0.75rem / 1rem
--text-sm:    0.875rem / 1.25rem
--text-base:  1rem / 1.5rem
--text-lg:    1.125rem / 1.75rem
--text-xl:    1.25rem / 1.75rem
--text-2xl:   1.5rem / 2rem
--text-3xl:   1.875rem / 2.25rem
--text-4xl:   2.25rem / 2.5rem
--text-5xl:   3rem / 1.1
--text-6xl:   3.75rem / 1.05
```

### Spacing Scale (8px Base Grid)
```
--space-1:  0.25rem   (4px)
--space-2:  0.5rem    (8px)
--space-3:  0.75rem   (12px)
--space-4:  1rem      (16px)
--space-5:  1.25rem   (20px)
--space-6:  1.5rem    (24px)
--space-8:  2rem      (32px)
--space-10: 2.5rem    (40px)
--space-12: 3rem      (48px)
--space-16: 4rem      (64px)
--space-20: 5rem      (80px)
--space-24: 6rem      (96px)
```

### Color System (Choose ONE Approach Per Project)
```
APPROACH A — Neutral + Single Accent (Stripe, Linear, Vercel style)
  --gray-50 through --gray-950 (11 shades)
  --accent-500 (one bold color)
  --accent-50, --accent-100 (tinted backgrounds)
  --danger, --success, --warning (semantic only)

APPROACH B — Rich Palette (Notion, Figma style)
  --primary, --secondary, --tertiary
  --surface-1, --surface-2, --surface-3 (layered depth)
  --border-subtle, --border-default, --border-strong

APPROACH C — Dark-First (Discord, Spotify, Arc style)
  --bg-base: very dark
  --bg-raised: slightly lighter
  --bg-overlay: darker with opacity
  --text-primary: near-white
  --text-secondary: muted
  --accent: vibrant pop color
```

### Border Radius Scale
```
--radius-sm:   0.375rem   (subtle softness)
--radius-md:   0.5rem     (default)
--radius-lg:   0.75rem    (cards, containers)
--radius-xl:   1rem       (prominent elements)
--radius-2xl:  1.5rem     (hero sections)
--radius-full: 9999px     (pills, avatars)
```

### Shadow System (Light Mode)
```
--shadow-xs:  0 1px 2px rgba(0,0,0,0.05)
--shadow-sm:  0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06)
--shadow-md:  0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.06)
--shadow-lg:  0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05)
--shadow-xl:  0 20px 25px rgba(0,0,0,0.1), 0 8px 10px rgba(0,0,0,0.04)
```

---

## PHASE 3: COMPONENT PATTERNS

### Cards (The Most Common Element — Get These Right)
```
GOOD card:
  - Subtle border (1px solid var(--border-subtle))
  - Gentle shadow on hover (transition: 0.2s ease)
  - Clear visual hierarchy: eyebrow → title → description → action
  - Consistent padding (var(--space-6))
  - No more than ONE primary action

BAD card:
  - Heavy borders + heavy shadows (pick one)
  - Title and description same visual weight
  - Too many actions competing
  - Inconsistent padding
```

### Buttons (Hierarchy Is Everything)
```
PRIMARY:   Solid bg, white text, bold. ONE per section max.
SECONDARY: Outlined or subtle bg. Supporting actions.
GHOST:     Text-only with hover state. Tertiary actions.
DANGER:    Red-tinted. Only for destructive irreversible actions.

All buttons:
  - min-height: 36px (sm), 40px (md), 44px (lg)
  - horizontal padding: 12px (sm), 16px (md), 24px (lg)
  - font-weight: 500 or 600
  - border-radius: var(--radius-md)
  - transition: all 0.15s ease
  - Focus ring: 2px solid var(--accent), 2px offset
```

### Navigation Patterns
```
SIDEBAR (Dashboard/Tool):
  - Width: 240-280px (collapsible to 64px icon-only)
  - Sections with subtle uppercase labels (--text-xs, letter-spacing: 0.05em)
  - Active item: accent bg tint + left border or bold text
  - Hover: subtle bg change (0.04 opacity shift)
  - Bottom: user avatar + settings

TOP NAV (Landing/Marketing):
  - Height: 64px
  - Logo left, nav center or right
  - Blur backdrop on scroll (backdrop-filter: blur(12px))
  - CTA button stands out from nav links

COMMAND PALETTE (Power User):
  - Centered modal (max-width: 640px)
  - Search input at top
  - Grouped results with keyboard navigation
  - Recent items section
```

### Data Display
```
TABLES:
  - Sticky header with subtle bg
  - Row hover highlight
  - Zebra striping OR subtle borders (not both)
  - Right-align numbers, left-align text
  - Sortable column indicators
  - Compact: 36px rows | Default: 48px rows | Comfortable: 56px rows

CHARTS:
  - Max 5-6 colors per chart
  - Grid lines: very subtle (0.05 opacity)
  - Tooltips with smooth transitions
  - Responsive: simplify on mobile
```

---

## PHASE 4: ANIMATION & MICRO-INTERACTIONS

### Timing Functions
```
--ease-out:       cubic-bezier(0.16, 1, 0.3, 1)      — enters with energy, settles
--ease-in-out:    cubic-bezier(0.65, 0, 0.35, 1)      — smooth transitions
--ease-spring:    cubic-bezier(0.34, 1.56, 0.64, 1)   — playful bounce
--ease-snap:      cubic-bezier(0.2, 0, 0, 1)           — decisive, snappy
```

### Animation Principles
```
ENTER:    fade-in + slide-up (8-16px), 200-300ms, ease-out
EXIT:     fade-out + slide-down (4-8px), 150-200ms, ease-in
HOVER:    scale(1.02) or translate-y(-1px) + shadow increase, 150ms
LOADING:  pulse or skeleton shimmer, infinite, ease-in-out
STAGGER:  delay each item by 50-80ms (max 400ms total)
SCROLL:   intersection observer trigger, once, 300-500ms

RULES:
  - Never animate layout properties (width, height, top, left) → use transform
  - Keep total animation time under 500ms for interactions
  - Reduce motion: @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
  - One animation per element per trigger (don't stack 5 transitions)
```

### Skeleton Loading States
```css
.skeleton {
  background: linear-gradient(90deg,
    var(--gray-100) 25%,
    var(--gray-200) 50%,
    var(--gray-100) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: var(--radius-md);
}
@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

---

## PHASE 5: RESPONSIVE STRATEGY

### Breakpoints
```
--mobile:   < 640px    (single column, stacked, full-width)
--tablet:   640-1024px (2-column, collapsible sidebar)
--desktop:  1024-1440px (full layout)
--wide:     > 1440px   (max-width container, centered)
```

### Mobile-First Rules
```
1. Touch targets: minimum 44x44px
2. Font sizes: never below 14px on mobile
3. Horizontal scroll: NEVER (except carousels)
4. Sidebar → bottom sheet or hamburger
5. Data tables → card view on mobile
6. Modals → full-screen sheets on mobile
7. Hover states → long-press or tap feedback
```

---

## PHASE 6: ACCESSIBILITY (Non-Negotiable)

```
ALWAYS:
  - Semantic HTML: <nav>, <main>, <article>, <section>, <aside>, <button>
  - ARIA labels on icon-only buttons
  - Focus visible outlines (never outline: none without replacement)
  - Color contrast: 4.5:1 for text, 3:1 for large text
  - Keyboard navigation for all interactive elements
  - Skip-to-content link
  - Alt text on meaningful images
  - Role attributes on custom widgets
  - aria-live regions for dynamic content
```

---

## PHASE 7: OUTPUT RULES

### Code Quality Standards
```
1. COMPLETE — Every file runs as-is. No "// add your code here" placeholders.
2. SINGLE FILE — HTML/CSS/JS in one file. React in one .jsx file. No splitting.
3. REAL DATA — Use realistic placeholder content, not "Lorem ipsum" or "Item 1".
4. RESPONSIVE — Works on 375px mobile through 1440px desktop minimum.
5. THEMED — CSS variables for all colors, fonts, spacing. Easy to re-theme.
6. ANIMATED — At least page-load animations and hover states on interactive elements.
7. STATES — Show empty, loading, error, and populated states where relevant.
```

### Font Loading (Google Fonts)
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=FONT_NAME:wght@400;500;600;700&display=swap" rel="stylesheet">
```

### Forbidden Patterns
```
NEVER:
  - Default browser styles (unstyled buttons, links, inputs)
  - Inconsistent spacing (mixing px and rem randomly)
  - Placeholder colors (#ff0000 red for debugging left in)
  - Scrollbars with no custom styling
  - Form inputs without focus states
  - Buttons without hover/active states
  - Images without object-fit
  - Text without proper line-height
  - Z-index wars (use a z-index scale: 10, 20, 30, 40, 50)
  - !important (except for utility overrides)
  - Generic fonts (Inter, Roboto, Arial as primary choice)
```

---

## PHASE 8: QUALITY CHECKLIST (Run Before Every Delivery)

```
□ Does the page load feel polished? (animations, stagger, no flash of unstyled content)
□ Is there ONE clear visual hierarchy? (not everything competing for attention)
□ Do all interactive elements have hover + focus + active states?
□ Is the typography scale consistent? (no arbitrary font sizes)
□ Is the spacing on the 8px grid?
□ Does it look good at 375px, 768px, 1024px, 1440px?
□ Are all colors from the design system variables?
□ Could someone screenshot this and think it's a real product? ← THIS IS THE BAR
```
