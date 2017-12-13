# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 23:57:37 2017

@author: peymanbey@github

Binary heap
"""

class BinaryHeap:
    """
    Binary heap
    Preserving heap completeness
    Preserving heap order
    """
    def __init__(self):
        """
        Initialize the heap
        First element at heap[0] is always 0 for parent calculation ease

        heap_list: list
        heap_size: int
        """
        self.heap_list = [0]
        self.currnt_size = 0

    @staticmethod
    def _left_right_parent(ind):
        """
        return left, right and parentindex
        """
        return 2 * ind, 2 * ind + 1, ind // 2

    def heap_up(self, ind):
        """
        Percolate and element up to its position

        Input
        -------
        ind: int, index of the element to percolate up
        -------
        """
        while ind // 2 > 0:
            _, _, parent = self._left_right_parent(ind)
            if self.heap_list[ind] < self.heap_list[parent]:
                temp = self.heap_list[parent]
                self.heap_list[parent] = self.heap_list[ind]
                self.heap_list[ind] = temp
            ind = parent

    def insert(self, elem):
        """
        Insert a new element to heap

        Input
        -------
        elem: obj,input element, arothmatic comparosion should be applicable
        -------
        """
        self.heap_list.append(elem)
        self.currnt_size += 1
        self.heap_up(self.currnt_size)

    def heap_down(self, ind):
        """
        Percolate down and element to preserve heap order

        Input
        -------
        ind: int, index of the element to percolate down
        """
        while (ind * 2) <= self.currnt_size:
            minimum_child = self.min_child(ind)
            if self.heap_list[ind] > self.heap_list[minimum_child]:
                temp = self.heap_list[minimum_child]
                self.heap_list[minimum_child] = self.heap_list[ind]
                self.heap_list[ind] = temp
            ind = minimum_child


    def min_child(self, ind):
        """
        Return the index of the child with the minimum value

        Input
        -------
        ind: int, index of the element for which to return the ind of the
        minimum child
        """
        left, right, _ = self._left_right_parent(ind)
        if right > self.currnt_size:
            min_child_ind = left
        else:
            if self.heap_list[left] < self.heap_list[right]:
                min_child_ind = left
            else:
                min_child_ind = right

        return min_child_ind

    def pop_min(self):
        """
        Pop the minimum value of the heap
        -------
        """
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.currnt_size]
        self.heap_list.pop()
        self.currnt_size -= 1
        self.heap_down(1)
#        TODO: raise StopIteration  when the list is exhausted
        return min_val

    def build_heap(self, elems):
        """
        Build a heap given the input list
        Input
        -------
        elems: list of values to fill the heap with
        """
        steps = len(elems) // 2
        self.currnt_size = len(elems)
        self.heap_list = [0] + elems[:]
        while steps > 0:
            self.heap_down(steps)
            steps = steps - 1


#####################
#test
import random

def generate_num(n=10):
    cntr = 0
    while cntr < n:
        yield random.randint(1,10**3)
        cntr += 1

heap = BinaryHeap()

for num in generate_num(n=10**2):
    heap.insert(num)
#    print(heap.heap_list)
#print(heap.heap_list)
for i in range(10):
    print(heap.pop_min())
#    print(heap.heap_list)