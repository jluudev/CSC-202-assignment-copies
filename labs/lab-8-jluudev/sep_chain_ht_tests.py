import unittest
from sep_chain_ht import *


class TestList(unittest.TestCase):

    def test_insert1(self) -> None:
        hash1 = MyHashTable()
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        self.assertEqual(hash1.size(), 2)
        with self.assertRaises(ValueError):
            hash1.insert(-5, "c")

    def test_get1(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        self.assertEqual(hash1.get_item(3), 'b')
        self.assertEqual(hash1.get_item(11), 'a')

    def test_get2(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        with self.assertRaises(LookupError):
            hash1.get_item(6)

    def test_remove1(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        self.assertEqual(hash1.remove(11), (11, 'a'))
        self.assertEqual(hash1.size(), 0)

    def test_load_factor1(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        hash1.insert(1, "c")
        hash1.insert(8, "d")
        hash1.insert(4, "e")
        hash1.insert(5, "f")
        hash1.insert(1, "g")
        hash1.insert(2, "h")
        self.assertEqual(hash1.load_factor(), 1.4)

    def test_collisions2(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        hash1.insert(1, "c")
        hash1.insert(8, "d")
        hash1.insert(4, "e")
        hash1.insert(5, "f")
        hash1.insert(1, "g")
        hash1.insert(2, "h")
        self.assertEqual(hash1.collisions(), 2)

    def test_neg_inset(self) -> None:
        hash1 = MyHashTable(5)
        with self.assertRaises(ValueError):
            hash1.insert(-1, "a")

    def test_load_great(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        hash1.insert(1, "c")
        self.assertEqual(hash1.load_factor(), 0.6)
        hash1.insert(5, "d")
        hash1.insert(9, "e")
        hash1.insert(6, "f")
        hash1.insert(1, "g")
        hash1.insert(2, "h")
        hash1.insert(21, "i")

    def test_lookup_remove(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        hash1.insert(1, "c")
        with self.assertRaises(LookupError):
            hash1.remove(9)


if __name__ == '__main__':
    unittest.main()
