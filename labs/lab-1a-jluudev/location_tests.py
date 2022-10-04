# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *


class TestLocation(unittest.TestCase):

    def test_repr(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

        loc2 = Location('LA', 34.1, 118.2)
        self.assertNotEqual(repr(loc2), "Location('SLO', 35.3, -120.7)")

    # Add more tests!
    def test_init(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(loc.name, 'SLO')
        self.assertAlmostEqual(loc.lat, 35.3)
        self.assertAlmostEqual(loc.lon, -120.7)

    def test_eq(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        loc2 = Location('Paris', 48.9, 2.4)
        loc3 = Location('Paris', 48.9, 2.4)
        loc4 = Location('LA', 34.1, 118.2)

        self.assertNotEqual(loc, loc2)
        self.assertNotEqual(loc, loc4)
        self.assertEqual(loc2, loc3)
        self.assertTrue(loc2 == loc3)

    def test_eq_not_loc(self) -> None:
        loc = Location('Paris', 48.9, 2.4)
        self.assertFalse(loc.__eq__(None))


if __name__ == "__main__":
    unittest.main()
