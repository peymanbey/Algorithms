# -*- coding: utf-8 -*-
"""
@author: peymanbey@github

Simple hash table in Python
"""

class HashTable(object):
    def __init__(self, size=32):
        """
        Initialize the hash table
        Internal representation is an array
        can pass the size of the array
        """
        self.array =  [None] * size
        self.size = size

    def _hash(self, key):
        """
        Return the hashed value for key
        I use a very simple hash function
        Can replace it with fancy functions
        """
        return sum(map(ord, str(key))) % self.size

    def add(self, key, value):
        """
        Add key, value pair to the hash table
        
        key: int, float or string
        value: object
        """
        ind = self._hash(key)
        if self.array[ind] is None:
            self.array[ind] = [(key, value),]
        else:
            self.array[ind].append((key, value))

    def _collision(self, ind, key):
        """
        Handle collisions
        If collision happens, compare the keys and return the correct item
        """
        for idx, item in enumerate(self.array[ind]):
                if item[0] == key:
                    return idx
        raise KeyError("key does not exist in the table")

    def get(self, key):
        """
        return the item corresponding to key 
        """
        ind = self._hash(key)
        if self.array[ind] is None:
            raise KeyError("key does not exist in the table")
        elif len(self.array[ind]) > 1:
            return self.array[ind][self._collision(ind, key)]
        else:
            return self.array[ind]
            
    def remove(self, key):
        """
        remove the item correspondig to key from table
        """
        ind = self._hash(key)
        if self.array[ind] is None:
            raise KeyError("key does not exist in the table")
        elif len(self.array[ind]) > 1:
            self.array[ind].pop(self._collision(ind, key))
        else:
            self.array.pop(ind)
#################
# test
if __name__ == "__main__":
    table = HashTable(size=6)
    inputlist = [["alks", 1234], [21.25, 5678],[1, "diooij"]]
    for key, value in inputlist:
        table.add(key, value)
    print(table.get(21.25))
    print(table.array)
    table.remove("alks")
    print(table.array)
    print(table.get("notPresentKey"))
    