class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """
        # parent index = (child_index - 1) // 2

        if self._size <= 1:
            return

        # set last element as initial index
        elem_index = self._size - 1

        while elem_index > 0:
            elem = self._heap[elem_index]
            parent_index = (elem_index - 1) // 2
            parent = self._heap[parent_index]

            if elem < parent:
                self._heap[parent_index] = elem
                self._heap[elem_index] = parent
                elem_index = parent_index
            else:
                return
            
    def insert(self, value):
        """
        Inserts a new element to the end of the heap
        """
        self._heap.append(value)
        self._size += 1
        self._float()

    def _sink(self):
        """
        Sinks the root node of the heap until the heap is in order
        """
        # child index (x = parent) = 2x + 1 (left) and 2x + 2 (right)

        if self._size <= 1:
            return
        
        index = 0

        # if at least one child
        while index*2+1 < self._size:
            left_index = index*2+1
            right_index = index*2+2
            # if two children
            if right_index < self._size:
                left = self._heap[left_index]
                right = self._heap[right_index]
                child_index = left_index if left <= right else right_index
            # only one child
            else:
                child_index = left_index

            parent = self._heap[index]
            child = self._heap[child_index]

            # swap parent and child
            if parent > child:
                self._heap[index] = child
                self._heap[child_index] = parent
                index = child_index
            else:
                return
