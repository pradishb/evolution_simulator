"Module to generate random connected graphs"
from random import choice, randint

import cv2
import numpy as np


def create_edges(n):
    "Generation of random graph"
    all_edges = set()
    for vertex_a in range(n):
        for vertex_b in range(vertex_a+1, n):
            all_edges.add((vertex_a, vertex_b))
    edges = set(
        filter(lambda edge: edge[0] + 1 == edge[1], all_edges))

    remaining_edges = all_edges - edges
    for _ in range(randint(0, len(remaining_edges))):
        random_edge = choice(list(remaining_edges))
        remaining_edges -= {(random_edge)}
        edges = edges.union({(random_edge)})
    return list(edges)


def create_vertices(n, size):
    "Generation of random vertices"
    vertices = []
    for _ in range(n):
        vertices.append((randint(0, size), randint(0, size)))
    return vertices


def resize_vertices(vertices, scale):
    "Resizes the vertices"
    output = []
    for vertex in vertices:
        output.append((vertex[0] * scale, vertex[1] * scale))
    return output


def find_adjacent_edges(my_edge, edges):
    "Finds the adjacent edges of an edge"
    adjacent = []
    for edge in edges:
        if tuple(edge) == tuple(my_edge):
            continue
        if my_edge[0] in edge:
            adjacent.append(edge)
    return adjacent


def draw_creature(vertices, edges, size, scale):
    "Draws connected graph using vertices and edges"
    padding = 50
    paper = np.ones((scale*size, scale*size, 3)).astype(np.uint8) * 255
    vertices = resize_vertices(vertices, scale)

    for edge in edges:
        start, end = vertices[edge[0]], vertices[edge[1]]
        cv2.line(paper, start, end, (0, 0, 255), 5)
    for vertex in vertices:
        cv2.circle(paper, vertex, 10, (255, 0, 0), -1)
    border = cv2.copyMakeBorder(
        paper,
        top=padding,
        bottom=padding,
        left=padding,
        right=padding, borderType=cv2.BORDER_CONSTANT, value=[255, 255, 255])
    cv2.imshow("", border)
    cv2.waitKey()
