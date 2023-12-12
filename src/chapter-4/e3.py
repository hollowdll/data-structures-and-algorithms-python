from e1 import Stack

class StackBasedQueue():
    def __init__(self):
        self._size = 0
        self._InboundStack = Stack()
        self._OutboundStack = Stack()
        
    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack]
        values.extend([c for c in self._OutboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        self._InboundStack.push(data)
        self._size += 1

    def dequeue(self):
        if not self._OutboundStack:
            if not self._InboundStack:
                return None

            while self._InboundStack:
                self._OutboundStack.push(self._InboundStack.pop())

        self._size -= 1
        return self._OutboundStack.pop()