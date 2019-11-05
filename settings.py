''' Stores the configuration of the program '''

# Reproduction
# Max number of edges that added and removed
MAX_EDGE_CHANGE_COUNT = 3
MAX_VERTICES_PIXEL_CHANGE = 2
MAX_SIZE = 7

# Creature
MIN_VERTICES_COUNT = 4
MAX_VERTICES_COUNT = 7
DENSITY = 3
FRICTION = 0.8

# Training
# Note:
# POPULATION_SIZE = SELECTION_SIZE * REPRODUCTION_PER_SELECTION_SIZE + RANDOM_NEW_POPULATION_SIZE
POPULATION_SIZE = 100
SELECTION_SIZE = 30
OFFSPRINGS_PER_SELECTION_SIZE = 1
RANDOM_NEW_POPULATION_SIZE = 40

# Tournament Selection
# Note: K_COUNT must be lower than POPULATION_SIZE
# More information on
# https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_parent_selection.htm
K_COUNT = 10

# Environment
STEP_LIMIT = 20 * 60  # step count, 60 steps = 1 sec
MOTOR_SPEED = 50
MAX_MOTOR_TORQUE = 150
