''' Module to create offsprings of a creature '''
from random import randint, choice, shuffle
from creature import Creature
from creature import get_all_possible_edges

from settings import MAX_EDGE_CHANGE_COUNT


def reproduce(creature: Creature):
    ''' Creates a offsprings of a creature by adding or removing some edges '''
    offspring = Creature(creature.n, creature.view_port, creature.size)
    offspring.vertices = creature.vertices
    offspring.edges = creature.edges

    all_edges = get_all_possible_edges(offspring.n)
    add_list = all_edges - set(offspring.edges)
    remove_list = set(filter(lambda edge: edge[0] + 1 != edge[1], offspring.edges))
    add = choice([True, False]) if add_list != set() else False
    if remove_list == set():
        add = True

    if add:
        # Adding edges logic
        edges = set(offspring.edges)
        for _ in range(randint(1, MAX_EDGE_CHANGE_COUNT)):
            if add_list == set():
                break
            random_edge = choice(list(add_list))
            add_list -= {(random_edge)}
            edges = edges.union({(random_edge)})
        offspring.edges = list(edges)
    else:
        # Removing edges logic
        edges = set(offspring.edges)
        for _ in range(randint(1, MAX_EDGE_CHANGE_COUNT)):
            if remove_list == set():
                break
            random_edge = choice(list(remove_list))
            remove_list -= {(random_edge)}
            edges = edges - {random_edge}
        offspring.edges = list(edges)

    return offspring
