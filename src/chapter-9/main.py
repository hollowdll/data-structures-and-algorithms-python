from sorting import insertion_sort, quick_sort
from random import randint
import time

def do_quicksort():
    arr = [6,8,5,1,2,23,98,69,420,5,8,12,9999999,12345,645,54,112,54534,666,12,53,63,2,434343]
    print('quick_sort:', quick_sort(arr))

    array = [randint(0,10000) for _ in range(10000)]
    start_time = time.time()
    quick_sort(array)
    end_time = time.time() - start_time
    print(f'quick_sort runtime: {end_time}')


def main():
    arr = [6,8,5,1,2,23,98,69,420,5,8,12,9999999,12345,645]
    insertion_sort(arr)
    print('insertion_sort:', arr)
    do_quicksort()

if __name__ == '__main__':
    main()