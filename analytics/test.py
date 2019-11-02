"Histogram"
import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import colors
# from matplotlib.ticker import PercentFormatter

plt.style.use('fivethirtyeight')

x = [0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 6, 6, 7, 7, 7, 7, 8, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11]
plt.hist(x, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], edgecolor='black')
plt.ylim((0, 10)) #sets y limits

MEDIAN = (max(x)+1)/2
plt.axvline(MEDIAN, color='r', label='Median')
plt.legend(loc='best')

plt.xlabel('Fitness Value')
plt.ylabel('Number of species')

# plt.tight_layout()
plt.show()
