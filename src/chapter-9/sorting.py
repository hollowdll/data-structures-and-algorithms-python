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