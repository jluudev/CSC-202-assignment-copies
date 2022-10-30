import unittest
from queue_array import Queue

class TestLab1(unittest.TestCase):

    def test_array(self) -> None:
        q = Queue(5)
        self.assertEqual(q.items, [None, None, None, None, None])
        self.assertEqual(q.get_items(), [])
        q.enqueue(1)
        self.assertEqual(q.items, [1, None, None, None, None])
        q.enqueue(2)
        self.assertEqual(q.items, [1, 2, None, None, None])

    def test_init_eq(self) -> None:
        with self.assertRaises(IndexError):
            q = Queue(5, [1, 2, 3, 4, 5, 6])
        q1 = Queue(5, [1, 2, 3, 4])
        self.assertEqual(q1.get_items(), [1, 2, 3, 4])
        q2 = Queue(5, [1, 2, 3, 4])
        self.assertEqual(q1, q2)

    def test_init_eq2(self) -> None:
        q1 = Queue(5, [1, 2, 3, 4, 5])
        q2 = Queue(5, [1, 2, 3, 4, 5])
        self.assertFalse(q1.__eq__(None))
        self.assertEqual(q1, q2)

    def test_repr(self) -> None:
        q1 = Queue(5, [])
        self.assertEqual(q1.__repr__(), "Queue(5, [])")

    def test_queue_simple(self) -> None:
        q = Queue(5)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 5)

    def test_empty(self) -> None:
        q = Queue(5)
        with self.assertRaises(IndexError):
            q.dequeue()

        self.assertTrue(q.is_empty())

        q.enqueue(3)
        q.enqueue(4)
        self.assertFalse(q.is_empty())


    def test_full(self) -> None:
        q = Queue(5)

        self.assertFalse(q.is_full())

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)

        with self.assertRaises(IndexError):
            q.enqueue(6)

        self.assertTrue(q.is_full())

    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_queue_01(self):
        """Test the queue by checking empty, full, adding 100, checking empty, full, removing 100, checking empty, full"""
        q = Queue(100)
        # Check empty, full, size
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 0)
        # Add items to the queue
        for i in range(100):
            q.enqueue(i)
        # Check empty, full, and size
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full)
        # Remove all the items from the queue
        for i in range(100):
            self.assertEqual(q.dequeue(), i)
        # Check empty, size, and full
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 0)

    def test_queue_empty_dequeue(self):
        """Make sure the queue raises an IndexError when trying to dequeue from an empty queue"""
        q = Queue(1)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_queue_full_enqueue(self):
        """Make sure the queue raises an IndexError when trying to enqueue a full queue"""
        q = Queue(1)
        q.enqueue("123abc")
        with self.assertRaises(IndexError):
            q.enqueue("123abc")

    def test_queue_large(self):
        """Test the queue by checking empty, full, adding 100000, checking empty, full, removing 1000000, checking empty, full"""
        q = Queue(100000)
        # Check empty, full, size
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 0)
        # Add items to the queue
        for i in range(100000):
            q.enqueue(i)
        # Check empty, full, and size
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full)
        # Remove all the items from the queue
        for i in range(100000):
            self.assertEqual(q.dequeue(), i)
        # Check empty, size, and full
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 0)



if __name__ == '__main__':
    unittest.main()
