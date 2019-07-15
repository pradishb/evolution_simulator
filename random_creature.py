from fisher_yates_shuffle import shuffle
from random import randint
import cv2
import numpy as np


def create_species(n):
    shuffled = shuffle(list(range(n)))
    print(shuffled)
    edges = []
    for i in range(n - 1):
        edges.append((shuffled[i], shuffled[i+1]))
    return edges


def create_vertices(n):
    vertices = []
    for _ in range(n):
        vertices.append((randint(0, 500), randint(0, 500)))
    return vertices


def draw_creature(vertices, edges):
    paper = np.ones((500, 500, 3)).astype(np.uint8) * 255

    for edge in edges:
        start, end = vertices[edge[0]], vertices[edge[1]]
        cv2.line(paper, start, end, (0, 0, 255), 5)
    for vertex in vertices:
        cv2.circle(paper, vertex, 10, (255, 0, 0), -1)
    cv2.imshow("", paper)
    cv2.waitKey()


def main():
    for _ in range(10):
        edges = create_species(6)
        for _ in range(10):
            vertices = create_vertices(6)
            draw_creature(vertices, edges)


if __name__ == "__main__":
    main()
