# CPE 202 Lab 1 Test Cases

import unittest
from typing import List

from lab1a import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):
    '''Tests max_list_iter() in the case that a list [1,2,3] has the max equals 3'''

    def test_max_list_01(self) -> None:
        tlist: List[int] = [1, 2, 3]  # int list of length 3
        self.assertEqual(max_list_iter(tlist), 3)  # length of list should equal 3

        tlist2: List[int] = [1]
        self.assertEqual(max_list_iter(tlist2), 1)

    '''Tests max_list_iter() in the case that a list is None, and should raise a ValueError'''

    def test_max_list_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    '''Tests max_list_iter() in the case that a list is empty or [], and should return None'''

    def test_max_list_03(self) -> None:
        tlist: List[int] = []
        self.assertEqual(max_list_iter(tlist), None)

    '''Tests max_list_iter() when list is not all integers'''
    def test_max_list_04(self) -> None:
        tlist: List = [1, 2, 'a', 'b', 'c']
        with self.assertRaises(ValueError):
            max_list_iter(tlist)

    '''Tests reverse_list() in which the original list is not changed and the list returned is equal to the reverse
    of the original list. Expects intList to be the same and revList to be the reverse of intList'''

    def test_reverse(self) -> None:
        intlist: List[int] = [1, 2, 3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, [3, 2, 1])
        self.assertEqual(intlist, [1, 2, 3])

    '''Tests reverse_list() when the list argument sent is equal to None and should expect a ValueError raised'''

    def test_reverse_2(self) -> None:
        intlist = None
        with self.assertRaises(ValueError):
            revList = reverse_list(intlist)

    '''Tests reverse_list_mutate(), in which the list passed in should be mutated and reversed.
    Expects intList = [3, 2, 1] after passing in intList = [1, 2, 3]'''

    def test_reverse_mutate(self) -> None:
        intlist: List[int] = [1, 2, 3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [3, 2, 1])

    '''Tests reverse_list_mutate() in the case that the argument list equals None, and should raise
    a ValueError'''

    def test_reverse_mutate_2(self) -> None:
        intlist = None
        with self.assertRaises(ValueError):
            reverse_list_mutate(intlist)


if __name__ == "__main__":
    unittest.main()
