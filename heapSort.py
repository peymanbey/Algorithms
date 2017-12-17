# -*- coding: utf-8 -*-
"""
@author: peymanbey@github

HeapSort
"""

class HeapSort(object):
    """
    heap sort algorithm, min heap
    """
    def __init__(self):
        self.array = [0]
        self.size = 0

    def sort_it(self, input_array):
        """return sorted input_array"""
        self._build_heap(input_array)
        while self.size > 0:
            self._swap(1, self.size)
            self.size -= 1
            self._heap_down(1)
        self.size = len(self.array)
        return self.array[:0:-1]


    def _build_heap(self, input_array):
        """
        Make a valid min-heap
        """
        self.array = [0] + input_array[:]
        self.size = len(input_array)

        ind = self.size // 2
        while ind > 0:
            self._heap_down(ind)
            ind -= 1

    def _heap_down(self, ind):
        while 2 * ind <= self.size:
            min_child = self._min_child(ind)
            if self.array[ind] > self.array[min_child]:
                self._swap(ind, min_child)
                ind = min_child
            else:
                break

    def _min_child(self, ind):
        left, right = ind * 2, ind * 2 + 1
        if right > self.size:
            return left
        elif self.array[left] > self.array[right]:
            return right
        else:
            return left

    def _swap(self, ind_a, ind_b):
        self.array[ind_a], self.array[ind_b] = \
        self.array[ind_b], self.array[ind_a]

###################
#test
if __name__ == "__main__":
    import random

    def generate_num(n=10):
        cntr = 0
        while cntr < n:
            yield random.randint(1, 10**6)
            cntr += 1

    heapsort = HeapSort()
    temp = [num for num in generate_num(10**5)]
    print(temp)
    print(heapsort.sort_it(temp))
