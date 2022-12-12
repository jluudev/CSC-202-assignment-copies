import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self) -> None:
        g = Graph('test1.txt')
        self.assertEqual([['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']], g.conn_components())
        self.assertTrue(g.is_bipartite())
        
    def test_02(self) -> None:
        g = Graph('test2.txt')
        self.assertEqual([['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']], g.conn_components())
        self.assertFalse(g.is_bipartite())

    def test_no_vert(self) -> None:
        g = Graph('test1.txt')
        self.assertEqual(g.get_vertex("v10"), None)

    def test_03(self) -> None:
        g = Graph('test3.txt')
        self.assertEqual([['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9']], g.conn_components())
        self.assertTrue(g.is_bipartite())

    def test_04(self) -> None:
        g = Graph('test4.txt')
        self.assertEqual([['v1', 'v2']], g.conn_components())
        self.assertTrue(g.is_bipartite())

if __name__ == '__main__':
   unittest.main()
