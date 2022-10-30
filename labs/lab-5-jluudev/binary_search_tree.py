from __future__ import annotations
from queue_array import Queue
from typing import Optional, Any, Tuple, List


class TreeNode:
    def __init__(self, key: Any, data: Any, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TreeNode):
            return (self.key == other.key
                    and self.data == other.data
                    and self.left == other.left
                    and self.right == other.right)
        else:
            return False

    def __repr__(self) -> str:
        return ("TreeNode({!r}, {!r}, {!r}, {!r})".format(self.key, self.data, self.left, self.right))


class BinarySearchTree:
    def __init__(self, root_node: Optional[TreeNode] = None):  # Returns empty BST
        self.root: Optional[TreeNode] = root_node

    # returns True if tree is empty, else False
    def is_empty(self) -> bool:
        return self.root is None

    # returns True if key is in a node of the tree, else False
    def search(self, key: Any) -> bool:
        if self.is_empty():
            return False
        else:
            r = self.root
            while r is not None and r.key != key:
                if key < r.key:
                    r = r.left
                else:
                    r = r.right
            if r is not None and r.key == key:
                return True
            else:
                return False

    # Inserts new node w/ key and data
    # If an item with the given key is already in the BST,
    # the data in the tree will be replaced with the new data
    # Example creation of node: temp = TreeNode(key, data)
    # On insert, can assume key not already in BST
    def insert(self, key: Any, data: Any = None) -> None:

        if self.is_empty():
            self.root = TreeNode(key, data)
        else:
            r = self.root
            while r:
                if key == r.key:
                    r.data = data
                    break
                elif key < r.key:
                    if r.left is None:
                        r.left = TreeNode(key, data)
                        break
                    else:
                        r = r.left
                else:
                    if r.right is None:
                        r.right = TreeNode(key, data)
                        break
                    else:
                        r = r.right



    # returns tuple with min key and associated data in the BST
    # returns None if the tree is empty
    def find_min(self) -> Optional[Tuple[Any, Any]]:
        if self.is_empty():
            return None

        r = self.root
        while r.left:  # type: ignore
            r = r.left  # type: ignore
        return (r.key, r.data) if r is not None else None

    # returns tuple with max key and associated data in the BST
    # returns None if the tree is empty
    def find_max(self) -> Optional[Tuple[Any, Any]]:
        if self.is_empty():
            return None

        r = self.root
        while r.right:  # type: ignore
            r = r.right  # type: ignore

        return (r.key, r.data) if r is not None else None

    # returns the height of the tree
    # if tree is empty, return None
    def tree_height(self) -> Optional[int]:
        if self.is_empty():
            return None
        return self.tree_height_helper(self.root)

    def tree_height_helper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        left = self.tree_height_helper(root.left)
        right = self.tree_height_helper(root.right)

        max_height: int = left
        if right > max_height:
            max_height = right
        return max_height + 1

    # returns Python list of BST keys representing inorder traversal of BST
    def inorder_list(self) -> List:
        ordered_list: List = []

        self.inorder_list_helper(self.root, ordered_list)

        return ordered_list

    def inorder_list_helper(self, root: Optional[TreeNode], li: List) -> None:
        if root:
            self.inorder_list_helper(root.left, li)
            li.append(root.key)
            self.inorder_list_helper(root.right, li)

    # returns Python list of BST keys representing preorder traversal of BST
    def preorder_list(self) -> List:
        preordered_list: List = []

        if not self.is_empty():
            self.preorder_list_helper(self.root, preordered_list)

        return preordered_list

    def preorder_list_helper(self, root: Optional[TreeNode], li: List) -> None:
        if root is not None:
            li.append(root.key)
            self.preorder_list_helper(root.left, li)
            self.preorder_list_helper(root.right, li)

    # returns Python list of BST keys representing level-order traversal of BST
    # You MUST use your queue_array data structure from lab 3 to implement this method
    def level_order_list(self) -> List:
        q = Queue(25000)  # Don't change this!
        height = self.tree_height()
        if height is None:
            return []

        for i in range(height + 1):
            self.level_order_helper(self.root, i, q)

        return q.get_items()

    def level_order_helper(self, root: Optional[TreeNode], level: int, q: Queue) -> None:
        if root is None:
            return
        elif level == 0:
            q.enqueue(root.key)
        elif level > 0:
            self.level_order_helper(root.left, level - 1, q)
            self.level_order_helper(root.right, level - 1, q)
