from __future__ import annotations
# NodeList version of ADT Queue

from typing import Optional, List, Any

#two stacks rear/front

# Node class for use with Queue implemented with linked list
# NodeList is one of
# None or
# Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value: Any, rest: Optional[Node]):
        self.value = value      # value
        self.rest = rest        # NodeList

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return self.value == other.value and self.rest == other.rest
        else:
            return False

    def __repr__(self) -> str:
        return ("Node({!r}, {!r})".format(self.value, self.rest))

class Queue:
    def __init__(self, rear: Optional[Node] = None, front: Optional[Node] = None, num_items: int = 0):
        self.rear = rear    # rear NodeList
        self.front = front   # front NodeList
        self.num_items = num_items  # number of items in Queue

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Queue):
            return self.get_items() == other.get_items()
        else:
            return False

    def __repr__(self) -> str:
        return ("Queue({!r}, {!r})".format(self.rear, self.front))

    # get_items returns array (Python list) of items in Queue
    # first item in the list will be front of queue, last item is rear of queue
    def get_items(self) -> List:
        items: List = []
        front = self.front
        while front is not None:
            items.append(front.value)
            front = front.rest
        if self.rear is not None:
            rear_items = []
            rear: Optional[Node] = self.rear
            while rear is not None:
                rear_items.append(rear.value)
                rear = rear.rest
            rear_items.reverse()
            items.extend(rear_items)
            return items
        return items

    def is_empty(self) -> bool:
        """Returns true if the queue is empty and false otherwise
        Must be O(1)"""
        if self.num_items == 0:
            return True
        else:
            return False
    def enqueue(self, item: Any) -> None:
        """enqueues item, adding it to the rear NodeList
        Must be O(1)"""
        self.rear = Node(item, self.rear)
        self.num_items += 1

    def dequeue(self) -> Any:
        """dequeues item, removing first item from front NodeList
        If front NodeList is empty, remove items from rear NodeList
        and add to front NodeList until rear NodeList is empty
        (This will still satisfy O(1) requirement for the operation,
        as the transfer is amortized across all dequeues)
        If front NodeList and rear NodeList are both empty, raise IndexError
        Must be O(1) - general case"""
        if self.is_empty():
            raise IndexError

        if self.front is None:
            while self.rear is not None:
                self.front = Node(self.rear.value, self.front)
                self.rear = self.rear.rest

        self.num_items -= 1
        if self.front is not None:
            dequeued_item: Any = self.front.value
            self.front = self.front.rest
        return dequeued_item



    def size(self) -> int:
        """Returns the number of items in the queue
        Must be O(1)"""
        return self.num_items

