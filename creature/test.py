"Module to perform unittest"
import unittest
from .creature import create_vertices, create_edges, draw_creature


class TestCases(unittest.TestCase):
    "Class that contains test cases for project"

    def test_creature_creation(self):
        n = 5
        for _ in range(10):
            vertices = create_vertices(n, 10)
            edges = create_edges(n)
            draw_creature(vertices, edges, 10, 50)


if __name__ == "__main__":
    unittest.main()
