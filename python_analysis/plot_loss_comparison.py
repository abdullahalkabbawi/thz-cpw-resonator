import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import os

datasets = [
    ("../data/trench_gaas_loss.csv", "GaAs Substrate", "blue"),
    ("../data/trench_si_loss.csv", "High-Resistivity Si Substrate", "red")
]

plt.figure(figsize=(10, 6))

for path, label, color in datasets:
    # Load data
    df = pd.read_csv(path, comment='#')
    freq = df.iloc[:, 0].values
    loss = df.iloc[:, 1].values
    
    # High-resolution Spline Interpolation
    cs = CubicSpline(freq, loss)
    f_fine = np.linspace(freq[0], freq[-1], 10000)
    loss_fine = cs(f_fine)
    
    # Plot original scatter data
    plt.scatter(freq, loss, color=color, s=20, alpha=0.6)
    
    # Plot Spline Fit
    plt.plot(f_fine, loss_fine, color=color, linewidth=2, label=label)

plt.xlim(0.1, 1.5)
plt.yscale('log')  # Log scale is crucial here because Si is ~0.001 and GaAs is ~0.1

plt.xlabel("Frequency (THz)", fontsize=12)
plt.ylabel("Propagation Loss (dB/mm)", fontsize=12)
plt.title("Substrate Propagation Loss Comparison (FDTD Port Analysis)", fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.tight_layout()

# Save figure
os.makedirs("../figures", exist_ok=True)
save_path = "../figures/substrate_loss_comparison.png"
plt.savefig(save_path, dpi=600)
print(f"Saved highly-resolved loss comparison plot to {save_path}")
