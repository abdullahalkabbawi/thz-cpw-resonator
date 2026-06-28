import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import os

datasets = [
    ("../data/trench_50um_depth_v2_S11.csv", "GaAs Substrate"),
    ("../data/trench_50um_si_S11.csv", "High-Resistivity Si Substrate")
]

plt.figure(figsize=(10, 6))
colors = ['blue', 'red']

for i, (path, label) in enumerate(datasets):
    # Load data
    df = pd.read_csv(path, comment='#')
    freq = df.iloc[:, 0].values
    s11 = df.iloc[:, 1].values
    
    # Sort data
    sort_idx = np.argsort(freq)
    freq = freq[sort_idx]
    s11 = s11[sort_idx]
    
    # Convert from Hz to THz if needed
    if np.max(freq) > 1e11:
        freq = freq / 1e12
        
    # Restrict to 0.4 - 0.8 THz for fitting to match S21
    mask = (freq >= 0.4) & (freq <= 0.8)
    freq_fit = freq[mask]
    s11_fit = s11[mask]
    
    # High-resolution Spline Interpolation
    cs = CubicSpline(freq_fit, s11_fit)
    f_fine = np.linspace(freq_fit[0], freq_fit[-1], 10000)
    s11_fine = cs(f_fine)
    
    # Find precise minimum (resonance dip)
    min_idx = np.argmin(s11_fine)
    f0 = f_fine[min_idx]
    min_val = s11_fine[min_idx]
    
    print(f"--- {label} ---")
    print(f"f0 (dip): {f0:.6f} THz")
    print(f"Min |S11|^2: {min_val:.6f}\n")
    
    # Plot original scatter data
    plt.scatter(freq_fit, s11_fit, color=colors[i], s=15, alpha=0.4)
    
    # Plot High Resolution Spline Fit
    plt.plot(f_fine, s11_fine, color=colors[i], label=f"{label} ($f_0$ = {f0:.4f} THz)")

plt.xlim(0.4, 0.8)
plt.ylim(0, 1.1)
plt.xlabel("Frequency (THz)")
plt.ylabel("$|S_{11}|^2$")
plt.title("Substrate Comparison: S11 Reflection (50 µm Trench Depth)")
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.tight_layout()

# Save figure
os.makedirs("../figures", exist_ok=True)
save_path = "../figures/substrate_comparison_s11.png"
plt.savefig(save_path, dpi=600)  # Extremely high resolution
print(f"Saved highly-resolved S11 plot to {save_path}")
