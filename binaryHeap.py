# -*- coding: utf-8 -*-
"""
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

    def _swap_elems(self, indA, indB):
        """
        swap element indA with element indB in array heaplist
        -------
        heaplist: list
        indA: int
        indB: int
        """
        self.heap_list[indA], self.heap_list[indB] = self.heap_list[indB],\
        self.heap_list[indA]

    def _heap_up(self, ind):
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
                self._swap_elems(parent, ind)
            ind = parent

    def _heap_down(self, ind):
        """
        Percolate down an element to preserve heap order

        Input
        -------
        ind: int, index of the element to percolate down
        """
        while (ind * 2) <= self.currnt_size:
            minimum_child = self._min_child(ind)
            if self.heap_list[ind] > self.heap_list[minimum_child]:
                self._swap_elems(minimum_child, ind)
            ind = minimum_child


    def _min_child(self, ind):
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
        self._heap_up(self.currnt_size)

    def pop_min(self):
        """
        Pop the minimum value of the heap
        -------
        """
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.currnt_size]
        self.heap_list.pop()
        self.currnt_size -= 1
        self._heap_down(1)
        return min_val

    def build_heap_down(self, elems):
        """
        Build a heap given the input list
        
        Input
        -------
        elems: list of values to fill the heap with
        """
        self.currnt_size = len(elems)
        least_parent = self.currnt_size // 2
        self.heap_list = [0] + elems[:]
        while least_parent > 0:
            self._heap_down(least_parent)
            least_parent -= 1

    def build_heap_up(self, elems):
        """"""
        size = len(elems)
        self.heap_list = [0] + elems[:]
        while self.currnt_size <= size:
            self._heap_up(self.currnt_size)
            self.currnt_size += 1
        self.currnt_size = len(elems)

#####################
#test
if __name__=="__main__":
    import random
    
    def generate_num(n=10):
        cntr = 0
        while cntr < n:
            yield random.randint(1, 10**2)
            cntr += 1
    
    heap = BinaryHeap()
    
    for num in generate_num(n=10**1):
        heap.insert(num)
    
    print(heap.heap_list)
    print([heap.pop_min() for _ in range(10)], "\n")
    
    
    heap1 = BinaryHeap()
    heap2 = BinaryHeap()
    
    sample = [num for num in generate_num(10)]
    print(sample, "\n")
    heap1.build_heap_down(sample)
    heap2.build_heap_up(sample)
    print(heap1.heap_list)
    print(heap2.heap_list)
    print([heap1.pop_min() for _ in range(10)])
    print([heap2.pop_min() for _ in range(10)])