"Module to perform unittest"
import unittest

from creature import Creature
from file import load_generations

from . import Simulation


class SimulationTestCase(unittest.TestCase):
    "Class that contains test cases for simulation package"

    def test_simulate(self):
        ''' Tests the simulate function '''
        data = load_generations('test_data/default.pickle')
        creatures = []

        for creature in data['generations'][-1]:
            creature = data['creatures'][creature]
            creature = Creature(**creature)
            creatures.append(creature)
        simulation = Simulation()
        print(simulation.simulate(creatures))


if __name__ == "__main__":
    unittest.main()
