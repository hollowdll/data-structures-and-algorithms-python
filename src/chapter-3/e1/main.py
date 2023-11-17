class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"<ListNode: {self.data}>"


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = ""
        while current_node:
            values += f", {current_node.data}"
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        node = ListNode(value)
        # If list is empty just point the header to the new node
        if not self._head:
            self._head = node
        else:
            # if list is not empty, search for the last element and point it to the new node
            current_node = self._head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node

    def pop(self):
        """
        Remove the last element from the list.

        Returns: The data removed or None if list is empty.
        """

        if not self._head:
            return None

        if self._head.next == None:
            val = self._head.data
            del self._head
            self._head = None
        else:
            current_node = self._head
            previous_node = None
            while current_node.next != None:
                previous_node = current_node
                current_node = current_node.next
            val = current_node.data
            del current_node
            previous_node.next = None

        return val


if __name__ == "__main__":
    list = SinglyLinkedList()
    for i in "abcd":
        list.append(i)
    val = list.pop()
    print(val, list)
