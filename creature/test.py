"Module to perform unittest"
import unittest
from . import Creature


class TestCases(unittest.TestCase):
    "Class that contains test cases for project"

    def test_creature_creation(self):
        ''' Tests the creation of some creatures '''
        n = 5
        for _ in range(10):
            creature = Creature(n)
            creature.draw_creature()


if __name__ == "__main__":
    unittest.main()
