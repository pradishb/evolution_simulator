"Module to perform unittest"
import unittest
from creature import Creature
from . import save_creature


class FileTestCase(unittest.TestCase):
    "Class that contains test cases for project"

    def test_creature_creation(self):
        ''' Tests the creation of some creatures '''
        creature = Creature(n=5)
        save_creature(creature.get_data())


if __name__ == "__main__":
    unittest.main()
