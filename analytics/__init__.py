'''Module for showing the analytics'''
import matplotlib.pyplot as plt
import numpy as np

from creature import Creature

TITLE_SIZE = 12
LABEL_SIZE = 10


def create_analytics_data(generations, serializable_creatures,):
    ''' Creates the necessary data for plots '''
    medians = []
    histogram = []
    species = {}
    generations_count = len(generations)
    for i, generation in enumerate(generations):
        median_index = (len(generation) - 1)//2
        creature_id = generation[median_index]
        creature = serializable_creatures[creature_id]
        medians.append(creature['fitness'])
        for creature_id in generation:
            creature = serializable_creatures[creature_id]
            creature = Creature(**creature)
            cspecies = creature.get_species()
            if cspecies not in species:
                species[cspecies] = [0] * generations_count
            species[cspecies][i] += 1

    for creature_id in generations[-1]:
        creature = serializable_creatures[creature_id]
        histogram.append(int(creature['fitness']))
    return histogram, medians, species


def show_analytics(generation_number, generations, serializable_creatures):
    ''' Shows the analytcs using matplotlib '''
    histogram, medians, species = create_analytics_data(generations, serializable_creatures)
    fig = plt.figure()

    fig.canvas.set_window_title('Analytics')

    # histogram
    plt.subplot2grid((2, 2), (0, 0))
    plt.hist(histogram, bins=60)
    plt.title(f'Histogram of generation #{generation_number}', fontsize=TITLE_SIZE)
    plt.xlabel('Fitness Value', fontsize=LABEL_SIZE)
    plt.ylabel('Number of Species', fontsize=LABEL_SIZE)

    # medians
    plt.subplot2grid((2, 2), (0, 1))
    plt.plot(range(1, len(medians)+1), medians)
    plt.title(f'Median fitness of all generations', fontsize=TITLE_SIZE)
    plt.ylabel('Median Fitness', fontsize=LABEL_SIZE)
    plt.xlabel('Generation', fontsize=LABEL_SIZE)

    # stackedplot for species
    plt.subplot2grid((2, 2), (1, 0), colspan=2)
    plt.stackplot(range(1, len(medians)+1), list(species.values()), labels=list(species.keys()))
    plt.title(f'Species population according to generations', fontsize=TITLE_SIZE)
    plt.ylabel('Number of Creatures', fontsize=LABEL_SIZE)
    plt.xlabel('Generation', fontsize=LABEL_SIZE)

    plt.legend(title='Species', title_fontsize=8, prop={'size': 8}, loc='lower left', ncol=8)
    fig.tight_layout()
    plt.show()
