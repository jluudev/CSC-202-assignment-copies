import unittest
from binary_search_tree import *
import random

class TestLab4(unittest.TestCase):

    def test_00(self) -> None:
        tn1 = TreeNode(1, None)
        tn2 = TreeNode(1, None)
        self.assertFalse(tn1.__eq__(None))
        self.assertEqual(tn1, tn2)
        self.assertEqual(tn1.__repr__(),"TreeNode(1, None, None, None)")

    def test_01_simple(self) -> None:
        bst = BinarySearchTree()
        self.assertEqual(bst.tree_height(), None)
        self.assertTrue(bst.is_empty())

    def test_02_simple(self) -> None:
        bst = BinarySearchTree(TreeNode(1, None))
        self.assertFalse(bst.is_empty())

    def test_02_insert_search(self) -> None:
        bst = BinarySearchTree()
        values = [99, -4, 167, 139, 55, -89, 13, 78, 128, 119]

        for val in values:
            bst.insert(val)

        for val in values:
            self.assertTrue(bst.search(val))
            self.assertFalse(bst.search(val - 1))
            self.assertFalse(bst.search(val + 1))
            
    def test_03_search_empty_list(self) -> None:
        bst = BinarySearchTree()
        self.assertFalse(bst.search(999))

    def test_04_pre_in_level_order_empty_list(self) -> None:
        bst = BinarySearchTree()
        self.assertEqual(bst.preorder_list(), [])
        self.assertEqual(bst.inorder_list(), [])
        self.assertEqual(bst.level_order_list(), [])
                
    def test_07_test_min_max_empty(self) -> None:
        bst = BinarySearchTree()
        self.assertEqual(None, bst.find_max())
        self.assertEqual(None, bst.find_min())

    def test_08_test_inorder(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])
      
        self.assertEqual(bst.inorder_list(), [-89, -4, 13, 55, 78, 99, 139, 167, 174, 178])

    def test_09_test_preorder(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])
      
        self.assertEqual(bst.preorder_list(), [99, -4, -89, 55, 13, 78, 167, 139, 178, 174])

    def test_09_test_level_order(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])
      
        self.assertEqual(bst.level_order_list(), [99, -4, 167, -89, 55, 139, 178, 13, 78, 174])
        
    def test_14_insert_replace(self) -> None:
        bst = BinarySearchTree()
        bst.insert(30, 'aaa')
        bst.insert(40, 'bbb')
        bst.insert(35, 'ccc')
        bst.insert(50, 'ddd')
        bst.insert(60, 'eee')
        bst.insert(60, 'zzz')
        self.assertEqual(bst.find_max(), (60, 'zzz'))
        self.assertEqual(bst.tree_height(), 3)

    def test_16_test_tree_height(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])
        self.assertEqual(bst.find_min(), (-89, None))
        self.assertEqual(bst.tree_height(), 3)

    def test_insert_none(self) -> None:
        bst = BinarySearchTree(TreeNode(1, 2, None, None))
        bst.insert(3)
        self.assertEqual(bst.tree_height(), 1)

    def test_insert_rand(self) -> None:
        bst = BinarySearchTree()
        keys = []
        for i in range(99):
            keys.append(random.randint(-100,100))

        for i in range(len(keys)):
            bst.insert(keys[i])

    def test_orders(self) -> None:
        bst = BinarySearchTree()
        keys = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertEqual(bst.inorder_list(), [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8 , 9])
        self.assertEqual(bst.preorder_list(), [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8 , 9])
        self.assertEqual(bst.level_order_list(), [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8 , 9])
        self.assertEqual(bst.tree_height(), 12)
        self.assertTrue(bst.search(0))
        self.assertEqual(bst.find_max(), (9, None))
        self.assertEqual(bst.find_min(), (-3, None))

    def test_orders_2(self) -> None:
        bst = BinarySearchTree()
        keys = [1, 0, 2, -1, 3, -2, 4]

        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertEqual(bst.inorder_list(), [-2, -1, 0, 1, 2, 3, 4])
        self.assertEqual(bst.preorder_list(), [1, 0, -1, -2, 2, 3, 4])
        self.assertEqual(bst.level_order_list(), [1, 0, 2, -1, 3, -2, 4])
        self.assertEqual(bst.tree_height(), 3)
        self.assertFalse(bst.search(-5))
        self.assertEqual(bst.find_min(), (-2, None))
        self.assertEqual(bst.find_max(), (4, None))

if __name__ == '__main__': 
    unittest.main()
