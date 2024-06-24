class StackUnderflow(Exception):
    def __init__(self, message="Stack is empty"):
        self.message = message
        super().__init__(self.message)

class StackOverflow(Exception):
    def __init__(self, message="Stack is full"):
        self.message = message
        super().__init__(self.message)

class MyStack:
    def __init__(self, capacity):
        self._capacity = capacity 
        self._stack = []

    def is_empty(self):
        return len(self._stack) == 0 

    def is_full(self):
        return len(self._stack) == self._capacity
    
    def pop(self):
        if self.is_empty():
            raise StackUnderflow() 
    
    def push(self, value):
        if self.is_full():
            raise StackOverflow() 
        self._stack.append(value)

    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return 
        return self._stack[-1]
