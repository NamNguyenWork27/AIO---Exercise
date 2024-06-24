class QueueUnderflow(Exception):
    def __init__(self, message="Queue is empty"):
        self.message = message
        super().__init__(self.message)

class QueueOverflow(Exception):
    def __init__(self, message="Queue is full"):
        self.message = message
        super().__init__(self.message)

class MyQueue:
    def __init__(self, capacity):
        self._capacity = capacity 
        self._queue = []

    def is_empty(self):
        return len(self._queue) == 0 
    
    def is_full(self):
        return len(self._queue) == self._capacity
    
    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflow()
        return self._queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise QueueOverflow()
        self._queue.append(value)
    
    def front(self):
        if self.is_empty():
            print('Queue is empty')
            return 
        return self._queue[0]
