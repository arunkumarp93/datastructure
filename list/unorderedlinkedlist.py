"""
Python linked list implementation and example
Node class implement the
linked list need data and next link so node initiated with data and next as None

"""
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    """
      To add the item set the new data to temp and
      next need to be set so use the setNext(self.head)
      self.head value move to next and temp added to self.head

      if self.head is empty temp.setNext() is skipped cos Node class
      self.next == None

      if self.head value is exist then it move to next and temp added to head
    """
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    """
    To remove the item from the node first need to search
    the value it it found then
    If it is in head and doesn't have previous then change the head to current.getNext()
    it will change the head to next

    if it's not head then get the current's next element use current.getNext()

    and add it to previous so the current can be remove

    """

    def remove(self,item):
        current = self.head
        found = False
        previous = None
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
