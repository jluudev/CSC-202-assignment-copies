import unittest
from huffman import *


class TestList(unittest.TestCase):
    def test_cnt_freq(self) -> None:
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)

    def test_combine(self) -> None:
        a = HuffmanNode(65, 1)
        b = HuffmanNode(66, 2)
        c = combine(a, b)
        if (c.left is not None) and (c.right is not None):
            self.assertEqual(c.left.char_ascii, 65)
            self.assertEqual(c.left.freq, 1)
            self.assertEqual(c.right.char_ascii, 66)
            self.assertEqual(c.right.freq, 2)
            self.assertEqual(c.char_ascii, 65)
            self.assertEqual(c.freq, 3)
        else:  # pragma: no cover
            self.fail()
        c = combine(b, a)
        if (c.left is not None) and (c.right is not None):
            self.assertEqual(c.left.char_ascii, 65)
            self.assertEqual(c.left.freq, 1)
            self.assertEqual(c.right.char_ascii, 66)
            self.assertEqual(c.right.freq, 2)
            self.assertEqual(c.char_ascii, 65)
            self.assertEqual(c.freq, 3)
        else:  # pragma: no cover
            self.fail()

    def test_create_huff_tree(self) -> None:
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        if hufftree is not None:
            self.assertEqual(hufftree.freq, 32)
            self.assertEqual(hufftree.char_ascii, 97)
            left = hufftree.left
            right = hufftree.right
            if (left is not None) and (right is not None):
                self.assertEqual(left.freq, 16)
                self.assertEqual(left.char_ascii, 97)
                self.assertEqual(right.freq, 16)
                self.assertEqual(right.char_ascii, 100)
            else:  # pragma: no cover
                self.fail()
        else:  # pragma: no cover
            self.fail()

    def test_create_header(self) -> None:
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self) -> None:
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_01_textfile(self) -> None:
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file1_out.txt", "file1_soln.txt"))

    def test_file_not_found(self) -> None:
        with self.assertRaises(FileNotFoundError):
            huffman_encode("asflkf.txt", "fdkfsl.txt")

    def test_empty_file(self) -> None:
        freqlist = cnt_freq("empty.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)

        self.assertEqual(freqlist, [0]*256)
        self.assertEqual(hufftree, None)
        self.assertEqual(codes, [""]*256)

    def test_empty_none(self) -> None:
        huffman_encode("empty.txt", "empty_out.txt")
        self.assertTrue(compare_files("empty.txt", "empty_out.txt"))

    def test_lt(self) -> None:
        huff_1 = HuffmanNode(75, 3)
        huff_2 = HuffmanNode(93, 2)
        self.assertFalse(huff_1.__lt__(huff_2))

    def test_decl(self) -> None:
        huffman_encode("declaration.txt", "declaration_out.txt")
        self.assertTrue(compare_files("declaration_out.txt", "declaration_soln.txt"))

    def test_file_2(self) -> None:
        huffman_encode("file2.txt", "file2_out.txt")
        self.assertTrue(compare_files("file2_out.txt", "file2_soln.txt"))

    def test_multiline(self) -> None:
        huffman_encode("multiline.txt", "multiline_out.txt")
        self.assertTrue(compare_files("multiline_out.txt", "multiline_soln.txt"))

# Compare files - takes care of CR/LF, LF issues
def compare_files(file1: str, file2: str) -> bool:  # pragma: no cover
    match = True
    done = False
    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            while not done:
                line1 = f1.readline().strip()
                line2 = f2.readline().strip()
                if line1 == '' and line2 == '':
                    done = True
                if line1 != line2:
                    done = True
                    match = False
    return match


if __name__ == '__main__':
    unittest.main()
