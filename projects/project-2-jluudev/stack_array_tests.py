import unittest
from stack_array import Stack


class TestLab2(unittest.TestCase):

    def test_init(self) -> None:
        stack = Stack(5)
        self.assertEqual(stack.items, [None] * 5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self) -> None:
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5, [1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_repr(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

    # WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.
    def test_push(self) -> None:
        stack = Stack(5, [1, 2])
        stack.push(3)
        self.assertEqual(stack, Stack(5, [1, 2, 3]))

    def test_push_2(self) -> None:
        stack = Stack(3, [1, 2, 3])
        with self.assertRaises(IndexError):
            stack.push(4)

    def test_pop(self) -> None:
        stack = Stack(5, [1, 2, 3])
        stack.pop()
        self.assertEqual(stack, Stack(5, [1, 2]))
        self.assertEqual(stack.pop(), 2)

    def test_pop_2(self) -> None:
        stack = Stack(5)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek(self) -> None:
        stack = Stack(5, [1, 2, 3])
        self.assertEqual(stack.peek(), 3)

    def test_peek_2(self) -> None:
        stack = Stack(5)
        with self.assertRaises(IndexError):
            stack.peek()

    def test_size(self) -> None:
        stack = Stack(5, [1, 2, 3, 4])
        self.assertEqual(stack.size(), 4)


if __name__ == '__main__':
    unittest.main()
