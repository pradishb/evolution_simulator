import numpy as np


def create_creature_connection_graph(size):
    "Generation of random graph"
    graph_size = (size*(size-1))//2
    return np.random.randint(2, size=graph_size)
