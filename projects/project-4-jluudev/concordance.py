from typing import Any, List, Optional
from hash_quad import *
import string


class Concordance:

    def __init__(self) -> None:
        """ Starting size of hash table should be 191: self.concordance_table = HashTable(191) """
        self.stop_table: Optional[HashTable] = None  # hash table for stop words
        self.concordance_table: HashTable = HashTable(191)  # hash table for concordance

    def load_stop_table(self, filename: str) -> None:
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)
        try:
            with open(filename) as file:
                for w in file:
                    split = w.rstrip()
                    self.stop_table.insert(split, 1)
        except:
            raise FileNotFoundError

    def load_concordance_table(self, filename: str) -> None:
        """ Read words from input text file (filename) and insert them into the concordance hash table,
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)

        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError """
        self.concordance_table = HashTable(191)
        count = 0
        try:
            with open(filename) as file:
                for ln in file:
                    count += 1

                    ln = ln.rstrip().lower()
                    for i in ln:
                        if i == "'":
                            ln = ln.replace(i, "")
                        if i in string.punctuation:
                            ln = ln.replace(i, " ")

                    split = ln.split()

                    for w in split:
                        if self.is_stop_word(w):
                            if self.concordance_table.get_value(w):
                                temp = self.concordance_table.get_value(w)
                                if count not in temp:
                                    temp = temp + [count]
                                    self.concordance_table.insert(w, temp)
                            else:
                                self.concordance_table.insert(w, [count])
        except:
            raise FileNotFoundError

    def is_stop_word(self, word: str) -> bool:
        """Checks if the word is in stop_words.txt and returns a bool.
        Helper function for load_concordance_table()"""
        return not self.stop_table.in_table(word) and not self.is_number(word)  # type: ignore

    def is_number(self, word: str) -> bool:
        """Checks if the word is a number, and returns a bool
        Helper function for load_concordance_table()"""
        try:
            float(word)
            return True
        except ValueError:
            return False

    def write_concordance(self, filename: str) -> None:
        """ Write the concordance entries to the output file(filename)
        See sample output files for format. """
        lst = []
        with open(filename, "w+") as file:
            for w in self.concordance_table.hash_table:
                if w:
                    lst.append(w)
            lst_sort = sorted(lst)
            for i, val in enumerate(lst_sort):
                w = val[0]
                val_lst = val[1]
                build_str = " ".join([str(j) for j in val_lst])
                file.write(w + ": " + build_str)
                if i != len(lst_sort) - 1:
                    file.write("\n")
