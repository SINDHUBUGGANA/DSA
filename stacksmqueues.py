"""Stacks
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed.

Key Operations of a Stack
Push: Add an element to the top of the stack.
Pop: Remove and return the top element of the stack.
Peek/Top: Return the top element without removing it.
isEmpty: Check if the stack is empty"""

class stack:
    def __init__(self):
        self.stack=[]

    def push(self, data):
        if self.is_empty:
            print("Stack is empty")
            return None
        self.stack.append(data)
    
    def pop(self):
        if self.is_empty:
            print("stack is empty to pop anything")
            return None
        print("popped {self.stack[-1]}")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty:
            print("stack is empty")
            return None
        print("top ele {self.stack[-1]}")
        return self.stack[-1]
    
    def _isempty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def printstack(self):
        print("the stack:", self.stack())

stack = stack()
stack.push(22)
stack.push(32)
stack.push(42)
stack.printstack()
stack.peek()
stack.pop()
stack.printstack()
stack.pop()