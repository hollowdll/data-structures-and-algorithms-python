def merge_sort(array):
    """
    Sort the array using the Merge sort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: The sorted array.
    """

    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    merged_array = []
    left_index = right_index = 0

    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    # loop the halves and compare the values
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged_array.append(left_half[left_index])
            left_index += 1
        else:
            merged_array.append(right_half[right_index])
            right_index += 1

    # add the remaining elements of the other half
    if left_index < len(left_half):
        merged_array.extend(left_half[left_index:])
    elif right_index < len(right_half):
        merged_array.extend(right_half[right_index:])

    return merged_array

def fib(n):
    """
    Calculate the Fibonacci's series value for integer n.
    This solution uses tabulation to calculate the result bottom-up.
    
    Parameters:
    - n: The number to use in the Fibonacci's series.
    
    Returns: The calculated value of the Fibonacci's series for n
    """
    if n < 2:
        return 1

    a = 1   # n - 1
    b = 1   # n - 2

    for _ in range(n-1):
        result = a + b
        a, b = result, a

    return result
