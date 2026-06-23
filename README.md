# Design and Simulation of Terahertz Coplanar Waveguide Resonators

> **MSc Project** — Terahertz CPW resonator design, capacitive coupling, and interdigital capacitor coupling using Ansys Lumerical FDTD.

---

## Project Overview

This MSc project investigates the design and simulation of terahertz coplanar waveguide (CPW) resonators using Ansys Lumerical FDTD. The main aim is to understand how resonator geometry controls the resonance frequency, transmission response, bandwidth, and loaded quality factor.

The project focuses on a planar CPW cavity operating around **0.8 THz**. Two coupling methods are studied:

1. **Simple capacitive gap coupling**
2. **Interdigital capacitor (IDC) coupling**

The work combines electromagnetic simulation, geometry scripting, S-parameter extraction, Lorentzian fitting, and quality factor analysis.

---

## Research Motivation

Terahertz resonators are important for compact high-frequency devices, sensing, spectroscopy, and future communication systems. At THz frequencies, the wavelength is very small, so the resonator geometry must be carefully designed at the micrometre scale.

A CPW resonator is useful because it provides strong electric-field confinement near the signal line and the ground gaps. By changing the cavity length and coupling geometry, the resonator response can be engineered for a target frequency and quality factor.

---

## Baseline CPW Design

The initial resonator was designed using the half-wavelength relation:

$$
L_{\mathrm{cav}} = \frac{c}{2 n_{\mathrm{eff}} f_0}
$$

where:

- $f_0 = 0.8~\mathrm{THz}$
- $n_{\mathrm{eff}} = 2.65$
- $c = 3\times10^8~\mathrm{m/s}$

This gives an initial cavity length of approximately:

$$
L_{\mathrm{cav}} \approx 70.75~\mu\mathrm{m}
$$

The main CPW dimensions used in the simulations are:

| Parameter | Symbol | Value |
|:---|:---:|---:|
| Centre conductor width | $s$ | $10~\mu\mathrm{m}$ |
| CPW slot gap | $w$ | $6.6~\mu\mathrm{m}$ to $7.5~\mu\mathrm{m}$ |
| Target frequency | $f_0$ | $0.8~\mathrm{THz}$ |
| Initial effective index | $n_{\mathrm{eff}}$ | 2.65 |
| Initial cavity length | $L_{\mathrm{cav}}$ | $70.75~\mu\mathrm{m}$ |

---

## Simple Gap-Coupled Resonator

The first design used two simple capacitive gaps at the ends of the cavity:

```text
Input feedline | gap | CPW cavity | gap | Output feedline
```

The capacitive gap electrically separates the feedline from the resonator, so energy couples into the cavity through the electric field across the gap.

Different gap sizes were simulated:

| Coupling gap | Expected coupling |
| ---: | --- |
| $5~\mu\mathrm{m}$ | Weakest |
| $3~\mu\mathrm{m}$ | Moderate |
| $1~\mu\mathrm{m}$ | Strong |
| $0.8~\mu\mathrm{m}$ | Strongest |

The expected behaviour is:

$$
\text{smaller gap} \Rightarrow \text{larger capacitance} \Rightarrow \text{stronger coupling}
$$

Stronger coupling gives a broader resonance and a lower loaded quality factor.

---

## Gap-Coupling Results

The simulated transmission spectra were analysed using Lorentzian fitting. The loaded quality factor was calculated using:

$$
Q_L = \frac{f_0}{\Delta f}
$$

where $\Delta f$ is the full width at half maximum.

Example fitted results from the reference-normalised first resonance are:

| Coupling gap | $f_0$ (THz) | $\Delta f$ (GHz) | $Q_L$ |
| ---: | ---: | ---: | ---: |
| $5~\mu\mathrm{m}$ | 0.6675 | 49.25 | 13.55 |
| $3~\mu\mathrm{m}$ | 0.6670 | 58.78 | 11.35 |
| $1~\mu\mathrm{m}$ | 0.6454 | 92.09 | 7.01 |
| $0.8~\mu\mathrm{m}$ | 0.6399 | 101.03 | 6.33 |

These results show that reducing the coupling gap increases the bandwidth and reduces the loaded quality factor.

---

## Effective Index and End Correction

A cavity length sweep showed that the simple half-wavelength equation does not fully describe the simulated resonance. This is because the capacitive gaps and fringing fields increase the effective electrical length of the resonator.

A corrected model is:

$$
f_0 = \frac{c}{2 n_{\mathrm{eff}}(L_{\mathrm{cav}}+\Delta L)}
$$

where $\Delta L$ is an end correction caused by fringing fields and capacitive loading.

The corrected fitting gave approximately:

- $n_{\mathrm{eff}} \approx 2.68$
- $\Delta L \approx 12.38~\mu\mathrm{m}$

This shows that the resonator behaves as if it is longer than the drawn metal length.

---

## Interdigital Capacitor Coupling

The second design replaced the simple capacitive gaps with interdigital capacitors. The IDC fingers are integrated into the signal conductor so that the feedline and the cavity are capacitively coupled through interleaved fingers.

The structure is:

```text
Port 1 → Left IDC → CPW cavity → Right IDC → Port 2
```

Two interdigital capacitors are used because this is a two-port ($S_{21}$) resonator measurement:

- The **left IDC** couples energy from the input feedline into the cavity.
- The **middle CPW section** defines the resonator cavity.
- The **right IDC** couples energy from the cavity to the output feedline.

The latest geometry uses one merged signal conductor polygon, where the IDC fingers are part of the same signal object rather than separate metal objects.

---

## IDC Geometry Parameters

The latest IDC design uses:

| Parameter | Symbol | Value |
| --- | ---: | ---: |
| IDC length | $L_{\mathrm{IDC}}$ | $12~\mu\mathrm{m}$ |
| Finger width | $w_f$ | $0.6~\mu\mathrm{m}$ |
| Finger gap | $g_f$ | $0.45~\mu\mathrm{m}$ |
| Tip gap | $g_{\mathrm{tip}}$ | $0.5~\mu\mathrm{m}$ |
| Fingers per side | $N$ | 4 |
| Total fingers | $2N$ | 8 |

The coupling capacitance increases when:

$$
N \uparrow,\quad L_{\mathrm{IDC}} \uparrow,\quad g_f \downarrow
$$

This gives the expected trend:

```text
More fingers → stronger coupling → wider bandwidth → lower loaded Q
```

---

## Latest IDC Simulation Status

The current IDC geometry successfully forms the intended layout:

```text
Input CPW → IDC → central cavity → IDC → output CPW
```

The simulated $S_{21}$ response currently shows a broad response with a strong feature below the target frequency and additional features around the THz range. This indicates that the IDC loading increases the effective electrical length of the cavity.

The strongest peak appears below $0.8~\mathrm{THz}$, meaning the IDC-coupled cavity is electrically longer than the simple half-wave design.

The next design step is to sweep the middle cavity length:

| Trial | Middle cavity length |
| --- | ---: |
| 1 | $30~\mu\mathrm{m}$ |
| 2 | $40~\mu\mathrm{m}$ |
| 3 | $50~\mu\mathrm{m}$ |
| 4 | $60~\mu\mathrm{m}$ |
| 5 | $70.75~\mu\mathrm{m}$ |

The correct cavity mode will be identified as the peak that shifts consistently with $L_{\mathrm{cav}}$.

---

## Mesh Strategy

The IDC region contains the smallest features in the model:

- finger gap: $0.45~\mu\mathrm{m}$
- tip gap: $0.5~\mu\mathrm{m}$
- finger width: $0.6~\mu\mathrm{m}$

Therefore, local mesh override regions are required around each IDC.

Recommended mesh:

| Region | Mesh size |
| --- | ---: |
| IDC local mesh (dx) | $0.05$–$0.10~\mu\mathrm{m}$ |
| IDC local mesh (dy) | $0.05$–$0.10~\mu\mathrm{m}$ |
| IDC local mesh (dz) | $0.2$–$0.5~\mu\mathrm{m}$ |
| General CPW region | coarser mesh |

Fine mesh should be applied only near the IDC regions to avoid excessive simulation runtime.

---

## Data Processing

The exported transmission data is $|S_{21}|^2$, so the dB conversion is:

$$
S_{21,\mathrm{dB}} = 10\log_{10}(|S_{21}|^2)
$$

For reference-normalised data:

$$
S_{21,\mathrm{norm,dB}} =
10\log_{10}\left(\frac{|S_{21}|^2}{|S_{21,\mathrm{ref}}|^2}\right)
$$

Lorentzian fitting is used to extract:

- resonance frequency $f_0$
- full width at half maximum $\Delta f$
- loaded quality factor $Q_L$

---

## Scaled 10 GHz PCB Version

A direct 0.8 THz PCB implementation is not practical because the required features are micrometre and sub-micrometre scale. However, a scaled microwave-frequency PCB prototype can be designed to validate the resonator physics.

A possible scaled version is a **10 GHz CPW resonator** on a low-loss RF PCB material such as Rogers RO4003C.

For a rough 10 GHz design:

$$
L_{\mathrm{cav}} \approx 10~\mathrm{mm}
$$

A scaled PCB prototype could be measured using a vector network analyser to validate:

- CPW resonance behaviour
- capacitive coupling
- IDC coupling
- loaded Q extraction
- $S_{11}$ and $S_{21}$ response

This would not prove the exact THz performance, but it would experimentally confirm the underlying resonator physics.

---

## Current Project Workflow

The project workflow is:

1. Build baseline CPW geometry.
2. Simulate a straight reference CPW line.
3. Design simple gap-coupled cavity.
4. Sweep capacitive gap size.
5. Extract $f_0$, $\Delta f$, and $Q_L$.
6. Fit length sweep to estimate $n_{\mathrm{eff}}$ and end correction.
7. Design IDC-coupled cavity.
8. Sweep IDC geometry and middle cavity length.
9. Compare gap coupling and IDC coupling.
10. Prepare final MSc report and poster.

---

## Key Equations

**Half-wave cavity:**

$$
L_{\mathrm{cav}} = \frac{c}{2n_{\mathrm{eff}}f_0}
$$

**Loaded quality factor:**

$$
Q_L = \frac{f_0}{\Delta f}
$$

**Internal, coupling, and loaded Q:**

$$
\frac{1}{Q_L} = \frac{1}{Q_i} + \frac{1}{Q_c}
$$

**Capacitive reactance:**

$$
X_C = \frac{1}{\omega C_c}
$$

---

## Main Findings So Far

- The simple half-wave equation gives a useful starting cavity length.
- Fringing fields and capacitive coupling increase the effective electrical length.
- Smaller coupling gaps produce stronger coupling and lower loaded quality factor.
- IDC coupling gives stronger and more complex capacitive loading than simple gaps.
- The IDC-coupled cavity must be tuned using a cavity-length sweep because the IDC loading shifts the resonance downward.
- Local mesh refinement is essential around sub-micrometre IDC gaps.

---

## Software and Tools

- Ansys Lumerical FDTD
- Python (NumPy, Pandas, Matplotlib, SciPy)
- Overleaf / LaTeX
- GitHub

---

## Repository Structure

```text
.
├── README.md
├── lumerical_scripts/
│   ├── gap_coupled_cavity.lsf
│   ├── idc_coupled_cavity.lsf
│   └── mesh_setup.lsf
├── python_analysis/
│   ├── lorentzian_fit.py
│   └── plot_s21.py
├── data/
│   ├── gap_sweep/
│   ├── length_sweep/
│   └── idc_sweep/
├── figures/
└── report/
    ├── main.tex
    └── references.bib
```

---

## Next Steps

1. Perform an IDC cavity length sweep from $30~\mu\mathrm{m}$ to $70.75~\mu\mathrm{m}$.
2. Identify which $S_{21}$ feature corresponds to the true cavity mode.
3. Refine the IDC mesh and check mesh convergence.
4. Compare gap coupling and IDC coupling in terms of bandwidth and $Q_L$.
5. Prepare final figures for the MSc report and poster.
6. Develop a possible 10 GHz scaled PCB validation design.

---

## Project Status

> **Current status: simulation and optimisation in progress.**

The baseline gap-coupled resonator has been analysed, and the IDC-coupled resonator geometry has been developed. The main remaining task is to tune the IDC-loaded cavity length and extract reliable quality factor values.
