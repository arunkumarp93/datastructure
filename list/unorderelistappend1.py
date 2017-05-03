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
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
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

    def remove(self,item):
        current = self.head
        previous = None
        found = False
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

    """
     previous append has the time complexity of O(n)
     this has O(1)
     assign the value to temp and move the previous value to next
     then add the temp to self.tail or self.head position
    """
    
    def addhead(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head=temp

    def addtail(self,item):
        temp = Node(item)
        temp.setNext(self.tail)
        self.tail = temp

mylist = UnorderedList()
mylist.addtail(5)
mylist.addtail(4)
mylist.addhead(3)
mylist.addhead(2)
