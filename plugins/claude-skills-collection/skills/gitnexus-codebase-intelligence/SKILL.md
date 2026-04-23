---
name: gitnexus-codebase-intelligence
description: GitNexus — codebase intelligence platform that transforms repos into knowledge graphs for AI agents. 7 MCP tools: symbol discovery (BM25+semantic), impact radius analysis, 360° symbol context, git-diff impact mapping, multi-file coordinated renaming,
kind: reference
category: dev/architecture
status: active
tags: [architecture, codebase, dev, gitnexus, intelligence, mcp]
related_skills: [agentic-storage, build-your-own-x]
---

# gitnexus-codebase-intelligence

USE FOR:
  - "understand codebase impact before editing"
  - "find all callers / dependents of a symbol"
  - "safe multi-file renaming"
  - "git diff impact analysis"
  - "MCP tool for codebase architecture understanding"
  - "knowledge graph of code structure"
  - "AI agent codebase context"
tags: [MCP, codebase, knowledge-graph, Tree-sitter, symbol-search, impact-analysis, Claude-Code, Cursor, Cypher]
kind: tool
category: pro-code-architecture

---

## What Is GitNexus?

Codebase intelligence platform — transforms repos into knowledge graphs for AI agents.
- Repo: https://github.com/abhigyanpatwari/GitNexus
- Web: gitnexus.vercel.app (no install)
- Integrations: **Claude Code**, Cursor, Windsurf, any MCP-compatible editor
- Privacy: **100% local** — code never leaves your machine

> "Building a nervous system for agent context"

---

## Core Problem Solved

Traditional AI assistants don't know when edits break downstream dependencies.
GitNexus precomputes architectural intelligence at index time → fast, accurate impact analysis at query time.

---

## 7 MCP Tools

| Tool | What It Does |
|------|-------------|
| `symbol_search` | BM25 + semantic hybrid search across codebase |
| `symbol_context` | 360° view: incoming + outgoing relationships for any symbol |
| `impact_radius` | All code that depends on a given symbol |
| `git_diff_impact` | Map git diff → which symbols are affected + their dependents |
| `multi_file_rename` | Coordinated safe rename across all references |
| `graph_query` | Raw Cypher queries on the knowledge graph |
| `discover_symbols` | List all symbols by type (functions, classes, methods) |

---

## Indexing Pipeline (6 Phases)

```
1. Structural mapping   → directory tree, file relationships
2. AST parsing          → Tree-sitter extracts symbols per language
3. Import/call resolve  → link usages to definitions
4. Community cluster    → group related modules
5. Execution flow trace → call chains, data flow paths
6. Hybrid search index  → BM25 + vector embeddings
```

---

## Installation & Setup

```bash
# Index a repository
npx gitnexus analyze

# Configure MCP for your editor (one-time, multi-project)
npx gitnexus setup
# → adds GitNexus MCP server to Claude Code / Cursor / Windsurf config
```

**Web UI** (no install):
```
https://gitnexus.vercel.app
# Upload or link repo → explore in browser
```

---

## Claude Code Integration

After `npx gitnexus setup`, Claude Code gets access to all 7 MCP tools:

```
# In Claude Code session:
> "What calls the processOrder function?"
→ Claude uses symbol_context MCP tool → instant impact map

> "I'm about to rename UserService — what breaks?"
→ Claude uses impact_radius → lists all 47 dependent symbols

> "Show me what this git diff affects"
→ Claude uses git_diff_impact → maps changed lines to affected call chains
```

---

## Supported Languages

| Language | Imports | Types | Frameworks |
|----------|---------|-------|------------|
| TypeScript / JS | ✓ | ✓ | React, Next.js |
| Python | ✓ | ✓ | Django, FastAPI |
| Java | ✓ | ✓ | Spring |
| Go | ✓ | ✓ | — |
| Rust | ✓ | ✓ | — |
| C# | ✓ | ✓ | .NET |
| PHP | ✓ | — | Laravel |
| + 6 more | varies | varies | — |

---

## Example: Impact Radius Query

```cypher
-- Raw Cypher query via graph_query tool
MATCH (s:Symbol {name: "UserService"})<-[:CALLS|IMPORTS*1..3]-(dep:Symbol)
RETURN dep.name, dep.file, dep.line
ORDER BY dep.file
```

Returns every symbol within 3 hops that depends on `UserService`.



---
# KNOWLEDGE INJECTION: OpenCV
# Source: https://github.com/opencv/opencv
# Routed to: development.md
# Date: 2026-03-18

# SKILL: opencv
name: opencv
description: >
  OpenCV - Open Source Computer Vision Library. 86k stars, 14 modules.
  imgproc (filtering/contours/warp), dnn (YOLO/ONNX inference), features2d
  (SIFT/ORB/AKAZE matching), objdetect (Haar/HOG/QR), calib3d, tracking (KCF/CSRT).
  pip install opencv-contrib-python. C++ and Python.
USE FOR:
  - image processing pipeline
  - contour detection and perspective warp
  - YOLO object detection with OpenCV dnn
  - feature matching SIFT ORB AKAZE
  - face detection Haar cascade
  - camera calibration undistort
  - object tracking KCF CSRT
  - chess board detection
  - color segmentation HSV mask
  - background subtraction optical flow
tags: [OpenCV, computer-vision, image-processing, DNN, YOLO, SIFT, ORB, contours, tracking, Python, C++]
kind: library
category: programmatic-drawing

---

## What Is OpenCV?

Open Source Computer Vision Library.
- Repo: https://github.com/opencv/opencv
- Stars: 86.6k | Forks: 56.6k | Contributors: 1,775+
- Languages: C++ (87%) with Python, Java, JS bindings
- Docs: https://docs.opencv.org/4.x/

---

## Installation

```bash
pip install opencv-contrib-python        # recommended (includes SIFT, tracking)
pip install opencv-contrib-python-headless  # no GUI (servers)
```

```python
import cv2
print(cv2.__version__)   # e.g. 4.9.0
```

---

## Module Map

| Module | Key Functions |
|--------|--------------|
| core | Mat, imread, imwrite, cvtColor |
| imgproc | GaussianBlur, Canny, threshold, findContours, warpPerspective |
| features2d | SIFT, ORB, AKAZE, BFMatcher, FLANN |
| objdetect | CascadeClassifier, QRCodeDetector |
| dnn | readNetFromONNX, blobFromImage, forward |
| video | BackgroundSubtractor, calcOpticalFlow |
| calib3d | calibrateCamera, undistort, findHomography |
| tracking | TrackerKCF, TrackerCSRT, TrackerMOSSE |
| ml | SVM, KMeans |
| photo | inpaint, fastNlMeansDenoising |

---

## Core: Load, Convert, Save

```python
import cv2, numpy as np

img  = cv2.imread("image.jpg")               # BGR uint8
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # for matplotlib
h, w, c = img.shape
roi  = img[y1:y2, x1:x2]                     # crop
cv2.imwrite("out.jpg", img)
cv2.imshow("win", img); cv2.waitKey(0)
```

---

## imgproc: Filters & Edges

```python
blur   = cv2.GaussianBlur(gray, (5,5), 0)
median = cv2.medianBlur(gray, 5)               # salt-and-pepper
bilat  = cv2.bilateralFilter(img, 9, 75, 75)   # edge-preserving

edges  = cv2.Canny(blur, 50, 150)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN,  kernel)  # remove noise
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)  # fill holes
```

---

## imgproc: Thresholding

```python
_, binary  = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
_, otsu    = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
adaptive   = cv2.adaptiveThreshold(gray, 255,
               cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Color range mask
lower = np.array([100, 50, 50])
upper = np.array([130, 255, 255])
mask  = cv2.inRange(hsv, lower, upper)
```

---

## imgproc: Contours

```python
cnts, hier = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in cnts:
    area = cv2.contourArea(cnt)
    if area < 500: continue

    peri   = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
    x,y,w,h = cv2.boundingRect(cnt)

    M  = cv2.moments(cnt)
    cx = int(M["m10"] / M["m00"])   # centroid
    cy = int(M["m01"] / M["m00"])

    cv2.drawContours(img, [cnt], 0, (0,255,0), 2)

# Shape by vertex count
n = len(approx)
if   n == 3: shape = "triangle"
elif n == 4: shape = "quad/rect"
elif n == 5: shape = "pentagon"
else:        shape = "circle"
```

---

## imgproc: Perspective Warp

```python
src = np.float32([[tl_x,tl_y],[tr_x,tr_y],[bl_x,bl_y],[br_x,br_y]])
dst = np.float32([[0,0],[W,0],[0,H],[W,H]])
M      = cv2.getPerspectiveTransform(src, dst)
warped = cv2.warpPerspective(img, M, (W, H))
```

---

## features2d: SIFT / ORB Matching

```python
sift  = cv2.SIFT_create()
orb   = cv2.ORB_create(nfeatures=1500)

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

bf      = cv2.BFMatcher(cv2.NORM_L2)           # L2 for SIFT
# bf   = cv2.BFMatcher(cv2.NORM_HAMMING)        # Hamming for ORB/AKAZE
matches = bf.knnMatch(des1, des2, k=2)
good    = [m for m,n in matches if m.distance < 0.75*n.distance]

if len(good) > 10:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
```

| Detector | Speed | Scale inv | Notes |
|----------|-------|-----------|-------|
| SIFT | Slow | Yes | Most accurate |
| ORB | Fast | No | Free, real-time |
| AKAZE | Medium | Yes | Balanced |
| FAST | Very fast | No | Corners only |

---

## objdetect: Face & QR

```python
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

qr = cv2.QRCodeDetector()
data, pts, _ = qr.detectAndDecode(img)
```

---

## dnn: YOLO / ONNX Inference

```python
net = cv2.dnn.readNetFromONNX("yolov8n.onnx")
# Optional GPU: net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)

blob = cv2.dnn.blobFromImage(img, 1/255, (640,640), swapRB=True)
net.setInput(blob)
outputs = net.forward(net.getUnconnectedOutLayersNames())

for det in outputs[0]:
    scores     = det[5:]
    class_id   = np.argmax(scores)
    confidence = scores[class_id]
    if confidence > 0.5:
        cx,cy,bw,bh = (det[:4] * np.array([W,H,W,H])).astype(int)
        cv2.rectangle(img, (cx-bw//2, cy-bh//2), (cx+bw//2, cy+bh//2), (0,255,0), 2)
```

Supported: ONNX | TensorFlow .pb | Caffe | Darknet YOLO | OpenVINO IR

---

## tracking: Object Trackers

```python
tracker = cv2.TrackerCSRT_create()    # best accuracy
# tracker = cv2.TrackerKCF_create()   # balanced
# tracker = cv2.TrackerMOSSE_create() # fastest

ok = tracker.init(frame, (x, y, w, h))
while cap.isOpened():
    ok, frame = cap.read()
    ok, bbox  = tracker.update(frame)
    if ok:
        x,y,w,h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
```

---

## calib3d: Camera Calibration

```python
objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

objpts, imgpts = [], []
for img in calib_images:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (9,6))
    if ret:
        objpts.append(objp)
        imgpts.append(cv2.cornerSubPix(gray, corners, (11,11), (-1,-1),
            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)))

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpts, imgpts, gray.shape[::-1], None, None)
undist = cv2.undistort(frame, mtx, dist)
```

---

## video: Background Subtraction & Optical Flow

```python
# Background subtraction
fgbg  = cv2.createBackgroundSubtractorMOG2(history=500, detectShadows=True)
fgmask = fgbg.apply(frame)

# Sparse optical flow (Lucas-Kanade)
p0     = cv2.goodFeaturesToTrack(prev_gray, 100, 0.3, 7)
p1, st, _ = cv2.calcOpticalFlowPyrLK(prev_gray, gray, p0, None)
good_new = p1[st==1]

# Dense optical flow
flow   = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
```

---

## Drawing Functions

```python
cv2.line(img, (x1,y1), (x2,y2), (B,G,R), thickness)
cv2.rectangle(img, (x1,y1), (x2,y2), color, thickness)   # -1 = filled
cv2.circle(img, (cx,cy), radius, color, thickness)
cv2.putText(img, "text", (x,y), cv2.FONT_HERSHEY_SIMPLEX, scale, color, thickness)
cv2.polylines(img, [pts], isClosed=True, color, thickness)
cv2.arrowedLine(img, pt1, pt2, color, thickness)
```

---

## Chess Board Pipeline (project context)

```python
# Used in chess/ desktop app (board_detector.py)
gray    = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
blur    = cv2.GaussianBlur(gray, (5,5), 0)
edges   = cv2.Canny(blur, 50, 150)
cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
board   = max(cnts, key=cv2.contourArea)   # largest contour = board
approx  = cv2.approxPolyDP(board, 0.02*cv2.arcLength(board,True), True)
# approx should have 4 points for the board corners
warped  = cv2.warpPerspective(screen, M, (512, 512))
# Then split warped into 8x8 grid -> classify each square
```


---
# KNOWLEDGE INJECTION: Orange3
# Source: https://github.com/biolab/orange3
# Routed to: development.md
# Date: 2026-03-18

# SKILL: orange3-data-mining
name: orange3-data-mining
description: >
  Orange3 - open-source visual data mining and ML platform by Univ. of Ljubljana.
  No-code canvas-based workflow: connect widgets for data loading, preprocessing,
  visualization, classification, clustering, regression. Add-ons: text, time series,
  bioinformatics, image analytics, geo. pip/conda/winget install.
USE FOR:
  - visual ML workflow no-code
  - data mining and visualization
  - interactive scatter plot histogram heatmap
  - decision tree random forest clustering
  - exploratory data analysis
tags: [Orange3, visual-ML, data-mining, no-code, clustering, classification, regression]
kind: tool
category: pro-code-architecture

---

## What Is Orange3?

Visual data mining and ML toolbox — no programming required.
- Repo: https://github.com/biolab/orange3
- By: University of Ljubljana Biolab
- Approach: Canvas-based drag-and-drop widget workflow

### Installation
```bash
winget install --id UniversityofLjubljana.Orange
conda install orange3
pip install orange3   # requires PyQt6 first
```

### Widget Categories
- **Data**: File, SQL, URL, Data Table, Select Rows, Feature Constructor
- **Visualize**: Scatter Plot, Box Plot, Distributions, Heatmap, Mosaic
- **Model**: Decision Tree, Random Forest, SVM, Naive Bayes, Neural Network, Logistic Regression
- **Evaluate**: Test & Score, Confusion Matrix, ROC, Calibration Plot
- **Unsupervised**: K-Means, Hierarchical Clustering, PCA, t-SNE, DBSCAN
- **Text**: Corpus, Preprocess Text, Bag of Words, Topic Modelling
- **Time Series**: As Timeseries, Moving Transform, Seasonal Adjustment

### Workflow Pattern
```
File → Preprocess → Select Features
                         → Train/Test Split → Random Forest → Evaluate
                         → PCA → Scatter Plot (colored by class)
```


---
# KNOWLEDGE INJECTION: xonsh
# Source: https://github.com/xonsh/xonsh
# Routed to: development.md
# Date: 2026-03-18

# SKILL: xonsh-python-shell
name: xonsh-python-shell
description: >
  xonsh - Python-powered cross-platform shell. Superset of Python 3: mix shell commands
  and Python code in the same session. Direct manipulation of command outputs as Python objects.
  Extension system (xontribs/plugins). AI-friendly. Used by conda, mamba, Snakemake, Jupyter.
  pip install xonsh.
USE FOR:
  - Python + shell hybrid scripting
  - manipulate command output as Python objects
  - automate shell tasks with Python logic
  - cross-platform shell scripting
  - conda mamba workflow automation
tags: [xonsh, Python-shell, hybrid, cross-platform, scripting, automation, xontribs]
kind: tool
category: pro-code-architecture

---

## What Is xonsh?

Python-powered shell — superset of Python 3, cross-platform, AI-friendly.
- Repo: https://github.com/xonsh/xonsh

### Install
```bash
pip install xonsh
# or via conda:
conda install -c conda-forge xonsh
```

### Syntax Examples
```python
# Standard shell commands
cd $HOME
cat /etc/passwd | grep root

# Python variables in commands
name = "snail"
echo @(name) > /tmp/@(name)

# Python expressions
var = "hello".upper()
echo @(var)

# Command output as Python object
result = $(ls -la).split("\n")
print(len(result))

# Mixed pipeline
len($(curl -L https://xon.sh))

# Subprocess mode with Python control flow
for f in $(find . -name "*.py").split():
    print(f)
```

### xontribs (Extensions)
```bash
xpip install xontrib-vox          # virtual environment manager
xpip install xontrib-prompt-ret   # return code in prompt
xpip install xontrib-autojump     # autojump integration
```

### Use Cases
- conda/mamba package management scripts
- Snakemake bioinformatics workflows
- Jupyter-based interactive computing
- DevOps automation with Python logic
- Data pipeline scripting


---
# KNOWLEDGE INJECTION: Orange3
# Source: https://github.com/biolab/orange3
# Routed to: development.md
# Date: 2026-03-18

# SKILL: orange3-data-mining
name: orange3-data-mining
description: >
  Orange3 - open-source visual data mining and ML platform by Univ. of Ljubljana.
  No-code canvas-based workflow: connect widgets for data loading, preprocessing,
  visualization, classification, clustering, regression. Add-ons: text, time series,
  bioinformatics, image analytics, geo. pip/conda/winget install.
USE FOR:
  - visual ML workflow no-code
  - data mining and visualization
  - interactive scatter plot histogram heatmap
  - decision tree random forest clustering
  - exploratory data analysis
tags: [Orange3, visual-ML, data-mining, no-code, clustering, classification, regression]
kind: tool
category: pro-code-architecture

---

## What Is Orange3?

Visual data mining and ML toolbox — no programming required.
- Repo: https://github.com/biolab/orange3
- By: University of Ljubljana Biolab
- Approach: Canvas-based drag-and-drop widget workflow

### Installation
```bash
winget install --id UniversityofLjubljana.Orange
conda install orange3
pip install orange3   # requires PyQt6 first
```

### Widget Categories
- **Data**: File, SQL, URL, Data Table, Select Rows, Feature Constructor
- **Visualize**: Scatter Plot, Box Plot, Distributions, Heatmap, Mosaic
- **Model**: Decision Tree, Random Forest, SVM, Naive Bayes, Neural Network, Logistic Regression
- **Evaluate**: Test & Score, Confusion Matrix, ROC, Calibration Plot
- **Unsupervised**: K-Means, Hierarchical Clustering, PCA, t-SNE, DBSCAN
- **Text**: Corpus, Preprocess Text, Bag of Words, Topic Modelling
- **Time Series**: As Timeseries, Moving Transform, Seasonal Adjustment

### Workflow Pattern
```
File → Preprocess → Select Features
                         → Train/Test Split → Random Forest → Evaluate
                         → PCA → Scatter Plot (colored by class)
```


---
# KNOWLEDGE INJECTION: OpenCV
# Source: https://github.com/opencv/opencv
# Routed to: development.md
# Date: 2026-03-18

# SKILL: opencv
name: opencv
description: >
  OpenCV - Open Source Computer Vision Library. 86k stars, 14 modules.
  imgproc (filtering/contours/warp), dnn (YOLO/ONNX inference), features2d
  (SIFT/ORB/AKAZE matching), objdetect (Haar/HOG/QR), calib3d, tracking (KCF/CSRT).
  pip install opencv-contrib-python. C++ and Python.
USE FOR:
  - image processing pipeline
  - contour detection and perspective warp
  - YOLO object detection with OpenCV dnn
  - feature matching SIFT ORB AKAZE
  - face detection Haar cascade
  - camera calibration undistort
  - object tracking KCF CSRT
  - chess board detection
  - color segmentation HSV mask
  - background subtraction optical flow
tags: [OpenCV, computer-vision, image-processing, DNN, YOLO, SIFT, ORB, contours, tracking, Python, C++]
kind: library
category: programmatic-drawing

---

## What Is OpenCV?

Open Source Computer Vision Library.
- Repo: https://github.com/opencv/opencv
- Stars: 86.6k | Forks: 56.6k | Contributors: 1,775+
- Languages: C++ (87%) with Python, Java, JS bindings
- Docs: https://docs.opencv.org/4.x/

---

## Installation

```bash
pip install opencv-contrib-python        # recommended (includes SIFT, tracking)
pip install opencv-contrib-python-headless  # no GUI (servers)
```

```python
import cv2
print(cv2.__version__)   # e.g. 4.9.0
```

---

## Module Map

| Module | Key Functions |
|--------|--------------|
| core | Mat, imread, imwrite, cvtColor |
| imgproc | GaussianBlur, Canny, threshold, findContours, warpPerspective |
| features2d | SIFT, ORB, AKAZE, BFMatcher, FLANN |
| objdetect | CascadeClassifier, QRCodeDetector |
| dnn | readNetFromONNX, blobFromImage, forward |
| video | BackgroundSubtractor, calcOpticalFlow |
| calib3d | calibrateCamera, undistort, findHomography |
| tracking | TrackerKCF, TrackerCSRT, TrackerMOSSE |
| ml | SVM, KMeans |
| photo | inpaint, fastNlMeansDenoising |

---

## Core: Load, Convert, Save

```python
import cv2, numpy as np

img  = cv2.imread("image.jpg")               # BGR uint8
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # for matplotlib
h, w, c = img.shape
roi  = img[y1:y2, x1:x2]                     # crop
cv2.imwrite("out.jpg", img)
cv2.imshow("win", img); cv2.waitKey(0)
```

---

## imgproc: Filters & Edges

```python
blur   = cv2.GaussianBlur(gray, (5,5), 0)
median = cv2.medianBlur(gray, 5)               # salt-and-pepper
bilat  = cv2.bilateralFilter(img, 9, 75, 75)   # edge-preserving

edges  = cv2.Canny(blur, 50, 150)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN,  kernel)  # remove noise
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)  # fill holes
```

---

## imgproc: Thresholding

```python
_, binary  = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
_, otsu    = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
adaptive   = cv2.adaptiveThreshold(gray, 255,
               cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Color range mask
lower = np.array([100, 50, 50])
upper = np.array([130, 255, 255])
mask  = cv2.inRange(hsv, lower, upper)
```

---

## imgproc: Contours

```python
cnts, hier = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in cnts:
    area = cv2.contourArea(cnt)
    if area < 500: continue

    peri   = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
    x,y,w,h = cv2.boundingRect(cnt)

    M  = cv2.moments(cnt)
    cx = int(M["m10"] / M["m00"])   # centroid
    cy = int(M["m01"] / M["m00"])

    cv2.drawContours(img, [cnt], 0, (0,255,0), 2)

# Shape by vertex count
n = len(approx)
if   n == 3: shape = "triangle"
elif n == 4: shape = "quad/rect"
elif n == 5: shape = "pentagon"
else:        shape = "circle"
```

---

## imgproc: Perspective Warp

```python
src = np.float32([[tl_x,tl_y],[tr_x,tr_y],[bl_x,bl_y],[br_x,br_y]])
dst = np.float32([[0,0],[W,0],[0,H],[W,H]])
M      = cv2.getPerspectiveTransform(src, dst)
warped = cv2.warpPerspective(img, M, (W, H))
```

---

## features2d: SIFT / ORB Matching

```python
sift  = cv2.SIFT_create()
orb   = cv2.ORB_create(nfeatures=1500)

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

bf      = cv2.BFMatcher(cv2.NORM_L2)           # L2 for SIFT
# bf   = cv2.BFMatcher(cv2.NORM_HAMMING)        # Hamming for ORB/AKAZE
matches = bf.knnMatch(des1, des2, k=2)
good    = [m for m,n in matches if m.distance < 0.75*n.distance]

if len(good) > 10:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
```

| Detector | Speed | Scale inv | Notes |
|----------|-------|-----------|-------|
| SIFT | Slow | Yes | Most accurate |
| ORB | Fast | No | Free, real-time |
| AKAZE | Medium | Yes | Balanced |
| FAST | Very fast | No | Corners only |

---

## objdetect: Face & QR

```python
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

qr = cv2.QRCodeDetector()
data, pts, _ = qr.detectAndDecode(img)
```

---

## dnn: YOLO / ONNX Inference

```python
net = cv2.dnn.readNetFromONNX("yolov8n.onnx")
# Optional GPU: net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)

blob = cv2.dnn.blobFromImage(img, 1/255, (640,640), swapRB=True)
net.setInput(blob)
outputs = net.forward(net.getUnconnectedOutLayersNames())

for det in outputs[0]:
    scores     = det[5:]
    class_id   = np.argmax(scores)
    confidence = scores[class_id]
    if confidence > 0.5:
        cx,cy,bw,bh = (det[:4] * np.array([W,H,W,H])).astype(int)
        cv2.rectangle(img, (cx-bw//2, cy-bh//2), (cx+bw//2, cy+bh//2), (0,255,0), 2)
```

Supported: ONNX | TensorFlow .pb | Caffe | Darknet YOLO | OpenVINO IR

---

## tracking: Object Trackers

```python
tracker = cv2.TrackerCSRT_create()    # best accuracy
# tracker = cv2.TrackerKCF_create()   # balanced
# tracker = cv2.TrackerMOSSE_create() # fastest

ok = tracker.init(frame, (x, y, w, h))
while cap.isOpened():
    ok, frame = cap.read()
    ok, bbox  = tracker.update(frame)
    if ok:
        x,y,w,h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
```

---

## calib3d: Camera Calibration

```python
objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

objpts, imgpts = [], []
for img in calib_images:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (9,6))
    if ret:
        objpts.append(objp)
        imgpts.append(cv2.cornerSubPix(gray, corners, (11,11), (-1,-1),
            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)))

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpts, imgpts, gray.shape[::-1], None, None)
undist = cv2.undistort(frame, mtx, dist)
```

---

## video: Background Subtraction & Optical Flow

```python
# Background subtraction
fgbg  = cv2.createBackgroundSubtractorMOG2(history=500, detectShadows=True)
fgmask = fgbg.apply(frame)

# Sparse optical flow (Lucas-Kanade)
p0     = cv2.goodFeaturesToTrack(prev_gray, 100, 0.3, 7)
p1, st, _ = cv2.calcOpticalFlowPyrLK(prev_gray, gray, p0, None)
good_new = p1[st==1]

# Dense optical flow
flow   = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
```

---

## Drawing Functions

```python
cv2.line(img, (x1,y1), (x2,y2), (B,G,R), thickness)
cv2.rectangle(img, (x1,y1), (x2,y2), color, thickness)   # -1 = filled
cv2.circle(img, (cx,cy), radius, color, thickness)
cv2.putText(img, "text", (x,y), cv2.FONT_HERSHEY_SIMPLEX, scale, color, thickness)
cv2.polylines(img, [pts], isClosed=True, color, thickness)
cv2.arrowedLine(img, pt1, pt2, color, thickness)
```

---

## Chess Board Pipeline (project context)

```python
# Used in chess/ desktop app (board_detector.py)
gray    = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
blur    = cv2.GaussianBlur(gray, (5,5), 0)
edges   = cv2.Canny(blur, 50, 150)
cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
board   = max(cnts, key=cv2.contourArea)   # largest contour = board
approx  = cv2.approxPolyDP(board, 0.02*cv2.arcLength(board,True), True)
# approx should have 4 points for the board corners
warped  = cv2.warpPerspective(screen, M, (512, 512))
# Then split warped into 8x8 grid -> classify each square
```


---
# KNOWLEDGE INJECTION: xonsh
# Source: https://github.com/xonsh/xonsh
# Routed to: development.md
# Date: 2026-03-18

# SKILL: xonsh-python-shell
name: xonsh-python-shell
description: >
  xonsh - Python-powered cross-platform shell. Superset of Python 3: mix shell commands
  and Python code in the same session. Direct manipulation of command outputs as Python objects.
  Extension system (xontribs/plugins). AI-friendly. Used by conda, mamba, Snakemake, Jupyter.
  pip install xonsh.
USE FOR:
  - Python + shell hybrid scripting
  - manipulate command output as Python objects
  - automate shell tasks with Python logic
  - cross-platform shell scripting
  - conda mamba workflow automation
tags: [xonsh, Python-shell, hybrid, cross-platform, scripting, automation, xontribs]
kind: tool
category: pro-code-architecture

---

## What Is xonsh?

Python-powered shell — superset of Python 3, cross-platform, AI-friendly.
- Repo: https://github.com/xonsh/xonsh

### Install
```bash
pip install xonsh
# or via conda:
conda install -c conda-forge xonsh
```

### Syntax Examples
```python
# Standard shell commands
cd $HOME
cat /etc/passwd | grep root

# Python variables in commands
name = "snail"
echo @(name) > /tmp/@(name)

# Python expressions
var = "hello".upper()
echo @(var)

# Command output as Python object
result = $(ls -la).split("\n")
print(len(result))

# Mixed pipeline
len($(curl -L https://xon.sh))

# Subprocess mode with Python control flow
for f in $(find . -name "*.py").split():
    print(f)
```

### xontribs (Extensions)
```bash
xpip install xontrib-vox          # virtual environment manager
xpip install xontrib-prompt-ret   # return code in prompt
xpip install xontrib-autojump     # autojump integration
```

### Use Cases
- conda/mamba package management scripts
- Snakemake bioinformatics workflows
- Jupyter-based interactive computing
- DevOps automation with Python logic
- Data pipeline scripting

