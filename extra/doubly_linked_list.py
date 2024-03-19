class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._previous = None
    def next(self):
        return self._next
    def previous(self):
        return self._previous
    def link_next(self, node):
        self._next = node
    def link_previous(self, node):
        self._previous = node
    def value(self):
        return self._data
    

class Sorted_Doubly_Linked_List:
    def __init__(self):
        self._head_node = None

    def print_list(self):
        current = self._head_node
        print('[', end='')
        while current is not None:
            print(current.value(), end='')
            current = current.next()
            if current is not None:
                print(', ', end='')
        print(']')

    # append elements in the way that the list remains sorted
    def append(self, data):
        current = self._head_node
        previous = None

        while current is not None:
            if data < current.value():
                new_node = Node(data)
                current.link_previous(new_node)
                new_node.link_next(current)

                if previous is None:
                    self._head_node = new_node
                elif previous is not None:
                    new_node.link_previous(previous)
                    previous.link_next(new_node)
                return
            elif current.next() is None:
                new_node = Node(data)
                new_node.link_previous(current)
                current.link_next(new_node)
                return

            current = current.next()
            previous = current.previous()

        if self._head_node is None:
            new_node = Node(data)
            self._head_node = new_node