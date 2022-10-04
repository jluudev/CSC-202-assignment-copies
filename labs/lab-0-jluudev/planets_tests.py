import unittest

from planets import *


# Write more test cases!

class Test_planets(unittest.TestCase):

    def test_mars(self) -> None:
        weight = 136
        self.assertAlmostEqual(weight_on_planets(weight, "Mars"), 51.68)

    def test_error(self) -> None:
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            weight = 99
            weight_on_planets(weight, "Neptune")

    def test_jupiter(self) -> None:
        weight = 105
        self.assertAlmostEqual(weight_on_planets(weight, "Jupiter"), 245.7)

    def test_venus(self) -> None:
        weight = 186
        self.assertAlmostEqual(weight_on_planets(weight, "Venus"), 169.26)


if __name__ == "__main__":
    unittest.main()
