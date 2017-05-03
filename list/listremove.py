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
class Orderlist:
    def __init__(self):
        self.head = None

    def add(self,item):
        current = self.head
        stop = False
        previous = None
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            #temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

"""remove the element from the last node of the list"""

    def delfront(self):
        current = self.head
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        previous.next = None

    """remove the single list head value
    """
    def delrear(self):
        self.head = None

mylist = Orderlist()
mylist.add(5)
mylist.delrear()
#mylist.search(6)
