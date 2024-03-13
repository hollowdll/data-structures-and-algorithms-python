# pseudocode: https://en.wikipedia.org/wiki/Insertion_sort
def insertion_sort(array):
    """
    Sort the array using the Insertion sort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: Nothing. The array is sorted in-place.
    """
    for i in range(1, len(array)):
        key = array[i]
        insert_pos = i

        while insert_pos > 0 and array[insert_pos-1] > key:
            array[insert_pos] = array[insert_pos-1]
            insert_pos -= 1

        array[insert_pos] = key

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot_index = len(array) // 2
    pivot = array[pivot_index]
    left = []
    right = []

    for i in range(len(array)):
        if i == pivot_index:
            continue
        elif array[i] <= pivot:
            left.append(array[i])
        else:
            right.append(array[i])
    
    return quick_sort(left) + [pivot] + quick_sort(right)

def sift_down(array, start, end):
    """
    This function sinks (if necessary) the given node of a MaxHeap structure
    
    Parameters:
    - array: The heap array
    - start: The index of the node that should be sinked.
    - end: The end of the heap inside the array. The index of the last node
    
    Returns: None
    """

    # left child index: 2 * current_index + 1
    # right child index: 2 * current_index + 2

    current_index = start

    # repeat while there is a left child
    while 2*current_index+1 <= end:
        swap_index = current_index
        left_index = 2*current_index+1
        right_index = 2*current_index+2

        if array[left_index] > array[current_index]:
            swap_index = left_index

        # if right child exists
        if right_index <= end:
            if array[right_index] > array[swap_index]:
                swap_index = right_index

        # if child node is bigger than the current node
        if array[swap_index] > array[current_index]:
            array[current_index], array[swap_index] = array[swap_index], array[current_index]
            current_index = swap_index
        else:
            return
        
def heap_sort(array):
    """
    Sorts the array using the Heapsort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: Nothing. The array is sorted in-place.
    """
    end = len(array) - 1
    # Start sinking from this index. Indices after this are leaves which don't need to be sunk.
    sink_start = len(array) // 2 - 1

    # Sink the array first so it becomes Max Heap
    for start in range(sink_start, -1, -1):
        sift_down(array, start, end)

    while end > 0:
        array[0], array[end] = array[end], array[0]
        end -= 1
        sift_down(array, 0, end)