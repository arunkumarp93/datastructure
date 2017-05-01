#from collections import deque
"""
Queue implementation used the deque from colections
here used the list to implement the Queue
"""
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
"""
queue example of hot poatato game
Add the all items of given list

assume the poatato is in the front of the queue
so move the front to rear
queue = susan,david,bill
move bill to rear like this do to all

n(n-1) step has to follow
now
queue = bill,susan,david
next move
queue = david,bill,susan
next move
queue = susan,david,bill



if all the people are shifted remove the front element
do this process until it finsih
"""
def hotPotato(numlist,num):

    d = Queue()
    for list in numlist:
        d.enqueue(list)
    while d.size() > 1:
        for i in range (num):
            d.enqueue(d.dequeue())
        d.dequeue()
    return d.dequeue()

print(hotPotato(["Bill","David","Susan"],3))
