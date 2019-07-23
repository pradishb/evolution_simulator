import unittest
from .maths import line_to_rectangle


class TestCases(unittest.TestCase):
    def test_line_to_rectangle(self):
        print(line_to_rectangle((1, 1), (5, 5), 2))


if __name__ == "__main__":
    unittest.main()
