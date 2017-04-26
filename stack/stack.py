class Stack(object):
    """
    Implementation the stack in python
    Last-in First out methos
    stack methods
    isEmpty()
    push(item) ---> not return
    pop() -->
    peek()---> give the last value in the stack
    size()---> give the size of the list
    """
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

"""
s = Stack()

print(s.isEmpty())
s.push(5)
s.push('arms')
print(s.pop())
s.push('penguin')
s.push('meerkat')
print(s.peek())
print(s.size())
print(s.isEmpty())
"""
