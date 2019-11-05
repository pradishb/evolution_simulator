"Module to perform unittest"
import unittest
from creature import Creature
from file import load_generations

from . import reproduce


class TestCases(unittest.TestCase):
    "Class that contains test cases for project"

    def test_reproduction(self):
        ''' Tests the reproduction of a creature '''
        data = load_generations('test_data/default.pickle')
        creatures = []

        for creature in data['generations'][-1]:
            creature = data['creatures'][creature]
            creature = Creature(**creature)
            creatures.append(creature)

        for creature in creatures:
            creature.draw_creature()
            offspring = reproduce(creature, data['creatures'])
            offspring.draw_creature()


if __name__ == "__main__":
    unittest.main()
