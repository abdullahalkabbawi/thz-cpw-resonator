import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load the data
data_path = '../data/trench_3um_capacitor_gap.csv'
df = pd.read_csv(data_path)

f = df['f(THz)'].values
Y = df['Y'].values

# Find peaks (resonances)
# Using a prominence to ignore tiny numerical ripples
peaks, properties = find_peaks(Y, prominence=0.05)

print("--- RESONANCE ANALYSIS ---")
print(f"Found {len(peaks)} main resonance mode(s).")

plt.figure(figsize=(10, 6))
plt.plot(f, Y, '-', label='Transmission |S21|')

# Extract Q factor for each peak
for i, peak_idx in enumerate(peaks):
    f_res = f[peak_idx]
    y_max = Y[peak_idx]
    
    # Calculate half-power points
    # Assuming Y is linear magnitude |S21|, half power is y_max / sqrt(2)
    # If Y is already power |S21|^2, half power is y_max / 2
    # We will use magnitude (y_max / 1.414) as is standard for S-parameters
    y_half = y_max / np.sqrt(2)
    
    # Interpolate to find exact FWHM frequencies
    # Left side of the peak
    left_side_f = f[:peak_idx]
    left_side_y = Y[:peak_idx]
    f1 = np.interp(y_half, left_side_y, left_side_f)
    
    # Right side of the peak
    right_side_f = f[peak_idx:]
    right_side_y = Y[peak_idx:]
    # np.interp needs x to be monotonically increasing, so we reverse it
    f2 = np.interp(y_half, right_side_y[::-1], right_side_f[::-1])
    
    delta_f = f2 - f1
    Q = f_res / delta_f
    
    print(f"\nMode {i+1}:")
    print(f"  Resonance Frequency (f_r): {f_res:.4f} THz")
    print(f"  Peak Amplitude (|S21|):    {y_max:.4f}")
    print(f"  3dB Bandwidth (\u0394f):      {delta_f:.4f} THz")
    print(f"  Loaded Q Factor (Q_L):     {Q:.2f}")
    
    # Plotting annotations
    plt.plot(f_res, y_max, 'ro', label=f'Peak {i+1} ({f_res:.3f} THz)')
    plt.hlines(y_half, f1, f2, color='red', linestyle='--', label=f'FWHM {i+1} (Q={Q:.1f})')
    plt.vlines([f1, f2], 0, y_half, color='gray', linestyle=':')

plt.title('THz CPW Resonator - 3\u03BCm Gap (Trench Model)')
plt.xlabel('Frequency (THz)')
plt.ylabel('Transmission Magnitude |S21|')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# Save plot
plot_path = '../figures/resonance_trench_3um.png'
plt.savefig(plot_path, dpi=300)
print(f"\nPlot saved successfully to: {plot_path}")
plt.show()
