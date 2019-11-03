''' Stores the configuration of the program '''

# Reproduction
# Max number of edges that added and removed
MAX_EDGE_CHANGE_COUNT = 3


# Training
# Note:
# POPULATION_SIZE = SELECTION_SIZE * REPRODUCTION_PER_SELECTION_SIZE + RANDOM_NEW_POPULATION_SIZE
POPULATION_SIZE = 10
SELECTION_SIZE = 3
REPRODUCTION_PER_SELECTION_SIZE = 2
RANDOM_NEW_POPULATION_SIZE = 4

# Tournament Selection
# Note: K_COUNT must be lower than POPULATION_SIZE
# More information on
# https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_parent_selection.htm
K_COUNT = 5


# Environment
RENDER = False

# time limit in seconds
TIME_LIMIT = 5
