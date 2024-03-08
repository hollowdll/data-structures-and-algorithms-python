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
    