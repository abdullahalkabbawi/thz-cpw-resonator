# -*- coding: utf-8 -*-
"""
plot_geometry.py
MSc Project -- THz CPW Resonator

Draws the exact 2-D metal layout defined by the Lumerical script.
Uses axhspan / fill_between for ground planes (avoids giant patch bboxes).

Two panels:
  Top    : full resonator view  (x = -55..+55 um, y = -16..+16 um)
  Bottom : left IDC zoom        (x = -36...-16 um, y = -7..+7 um)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

SCRIPT_DIR  = Path(__file__).resolve().parent
FIGURES_DIR = SCRIPT_DIR.parent / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# Parameters -- all in metres; converted to um when plotting
# ============================================================
L_cav      = 40e-6
s          = 10.05e-6
w          = 6.6e-6
IDC_L      = 12e-6
finger_w   = 0.6e-6
finger_gap = 0.45e-6
tip_gap    = 0.5e-6
N_total    = 10
overlap    = 0.03e-6

IDC_height  = N_total * finger_w + (N_total - 1) * finger_gap
edge_margin = (s - IDC_height) / 2

x_cav_left  = -L_cav / 2
x_cav_right =  L_cav / 2
xL_start    = x_cav_left  - IDC_L
xL_end      = x_cav_left
xR_start    = x_cav_right
xR_end      = x_cav_right + IDC_L

U = 1e6   # metres -> micrometres

# ============================================================
# Colour palette
# ============================================================
C_BG  = "#0f1117"
C_GND = "#b8cce8"
C_FL  = "#4da6ff"   # feedline conductor
C_CAV = "#ffd700"   # cavity conductor
C_ANN = "#2ecc71"
C_DIM = "#e74c3c"
C_FW  = "#ff9f43"

# ============================================================
# Helper: draw a filled rectangle (in um) on an axis
# ============================================================
def filled_rect(ax, xmin_m, xmax_m, ymin_m, ymax_m, color, zorder=3, alpha=0.92):
    ax.fill(
        [xmin_m*U, xmax_m*U, xmax_m*U, xmin_m*U],
        [ymin_m*U, ymin_m*U, ymax_m*U, ymax_m*U],
        color=color, alpha=alpha, zorder=zorder
    )

# ============================================================
# Draw all geometry onto a given axis
# ============================================================
def draw_geometry(ax, xlim_m, ylim_m):
    xlo, xhi = xlim_m
    ylo, yhi = ylim_m

    # ---- Ground planes (clipped to view window) ----
    filled_rect(ax, xlo, xhi,  ylo,            -s/2 - w, C_GND, zorder=2)
    filled_rect(ax, xlo, xhi,   s/2 + w,        yhi,     C_GND, zorder=2)

    # ---- Signal feedlines (clipped to view window) ----
    filled_rect(ax, xlo,     xL_start, -s/2, s/2, C_FL, zorder=3)
    filled_rect(ax, xR_end,  xhi,      -s/2, s/2, C_FL, zorder=3)

    # ---- Middle cavity ----
    filled_rect(ax, x_cav_left, x_cav_right, -s/2, s/2, C_CAV, zorder=3)

    # ---- IDC fingers ----
    for n in range(1, N_total + 1):
        y_top = s/2 - edge_margin - (n - 1) * (finger_w + finger_gap)
        y_bot = y_top - finger_w
        odd   = (n % 2 == 1)

        # LEFT IDC
        if odd:   # feedline finger
            filled_rect(ax, xL_start - overlap, xL_end - tip_gap, y_bot, y_top, C_FL,  zorder=4)
        else:     # cavity finger
            filled_rect(ax, xL_start + tip_gap, xL_end + overlap, y_bot, y_top, C_CAV, zorder=4)

        # RIGHT IDC
        if odd:   # cavity finger
            filled_rect(ax, xR_start - overlap, xR_end - tip_gap, y_bot, y_top, C_CAV, zorder=4)
        else:     # feedline finger
            filled_rect(ax, xR_start + tip_gap, xR_end + overlap, y_bot, y_top, C_FL,  zorder=4)


# ============================================================
# Figure
# ============================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 8),
                                gridspec_kw={"hspace": 0.55})
fig.patch.set_facecolor(C_BG)

for ax in (ax1, ax2):
    ax.set_facecolor(C_BG)
    ax.tick_params(colors="#aaaaaa", which="both", direction="in")
    ax.spines[:].set_color("#444444")
    ax.grid(color="#1e2233", lw=0.5, zorder=0)


# ── TOP PANEL: full resonator view ──────────────────────────
VIEW1_X = (-55e-6, 55e-6)
VIEW1_Y = (-16e-6, 16e-6)
draw_geometry(ax1, VIEW1_X, VIEW1_Y)

ax1.set_xlim(VIEW1_X[0]*U, VIEW1_X[1]*U)
ax1.set_ylim(VIEW1_Y[0]*U, VIEW1_Y[1]*U)
ax1.set_xlabel("x (um)", color="#cccccc", fontsize=11)
ax1.set_ylabel("y (um)", color="#cccccc", fontsize=11)
ax1.set_title(
    "THz CPW Resonator  --  5+5 Finger IDC  |  $L_{\\rm cav}$ = 40 um,  s = 10.05 um,  w = 6.6 um",
    color="white", fontsize=11, pad=10
)

# Dimension annotations
s_u  = s * U
w_u  = w * U
IL_u = IDC_L * U
xCL  = x_cav_left  * U
xCR  = x_cav_right * U
xLL  = xL_start * U
xLR  = xL_end   * U
xRL  = xR_start * U
xRR  = xR_end   * U

def double_arrow(ax, x1, x2, y, label, col, dy=1.0, fs=8):
    ax.annotate("", xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="<->", color=col, lw=1.1))
    ax.text((x1+x2)/2, y + dy, label, ha="center", va="bottom",
            fontsize=fs, color=col)

# L_cav
double_arrow(ax1, xCL, xCR, -13.5, f"L_cav = {L_cav*U:.0f} um", C_CAV, dy=0.4, fs=8)
# IDC lengths
double_arrow(ax1, xLL, xLR,  13,   f"IDC_L = {IDC_L*U:.0f} um", C_ANN, dy=0.4, fs=8)
double_arrow(ax1, xRL, xRR,  13,   f"IDC_L = {IDC_L*U:.0f} um", C_ANN, dy=0.4, fs=8)

# s label (left margin)
ax1.annotate("", xy=(-54, -s_u/2), xytext=(-54, s_u/2),
             arrowprops=dict(arrowstyle="<->", color=C_FW, lw=1.0))
ax1.text(-53.2, 0, f"s={s_u:.2f}um", ha="left", va="center", fontsize=7.5, color=C_FW)

# w label
ax1.annotate("", xy=(-54, -(s_u/2+w_u)), xytext=(-54, -s_u/2),
             arrowprops=dict(arrowstyle="<->", color=C_DIM, lw=1.0))
ax1.text(-53.2, -(s_u/2+w_u/2), f"w={w_u:.1f}um", ha="left", va="center", fontsize=7.5, color=C_DIM)

# Vertical boundary lines
for xv in [xLL, xLR, xRL, xRR]:
    ax1.axvline(xv, color="#555577", lw=0.7, ls=":", zorder=1)

# Legend
leg = [
    mpatches.Patch(facecolor=C_GND, label="Ground (PEC)"),
    mpatches.Patch(facecolor=C_FL,  label="Feedline signal"),
    mpatches.Patch(facecolor=C_CAV, label="Cavity"),
]
ax1.legend(handles=leg, loc="upper right", fontsize=8.5,
           framealpha=0.25, edgecolor="#4da6ff", labelcolor="#cccccc")


# ── BOTTOM PANEL: left IDC zoom ──────────────────────────────
PAD = 2.5e-6
VIEW2_X = (xL_start - PAD, xL_end + PAD)
VIEW2_Y = (-s/2 - 2e-6, s/2 + 2e-6)
draw_geometry(ax2, VIEW2_X, VIEW2_Y)

ax2.set_xlim(VIEW2_X[0]*U, VIEW2_X[1]*U)
ax2.set_ylim(VIEW2_Y[0]*U, VIEW2_Y[1]*U)
ax2.set_xlabel("x (um)", color="#cccccc", fontsize=11)
ax2.set_ylabel("y (um)", color="#cccccc", fontsize=11)
ax2.set_title(
    "Left IDC  --  blue fingers connected to feedline, gold fingers connected to cavity",
    color="white", fontsize=10, pad=8
)

# Dimension annotations in zoom panel
fw_u = finger_w * U
fg_u = finger_gap * U
tg_u = tip_gap * U

# Finger width -- annotate on n=1 finger (draw arrow to the LEFT of feedline edge)
y_top1 = (s/2 - edge_margin) * U
y_bot1 = y_top1 - fw_u
x_ann  = VIEW2_X[0]*U + 0.8   # just inside left edge

ax2.annotate("", xy=(x_ann, y_bot1), xytext=(x_ann, y_top1),
             arrowprops=dict(arrowstyle="<->", color=C_FW, lw=1.1))
ax2.text(x_ann + 0.2, (y_top1+y_bot1)/2,
         f"fw={fw_u:.2f}um", ha="left", va="center", fontsize=7.5, color=C_FW)

# Finger gap -- between n=1 and n=2
y_top2 = y_bot1 - fg_u
ax2.annotate("", xy=(x_ann, y_top2), xytext=(x_ann, y_bot1),
             arrowprops=dict(arrowstyle="<->", color="#9b59b6", lw=1.1))
ax2.text(x_ann + 0.2, (y_bot1+y_top2)/2,
         f"fg={fg_u:.2f}um", ha="left", va="center", fontsize=7.5, color="#9b59b6")

# Tip gap -- horizontal arrow at n=1 finger tip
y_mid1 = (y_top1 + y_bot1) / 2
x_tip  = (xL_end - tip_gap) * U
x_end  = xL_end * U
ax2.annotate("", xy=(x_end, y_mid1), xytext=(x_tip, y_mid1),
             arrowprops=dict(arrowstyle="<->", color=C_DIM, lw=1.1))
ax2.text((x_tip + x_end)/2, y_mid1 + 0.3,
         f"tip_gap={tg_u:.2f}um", ha="center", va="bottom", fontsize=7.5, color=C_DIM)

# Region labels
ax2.text((VIEW2_X[0]*U + xLL)/2, 0,
         "Feedline", ha="center", va="center", fontsize=8.5, color=C_FL, alpha=0.8, style="italic")
ax2.text((xCL + xCR)/2 * U if (xCL+xCR)/2*U < VIEW2_X[1]*U else VIEW2_X[1]*U - 1,
         0, "Cavity", ha="center", va="center", fontsize=8.5, color=C_CAV, alpha=0.8, style="italic")


# ── Save ─────────────────────────────────────────────────────
plt.suptitle(
    "CPW Resonator Geometry  |  s=10.05um  w=6.6um  N=5+5 IDC fingers  L_cav=40um",
    color="white", fontsize=11, y=0.99
)
outfile = FIGURES_DIR / "cpw_idc_geometry.png"
fig.savefig(outfile, dpi=150, bbox_inches="tight", facecolor=C_BG)
print(f"Saved -> {outfile}")
plt.show()
