"""
BinaryHeap is tree with min or max order it's stored in list
No link only heap and size need to implement
"""
class BinaryHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentsize = len(self.heaplist)
    """
     Insert is eay append to end of list
     but has to check with other elements in the list to
     maintain the heap structure

     To acheive this precup helper function is used
    """
    def insert(self,newvalue):
        self.heaplist.append(newvalue)
        self.currentlist = self.currentlist + 1
        self.precup(self.currentlist)
    """
      Divide the list into half and check the last and currentvalue
      if currentvalue is less than upper value sawp it
    """
    def precup(self,i):
        while i // 2:
            if self.heaplist[i] < self.heaplist[i//2]:
                tmp = self.heaplist[i//2]
                self.heaplist[i//2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2
    """
    Check the values in down and value is smaller than
    parent node move it
    """
    def precdown(self,i):
        while (i*2) <= self.currentsize:
            mc = self.minchild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc
   """
    Find the minimum child position
   """
    def minchild(self,i):
        if i * 2 + 1 > self.currentsize:
            return i * 2
        elif self.heaplist[i*2] < self.heaplist[i*2+1]:
            return i * 2
        else:
            return i * 2 + 1
    """
    delete the minmum child and move the last element to
    top and do the precdown and kept the binaryheap struture true
    """
    def delmin(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.currentsize = self.currentsize - 1
        self.heaplist.pop()
        self.precdown(1)
        return retval
    """
    Build the heap in the list and do the precdown
    to keep the structure for binaryheap
    """
    def buildheap(self,alist):
        i = len(alist) // 2
        self.currentsize = len(alist)
        self.heaplist = [0] + alist[:]
        while i > 0:
            self.precdown(i)
            i = i -1

bh = BinaryHeap()
bh.buildheap([9,5,6,2,3])

print(bh.delmin())
print(bh.delmin())
print(bh.delmin())
print(bh.delmin())
print(bh.delmin())
