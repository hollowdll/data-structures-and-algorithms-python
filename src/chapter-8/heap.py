class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """
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