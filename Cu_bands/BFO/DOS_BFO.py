# -*- coding=utf-8 -*-

import sys
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.gridspec import GridSpec

from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.core import Spin, OrbitalType


if __name__ == "__main__":
    # read data
    # ---------

    # density of states
    dosrun = Vasprun("./DOS/vasprun.xml")
    spd_dos = dosrun.complete_dos.get_spd_dos()

    # set up matplotlib plot
    # ----------------------

    # general options for plot
    font = {'family': 'serif', 'size': 24}
    plt.rc('font', **font)

    # set up 2 graph with aspec ration 2/1
    # plot 1: bands diagram
    # plot 2: Density of States
    #gs = GridSpec(1, 2, width_ratios=[2, 1])
    gs = GridSpec(1, 1)
#    fig = plt.figure(figsize=(11.69, 8.27))
    fig = plt.figure(figsize=(12, 8))
    fig.suptitle("Bands diagram of copper")
#    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[0])  # , sharey=ax1)

    # set ylim for the plot
    # ---------------------
    emin = -40.
    emax = 40.
#    ax1.set_ylim(emin, emax)
    ax2.set_ylim(emin, emax)

    # Band Diagram
    # ------------
    name = "Cu"

    # Density of states
    # ----------------

    ax2.set_xticks([])
    ax2.set_yticklabels([])
    ax2.grid()
    ax2.set_ylim(1e-4, 20)
    ax2.set_xticklabels([])
    ax2.hlines(y=0, xmin=0, xmax=5, color="k", lw=2)
    ax2.set_ylabel("Density of States", labelpad=28)
    ax2.set_xlabel("Energy (eV)", labelpad=28)

    # spd contribution
    ax2.plot(dosrun.tdos.energies - dosrun.efermi,
             spd_dos[OrbitalType.s].densities[Spin.up],
             "r-", label="3s", lw=2)
    ax2.plot(dosrun.tdos.energies - dosrun.efermi,
             spd_dos[OrbitalType.p].densities[Spin.up],
             "g-", label="3p", lw=2)
    ax2.plot(dosrun.tdos.energies - dosrun.efermi,
             spd_dos[OrbitalType.d].densities[Spin.up],
             "b-", label="3d", lw=2)

    # total dos
    ax2.fill_between(dosrun.tdos.energies - dosrun.efermi,
                     dosrun.tdos.densities[Spin.up],
                     0,
                     color=(0.7, 0.7, 0.7),
                     facecolor=(0.7, 0.7, 0.7))

    ax2.plot(dosrun.tdos.energies - dosrun.efermi,
             dosrun.tdos.densities[Spin.up],
             color=(0.6, 0.6, 0.6),
             label="total DOS")

    # plot format style
    # -----------------
    ax2.legend(fancybox=True, shadow=True, prop={'size': 18})
    plt.subplots_adjust(wspace=0)

    # plt.show()
#    plt.tight_layout()
    plt.savefig(sys.argv[0].strip(".py") + ".pdf", format="pdf")
