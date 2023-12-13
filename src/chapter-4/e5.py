from e4 import Queue

def get_pairs(nums: list) -> list:
    output = []
    even_queue = Queue()
    odd_queue = Queue()

    for num in nums:
        if num % 2 == 0:
            # num is even
            val = odd_queue.dequeue()
            if val:
                output.append((num, val))
            else:
                even_queue.enqueue(num)
        else:
            # num is odd
            val = even_queue.dequeue()
            if val:
                output.append((val, num))
            else:
                odd_queue.enqueue(num)

    return output