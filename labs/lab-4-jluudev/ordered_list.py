from __future__ import annotations
from typing import Optional, Any, List


class Node:
    """Node for use with doubly-linked list"""

    def __init__(self, item: Any):
        self.item = item  # item held by Node
        self.next: Node = self  # reference to next Node, init to this Node
        self.prev: Node = self  # reference to previous Node, init to this Node


class OrderedList:
    """A doubly-linked ordered list of integers, 
    from lowest (head of list, sentinel.next) to highest (tail of list, sentinel.prev)"""

    def __init__(self) -> None:
        """Use only a sentinel Node. No other instance variables"""
        self.sentinel: Node = Node(None)  # Empty linked list, just sentinel Node
        self.sentinel.next = self.sentinel  # Initialize next to sentinel
        self.sentinel.prev = self.sentinel  # Initialize prev to sentinel

    def __eq__(self, other: object) -> bool:
        lists_equal = True
        if not isinstance(other, OrderedList):
            lists_equal = False
        else:
            s_cur = self.sentinel.next
            o_cur = other.sentinel.next
            while s_cur != self.sentinel and o_cur != other.sentinel:
                if s_cur.item != o_cur.item:
                    lists_equal = False
                s_cur = s_cur.next
                o_cur = o_cur.next
            if s_cur != self.sentinel or o_cur != other.sentinel:
                lists_equal = False
        return lists_equal

    def is_empty(self) -> bool:
        """Returns back True if OrderedList is empty"""
        if self.sentinel.next == self.sentinel and self.sentinel.prev == self.sentinel:
            return True
        return False

    def add(self, item: Any) -> None:
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list)
        If item is already in list, do not add again (no duplicate items)"""
        cur = self.sentinel.next

        while cur is not self.sentinel and item > cur.item:
            cur = cur.next
        if item != cur.item:
            temp = Node(item)
            temp.next = cur
            temp.prev = cur.prev
            cur.prev.next = temp
            cur.prev = temp

    def remove(self, item: Any) -> bool:
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False"""

        cur = self.sentinel.next
        while cur.item != item:
            cur = cur.next
            if cur is self.sentinel or cur.item > item:
                return False

        temp = cur.next
        temp.prev = cur.prev
        cur.prev.next = temp
        return True

    def index(self, item: Any) -> Optional[int]:
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""
        index = 0
        cur = self.sentinel.next
        while cur is not self.sentinel:
            if cur.item == item:
                return index
            else:
                index += 1
                cur = cur.next
        return None

    def pop(self, index: int) -> Any:
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError"""
        if index < 0 or index >= self.size():
            raise IndexError
        else:
            cur = self.sentinel.next
            for i in range(index):
                cur = cur.next
            temp_val = cur.item
            temp = cur.next
            temp.prev = cur.prev
            cur.prev.next = temp
        return temp_val

    def search(self, item: Any) -> bool:
        """Searches OrderedList for item, returns True if item is in list, False otherwise - USE RECURSION"""
        return self.search_helper(self.sentinel.next, item)

    def search_helper(self, cur_node: Node, item: Any) -> bool:
        if cur_node is self.sentinel or cur_node.item > item:
            return False
        else:
            if cur_node.item == item:
                return True
            else:
                return self.search_helper(cur_node.next, item)

    def python_list(self) -> List:
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        list_rep: List = []
        cur = self.sentinel.next
        while cur is not self.sentinel:
            list_rep.append(cur.item)
            cur = cur.next
        return list_rep

    def python_list_reversed(self) -> List:
        """Return a Python list representation of OrderedList, from tail to head, USING RECURSION
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""
        list_rep: List = []
        self.python_list_reversed_helper(self.sentinel.prev, list_rep)
        return list_rep

    def python_list_reversed_helper(self, cur_node: Node, list_rep: List) -> None:
        if cur_node is not self.sentinel:
            list_rep.append(cur_node.item)
            self.python_list_reversed_helper(cur_node.prev, list_rep)

    def size(self) -> int:
        """Returns number of items in the OrderedList - USE RECURSION"""
        return self.size_helper(self.sentinel.next, 0)

    def size_helper(self, cur_node: Node, count: int) -> int:
        if cur_node is self.sentinel:
            return count
        else:
            return self.size_helper(cur_node.next, count + 1)
