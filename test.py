"Module to perform unittest"
import unittest
from creature import creature


class TestCases(unittest.TestCase):
    "Class that contains test cases for project"

    def test_create_creature_connection_graph(self):
        "Tests the creature connection graph funciton"
        expected_value = 10
        array = creature.create_creature_connection_graph(5)
        self.assertEqual(array.shape[0], expected_value)


if __name__ == "__main__":
    unittest.main()
