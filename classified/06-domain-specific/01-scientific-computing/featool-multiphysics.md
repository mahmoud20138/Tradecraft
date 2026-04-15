---
name: featool-multiphysics
description: FEATool Multiphysics — physics simulation platform for FEA/CFD modeling. Covers finite element analysis, computational fluid dynamics, heat transfer, structural mechanics, electromagnetics, and custom PDEs. Integrates with OpenFOAM, FEniCS, SU2. Scri
kind: tool
category: domain/scientific
status: active
tags: [domain, featool, multiphysics, scientific]
---

# featool-multiphysics

USE FOR:

- "simulate heat transfer / fluid flow / structural analysis"
- "finite element analysis (FEA) setup and workflow"
- "CFD modeling with OpenFOAM or FEniCS"
- "multiphysics coupling (thermal + structural + fluid)"
- "engineering simulation for research or education"
- "custom PDE solver setup"
- "parametric simulation and post-processing"
tags: [FEA, CFD, simulation, multiphysics, engineering, physics, OpenFOAM, FEniCS, SU2, heat-transfer, structural-mechanics]
kind: tool
category: scientific-computing

---

## What Is FEATool Multiphysics?

FEATool (Finite Element Analysis Toolbox) is an integrated simulation platform
for modeling coupled physics phenomena, continuum mechanics, and engineering problems.
Tagline: **"Physics Simulation Made Easy"**

- GitHub: [https://github.com/precise-simulation/featool-multiphysics](https://github.com/precise-simulation/featool-multiphysics)
- Docs: [https://featool.com/doc](https://featool.com/doc)
- Latest: v1.18 (February 2026) · 428 GitHub stars

---

## Supported Physics Domains

| Domain | Examples |
| -------- | --------- |
| Heat & Mass Transfer | conduction, convection, diffusion |
| Fluid Dynamics (CFD) | laminar/turbulent flow, Navier-Stokes |
| Structural Mechanics | stress, strain, deformation |
| Electromagnetics | electrostatics, magnetostatics |
| Custom PDEs | user-defined equations in natural math notation |

---

## Solver Integrations

| Solver | Type | Notes |
| -------- | ------ | ------- |
| **OpenFOAM** | CFD | Open-source, industry-grade CFD |
| **FEniCS** | FEA/Multiphysics | Python-based FEM framework |
| **SU2** | CFD | Aerospace-grade solver |
| Built-in | General FEM | Default solver, no external deps |

---

## Standard Modeling Workflow (6 Steps)

```
1. Geometry   → define 1D/2D/3D shapes (CAD primitives or import)
2. Grid       → automatic mesh generation (structured/unstructured)
3. Equation   → select physics mode or enter custom PDEs
4. Boundary   → assign boundary conditions (Dirichlet, Neumann, Robin)
5. Solve      → run solver (built-in or external: OpenFOAM/FEniCS/SU2)
6. Post       → visualize results (ParaView, Plotly web plots, export)
```

---

## Installation

### Stand-alone (Windows/Linux/macOS)

```bash
# Download installer from GitHub Releases
# https://github.com/precise-simulation/featool-multiphysics/releases
# Minimum: 64-bit OS, 4 GB RAM, up to 10 GB disk
```

### MATLAB Toolbox

```matlab
% Install .mlappinstall via MATLAB APPS toolbar
% Then launch:
featool
```

### Python (FEniCS integration)

```bash
# FEniCS must be installed separately
pip install fenics-dolfinx  # or via conda
```

---

## Python API Scripting

FEATool supports programmable workflows via Python scripts:

```python
import featool

# Load a model
model = featool.load('heat_exchanger.fea')

# Run solver
model.solve()

# Extract results
T = model.get_field('T')  # Temperature field
print(f"Max temperature: {max(T):.2f} K")

# Export to ParaView
model.export('results.vtk')
```

---

## MATLAB API Scripting

```matlab
% Create new model
fea = feamodel();
fea.sdim = {'x', 'y'};         % 2D problem

% Define geometry
fea.geom = gobj_rectangle(0, 1, 0, 1);

% Set physics (heat equation)
fea = addphys(fea, @heattransfer);
fea.phys.ht.bdr.coef{2,end} = 100;  % Boundary temp = 100°C

% Mesh and solve
fea = parsephys(fea);
fea = parsegeom(fea);
fea = meshgeo(fea, 'hmax', 0.05);
fea = solvetime(fea);

% Post-process
postplot(fea, 'surfexpr', 'T');
```

---

## Custom PDE Definition

Enter equations in natural notation:

```
∂u/∂t - ∇·(k∇u) = f

# In FEATool syntax:
# Equation: ut - k*(uxx + uyy) = f
# Where k = thermal conductivity coefficient
```

---

## Export Formats

| Format | Use Case |
| -------- | --------- |
| `.fea` binary | Save/reload FEATool models |
| MATLAB `.m` script | Reproducible parametric studies |
| Python/FEniCS `.py` | Open-source solver pipeline |
| ParaView `.vtk/.vtp` | Advanced 3D visualization |
| Plotly HTML | Interactive web plots |

---

## Use Case Examples

### Heat Exchanger Analysis

```matlab
% Load built-in example
fea = ex_heattransfer1();
fea = solvetime(fea);
postplot(fea, 'surfexpr', 'T', 'title', 'Temperature Distribution')
```

### Fluid Flow (Navier-Stokes)

```matlab
fea = feamodel();
fea = addphys(fea, @navierstokes);
% Set Reynolds number, inlet velocity, solve
fea = solvetime(fea);
postplot(fea, 'surfexpr', 'sqrt(u^2+v^2)', 'title', 'Velocity magnitude')
```

### Structural Mechanics

```matlab
fea = feamodel();
fea = addphys(fea, @linearelasticity);
% Define material (E, nu), boundary loads
fea = solvetime(fea);
postplot(fea, 'surfexpr', 'von_mises', 'title', 'Von Mises Stress')
```

---

## When to Use Which Solver

| Scenario | Recommended Solver |
| ---------- | -------------------- |
| Simple heat/structural | Built-in FEM |
| Complex CFD / turbulence | OpenFOAM |
| Coupled multiphysics research | FEniCS |
| Aerodynamics / aerospace CFD | SU2 |
| Education / quick prototyping | Built-in GUI |

---

## Key Tips

- Use **model examples** (File → Model Examples) to bootstrap any physics type
- **Parametric expressions** allow sweeping parameters without re-building geometry
- For large 3D problems, export to OpenFOAM for HPC cluster execution
- Results can be exported to **Plotly** for shareable interactive web reports
- FEniCS export generates standalone Python scripts — useful for CI/automation

---
