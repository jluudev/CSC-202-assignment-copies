import unittest
import perm_lex
from typing import List

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self) -> None:
        '''tests that the string "ab" should have two permutations in the list matching "ab" and "ba"'''
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])
    def test_perm_gen_lex_02(self) -> None:
        '''tests that a string of length 1 returns a list containing only that string'''
        self.assertEqual(perm_lex.perm_gen_lex('a'), ['a'])
    def test_perm_gen_lex_03(self) -> None:
        '''tests that a string of length 0 returns an empty list'''
        self.assertEqual(perm_lex.perm_gen_lex(''), [])
    def test_perm_gen_lex_04(self) -> None:
        '''tests that the string "abc" should have 6 permutations in the list in lexicographic order'''
        self.assertEqual(perm_lex.perm_gen_lex(('abc')), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
if __name__ == "__main__":
        unittest.main()
