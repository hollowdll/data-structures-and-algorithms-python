from algorithms import merge_sort

def main():
    array = [7,3,8,99,69,232,1,2,5,42,44343,3342,6656,99999,777]
    sorted_array = merge_sort(array)
    print(f'original array: {array}')
    print(f'sorted array with merge sort: {sorted_array}')

if __name__ == '__main__':
    main()