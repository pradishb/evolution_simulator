''' Module for the utility functions of the program '''
from datetime import datetime
from settings import POPULATION_SIZE


def get_default_name():
    ''' Returns a default name value '''
    return f'P{POPULATION_SIZE}_{datetime.now().strftime("%m-%d-%YT%H-%M")}'
