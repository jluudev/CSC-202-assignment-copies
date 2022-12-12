from typing import List, Any, Optional


class HashTable:

    def __init__(self, table_size: int):  # can add additional attributes
        self.table_size = table_size  # initial table size
        self.hash_table: List = [None] * table_size  # hash table
        self.num_items = 0  # empty hash table

    def insert(self, key: str, value: Any) -> None:
        """ Inserts an entry into the hash table (using Horner hash function to determine index,
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        hash_val = self.horner_hash(key)
        index = 0

        for k in range(self.table_size):
            index = (hash_val + k**2) % self.table_size

            if not self.hash_table[index]:
                self.hash_table[index] = (key, value)
                self.num_items += 1

                if self.get_load_factor() > 0.5:
                    new_hash = HashTable(self.table_size * 2 + 1)
                    for l in self.hash_table:
                        if l:
                            new_hash.insert(l[0], l[1])
                    self.hash_table = new_hash.hash_table
                    self.table_size = new_hash.table_size
                    self.num_items = new_hash.num_items
                else:
                    break
                return

            elif self.hash_table[index][0] == key:
                self.hash_table[index] = (key, value)
                return

    def horner_hash(self, key: str) -> int:
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        j = 0
        for i in range(min(len(key), 8)):
            j = j * 31 + ord(key[i])
        return j % self.table_size

    def in_table(self, key: str) -> bool:
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""
        hash_val = self.horner_hash(key)
        index = 0
        for k in range(self.table_size):
            index = (hash_val + k ** 2) % self.table_size
            if self.hash_table[index] and self.hash_table[index][0] == key:
                return True

        return False

    def get_index(self, key: str) -> Optional[int]:
        """ Returns the index of the hash table entry containing the provided key.
        If there is not an entry with the provided key, returns None. Must be O(1)."""

        hash_val = self.horner_hash(key)

        for j in range(self.table_size):
            index = (hash_val + j**2) % self.table_size
            if self.hash_table[index] and self.hash_table[index][0] == key:
                return index

        return None

    def get_all_keys(self) -> List:
        """ Returns a Python list of all keys in the hash table."""
        lst = []
        for key in self.hash_table:
            if key is not None:
                lst.append(key[0])
        return lst

    def get_value(self, key: str) -> Any:
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""
        hash_val = self.horner_hash(key)
        index = 0
        for j in range(self.table_size):
            index = (hash_val + j ** 2) % self.table_size
            if self.hash_table[index] and self.hash_table[index][0] == key:
                return self.hash_table[index][1]
        return None

    def get_num_items(self) -> int:
        """ Returns the number of entries (words) in the table. Must be O(1)."""
        return self.num_items

    def get_table_size(self) -> int:
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self) -> float:
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size
