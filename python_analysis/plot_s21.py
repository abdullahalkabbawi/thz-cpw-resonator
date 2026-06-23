"""
plot_s21.py
MSc Project — THz CPW Resonator

Plot S21 transmission spectra from CSV files for gap-size or
cavity-length sweeps.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]


def load_s21(csv_path):
    """Load frequency and S21 data from a two-column CSV file."""
    df = pd.read_csv(csv_path)
    return df["frequency_THz"].values, df["S21_dB_norm"].values


def plot_gap_sweep(data_dir, gaps_um, save_path=None):
    """
    Plot S21 for multiple coupling gap sizes.

    Parameters
    ----------
    data_dir : str or Path, directory containing gap CSV files
    gaps_um  : list of float, gap sizes in µm
    save_path: str or None, path to save figure
    """
    data_dir = Path(data_dir)
    fig, ax = plt.subplots(figsize=(8, 5))

    for i, g in enumerate(gaps_um):
        fname = data_dir / f"gap_{str(g).replace('.', 'p')}um_norm.csv"
        try:
            freq, s21 = load_s21(fname)
            ax.plot(freq, s21, color=COLORS[i % len(COLORS)], lw=1.4,
                    label=f"Gap = {g} µm")
        except FileNotFoundError:
            print(f"File not found: {fname}")

    ax.set_xlabel("Frequency (THz)")
    ax.set_ylabel("$S_{21}$ (dB, normalised)")
    ax.set_title("Gap sweep — CPW resonator transmission")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150)
        print(f"Saved: {save_path}")

    plt.show()
    return fig


def plot_length_sweep(data_dir, lengths_um, save_path=None):
    """
    Plot S21 for multiple cavity lengths.

    Parameters
    ----------
    data_dir    : str or Path
    lengths_um  : list of float, cavity lengths in µm
    save_path   : str or None
    """
    data_dir = Path(data_dir)
    fig, ax = plt.subplots(figsize=(8, 5))

    for i, L in enumerate(lengths_um):
        fname = data_dir / f"length_{str(L).replace('.', 'p')}um_norm.csv"
        try:
            freq, s21 = load_s21(fname)
            ax.plot(freq, s21, color=COLORS[i % len(COLORS)], lw=1.4,
                    label=f"$L_{{\\rm cav}}$ = {L} µm")
        except FileNotFoundError:
            print(f"File not found: {fname}")

    ax.set_xlabel("Frequency (THz)")
    ax.set_ylabel("$S_{21}$ (dB, normalised)")
    ax.set_title("Cavity length sweep — IDC resonator transmission")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150)
        print(f"Saved: {save_path}")

    plt.show()
    return fig


if __name__ == "__main__":
    # Gap sweep plot
    plot_gap_sweep(
        data_dir="../data/gap_sweep",
        gaps_um=[5, 3, 1, 0.8],
        save_path="../figures/s21_gap_sweep.png",
    )

    # IDC cavity length sweep plot
    plot_length_sweep(
        data_dir="../data/idc_sweep",
        lengths_um=[30, 40, 50, 60, 70.75],
        save_path="../figures/s21_idc_length_sweep.png",
    )
