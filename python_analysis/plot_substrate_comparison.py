import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
import os

def extract_q_from_spline(freq, s21_sq, label):
    sort_idx = np.argsort(freq)
    freq = freq[sort_idx]
    s21_sq = s21_sq[sort_idx]
    
    mask = (freq >= 0.4) & (freq <= 0.8)
    freq_fit = freq[mask]
    s21_fit = s21_sq[mask]
    
    cs = CubicSpline(freq_fit, s21_fit)
    f_fine = np.linspace(freq_fit[0], freq_fit[-1], 10000)
    s21_fine = cs(f_fine)
    
    peak_idx = np.argmax(s21_fine)
    f0 = f_fine[peak_idx]
    peak_val = s21_fine[peak_idx]
    half_max = peak_val / 2.0
    
    def root_func(f): return cs(f) - half_max
    
    try:
        f_left = root_scalar(root_func, bracket=[freq_fit[0], f0]).root
    except ValueError:
        f_left = np.nan
        
    try:
        f_right = root_scalar(root_func, bracket=[f0, freq_fit[-1]]).root
    except ValueError:
        f_right = np.nan
        
    delta_f = f_right - f_left if not np.isnan(f_left) and not np.isnan(f_right) else np.nan
    ql = f0 / delta_f if not np.isnan(delta_f) else np.nan
        
    print(f"--- {label} ---")
    print(f"f0 (spline): {f0:.6f} THz")
    print(f"Peak |S21|^2: {peak_val:.6f}")
    print(f"Delta f: {delta_f*1000:.3f} GHz")
    print(f"Q-factor: {ql:.2f}\n")
    
    return f_fine, s21_fine, f0, ql

datasets = [
    ("../data/trench_50um_depth_v2_S21.csv", "GaAs Substrate"),
    ("../data/trench_50um_si_S21.csv", "High-Resistivity Si Substrate")
]

plt.figure(figsize=(10, 6))
colors = ['blue', 'red']

for i, (path, label) in enumerate(datasets):
    df = pd.read_csv(path, comment='#')
    freq = df.iloc[:, 0].values
    s21 = df.iloc[:, 1].values
    
    if np.max(freq) > 1e11: freq = freq / 1e12
    
    f_fine, s21_fine, f0, ql = extract_q_from_spline(freq, s21, label)
    
    mask = (freq >= 0.4) & (freq <= 0.8)
    plt.scatter(freq[mask], s21[mask], color=colors[i], s=15, alpha=0.6)
    plt.plot(f_fine, s21_fine, color=colors[i], label=f"{label} (Q = {ql:.1f})")

plt.xlim(0.4, 0.8)
plt.xlabel("Frequency (THz)")
plt.ylabel("$|S_{21}|^2$")
plt.title("Substrate Comparison: GaAs vs Si (50 µm Trench Depth)")
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.tight_layout()

os.makedirs("../figures", exist_ok=True)
save_path = "../figures/substrate_comparison_si_vs_gaas.png"
plt.savefig(save_path, dpi=300)
print(f"Saved plot to {save_path}")
