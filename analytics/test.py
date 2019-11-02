"""
==========
Histograms
==========

Demonstrates how to plot histograms with matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# Fixing random state for reproducibility
np.random.seed(100)

N_points = 1000
n_bins = 5

# Generate a normal distribution, center at x=0 and y=5
x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#y = [10.0, 6.0, 7.0, 8.0, 9.0]

fig, axs = plt.subplots(1, 2, sharey=False, tight_layout=True)

# We can set the number of bins with the `bins` kwarg
axs[0].hist(x, bins=n_bins)
#axs[1].hist(y, bins=n_bins)

plt.show()
