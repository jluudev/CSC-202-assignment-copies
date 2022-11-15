from __future__ import annotations

import functools
from typing import List, Optional


class HuffmanNode:
    def __init__(self, char_ascii: int, freq: int, left: Optional[HuffmanNode] = None,
                 right: Optional[HuffmanNode] = None):
        self.char_ascii = char_ascii  # stored as an integer - the ASCII character code value
        self.freq = freq  # the frequency associated with the node
        self.left = left  # Huffman tree (node) to the left!
        self.right = right  # Huffman tree (node) to the right

    def __lt__(self, other: HuffmanNode) -> bool:
        return comes_before(self, other)


def comes_before(a: HuffmanNode, b: HuffmanNode) -> bool:
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq < b.freq:
        return True
    elif a.freq == b.freq:
        return a.char_ascii < b.char_ascii
    else:
        return False


def combine(a: HuffmanNode, b: HuffmanNode) -> HuffmanNode:
    """Creates a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lower of the a and b char ASCII values"""
    freq = a.freq + b.freq  # sum of freq of a and b
    if comes_before(a, b):
        n = HuffmanNode(min(a.char_ascii, b.char_ascii), freq, a, b)
    else:
        n = HuffmanNode(min(a.char_ascii, b.char_ascii), freq, b, a)
    return n


def cnt_freq(filename: str) -> List:
    """Opens a text file with a given file name (passed as a string) and counts the
    frequency of occurrences of all the characters within that file
    Returns a Python List with 256 entries - counts are initialized to zero.
    The ASCII value of the characters are used to index into this list for the frequency counts"""
    freq_list: List = [0] * 256  # empty freq list of 256, 0s
    try:
        with open(filename) as file:
            read = file.read()
            for ch in read:
                freq_list[ord(ch)] += 1
    except:
        raise FileNotFoundError
    return freq_list


def create_huff_tree(char_freq: List) -> Optional[HuffmanNode]:
    """Input is the list of frequencies (provided by cnt_freq()).
    Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree. Returns None if all counts are zero."""
    non_zero_freq: List = []
    for i in range(len(char_freq)):
        if char_freq[i] != 0:
            n = HuffmanNode(i, char_freq[i])
            non_zero_freq.append(n)
    if len(non_zero_freq) == 0:
        return None

    while not len(non_zero_freq) <= 1:
        n1 = min_between(non_zero_freq)
        non_zero_freq.remove(n1)
        n2 = min_between(non_zero_freq)
        non_zero_freq.remove(n2)

        if n1 is not None and n2 is not None:
            non_zero_freq.insert(0, (combine(n1, n2)))

    return non_zero_freq[0]


def min_between(li: List) -> Optional[HuffmanNode]:
    """Helper function for create_huff_tree to find the min between two nodes"""
    min = li[0]
    for i in range(len(li)):
        cur = li[i]
        if comes_before(cur, min):
            min = cur
    return min


def create_code(node: Optional[HuffmanNode]) -> List:
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the array, with the resulting Huffman code for that character stored at that location.
    Characters that are unused should have an empty string at that location"""
    char_list: List = [""] * 256  # empty string list of Huffman Codes
    if node is None:
        return char_list
    else:
        _create_code(node, char_list)
        return char_list


def _create_code(node: HuffmanNode, li: List, code: str = "") -> None:
    """Helper function for create_code()
    Takes in a node, the string list of ASCII representation, and a string code, which builds the resulting Huffman
    code for the character stores in the location.
    """
    if node.left is None and node.right is None:
        li[node.char_ascii] = code
    if node.left is not None:
        temp = code
        code += "0"
        _create_code(node.left, li, code)
        code = temp
    if node.right is not None:
        temp = code
        code += "1"
        _create_code(node.right, li, code)
        code = temp


def create_header(freqs: List) -> str:
    """Input is the list of frequencies (provided by cnt_freq()).
    Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    header_list: List = []
    for i in range(len(freqs)):
        if freqs[i] != 0:
            header_list.append(str(i))
            header_list.append(str(freqs[i]))
    return " ".join(header_list)


def huffman_encode(in_file: str, out_file: str) -> None:
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    freqs = cnt_freq(in_file)
    huffman_tree = create_huff_tree(freqs)
    code_str = create_code(huffman_tree)

    with open(in_file, "r", newline='') as i_f:
        with open(out_file, "w", newline='') as i_o:
            read = i_f.read()
            if huffman_tree is None:
                i_o.write("")
            elif huffman_tree.left is None and huffman_tree.right is None:
                i_o.write(create_header(freqs) + "\n")
            elif huffman_tree.left is not None and huffman_tree.right is not None:
                i_o.write(create_header(freqs) + "\n")
                for c in read:
                    new_code = code_str[ord(c)]
                    i_o.write(new_code)

def huffman_decode(encoded_file: str, decode_file: str) -> None:
    try:
        with open(encoded_file, 'r', newline='') as read:
            with open(decode_file, 'w+', newline='') as decode:
                line_1 = read.readline()
                if len(line_1) == 0:
                    decode.write("")
                else:
                    lst = line_1.split()
                    if len(lst) == 2:
                        decode.write(chr(int(lst[0])) * int(lst[1]))
                    else:
                        freq_list = parse_header(line_1)
                        hufftree = create_huff_tree(freq_list)
                        line_2 = read.readline()
                        cur = hufftree
                        #if len(line_2) == 0:
                            #decode.write(chr(cur.char_ascii) * cur.freq)
                        for i in line_2:
                            if i == "0":
                                cur = cur.left
                                if cur.left is None and cur.right is None:
                                    decode.write(chr(cur.char_ascii))
                                    cur = hufftree
                            elif i == "1":
                                cur = cur.right
                                if cur.left is None and cur.right is None:
                                    decode.write(chr(cur.char_ascii))
                                    cur = hufftree
    except:
        raise FileNotFoundError


def parse_header(header_string: str) -> List:
    lst: List = [0] * 256
    split_head = header_string.split()
    for i in range(0, len(split_head), 2):
        frq = int(split_head[i + 1])
        lst[int(split_head[i])] = frq
    return lst
