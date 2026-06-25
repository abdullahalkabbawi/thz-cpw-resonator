import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the datasets
trench_data = pd.read_csv('../data/trench_3um_capacitor_gap.csv')
notrench_data = pd.read_csv('../data/notrench_3um_capacitor_gap.csv')

# --- Process Trench Data ---
# Frequency is already in THz
f_trench = trench_data['f(THz)'].values
# Calculate Power Transmission |S21|^2
Y_trench_power = trench_data['Y'].values**2

# --- Process No-Trench Data ---
# Frequency is in Hz, convert to THz
f_notrench = notrench_data['f(Hz)'].values / 1e12
# Calculate Power Transmission |S21|^2
Y_notrench_power = notrench_data['Y'].values**2

# --- Plotting ---
plt.figure(figsize=(10, 6))

# Plot both lines
plt.plot(f_trench, Y_trench_power, 'b-', linewidth=2, label='With Trench (Q = 38.7)')
plt.plot(f_notrench, Y_notrench_power, 'r--', linewidth=2, label='No Trench (Q = 17.5)')

# Highlight the peaks
trench_peak_idx = np.argmax(Y_trench_power[(f_trench >= 0.1) & (f_trench <= 1.0)])
f_trench_peak = f_trench[(f_trench >= 0.1) & (f_trench <= 1.0)][trench_peak_idx]
y_trench_peak = Y_trench_power[(f_trench >= 0.1) & (f_trench <= 1.0)][trench_peak_idx]

notrench_peak_idx = np.argmax(Y_notrench_power[(f_notrench >= 0.1) & (f_notrench <= 1.0)])
f_notrench_peak = f_notrench[(f_notrench >= 0.1) & (f_notrench <= 1.0)][notrench_peak_idx]
y_notrench_peak = Y_notrench_power[(f_notrench >= 0.1) & (f_notrench <= 1.0)][notrench_peak_idx]

plt.plot(f_trench_peak, y_trench_peak, 'bo', markersize=8)
plt.plot(f_notrench_peak, y_notrench_peak, 'ro', markersize=8)

# Formatting
plt.title('THz CPW Resonator Comparison (3\u03BCm Gap): Trench vs No Trench', fontsize=14, pad=15)
plt.xlabel('Frequency (THz)', fontsize=12)
plt.ylabel('Power Transmission |S21|\u00B2', fontsize=12)
plt.xlim([0.4, 0.9])  # Zoomed into the fundamental resonance window
plt.ylim([0, 0.2])   # Scaled nicely
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend(fontsize=12, loc='upper left')
plt.tight_layout()

# Save plot
plot_path = '../figures/comparison_trench_vs_notrench_3um.png'
plt.savefig(plot_path, dpi=300)
print(f"Comparison plot successfully saved to: {plot_path}")
plt.show()
