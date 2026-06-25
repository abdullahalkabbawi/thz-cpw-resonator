# Lumerical FDTD Simulation Dimensions
# CPW Buried Trench Resonator — MSc Project
# Last updated: 2026-06-25
# Source: User screenshots from Lumerical FDTD GUI

---

## 1. Substrate (Rectangle object)
| Parameter      | Value                  |
|----------------|------------------------|
| x              | 0 µm                   |
| x min          | -2000 µm               |
| x max          | +2000 µm               |
| x span         | 4000 µm                |
| y              | 0 µm                   |
| y min          | -1000 µm               |
| y max          | +1000 µm               |
| y span         | 2000 µm                |
| z              | -250 µm                |
| z min          | -500 µm                |
| z max          | 0 µm                   |
| z span         | 500 µm                 |
| Top surface    | z = 0 (CPW metal plane)|
| Material       | Si hires - THz (High-Resistivity Silicon, from Lumerical material database) |
| Mesh order     | 2                      |
| Rotations      | None (all axes = none) |
| Render type    | Detailed, alpha = 1    |
| Relative coords| Yes                    |

NOTE: Si hires - THz has permittivity ε ≈ 11.7, refractive index n ≈ 3.42.
This significantly slows the guided mode (lower phase velocity) and shifts
the resonance frequency downward compared to an air substrate.

---

## 2. CPW Buried Trench (trench_geometry.lsf — user properties panel)
| Parameter       | Symbol        | Value  | Unit |
|-----------------|---------------|--------|------|
| Signal width     | s             | 10     | µm   |
| Slot width       | w             | 7.5    | µm   |
| Coupling gap     | C_g           | 3      | µm   |
| Cavity length    | cav_L         | 80     | µm   |
| Trench width (y) | L_burried     | 5      | µm   |
| Ground offset    | y_height      | 5      | µm   |
| Trench depth (z) | h_burried     | 50     | µm   |
| Cavity x-offset  | x_offset      | -200   | µm   |
| Conductor        | material      | PEC (Perfect Electrical Conductor) |  |
| Trench fill      | air           | etch   |      |

Cavity spans from x = (x_offset - cav_L/2) = -240 µm to (x_offset + cav_L/2) = -160 µm.
Left gap:  x = -243 µm to -240 µm (width = C_g = 3 µm)
Right gap: x = -160 µm to -157 µm (width = C_g = 3 µm)

---

## 3. FDTD Simulation Region
| Parameter             | Value        |
|-----------------------|--------------|
| Dimension             | 3D           |
| Simulation time       | 100,000 fs (100 ps) |
| Temperature           | 300 K        |
| Background material   | Object defined dielectric |
| Background index      | 1            |
| x centre              | -150 µm      |
| x min                 | -1000 µm     |
| x max                 | +700 µm      |
| x span                | 1700 µm      |
| y centre              | 0 µm         |
| y min                 | -200 µm      |
| y max                 | +200 µm      |
| y span                | 400 µm       |
| z centre              | -200 µm      |
| z min                 | -500 µm      |
| z max                 | +100 µm      |
| z span                | 600 µm       |

---

## 4. Port 1
| Parameter  | Value     |
|------------|-----------|
| x          | -500 µm   |
| x span     | 0         |
| y          | 0 µm      |
| y min      | -125 µm   |
| y max      | +125 µm   |
| y span     | 250 µm    |
| z centre   | -55 µm    |
| z min      | -210 µm   |
| z max      | +100 µm   |
| z span     | 310 µm    |

---

## 5. Port 2
| Parameter  | Value     |
|------------|-----------|
| x          | +250 µm   |
| x span     | 0         |
| y          | 0 µm      |
| y min      | -125 µm   |
| y max      | +125 µm   |
| y span     | 250 µm    |
| z centre   | -10 µm    |
| z min      | -210 µm   |
| z max      | +100 µm   |
| z span     | 310 µm    |

---

## 5b. Global Source Settings
| Parameter               | Value         |
|-------------------------|---------------|
| Mode                    | Frequency/Wavelength |
| Frequency start         | 0.1 THz       |
| Frequency stop          | 1.5 THz       |
| Pulse type              | Broadband     |
| Center frequency        | 0.8 THz       |
| Pulse length            | 1332.45 fs    |
| Offset                  | 3777.91 fs    |
| Bandwidth               | 1.4 THz       |
| Eliminate discontinuities | Yes         |
| Optimize for short pulse | Yes          |
| Eliminate DC            | Yes           |

---

## 6. Mesh Override — mesh port1
### General
| Parameter       | Value  |
|-----------------|--------|
| override x mesh | No     |
| override y mesh | Yes    |
| dy              | 2 µm   |
| override z mesh | Yes    |
| dz              | 2 µm   |

### Geometry
| Parameter   | Value      |
|-------------|------------|
| x           | -450 µm    |
| x span      | 1 µm       |
| x min       | -450.5 µm  |
| x max       | -449.5 µm  |
| y           | 0 µm       |
| y span      | 40 µm      |
| y min       | -20 µm     |
| y max       | +20 µm     |
| z           | -24 µm     |
| z span      | 52 µm      |
| z min       | -50 µm     |
| z max       | +2 µm      |
| Relative coords | Yes    |

NOTE: y span (40 µm) covers signal s=10 µm + both slots w=7.5 µm = 25 µm total — good.
      z span (52 µm) covers surface (z=0) down to trench depth h_burried=50 µm — good.
      dy and dz updated from 0.5/1 µm to 2 µm each ✅ (applied fix)

---

## 7. Mesh Override — mesh port2
### General
| Parameter       | Value  |
|-----------------|--------|
| override x mesh | No     |
| override y mesh | Yes    |
| dy              | 2 µm   |
| override z mesh | Yes    |
| dz              | 2 µm   |

### Geometry
| Parameter   | Value      |
|-------------|------------|
| x           | 50 µm      |
| x span      | 1 µm       |
| x min       | 49.5 µm    |
| x max       | 50.5 µm    |
| y           | 0 µm       |
| y span      | 40 µm      |
| y min       | -20 µm     |
| y max       | +20 µm     |
| z           | -24 µm     |
| z span      | 52 µm      |
| z min       | -50 µm     |
| z max       | +2 µm      |
| Relative coords | Yes    |

NOTE: dy and dz updated from 0.5/1 µm to 2 µm each ✅ (applied fix). Geometry mirrors port 1 ✅.

---

## 8. Mesh Override — mesh cap (Right Gap)
### Geometry
| Parameter   | Value      |
|-------------|------------|
| x           | -158.5 µm  |
| x span      | 3 µm       |
| x min       | -160 µm    |
| x max       | -157 µm    |
| y           | 0 µm       |
| y span      | 10 µm      |
| y min       | -5 µm      |
| y max       | +5 µm      |
| z           | 0 µm       |
| z span      | 10 µm      |
| z min       | -5 µm      |
| z max       | +5 µm      |
| Relative coords | Yes    |

NOTE: This geometry correctly covers the right coupling gap (x = -160 to -157 µm). ✅

---

## 8b. Mesh Override — mesh cap2 (Left Gap)
### General
| Parameter       | Value   |
|-----------------|---------|
| override x mesh | Yes     |
| dx              | 0.2 µm  |
| override y mesh | No      |
| override z mesh | Yes     |
| dz              | 2 µm    |

NOTE: We can infer this is for the left coupling gap. The refined dx=0.2 µm combined with a small x span will drastically reduce cell count compared to the old 120 µm span. ✅

---

## 9. Frequency Domain Monitor (monitor)
### General & Geometry
| Parameter          | Value         |
|--------------------|---------------|
| Monitor type       | 2D Z-normal   |
| x                  | -220 µm       |
| x span             | 290 µm        |
| y                  | 0 µm          |
| y span             | 80 µm         |
| z                  | -0.1 µm       |
| Relative coords    | Yes           |
| Simulation type    | All           |
| Sample spacing     | Uniform       |
| Use source limits  | Yes           |
| Frequency points   | 201           |

### Data to record & Advanced
| Parameter          | Value         |
|--------------------|---------------|
| Standard Fourier   | Yes           |
| Fields             | Ex, Ey, Ez, Hx, Hy, Hz |
| Poynting & Power   | output power  |
| Apodization        | None          |
| Spatial interp.    | specified position |-

## Port Group Settings
| Parameter        | Value  |
|------------------|--------|
| Source port      | Port 1 |
| Source mode      | Mode 1 |
| Frequency points | 201    |
| Calculate group delay | No |

---

## Notes / Known Issues
- Port 2 corrected: z max set to 100 µm to match FDTD simulation region
- mesh x dx=0.2 µm over large x span is the main cause of slow simulation
- mesh port1/port2 dy=0.5 µm over 250 µm y span creates excessive cell count
- FDTD region is not symmetric in x (centre at -150 µm, not 0)
- Cavity is centred at x = -150 µm (set by x_offset in script)
