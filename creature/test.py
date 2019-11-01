"Module to perform unittest"
import unittest
from . import Creature


class TestCases(unittest.TestCase):
    "Class that contains test cases for project"

    def test_creature_creation(self):
        n = 5
        for _ in range(100):
            creature = Creature(n)
            creature.draw_creature()


if __name__ == "__main__":
    unittest.main()
