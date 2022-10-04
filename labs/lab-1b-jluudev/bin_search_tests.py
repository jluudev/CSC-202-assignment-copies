import unittest
from bin_search import *
from typing import List


class TestLab1b(unittest.TestCase):

    def test_bin_search_iter_01(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]    #tests target at low half of list
        self.assertEqual(bin_search_iter(tlist, 5), 0)

    def test_bin_search_iter_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            bin_search_iter(tlist, 5)

    def test_bin_search_iter_03(self) -> None:
        tlist = [1, 5, 7, 12, 15]   #tests when target does not exist within list
        self.assertEqual(bin_search_iter(tlist, 50), None)

    def test_bin_search_iter_04(self) -> None:
        tlist = [5, 9, 18, 23, 55, 72]  #tests target at high half
        self.assertEqual(bin_search_iter(tlist, 55), 4)

    def test_bin_search_iter_05(self) -> None:
        tlist = [1, 2, 3, 4, 5, 6, 7]   #tests target at middle
        self.assertEqual(bin_search_iter(tlist, 4), 3)

    def test_bin_search_rec_01(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]    #tests target at low half
        self.assertEqual(bin_search_rec(tlist, 5), 0)

    def test_bin_search_rec_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            bin_search_rec(tlist, 5)

    def test_bin_search_rec_03(self) -> None:
        tlist = [1, 5, 7, 12, 15]   #tests when target not located in list
        self.assertEqual(bin_search_rec(tlist, 11), None)

    def test_bin_search_rec_04(self) -> None:
        tlist = [1, 2, 3, 4, 5, 6, 7]   #tests for target in middle
        self.assertEqual(bin_search_rec(tlist, 4), 3)

    def test_bin_search_rec_05(self) -> None:
        tlist = [5, 9, 18, 23, 55, 72]  #tests for target in high half
        self.assertEqual(bin_search_rec(tlist, 55), 4)
if __name__ == "__main__":
    unittest.main()
