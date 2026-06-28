import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("../data/trench_si_loss.csv", comment='#')
freq = df.iloc[:, 0].values
loss = df.iloc[:, 1].values

# High-resolution Spline Interpolation
cs = CubicSpline(freq, loss)
f_fine = np.linspace(freq[0], freq[-1], 10000)
loss_fine = cs(f_fine)

plt.figure(figsize=(10, 6))

# Plot original scatter data
plt.scatter(freq, loss, color='red', s=20, alpha=0.6, label="FDTD Data Points")

# Plot Spline Fit
plt.plot(f_fine, loss_fine, color='darkred', linewidth=2, label="Cubic Spline Fit")

# Highlight resonance frequency
f0 = 0.6273  # Target resonance from our S21/S11 analysis
loss_at_f0 = cs(f0)
plt.axvline(x=f0, color='blue', linestyle='--', alpha=0.6, label=f"Fundamental Resonance ($f_0$ = {f0} THz)")
plt.scatter([f0], [loss_at_f0], color='blue', s=60, zorder=5)
plt.annotate(f"{loss_at_f0:.5f} dB/mm", (f0 + 0.03, loss_at_f0), color='blue', fontsize=11, fontweight='bold')

plt.xlim(0.1, 1.5)
# Use log scale since loss drops rapidly and we want to see it clearly, or just linear since the curve looks quite smooth
# The values range from 0.001 to 0.026, so linear is actually fine and easy to read.

plt.xlabel("Frequency (THz)", fontsize=12)
plt.ylabel("Propagation Loss (dB/mm)", fontsize=12)
plt.title("Silicon Substrate Propagation Loss vs Frequency (FDTD Port Analysis)", fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.tight_layout()

# Save figure
os.makedirs("../figures", exist_ok=True)
save_path = "../figures/si_substrate_propagation_loss.png"
plt.savefig(save_path, dpi=600)
print(f"Saved highly-resolved loss plot to {save_path}")
