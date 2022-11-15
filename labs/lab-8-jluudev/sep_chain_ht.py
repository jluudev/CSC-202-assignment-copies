from typing import Any, Tuple, List

class MyHashTable:

    def __init__(self, table_size: int = 11):
        self.table_size = table_size
        self.hash_table: List = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0

    def insert(self, key: int, value: Any) -> None:
        """Takes a key, and an item.  Keys are valid Python non-negative integers.
        If key is negative, raise ValueError exception
        The function will insert the key-item pair into the hash table based on the
        hash value of the key mod the table size (hash_value = key % table_size)"""
        if key < 0:
            raise ValueError
        hash_value = key % self.table_size
        key_pair = (key, value)
        col = False

        for i in range(len(self.hash_table[hash_value])):
            if self.hash_table[hash_value][i][0] == key:
                self.hash_table[hash_value][i] = (key, value)
                self.num_items -= 1
                col = True

        self.num_items += 1

        if len(self.hash_table[hash_value]) > 0 and not col:
            self.num_collisions += 1

        if not col:
            self.hash_table[hash_value].append(key_pair)

        if self.load_factor() > 1.5:
            old_hash = self.hash_table
            self.hash_table = [[] for _ in range((2 * self.table_size) + 1)]
            self.num_items = 0
            self.table_size = 2*self.table_size+1
            collisions = self.num_collisions
            for i in old_hash:
                for j in i:
                    self.insert(j[0], j[1])
            self.num_collisions = collisions


    def get_item(self, key: int) -> Any:
        """Takes a key and returns the item from the hash table associated with the key.
        If no key-item pair is associated with the key, the function raises a LookupError exception."""
        hash_value = key % self.table_size

        for i in range(len(self.hash_table[hash_value])):
            if self.hash_table[hash_value][i][0] == key:
                return self.hash_table[hash_value][i][1]

        raise LookupError

    def remove(self, key: int) -> Tuple[int, Any]:
        """Takes a key, removes the key-item pair from the hash table and returns the key-item pair.
        If no key-item pair is associated with the key, the function raises a LookupError exception.
        (The key-item pair should be returned as a tuple)"""
        hash_value = key % self.table_size

        for i in range(len(self.hash_table[hash_value])):
            if self.hash_table[hash_value][i][0] == key:
                removed = self.hash_table[hash_value].pop(i)
                self.num_items -= 1
                return removed

        raise LookupError

    def load_factor(self) -> float:
        """Returns the current load factor of the hash table"""
        return self.num_items / self.table_size

    def size(self) -> int:
        """Returns the number of key-item pairs currently stored in the hash table"""
        return self.num_items

    def collisions(self) -> int:
        """Returns the number of collisions that have occurred during insertions into the hash table"""
        return self.num_collisions
