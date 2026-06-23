# -*- coding: utf-8 -*-
"""
plot_idc_5x5.py
MSc Project — THz CPW Resonator

Plot the simulated S21 transmission for the 5+5 finger interdigital
capacitor (IDC) coupled CPW resonator, digitised from the Lumerical
FDTD Visualiser output.

Run:
    python plot_idc_5x5.py

Requires:
    numpy, scipy, matplotlib
"""

import numpy as np
from pathlib import Path
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Resolve paths relative to this script
SCRIPT_DIR = Path(__file__).resolve().parent
FIGURES_DIR = SCRIPT_DIR.parent / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# ─── Digitised data from Lumerical Visualiser screenshot ─────────────────────
# Frequency axis (THz), |S21| linear (0–1 scale)
freq_pts = np.array([
    0.00, 0.03, 0.06, 0.10, 0.14, 0.18, 0.22, 0.26,
    0.30, 0.34, 0.38, 0.42, 0.45, 0.48, 0.52, 0.56,
    0.60, 0.64, 0.68, 0.72, 0.76, 0.80, 0.84, 0.87,
    0.90, 0.94, 0.98, 1.02, 1.06, 1.10, 1.15, 1.20,
    1.25, 1.28, 1.32, 1.36, 1.40, 1.45, 1.50,
])

s21_pts = np.array([
    0.020, 0.040, 0.085, 0.130, 0.190, 0.270, 0.365, 0.455,
    0.535, 0.600, 0.648, 0.672, 0.680, 0.668, 0.640, 0.600,
    0.555, 0.505, 0.455, 0.410, 0.368, 0.335, 0.316, 0.310,
    0.305, 0.272, 0.228, 0.185, 0.148, 0.118, 0.088, 0.062,
    0.038, 0.022, 0.042, 0.058, 0.056, 0.048, 0.040,
])

# ─── Smooth interpolation for a clean curve ──────────────────────────────────
f_fine = np.linspace(freq_pts[0], freq_pts[-1], 1500)
spline = make_interp_spline(freq_pts, s21_pts, k=3)
s21_fine = np.clip(spline(f_fine), 0, 1)

# ─── Derived quantities ───────────────────────────────────────────────────────
i_peak   = np.argmax(s21_fine)
f0       = f_fine[i_peak]
s21_peak = s21_fine[i_peak]

# FWHM: half-power (|S21| = peak / sqrt(2) since data is |S21| not |S21|²)
half     = s21_peak / np.sqrt(2)
left_idx = np.argmin(np.abs(s21_fine[:i_peak] - half))
right_candidates = np.where(s21_fine[i_peak:] < half)[0]
right_idx = i_peak + right_candidates[0] if len(right_candidates) else len(f_fine) - 1
f_lo, f_hi = f_fine[left_idx], f_fine[right_idx]
delta_f  = f_hi - f_lo          # THz
Q_L      = f0 / delta_f if delta_f > 0 else float("nan")

# ─── Figure ──────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#0f1117")

# Main trace
ax.plot(f_fine, s21_fine, color="#4da6ff", lw=2.0, label=r"$|S_{21}|$ — 5+5 finger IDC")

# Peak marker
ax.axvline(f0, color="#ff9f43", lw=1.0, ls="--", alpha=0.8)
ax.scatter([f0], [s21_peak], color="#ff9f43", zorder=5, s=60)
ax.annotate(
    f"Peak: {f0:.3f} THz\n$|S_{{21}}|$ = {s21_peak:.3f}",
    xy=(f0, s21_peak),
    xytext=(f0 + 0.08, s21_peak - 0.10),
    fontsize=9, color="#ff9f43",
    arrowprops=dict(arrowstyle="->", color="#ff9f43", lw=0.8),
)

# FWHM span
ax.annotate(
    "", xy=(f_hi, half), xytext=(f_lo, half),
    arrowprops=dict(arrowstyle="<->", color="#2ecc71", lw=1.2),
)
ax.text(
    (f_lo + f_hi) / 2, half + 0.018,
    f"FWHM = {delta_f*1e3:.1f} GHz\n$Q_L$ ≈ {Q_L:.1f}",
    ha="center", va="bottom", fontsize=8.5, color="#2ecc71",
)

# IDC parameters annotation box
param_text = (
    "IDC parameters\n"
    "──────────────\n"
    "Fingers per side $N$ = 5\n"
    "Total fingers $2N$ = 10\n"
    r"$L_{\rm IDC}$ = 12 µm" "\n"
    r"$w_f$ = 0.6 µm" "\n"
    r"$g_f$ = 0.45 µm" "\n"
    r"$g_{\rm tip}$ = 0.5 µm"
)
ax.text(
    1.08, 0.65, param_text,
    fontsize=8, color="#cccccc",
    va="top", ha="left",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#1a1d2e", edgecolor="#4da6ff", alpha=0.85),
    transform=ax.transData,
)

# Axes formatting
ax.set_xlabel("Frequency (THz)", color="#cccccc", fontsize=12)
ax.set_ylabel(r"$|S_{21}|$ (linear)", color="#cccccc", fontsize=12)
ax.set_title(
    "IDC-Coupled THz CPW Resonator — 5+5 Finger IDC\n"
    "Simulated transmission $S_{21}$  |  Ansys Lumerical FDTD",
    color="white", fontsize=13, pad=12,
)

ax.set_xlim(0, 1.5)
ax.set_ylim(0, 0.75)
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))

ax.tick_params(colors="#aaaaaa", which="both", direction="in", top=True, right=True)
ax.spines[:].set_color("#444444")
ax.grid(which="major", color="#2a2d3e", lw=0.7, ls="-")
ax.grid(which="minor", color="#1f2230", lw=0.4, ls=":")

# Target frequency reference line
ax.axvline(0.8, color="#e74c3c", lw=0.8, ls=":", alpha=0.7)
ax.text(0.81, 0.02, "Target\n0.8 THz", color="#e74c3c", fontsize=7.5, va="bottom")

ax.legend(loc="upper right", framealpha=0.2, edgecolor="#4da6ff",
          labelcolor="#cccccc", fontsize=10)

plt.tight_layout()
plt.savefig(FIGURES_DIR / "idc_5x5_s21.png", dpi=200, bbox_inches="tight",
            facecolor=fig.get_facecolor())
print("Figure saved -> figures/idc_5x5_s21.png")
print("\nExtracted resonance parameters:")
print(f"  Peak frequency  f0   = {f0:.4f} THz")
print(f"  FWHM            df   = {delta_f*1e3:.2f} GHz")
print(f"  Loaded Q factor Q_L  = {Q_L:.1f}")
plt.show()
