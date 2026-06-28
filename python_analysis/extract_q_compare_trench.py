import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
import os

def extract_q_from_spline(freq, s21_sq, label):
    # Sort data to ensure strictly increasing frequency for spline
    sort_idx = np.argsort(freq)
    freq = freq[sort_idx]
    s21_sq = s21_sq[sort_idx]
    
    # Filter frequency range around the expected fundamental resonance (0.4 to 1.0 THz)
    mask = (freq >= 0.4) & (freq <= 1.0)
    f_sub = freq[mask]
    s21_sub = s21_sq[mask]
    
    # Create Cubic Spline
    cs = CubicSpline(f_sub, s21_sub)
    
    # Create fine frequency array
    f_fine = np.linspace(f_sub[0], f_sub[-1], 10000)
    s21_fine = cs(f_fine)
    
    # Find peak
    peak_idx = np.argmax(s21_fine)
    f0 = f_fine[peak_idx]
    peak_val = s21_fine[peak_idx]
    
    # Half-power point
    half_power = peak_val / 2
    
    # Find intersections with half-power line
    def f_half(x):
        return cs(x) - half_power
        
    try:
        # Lower bound
        sol_low = root_scalar(f_half, bracket=[f_sub[0], f0], method='brentq')
        f_low = sol_low.root
        
        # Upper bound
        sol_high = root_scalar(f_half, bracket=[f0, f_sub[-1]], method='brentq')
        f_high = sol_high.root
        
        bandwidth = f_high - f_low
        Q = f0 / bandwidth
        
        print(f"--- {label} ---")
        print(f"Peak Frequency (f0): {f0:.4f} THz")
        print(f"Peak Transmission |S21|^2: {peak_val:.4f}")
        print(f"3dB Bandwidth: {bandwidth*1000:.2f} GHz")
        print(f"Loaded Quality Factor (QL): {Q:.1f}\n")
        
        return f_fine, s21_fine, f0, peak_val, Q
    except ValueError as e:
        print(f"Error finding 3dB points for {label}: {e}")
        return f_fine, s21_fine, f0, peak_val, None

# Load the datasets
trench_data = pd.read_csv('../data/trench_3um_capacitor_gap.csv')
notrench_data = pd.read_csv('../data/notrench_3um_capacitor_gap.csv')

# --- Process Trench Data ---
f_trench = trench_data['f(THz)'].values
Y_trench_power = trench_data['Y'].values**2
f_fine_t, s21_fine_t, f0_t, peak_t, Q_t = extract_q_from_spline(f_trench, Y_trench_power, "GaAs With Trench (3um gap)")

# --- Process No-Trench Data ---
# Frequency is in Hz, convert to THz
f_notrench = notrench_data['f(Hz)'].values / 1e12
Y_notrench_power = notrench_data['Y'].values**2
f_fine_nt, s21_fine_nt, f0_nt, peak_nt, Q_nt = extract_q_from_spline(f_notrench, Y_notrench_power, "GaAs No Trench (3um gap)")

# --- Plotting ---
plt.figure(figsize=(10, 6))

plt.plot(f_fine_t, s21_fine_t, 'b-', linewidth=2, label=f'With Trench ($Q_L$ = {Q_t:.1f}, $f_0$ = {f0_t:.4f} THz)')
plt.plot(f_fine_nt, s21_fine_nt, 'r-', linewidth=2, label=f'No Trench ($Q_L$ = {Q_nt:.1f}, $f_0$ = {f0_nt:.4f} THz)')

# Scatter original points to show it's a fit
mask_t = (f_trench >= 0.4) & (f_trench <= 0.8)
plt.scatter(f_trench[mask_t], Y_trench_power[mask_t], color='blue', s=20, alpha=0.5)

mask_nt = (f_notrench >= 0.4) & (f_notrench <= 0.8)
plt.scatter(f_notrench[mask_nt], Y_notrench_power[mask_nt], color='red', s=20, alpha=0.5)

# Formatting
plt.title('High-Resolution Spline: Trench vs No Trench (GaAs, 3\u03BCm Gap)', fontsize=14)
plt.xlabel('Frequency (THz)', fontsize=12)
plt.ylabel('Power Transmission $|S_{21}|^2$', fontsize=12)
plt.xlim([0.45, 0.75])  # Zoomed into the fundamental resonance window
plt.ylim([0, max(peak_t, peak_nt) * 1.2]) 
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.legend(fontsize=12, loc='upper left')
plt.tight_layout()

# Save plot
os.makedirs("../figures", exist_ok=True)
plot_path = '../figures/spline_comparison_trench_vs_notrench_3um.png'
plt.savefig(plot_path, dpi=600)
print(f"High-resolution comparison plot saved to: {plot_path}")
