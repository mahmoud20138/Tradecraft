---
name: programmatic-drawing
description: Expert skill for generating visual art, diagrams, illustrations, charts, and drawings programmatically using SVG, HTML Canvas, p5.js, Three.js, Mermaid, and D3. Trigger whenever the user asks to draw, illustrate, visualize, diagram, create art, generate graphics, make a flowchart, render shapes, animate visuals, create infographics, or produce any kind of visual output through code. Also trigger for data visualization, generative art, interactive graphics, and technical diagrams.
kind: tool
category: dev/ui
status: active
tags: [dev, drawing, programmatic]
related_skills: [elite-ui-design, frontend-design, playground]
---

# Programmatic Drawing Skill — Visual Generation Through Code

## Identity
You are a creative technologist who generates stunning visuals through code.
You think in coordinates, gradients, and composition. Every visual has intention
behind its layout, color, and movement. You choose the right rendering technology
for the job and produce complete, runnable visual code.

---

## TECHNOLOGY SELECTION GUIDE

### Choose the Right Tool

```
NEED                              → USE
─────────────────────────────────────────────────
Static diagram / flowchart        → Mermaid or SVG
Icon / logo / simple illustration → SVG (inline or file)
Data visualization / charts       → D3.js or Recharts or Chart.js
Interactive 2D graphics           → HTML Canvas API
Generative / algorithmic art      → p5.js
3D scenes / models                → Three.js
Architecture / sequence diagrams  → Mermaid
Infographics / mixed text+visual  → SVG + HTML overlay
Animated illustrations            → SVG + CSS animations or p5.js
Particle systems / simulations    → p5.js or Canvas API
```

---

## MODULE 1: SVG — Scalable Vector Graphics

### When to Use
- Diagrams, icons, logos, illustrations with clean lines
- Anything that needs to scale without pixelation
- Visuals that need CSS styling and DOM manipulation
- Animated illustrations (CSS or SMIL animations)

### SVG Fundamentals
```xml
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <!-- Coordinate system: origin top-left, y increases downward -->

  <!-- Basic Shapes -->
  <rect x="10" y="10" width="100" height="50" rx="8" fill="#4F46E5" />
  <circle cx="200" cy="100" r="40" fill="#EC4899" opacity="0.8" />
  <ellipse cx="350" cy="100" rx="60" ry="30" fill="#10B981" />
  <line x1="10" y1="200" x2="300" y2="200" stroke="#6B7280" stroke-width="2" />
  <polyline points="10,250 50,220 90,260 130,230" fill="none" stroke="#F59E0B" stroke-width="2" />
  <polygon points="200,220 240,260 160,260" fill="#EF4444" />

  <!-- Paths (most powerful) -->
  <path d="M 10 300 C 50 280, 90 320, 130 300" fill="none" stroke="#8B5CF6" stroke-width="2" />

  <!-- Text -->
  <text x="400" y="100" font-family="system-ui" font-size="24" fill="#1F2937"
        text-anchor="middle" dominant-baseline="middle">Label</text>

  <!-- Groups with transforms -->
  <g transform="translate(400, 300) rotate(45)">
    <rect x="-20" y="-20" width="40" height="40" fill="#F97316" />
  </g>

  <!-- Gradients -->
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#667EEA" />
      <stop offset="100%" stop-color="#764BA2" />
    </linearGradient>
    <radialGradient id="grad2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FDE68A" />
      <stop offset="100%" stop-color="#F59E0B" />
    </radialGradient>
  </defs>
  <rect x="10" y="400" width="200" height="100" rx="12" fill="url(#grad1)" />

  <!-- Filters (shadows, blur, glow) -->
  <defs>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="4" stdDeviation="4" flood-color="#00000033" />
    </filter>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
    </filter>
  </defs>

  <!-- Clip paths and masks -->
  <defs>
    <clipPath id="circleClip">
      <circle cx="100" cy="100" r="50" />
    </clipPath>
  </defs>
  <image href="..." clip-path="url(#circleClip)" />
</svg>
```

### SVG Animation (CSS)
```css
@keyframes draw {
  from { stroke-dashoffset: 1000; }
  to { stroke-dashoffset: 0; }
}
.animated-path {
  stroke-dasharray: 1000;
  animation: draw 2s ease-out forwards;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.1); opacity: 0.7; }
}
.pulsing { animation: pulse 2s ease-in-out infinite; }
```

### SVG Best Practices
```
1. Always set viewBox (not width/height) for responsiveness
2. Use <defs> for reusable elements (gradients, filters, clip-paths)
3. Group related elements with <g> and apply transforms to groups
4. Use stroke-linecap="round" and stroke-linejoin="round" for polished paths
5. Layer elements bottom-to-top (SVG paints in document order)
6. Use text-anchor and dominant-baseline for text alignment
7. Optimize: remove unnecessary precision (2 decimal places max)
```

---

## MODULE 2: HTML CANVAS API

### When to Use
- Pixel-level control needed
- Real-time rendering (games, simulations)
- Large number of elements (>1000 shapes)
- Image manipulation

### Canvas Fundamentals
```javascript
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Set canvas size (account for DPI)
const dpr = window.devicePixelRatio || 1;
canvas.width = 800 * dpr;
canvas.height = 600 * dpr;
canvas.style.width = '800px';
canvas.style.height = '600px';
ctx.scale(dpr, dpr);

// Shapes
ctx.fillStyle = '#4F46E5';
ctx.fillRect(10, 10, 100, 50);                    // Rectangle
ctx.strokeStyle = '#EC4899';
ctx.lineWidth = 2;
ctx.strokeRect(10, 10, 100, 50);                   // Outlined rect

ctx.beginPath();                                    // Circle
ctx.arc(200, 100, 40, 0, Math.PI * 2);
ctx.fill();

ctx.beginPath();                                    // Custom path
ctx.moveTo(10, 200);
ctx.lineTo(50, 170);
ctx.quadraticCurveTo(90, 230, 130, 200);
ctx.bezierCurveTo(160, 170, 200, 230, 230, 200);
ctx.stroke();

// Rounded rectangle helper
function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.arcTo(x + w, y, x + w, y + h, r);
  ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r);
  ctx.arcTo(x, y, x + w, y, r);
  ctx.closePath();
}

// Gradients
const grad = ctx.createLinearGradient(0, 0, 200, 200);
grad.addColorStop(0, '#667EEA');
grad.addColorStop(1, '#764BA2');
ctx.fillStyle = grad;

// Shadows
ctx.shadowColor = 'rgba(0, 0, 0, 0.2)';
ctx.shadowBlur = 10;
ctx.shadowOffsetX = 2;
ctx.shadowOffsetY = 4;

// Text
ctx.font = '600 24px system-ui';
ctx.textAlign = 'center';
ctx.textBaseline = 'middle';
ctx.fillText('Label', 400, 300);

// Transforms
ctx.save();
ctx.translate(400, 300);
ctx.rotate(Math.PI / 4);
ctx.fillRect(-20, -20, 40, 40);
ctx.restore();

// Animation loop
function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // draw frame...
  requestAnimationFrame(animate);
}
animate();
```

---

## MODULE 3: p5.js — Creative Coding

### When to Use
- Generative art, algorithmic patterns
- Particle systems, flow fields
- Interactive visual experiments
- Rapid prototyping of visual ideas

### p5.js Structure
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>
<script>
let seed;

function setup() {
  createCanvas(800, 600);
  seed = random(10000);
  noLoop(); // Call for static art, remove for animation
}

function draw() {
  randomSeed(seed); // Reproducible randomness
  background(15, 15, 20);

  // Your art here
}
</script>
```

### Common Generative Patterns

#### Flow Fields
```javascript
function draw() {
  background(15, 15, 20, 5);
  let cols = floor(width / 20);
  let rows = floor(height / 20);
  let noiseScale = 0.005;

  for (let i = 0; i < 500; i++) {
    let x = random(width);
    let y = random(height);
    let angle = noise(x * noiseScale, y * noiseScale, frameCount * 0.005) * TWO_PI * 2;
    let len = 15;
    stroke(map(angle, 0, TWO_PI * 2, 100, 300), 80, 90, 40);
    strokeWeight(1);
    line(x, y, x + cos(angle) * len, y + sin(angle) * len);
  }
}
```

#### Particle Systems
```javascript
class Particle {
  constructor(x, y) {
    this.pos = createVector(x, y);
    this.vel = p5.Vector.random2D().mult(random(1, 3));
    this.acc = createVector(0, 0);
    this.life = 255;
    this.size = random(2, 8);
    this.color = color(random(180, 260), 80, 95, this.life);
  }
  update() {
    this.vel.add(this.acc);
    this.pos.add(this.vel);
    this.acc.mult(0);
    this.life -= 3;
  }
  draw() {
    noStroke();
    fill(hue(this.color), saturation(this.color), brightness(this.color), this.life);
    circle(this.pos.x, this.pos.y, this.size);
  }
  isDead() { return this.life <= 0; }
}
```

#### Recursive Patterns
```javascript
function fractalTree(x, y, len, angle, depth) {
  if (depth <= 0 || len < 2) return;
  let x2 = x + cos(angle) * len;
  let y2 = y + sin(angle) * len;

  strokeWeight(map(depth, 0, 10, 0.5, 4));
  stroke(map(depth, 0, 10, 120, 30), 70, 80);
  line(x, y, x2, y2);

  let spread = PI / 6 + random(-0.1, 0.1);
  fractalTree(x2, y2, len * 0.72, angle - spread, depth - 1);
  fractalTree(x2, y2, len * 0.72, angle + spread, depth - 1);
}
```

---

## MODULE 4: MERMAID — Technical Diagrams

### Diagram Types
```mermaid
%% Flowchart
graph TD
  A[Start] --> B{Decision?}
  B -->|Yes| C[Action 1]
  B -->|No| D[Action 2]
  C --> E[End]
  D --> E

%% Sequence Diagram
sequenceDiagram
  Client->>+API: POST /orders
  API->>+DB: INSERT order
  DB-->>-API: order_id
  API->>+Queue: publish OrderCreated
  API-->>-Client: 201 Created

%% Class Diagram
classDiagram
  class Order {
    +String id
    +Money total
    +Status status
    +addItem(item)
    +cancel()
  }

%% State Machine
stateDiagram-v2
  [*] --> Draft
  Draft --> Submitted: submit()
  Submitted --> Approved: approve()
  Submitted --> Rejected: reject()
  Approved --> [*]
  Rejected --> Draft: revise()
```

---

## MODULE 5: D3.js — Data Visualization

### When to Use
- Custom data visualizations beyond standard charts
- Interactive, data-driven graphics
- Maps, network graphs, hierarchical data

### D3 Pattern
```javascript
// Data → Scale → Shape → Bindimport * as d3 from 'd3';

const data = [10, 25, 40, 15, 60, 35];
const width = 600, height = 400, margin = { top: 20, right: 20, bottom: 40, left: 50 };

const svg = d3.select('#chart').append('svg')
  .attr('viewBox', `0 0 ${width} ${height}`);

const x = d3.scaleBand()
  .domain(data.map((_, i) => i))
  .range([margin.left, width - margin.right])
  .padding(0.2);

const y = d3.scaleLinear()
  .domain([0, d3.max(data)])
  .range([height - margin.bottom, margin.top]);

svg.selectAll('rect')
  .data(data)
  .join('rect')
  .attr('x', (_, i) => x(i))
  .attr('y', d => y(d))
  .attr('width', x.bandwidth())
  .attr('height', d => height - margin.bottom - y(d))
  .attr('rx', 4)
  .attr('fill', '#4F46E5');
```

---

## MODULE 6: THREE.js — 3D Graphics

### Basic 3D Scene
```javascript
import * as THREE from 'three';

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x111118);

const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);
document.body.appendChild(renderer.domElement);

// Lighting
const ambientLight = new THREE.AmbientLight(0x404040, 0.5);
scene.add(ambientLight);
const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(5, 5, 5);
scene.add(directionalLight);

// Mesh
const geometry = new THREE.IcosahedronGeometry(1, 1);
const material = new THREE.MeshStandardMaterial({
  color: 0x4F46E5,
  metalness: 0.3,
  roughness: 0.4
});
const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh);

function animate() {
  requestAnimationFrame(animate);
  mesh.rotation.x += 0.005;
  mesh.rotation.y += 0.008;
  renderer.render(scene, camera);
}
animate();
```

---

## COLOR PALETTES FOR VISUALS

### Professional Palettes
```
MIDNIGHT TECH:    #0F172A, #1E293B, #3B82F6, #60A5FA, #BFDBFE
SUNSET WARM:      #1A1A2E, #E94560, #F97316, #FCD34D, #FEF3C7
FOREST ORGANIC:   #064E3B, #059669, #34D399, #6EE7B7, #D1FAE5
OCEAN DEPTH:      #0C4A6E, #0284C7, #38BDF8, #7DD3FC, #E0F2FE
PURPLE HAZE:      #2E1065, #7C3AED, #A78BFA, #C4B5FD, #EDE9FE
MONOCHROME:       #09090B, #27272A, #52525B, #A1A1AA, #E4E4E7
NEON DARK:        #000000, #FF006E, #00F5D4, #FEE440, #9B5DE5
```

### Color Usage Rules
```
1. Background: darkest shade (60% of visual area)
2. Primary elements: mid tones (30%)
3. Accents/highlights: brightest colors (10%)
4. Never use pure black (#000000) for backgrounds — use very dark tinted colors
5. Add slight transparency to overlapping elements for depth
6. Use HSL for color manipulation: adjust lightness for shades, saturation for vibrancy
```

---

## COMPOSITION RULES

```
1. RULE OF THIRDS: Place focal points at intersections of a 3x3 grid
2. VISUAL HIERARCHY: Size > Color > Position > Shape
3. WHITESPACE: Empty space is a design element — don't fill everything
4. CONTRAST: Light on dark or dark on light. Never medium on medium.
5. REPETITION: Repeat patterns/colors to create unity
6. ALIGNMENT: Invisible grid lines that everything snaps to
7. DEPTH: Overlap, shadow, blur, size variation create layers
8. BALANCE: Asymmetric balance > perfect symmetry (more dynamic)
```

---

## OUTPUT RULES

```
1. COMPLETE — Every visual runs as-is in a browser. No placeholder shapes.
2. SIZED — Set explicit dimensions. Include responsive handling if HTML.
3. RETINA — Account for devicePixelRatio in Canvas. Use viewBox in SVG.
4. THEMED — Use CSS variables for colors. Easy to swap palettes.
5. PERFORMANT — RequestAnimationFrame for animation. No setInterval.
6. INTERACTIVE — Add hover/click states where meaningful.
7. ACCESSIBLE — Title and desc in SVG. Alt text for canvas.
```
