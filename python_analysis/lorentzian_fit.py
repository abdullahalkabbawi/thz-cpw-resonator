"""
lorentzian_fit.py
MSc Project — THz CPW Resonator

Fit a Lorentzian lineshape to S21 transmission data to extract:
  - resonance frequency f0
  - full width at half maximum (FWHM) Δf
  - loaded quality factor Q_L = f0 / Δf
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def lorentzian(f, f0, gamma, A, offset):
    """
    Lorentzian lineshape.

    Parameters
    ----------
    f      : array-like, frequency (Hz or THz)
    f0     : float, resonance frequency
    gamma  : float, half-width at half-maximum (HWHM)
    A      : float, amplitude
    offset : float, vertical offset

    Returns
    -------
    array-like, Lorentzian evaluated at f
    """
    return offset + A * (gamma**2) / ((f - f0)**2 + gamma**2)


def fit_lorentzian(freq, s21_db, f_min=None, f_max=None):
    """
    Fit a Lorentzian to S21 (dB) data.

    Parameters
    ----------
    freq   : array-like, frequency axis (THz)
    s21_db : array-like, S21 in dB (normalised)
    f_min  : float, lower bound of fit window (THz)
    f_max  : float, upper bound of fit window (THz)

    Returns
    -------
    dict with keys: f0, delta_f, Q_L, popt, pcov
    """
    freq = np.asarray(freq)
    s21_db = np.asarray(s21_db)

    # Restrict to fit window
    mask = np.ones(len(freq), dtype=bool)
    if f_min is not None:
        mask &= freq >= f_min
    if f_max is not None:
        mask &= freq <= f_max

    f_fit = freq[mask]
    s_fit = s21_db[mask]

    # Initial guesses
    i_peak = np.argmax(s_fit)
    f0_guess = f_fit[i_peak]
    gamma_guess = (f_fit[-1] - f_fit[0]) / 10
    A_guess = s_fit[i_peak] - s_fit.min()
    offset_guess = s_fit.min()

    p0 = [f0_guess, gamma_guess, A_guess, offset_guess]
    popt, pcov = curve_fit(lorentzian, f_fit, s_fit, p0=p0, maxfev=10000)

    f0, gamma, A, offset = popt
    delta_f = 2 * abs(gamma)  # FWHM
    Q_L = f0 / delta_f

    return {
        "f0": f0,
        "delta_f": delta_f,
        "Q_L": Q_L,
        "popt": popt,
        "pcov": pcov,
        "f_fit": f_fit,
        "s_fit": s_fit,
    }


def plot_fit(freq, s21_db, result, title="Lorentzian fit", save_path=None):
    """Plot S21 data with the Lorentzian fit overlaid."""
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(freq, s21_db, "C0", lw=1.2, label="Simulation")
    ax.plot(
        result["f_fit"],
        lorentzian(result["f_fit"], *result["popt"]),
        "C1--",
        lw=1.5,
        label="Lorentzian fit",
    )
    ax.axvline(result["f0"], color="C2", ls=":", lw=1, label=f"$f_0$ = {result['f0']:.4f} THz")
    ax.set_xlabel("Frequency (THz)")
    ax.set_ylabel("$S_{21}$ (dB, normalised)")
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    plt.show()
    return fig


if __name__ == "__main__":
    # Example: load data and fit
    # Replace with your actual CSV path
    # Expected columns: frequency_THz, S21_dB_norm
    data_path = "../data/gap_sweep/gap_1um_norm.csv"

    try:
        df = pd.read_csv(data_path)
        freq = df["frequency_THz"].values
        s21 = df["S21_dB_norm"].values

        result = fit_lorentzian(freq, s21, f_min=0.5, f_max=0.9)

        print(f"Resonance frequency  f0   = {result['f0']:.4f} THz")
        print(f"FWHM                 Δf   = {result['delta_f']*1e3:.2f} GHz")
        print(f"Loaded quality factor Q_L = {result['Q_L']:.2f}")

        plot_fit(freq, s21, result, title="Gap = 1 µm", save_path="../figures/lorentzian_fit.png")

    except FileNotFoundError:
        print(f"Data file not found: {data_path}")
        print("Run the Lumerical simulation first and export the S21 data.")
