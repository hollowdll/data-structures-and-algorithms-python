class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def next(self):
        return self._next

    def link(self, node):
        self._next = node

    def value(self):
        return self._data


class Singly_Linked_List:
    def __init__(self):
        self._head_node = None

    def append(self, data):
        current = self._head_node
        previous = None
        while current is not None:
            previous = current
            current = current.next()
        new_node = Node(data)
        if previous is None:
            self._head_node = new_node
        else:
            previous.link(new_node)

    def print_list(self):
        current = self._head_node
        print('[', end='')
        while current is not None:
            print(current.value(), end='')
            current = current.next()
            if current is not None:
                print(', ', end='')
        print(']')

    # reverse the order of the list. For example [1,2,3] -> [3,2,1]
    def reverse(self):
        prev = None
        current = self._head_node

        while current:
            next = current.next()
            current.link(prev)
            prev = current
            current = next

        self._head_node = prev
