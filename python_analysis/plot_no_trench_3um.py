import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load the data
data_path = '../data/notrench_3um_capacitor_gap.csv'
df = pd.read_csv(data_path)

# Convert frequency from Hz to THz
f_thz = df['f(Hz)'].values / 1e12

# Convert Transmission |S21| to Power Transmission |S21|^2
Y_mag = df['Y'].values
Y_power = Y_mag**2

# Zoom in on the fundamental mode (e.g. 0.1 THz to 1.0 THz)
# This ignores the second harmonic mode
zoom_mask = (f_thz >= 0.1) & (f_thz <= 1.0)
f_zoom = f_thz[zoom_mask]
Y_zoom = Y_power[zoom_mask]

# Find peaks (resonances) in the zoomed data
peaks, properties = find_peaks(Y_zoom, prominence=0.005)

print("--- RESONANCE ANALYSIS (NO TRENCH) ---")

plt.figure(figsize=(10, 6))
plt.plot(f_zoom, Y_zoom, '-', label='Power Transmission |S21|²')

# Extract Q factor for the fundamental peak
for i, peak_idx in enumerate(peaks):
    f_res = f_zoom[peak_idx]
    y_max = Y_zoom[peak_idx]
    
    # Calculate half-power points (Since Y is already power |S21|^2, half is y_max / 2)
    y_half = y_max / 2.0
    
    # Interpolate to find exact FWHM frequencies
    # Left side of the peak
    left_side_f = f_zoom[:peak_idx]
    left_side_y = Y_zoom[:peak_idx]
    f1 = np.interp(y_half, left_side_y, left_side_f)
    
    # Right side of the peak
    right_side_f = f_zoom[peak_idx:]
    right_side_y = Y_zoom[peak_idx:]
    # np.interp needs x to be monotonically increasing, so we reverse it
    f2 = np.interp(y_half, right_side_y[::-1], right_side_f[::-1])
    
    delta_f = f2 - f1
    Q = f_res / delta_f
    
    print(f"\nFundamental Mode:")
    print(f"  Resonance Frequency (f_r): {f_res:.4f} THz")
    print(f"  Peak Power (|S21|²):       {y_max:.4f}")
    print(f"  3dB Bandwidth (\u0394f):      {delta_f:.4f} THz")
    print(f"  Loaded Q Factor (Q_L):     {Q:.2f}")
    
    # Plotting annotations
    plt.plot(f_res, y_max, 'ro', label=f'Peak ({f_res:.3f} THz)')
    plt.hlines(y_half, f1, f2, color='red', linestyle='--', label=f'FWHM (Q={Q:.1f})')
    plt.vlines([f1, f2], 0, y_half, color='gray', linestyle=':')

plt.title('THz CPW Resonator - 3\u03BCm Gap (NO TRENCH)')
plt.xlabel('Frequency (THz)')
plt.ylabel('Power Transmission |S21|²')
plt.xlim([0.1, 1.0])
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# Save plot
plot_path = '../figures/resonance_notrench_3um.png'
plt.savefig(plot_path, dpi=300)
print(f"\nPlot saved successfully to: {plot_path}")
plt.show()
