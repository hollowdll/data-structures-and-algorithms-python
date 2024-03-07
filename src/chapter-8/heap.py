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
        index = self._size - 1

        while index > 0:
            child = self._heap[index]
            parent_index = (index - 1) // 2
            parent = self._heap[parent_index]

            if child < parent:
                self._heap[parent_index] = child
                self._heap[index] = parent
                index = parent_index
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
            
def binary_search_iterative(array, value):
    """
    Performs a binary search in the the array for the given value
    
    Parameters:
    - array: The array where to perform the search
    - value: The value being searched
    
    Returns: The index of the value if it is found or None if it is not found.
    """
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = start + (end - start + 1) // 2

        if array[mid] == value:
            return mid
        elif value < array[mid]:    # check left half
            end = mid - 1
        elif value > array[mid]:    # check right half
            start = mid + 1

    return None

def interpolation_search(array, value, start=None, end=None):
    """
    Performs an Interpolation search in the the array for the given value
    
    Parameters:
    - array: The array where to perform the search
    - value: The value being searched
    
    Returns: The index of the value if it is found or None if it is not found.
    """
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1

    mid = start + int((end - start) * ((value - array[start]) / (array[end] - array[start])))

    if mid > end or mid < start:
        return None

    if value == array[mid]:
        return mid
    elif value < array[mid] and mid >= start + 1:
        return interpolation_search(array, value, start=start, end=mid-1)
    elif value > array[mid] and mid <= end - 1:
        return interpolation_search(array, value, start=mid+1, end=end)
    
    return None