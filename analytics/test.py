"Module to perform unittest"
import unittest

from file import load_generations

from . import show_analytics


class FileTestCase(unittest.TestCase):
    "Class that contains test cases for project"

    def test_creature_creation(self):
        ''' Tests the creation of some creatures '''
        data = load_generations('test_data/default.pickle')
        show_analytics('Test', data['generations'], data['creatures'])


if __name__ == "__main__":
    unittest.main()
