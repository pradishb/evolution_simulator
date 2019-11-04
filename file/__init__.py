''' Module to save and load creature data to file '''
import pickle
import os

from creature import Creature


def save_creature(creature: dict):
    ''' Saves a single instance of creature to a file '''
    identity = creature['identity']
    file_path = f'data/creatures/{identity}.pickle'
    if not file_path:
        with open(file_path, 'wb') as file:
            pickle.dump(creature, file)


def save_generations(generations, creatures, file_name):
    ''' Saves generations data to a file '''
    file_path = f'data/generations/{file_name}.pickle'
    with open(file_path, 'wb') as file:
        pickle.dump({'generations': generations,
                     'creatures': creatures,
                     'creature_count': Creature.count}, file)


def load_generations(file_path):
    ''' Loads generations data from a file '''
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
        Creature.count = data['creature_count']
        return data
