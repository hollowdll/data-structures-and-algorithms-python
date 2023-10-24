"""
Write a function named combine_lists that accepts two lists of integers as parameters.
Consider that the two lists are already sorted (The numbers are already in order from smallest to biggest number).
Your function should return a list that combines the two lists and at the same time is itself also sorted.
To be clear all elements of the input lists should be in the output list
and len(input_list1)+len(input_list2) == len(output_list).
Notice that your function should return the list, not print it.

You can use whatever you want as the name of the parameters.
You don't need to use any special function or functionality to complete the task.
Specially don't use any kind of sorting function of lists or Python in general.
Just normal Python list actions are enough for this task.
Iterate over the lists adding one by one the the smallest of the remaining elements of the two lists.
When one of the lists have been exhausted, you can just add the remaining elements of the other list to the output list.
"""

def combine_lists(input_list1: list[int], input_list2: list[int]) -> list[int]:
    output_list = []

    while True:
        if len(input_list1) < 1 and len(input_list2) < 1:
            return output_list

        if len(input_list1) < 1:
            if len(input_list2) > 0:
                output_list.append(input_list2[0])
                input_list2.pop(0)
                continue
        
        if len(input_list2) < 1:
            if len(input_list1) > 0:
                output_list.append(input_list1[0])
                input_list1.pop(0)
                continue
        
        if input_list1[0] < input_list2[0]:
            output_list.append(input_list1[0])
            if len(input_list1) > 0:
                input_list1.pop(0)
        else:
            output_list.append(input_list2[0])
            if len(input_list2) > 0:
                input_list2.pop(0)
        


def main():
    print(combine_lists([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]))  # output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    main()