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
    def isEmpty(self):
        return self.head == None

    """
     search same as the UnorderedList only diff is
     stop when it find the item
     
    """
    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    """
     Orderlist benefit no need to check the whole list if item is less than

     the current value we can stop remaining in the list

     add the item by previous to the item and item to the current node

    """

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

mylist = Orderlist()
mylist.add(5)
mylist.add(6)
#mylist.search(6)
