# Queue using doubly linked list

class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode: {self.data}>'

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None
    
    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Queue ({self._size} element{plural}): [{values.lstrip(", ")}]>'
    
    def enqueue(self, data):
        previous_node = None
        next_node = self._head

        new_node = ListNode(data, next=next_node, prev=previous_node)
        self._head = new_node
        
        # If list is empty
        if next_node is None:
            self._tail = new_node
        else:
            next_node.prev = new_node

        self._size += 1

    def dequeue(self):
        if not self._size:
            return None
        
        node_to_remove = self._tail
        previous_node = node_to_remove.prev

        # If node to remove is first node
        if previous_node is None:
            self._head = None
        else:
            previous_node.next = None

        self._tail = previous_node
        self._size -= 1
        value = node_to_remove.data
        del(node_to_remove)

        return value