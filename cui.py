''' Main script of the program '''

import os
import random
from argparse import ArgumentParser
from copy import copy

from tqdm import tqdm

from reproduction import reproduce
from creature import Creature
from file import save_generations, load_generations
from simulation import Simulation
from settings import (
    POPULATION_SIZE, SELECTION_SIZE, OFFSPRINGS_PER_SELECTION_SIZE, RANDOM_NEW_POPULATION_SIZE,
    MIN_VERTICES_COUNT, MAX_VERTICES_COUNT, MAX_SIZE, K_COUNT)
from util import get_default_name
COL_COUNT = 8


def create_directories():
    "Creates necesesary directories"
    os.makedirs('data/generations', exist_ok=True)


class Cui:
    ''' Main cui class '''

    def __init__(self, repeat=100, load_path=None):
        self.repeat = repeat
        self.completed = 0
        self.load_path = load_path
        self.save_as = get_default_name()
        self.simulation = Simulation()
        self.creatures = []
        self.serializable_creatures = {}
        self.generations = []

    def create_generation(self):
        ''' Creates a generation file '''
        print('Saving the generations data to file')
        creatures = []
        for creature in self.creatures:
            data = creature.get_data()
            self.serializable_creatures[creature.identity] = data
            creatures.append(creature.identity)
        self.generations.append(creatures)
        save_generations(
            self.generations,
            self.serializable_creatures,
            self.save_as,
        )

    def threaded_create(self):
        ''' Creates an initial population of creatures '''
        print('Creating initial population')
        for _ in range(POPULATION_SIZE):
            creature = Creature(
                n=random.randint(MIN_VERTICES_COUNT, MAX_VERTICES_COUNT),
                size=MAX_SIZE)
            self.creatures.append(creature)

    def threaded_find_fitness_no_gui(self):
        ''' Finds the fitness of all the creatures with render off '''
        print('Finding the fitness of all the population')
        fitness = self.simulation.simulate(self.creatures)
        for creature in self.creatures:
            creature.fitness = fitness[creature.identity]

    def threaded_sort(self):
        ''' Sorts the creatures based on the fitness values '''
        print('Sorting the population according to the fitness')
        self.creatures.sort(key=lambda c: c.fitness, reverse=True)
        self.completed += 1
        print('-'*100)
        print(f'End of generation #{self.get_generation()}')
        print(f'Max fitness: {"{:.2f}".format(self.creatures[0].fitness)}')
        print(f'{self.completed}/{self.repeat} generations completed')
        print('-'*100)
        self.create_generation()

    def threaded_selection(self):
        ''' Selects the creatures based on the fitness values '''
        print('Selecting the creatures based on the fitness values')
        selected_population = []
        creatures = copy(self.creatures)
        for _ in range(SELECTION_SIZE):
            selected = max(random.choices(creatures, k=K_COUNT), key=lambda c: c.fitness)
            selected_population.append(selected)
            creatures.remove(selected)

        for _, creature in enumerate(copy(self.creatures)):
            if creature not in selected_population:
                self.creatures.remove(creature)

    def threaded_reproduce(self):
        ''' Reproduces the creatures '''
        print('Reproducing the creatures')
        creatures = copy(self.creatures)
        self.creatures = []
        for creature in creatures:
            self.creatures.append(creature)
            for _ in range(OFFSPRINGS_PER_SELECTION_SIZE):
                offspring = reproduce(creature)
                self.creatures.append(offspring)

        for _ in range(RANDOM_NEW_POPULATION_SIZE):
            creature = Creature(
                n=random.randint(MIN_VERTICES_COUNT, MAX_VERTICES_COUNT),
                size=MAX_SIZE)
            self.creatures.append(creature)

    def threaded_train(self):
        ''' Does training for x generations '''
        if self.load_path is None:
            self.completed -= 1
            self.threaded_create()
            self.threaded_find_fitness_no_gui()
            self.threaded_sort()
        else:
            self.threaded_load()
        for _ in range(self.repeat):
            self.threaded_selection()
            self.threaded_reproduce()
            self.threaded_find_fitness_no_gui()
            self.threaded_sort()

    def threaded_load(self):
        ''' Loads the saved data from file '''
        data = load_generations(self.load_path)
        self.serializable_creatures = data['creatures']
        self.generations = data['generations']

        self.creatures = []
        for creature_id in self.generations[-1]:
            creature_data = self.serializable_creatures[creature_id]
            creature = Creature(**creature_data)
            self.creatures.append(creature)

    def get_generation(self):
        ''' Returns the current generation '''
        return len(self.generations)+1


def main():
    ''' Main function of the script '''
    parser = ArgumentParser(description='Script to train the creatures using cli')
    parser.add_argument('--load-path', '-l', help='path to the exisiting generations data')
    parser.add_argument('--repeat', '-r', help='number of generations to train', default=100)

    args = parser.parse_args()

    try:
        cui = Cui(int(args.repeat), args.load_path)
        cui.threaded_train()
    except ValueError:
        print('Make sure that repeat argument is an integer')


if __name__ == '__main__':
    create_directories()
    main()
