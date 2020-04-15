class Stack:
    
    """
    Implementation the stack in python using list
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
  Singly Linked list creation

  Each Node must have
  Data
  pointer

  Linked List should have head and tail
  Head
  Tail

"""
class Node:
   def __init__(self, data, next_node=None):
      self.data = data
      self.next = next_node

class LinkedList:
   def __init__(self, value=None, values = None):
      self.head = None
      self.tail = None
      if value:
          self.insert_first(value)
      if values:
         self.insert_bulk(values)

   def insert_first(self, value):
       node = Node(value)
       if self.head:
           node.next = self.head
           self.head = node
       else:
           self.head = self.tail = node

   def delete_first(self):
       if self.head:
           temp = self.head.data
           self.head = self.head.next
           return temp

   def peek(self):
       return self.head.data

   def insert_bulk(self, values):
       if isinstance(values, list):
          for value in values:
              self.insert_first(value)
       else:
           raise Exception('Values must be List object')


   #miscellaneous
   def __iter__(self):
       """
         get all the values from LinkedList
       """
       if self.head:
          node = self.head
          while node:
              yield node.data
              node = node.next
       return None

   def __str__(self):
       """
         reutrn all the values in the linked list
       """
       values = [str(x) for x in self]
       return "->".join(values)

class Stack(LinkedList):
    
    """
      Stack Implementation using linked list 
    """
    def __init__(self, value=None):
        super().__init__()
        if value:
            if isinstance(value, list):
                self.push_bulk(value)
            else:
                self.push(value)

    def push_bulk(self, values):
        super().insert_bulk(values)

    def push(self, value):
        super().insert_first(value)

    def pop(self):
        return super().delete_first()

    def isEmpty(self):
        if self.head:
            return True
        return False


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
