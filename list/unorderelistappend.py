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
     check all the list until the tail and add the value at end of the linked list
     time complexity O(n)
     
    """
    def append(self,item):
        current = self.head
        tail = current
        while current != None:
            current = current.getNext()
            if current != None:
                tail = current
        if tail == None:
            self.head = Node(item)
        else:
            temp = Node(item)
            tail.setNext(temp)

mylist = UnorderedList()
mylist.add(5)
mylist.add(6)
mylist.append(7)
