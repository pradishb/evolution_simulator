'''Module for showing the analytics'''
import matplotlib.pyplot as plt
import numpy as np


def show_analytics(generation, histogram, medians, species):
    ''' Shows the analytcs using matplotlib '''
    fig = plt.figure()
    fig.canvas.set_window_title('Analytics')

    # histogram
    plt.subplot2grid((2, 2), (0, 0))
    plt.hist(histogram, edgecolor='black')
    plt.title(f'Histogram of generation #{generation}')
    plt.xlabel('Fitness Value')
    plt.ylabel('Number of species')

    # medians
    plt.subplot2grid((2, 2), (1, 0))
    plt.plot(medians)
    plt.title(f'Median fitness of all generations')
    plt.ylabel('Median Fitness')
    plt.xlabel('Generation')

    # stackedplot for species
    plt.subplot2grid((2, 2), (0, 1), rowspan=2)
    plt.stackplot(range(1, len(medians)+1), list(species.values()), labels=list(species.keys()))
    plt.title(f'Species population according to generations')
    plt.ylabel('Species Count')
    plt.xlabel('Generation')
    plt.legend(loc='upper left')
    plt.show()
