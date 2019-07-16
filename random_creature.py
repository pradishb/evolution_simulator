"Module to generate random connected graphs"
from random import choice, randint

import cv2
import numpy as np


def create_edges(size):
    "Generation of random graph"
    all_edges = set()
    for vertex_a in range(size):
        for vertex_b in range(vertex_a+1, size):
            all_edges.add((vertex_a, vertex_b))
    edges = set(
        filter(lambda edge: edge[0] + 1 == edge[1], all_edges))

    remaining_edges = all_edges - edges
    for _ in range(randint(0, len(remaining_edges))):
        random_edge = choice(list(remaining_edges))
        remaining_edges -= {(random_edge)}
        edges = edges.union({(random_edge)})
    return list(edges)


def create_vertices(n):
    "Generation of random vertices"
    vertices = []
    for _ in range(n):
        vertices.append((randint(0, 500), randint(0, 500)))
    return vertices


def draw_creature(vertices, edges):
    "Draws connected graph using vertices and edges"
    paper = np.ones((500, 500, 3)).astype(np.uint8) * 255

    for edge in edges:
        start, end = vertices[edge[0]], vertices[edge[1]]
        cv2.line(paper, start, end, (0, 0, 255), 5)
    for vertex in vertices:
        cv2.circle(paper, vertex, 10, (255, 0, 0), -1)
    cv2.imshow("", paper)
    cv2.waitKey()


def main():
    "Main function of the module"
    n = 5
    for _ in range(10):
        vertices = create_vertices(n)
        edges = create_edges(n)
        draw_creature(vertices, edges)


if __name__ == "__main__":
    main()
