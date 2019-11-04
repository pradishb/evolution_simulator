"Module to perform unittest"
import unittest
from creature import Creature
from . import reproduce


class TestCases(unittest.TestCase):
    "Class that contains test cases for project"

    def test_reproduction(self):
        ''' Tests the reproduction of a creature '''
        for _ in range(10):
            creature = Creature(n=5)
            creature.draw_creature()
            offspring = reproduce(creature)
            offspring.draw_creature()


if __name__ == "__main__":
    unittest.main()
