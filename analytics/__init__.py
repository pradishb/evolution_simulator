'''Module for showing the analytics'''
import matplotlib.pyplot as plt
import numpy as np

LABEL_SIZE = 9

def show_analytics(generation, histogram, medians, species):
    ''' Shows the analytcs using matplotlib '''
    fig = plt.figure()
    fig.canvas.set_window_title('Analytics')

    # histogram
    plt.subplot2grid((2, 2), (0, 0))
    plt.hist(histogram, edgecolor='black')
    plt.title(f'Histogram of generation #{generation}', fontsize=10)
    plt.xlabel('Fitness Value', fontsize=LABEL_SIZE)
    plt.ylabel('Number of species', fontsize=LABEL_SIZE)

    # medians
    plt.subplot2grid((2, 2), (1, 0))
    plt.plot(medians)
    plt.title(f'Median fitness of all generations', fontsize=10)
    plt.ylabel('Median Fitness', fontsize=LABEL_SIZE)
    plt.xlabel('Generation', fontsize=LABEL_SIZE)

    # stackedplot for species
    plt.subplot2grid((2, 2), (0, 1), rowspan=2)
    plt.stackplot(range(1, len(medians)+1), list(species.values()), labels=list(species.keys()))
    plt.title(f'Species population according to generations', fontsize=10)
    plt.ylabel('Species Count', fontsize=LABEL_SIZE)
    plt.xlabel('Generation', fontsize=LABEL_SIZE)
    plt.legend(loc='upper left', prop={'size': 6})
    # plt.subplots_adjust(hspace=1, wspace=1)
    fig.canvas.manager.full_screen_toggle()
    fig.tight_layout()
    plt.show()
