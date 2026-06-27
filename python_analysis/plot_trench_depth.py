import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
import os

def extract_q_from_spline(freq, s21_sq, label):
    # Sort data just in case
    sort_idx = np.argsort(freq)
    freq = freq[sort_idx]
    s21_sq = s21_sq[sort_idx]
    
    # Restrict to 0.4 - 0.8 THz for fitting
    mask = (freq >= 0.4) & (freq <= 0.8)
    freq_fit = freq[mask]
    s21_fit = s21_sq[mask]
    
    # Create CubicSpline
    cs = CubicSpline(freq_fit, s21_fit)
    
    # Evaluate over a very fine grid to find the peak
    f_fine = np.linspace(freq_fit[0], freq_fit[-1], 10000)
    s21_fine = cs(f_fine)
    
    peak_idx = np.argmax(s21_fine)
    f0 = f_fine[peak_idx]
    peak_val = s21_fine[peak_idx]
    
    # Find FWHM
    half_max = peak_val / 2.0
    
    # Function to find roots: cs(f) - half_max = 0
    def root_func(f):
        return cs(f) - half_max
    
    # Search for left crossing between f_fine[0] and f0
    try:
        sol_left = root_scalar(root_func, bracket=[freq_fit[0], f0])
        f_left = sol_left.root
    except ValueError:
        f_left = np.nan
        
    # Search for right crossing between f0 and f_fine[-1]
    try:
        sol_right = root_scalar(root_func, bracket=[f0, freq_fit[-1]])
        f_right = sol_right.root
    except ValueError:
        f_right = np.nan
        
    if not np.isnan(f_left) and not np.isnan(f_right):
        delta_f = f_right - f_left
        ql = f0 / delta_f
    else:
        delta_f = np.nan
        ql = np.nan
        
    print(f"--- {label} ---")
    print(f"f0 (spline): {f0:.6f} THz")
    print(f"Peak |S21|^2: {peak_val:.6f}")
    print(f"Delta f: {delta_f*1000:.3f} GHz")
    print(f"Q-factor: {ql:.2f}\n")
    
    return f_fine, s21_fine, f0, ql

# Load files
datasets = [
    ("../data/trench_30um_depth_3um_gap_S21.csv", "30 \u00b5m Depth"),
    ("../data/trench_50um_depth_v2_S21.csv", "50 \u00b5m Depth (v2)"),
    ("../data/trench_70um_depth_3um_gap_S21.csv", "70 \u00b5m Depth")
]

plt.figure(figsize=(10, 6))
colors = ['blue', 'orange', 'green']

for i, (path, label) in enumerate(datasets):
    df = pd.read_csv(path, comment='#')
    freq = df.iloc[:, 0].values
    s21 = df.iloc[:, 1].values
    
    # Convert from Hz to THz if needed
    if np.max(freq) > 1e11:
        freq = freq / 1e12
    
    f_fine, s21_fine, f0, ql = extract_q_from_spline(freq, s21, label)
    
    # Plot original scatter data (restricted to 0.4-0.8)
    mask = (freq >= 0.4) & (freq <= 0.8)
    plt.scatter(freq[mask], s21[mask], color=colors[i], s=15, alpha=0.6)
    
    # Plot Spline Fit
    plt.plot(f_fine, s21_fine, color=colors[i], label=f"{label} (Q = {ql:.1f})")

plt.xlim(0.4, 0.8)
plt.xlabel("Frequency (THz)")
plt.ylabel("$|S_{21}|^2$")
plt.title("Trench Depth Sweep: Spline Interpolation (0.4 - 0.8 THz)")
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.tight_layout()

# Save figure
os.makedirs("../figures", exist_ok=True)
save_path = "../figures/trench_depth_spline_zoom.png"
plt.savefig(save_path, dpi=300)
print(f"Saved plot to {save_path}")
