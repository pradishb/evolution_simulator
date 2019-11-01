from math import sqrt
import numpy as np

def line_to_rectangle(p1, p2, thickness):
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    length = sqrt(dx ** 2 + dy ** 2)

    dx = dx/length if length != 0 else 0
    dy = dy/length if length != 0 else 0

    px = 0.5 * thickness * -dy
    py = 0.5 * thickness * dx

    ux = thickness * 0.5 * dx
    uy = thickness * 0.5 * dy

    return [
        (x1 + px - ux, y1 + py - uy),
        (x2 + px + ux, y2 + py + uy),
        (x2 - px + ux, y2 - py + uy),
        (x1 - px - ux, y1 - py - uy),
    ]

def get_position_of_creature(bodies):
    ''' Give the maxmium displacement of the given creature'''
    temp_data_x = []
    for body in bodies:
        if body.worldCenter.x != 0:
            temp_data_x.append(body.worldCenter.x)
    if temp_data_x:
        return np.amax(temp_data_x)
    return 0

def get_fitness(bodies, starting_position):
    ''' returns fitness of the creature'''
    fitness = get_position_of_creature(bodies) - starting_position
    return fitness
