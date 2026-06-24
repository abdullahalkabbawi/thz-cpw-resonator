import io
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Configure matplotlib for headless environment if needed
os.environ["MPLBACKEND"] = "Agg"

# ---------------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------------
data_str = """f(THz), Y
0.1, 0.058458
0.107, 0.0680156
0.114, 0.0773864
0.121, 0.0885805
0.128, 0.0988577
0.135, 0.110985
0.142, 0.122846
0.149, 0.135235
0.156, 0.149148
0.163, 0.161871
0.17, 0.177395
0.177, 0.190761
0.184, 0.206998
0.191, 0.221673
0.198, 0.23775
0.205, 0.253891
0.212, 0.269387
0.219, 0.286897
0.226, 0.302165
0.233, 0.320216
0.24, 0.33583
0.247, 0.353638
0.254, 0.370019
0.261, 0.387096
0.268, 0.404092
0.275, 0.420331
0.282, 0.437397
0.289, 0.453089
0.296, 0.469655
0.303, 0.484993
0.31, 0.500326
0.317, 0.515538
0.324, 0.529873
0.331, 0.544397
0.338, 0.557838
0.345, 0.571114
0.352, 0.583795
0.359, 0.595454
0.366, 0.607339
0.373, 0.617369
0.38, 0.628079
0.387, 0.636712
0.394, 0.645756
0.401, 0.65328
0.408, 0.660308
0.415, 0.6668
0.422, 0.671779
0.429, 0.677064
0.436, 0.680266
0.443, 0.684192
0.45, 0.68624
0.457, 0.688452
0.464, 0.689425
0.471, 0.689872
0.478, 0.68988
0.485, 0.68884
0.492, 0.68812
0.499, 0.686343
0.506, 0.684586
0.513, 0.682065
0.52, 0.679222
0.527, 0.676096
0.534, 0.672342
0.541, 0.668858
0.548, 0.664758
0.555, 0.660549
0.562, 0.656025
0.569, 0.651035
0.576, 0.646183
0.583, 0.640531
0.59, 0.6355
0.597, 0.629581
0.604, 0.623903
0.611, 0.617796
0.618, 0.611548
0.625, 0.605336
0.632, 0.598569
0.639, 0.592477
0.646, 0.585539
0.653, 0.579191
0.66, 0.572197
0.667, 0.565491
0.674, 0.558589
0.681, 0.551579
0.688, 0.54503
0.695, 0.537991
0.702, 0.531461
0.709, 0.524428
0.716, 0.51775
0.723, 0.510877
0.73, 0.504054
0.737, 0.497613
0.744, 0.490786
0.751, 0.484421
0.758, 0.477607
0.765, 0.47112
0.772, 0.464481
0.779, 0.457867
0.786, 0.451719
0.793, 0.445023
0.8, 0.438962
0.807, 0.43221
0.814, 0.425987
0.821, 0.419386
0.828, 0.412925
0.835, 0.406826
0.842, 0.399961
0.849, 0.393828
0.856, 0.386426
0.863, 0.379643
0.87, 0.371578
0.877, 0.363139
0.884, 0.353655
0.891, 0.340958
0.898, 0.326312
0.905, 0.305064
0.912, 0.286919
0.919, 0.276678
0.926, 0.278312
0.933, 0.296402
0.94, 0.307559
0.947, 0.30816
0.954, 0.307902
0.961, 0.304266
0.968, 0.300529
0.975, 0.295976
0.982, 0.290953
0.989, 0.285991
0.996, 0.280373
1.003, 0.275048
1.01, 0.269292
1.017, 0.263647
1.024, 0.258083
1.031, 0.252421
1.038, 0.246859
1.045, 0.24119
1.052, 0.235575
1.059, 0.230016
1.066, 0.224382
1.073, 0.219096
1.08, 0.213692
1.087, 0.208429
1.094, 0.203219
1.101, 0.19794
1.108, 0.192947
1.115, 0.187754
1.122, 0.183021
1.129, 0.178161
1.136, 0.173401
1.143, 0.168874
1.15, 0.164065
1.157, 0.159836
1.164, 0.155178
1.171, 0.151162
1.178, 0.14697
1.185, 0.142812
1.192, 0.139169
1.199, 0.134843
1.206, 0.131632
1.213, 0.127464
1.22, 0.124354
1.227, 0.120826
1.234, 0.117233
1.241, 0.114587
1.248, 0.110372
1.255, 0.108321
1.262, 0.103979
1.269, 0.101469
1.276, 0.0978796
1.283, 0.0929984
1.29, 0.0905024
1.297, 0.0807516
1.304, 0.0762342
1.311, 0.0530561
1.318, 0.0117136
1.325, 0.000115124
1.332, 0.00374956
1.339, 0.0153548
1.346, 0.0296728
1.353, 0.0376573
1.36, 0.0465121
1.367, 0.0487786
1.374, 0.0522555
1.381, 0.0534615
1.388, 0.0533185
1.395, 0.054678
1.402, 0.0528504
1.409, 0.0538119
1.416, 0.0521704
1.423, 0.0519137
1.43, 0.0513575
1.437, 0.0498926
1.444, 0.0503868
1.451, 0.0486051
1.458, 0.0494305
1.465, 0.0485273
1.472, 0.0487196
1.479, 0.0491308
1.486, 0.0482615
1.493, 0.0494528
1.5, 0.0477633
"""

data = np.loadtxt(io.StringIO(data_str), delimiter=',', skiprows=1)
freq = data[:, 0]  # Frequency in THz
y = data[:, 1]     # S-parameters or Y-value

# ---------------------------------------------------------
# 2. DEFINE LORENTZIAN FUNCTION
# ---------------------------------------------------------
def lorentzian(f, f0, df, A, y0):
    """
    f: Frequency array
    f0: Resonance frequency (peak center)
    df: Full Width at Half Maximum (FWHM)
    A: Peak amplitude height above baseline
    y0: Baseline offset
    """
    return y0 + A * (df/2)**2 / ((f - f0)**2 + (df/2)**2)

# ---------------------------------------------------------
# 3. INITIAL GUESS & CURVE FITTING
# ---------------------------------------------------------
# We select the peak region for fitting to ignore outer noise/dips (e.g. the notch at 1.32 THz)
# This focuses on the resonance behavior of the main mode around 0.47 THz.
fit_mask = (freq >= 0.2) & (freq <= 0.8)

idx_max = np.argmax(y)
f0_guess = freq[idx_max]
y0_guess = np.min(y)
A_guess = y[idx_max] - y0_guess
df_guess = 0.4  # Guess 400 GHz FWHM

p0 = [f0_guess, df_guess, A_guess, y0_guess]

popt, pcov = curve_fit(lorentzian, freq[fit_mask], y[fit_mask], p0=p0)
f0_fit, df_fit, A_fit, y0_fit = popt

# Calculate Quality Factor Q = f0 / df
Q_factor = f0_fit / df_fit

# Print metrics
print("=" * 40)
print("EXTRACTED RESONANCE PARAMETERS:")
print(f"Resonance Frequency (f0): {f0_fit:.4f} THz")
print(f"FWHM (df):                {df_fit * 1e3:.2f} GHz ({df_fit:.4f} THz)")
print(f"Quality Factor (Q):       {Q_factor:.4f}")
print("=" * 45)

# ---------------------------------------------------------
# 4. GENERATE PUBLICATION-STYLE PLOT
# ---------------------------------------------------------
plt.rcParams.update({
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'figure.titlesize': 12,
    'font.family': 'sans-serif'
})

fig, ax = plt.subplots(figsize=(5.0, 3.8), dpi=300)

# Plot raw data points (smaller size s=5, and transparent to see the curve)
ax.scatter(freq, y, color='#1f77b4', s=5, alpha=0.5, label='Raw Data')

# Plot Lorentzian fit line over the full range of interest
freq_fit_line = np.linspace(0.1, 1.2, 500)
y_fit_line = lorentzian(freq_fit_line, *popt)
ax.plot(freq_fit_line, y_fit_line, color='#d62728', lw=1.5, label='Lorentzian Fit')

# Add metrics text box (smaller box and text)
annotation_text = (
    f"$f_0 = {f0_fit:.3f}$ THz\n"
    f"$\\Delta f = {df_fit*1e3:.1f}$ GHz\n"
    f"$Q = {Q_factor:.3f}$"
)
ax.text(0.68, 0.75, annotation_text, transform=ax.transAxes,
        bbox=dict(facecolor='white', edgecolor='#dddddd', boxstyle='round,pad=0.3', alpha=0.9),
        fontsize=8, color='#333333')

# Labels and Styling
ax.set_xlabel('Frequency (THz)', fontweight='medium')
ax.set_ylabel('Amplitude (Y)', fontweight='medium')
ax.set_title('Resonance Extraction & Lorentzian Fitting', pad=8, fontweight='bold')
ax.grid(True, which='both', linestyle='--', alpha=0.3)
ax.legend(loc='upper right')
ax.set_xlim(0.1, 1.2)
ax.set_ylim(0, 0.8)

plt.tight_layout()

# Save figure
output_dir = 'figures'
os.makedirs(output_dir, exist_ok=True)
plot_path = os.path.join(output_dir, 'extracted_q_factor_fit.png')
plt.savefig(plot_path, dpi=300)
print(f"Plot saved successfully to: {plot_path}")
