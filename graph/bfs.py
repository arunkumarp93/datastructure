from collections import deque
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.dist = 0
        self.pred = None
        self.color = 'white'

    def getid(self):
        return self.id
    def getconnections(self):
        return self.connectedTo.keys()
    def getdistance(self):
        return self.dist
    def getpred(self):
        return self.pred
    def getcolor(self):
        return self.color
    def addneighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    def setdistance(self,d):
        self.dist = d
    def setpred(self,p):
        self.pred = p
    def setcolor(self,color):
        self.color = color

    #__str__ need to print the values
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

class Graph:
    def __init__(self):
        self.vertlist = {}
        self.numvertlist=0

    def getvetlist(self):
        return list(self.vertlist.keys())

    def getvertex(self,n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return None

    def addvertex(self,key):
        self.numvertlist += 1
        newvertex = Vertex(key)
        self.vertlist[key] = newvertex
        return newvertex

    def addedge(self,f,t,cost=0):
        if f not in self.vertlist:
            nv = self.addvertex(f)
        elif t not in self.vertlist:
            nv = self.addvertex(t)
        self.vertlist[f].addneighbor(self.vertlist[t],cost)
    def bfs(self,start):
        start.setdistance(0)
        start.setpred(None)
        vertqueue = deque([])
        vertqueue.append(start)
        print vertqueue.append(start)
        while (len(vertqueue) > 0):
            #remove the first value from queue
            currentvert = vertqueue.popleft()
            for nbr in currentvert.getconnections():
                """
                get the next vertex of currentvert in nbr and change the color to gray
                add distance and precedence

                Then add it to queue now currentvert move to next vertex in queue
                and examine it

                """
                if nbr.getcolor() == 'white':
                    nbr.setcolor('gray')
                    nbr.setdistance(currentvert.getdistance()+1)
                    nbr.setpred(currentvert)
                    vertqueue.append(nbr)
                currentvert.setcolor('black')
    def traverse(self,y):

        x = y
        #get the precedence of given vertex
        #eg: for 3 , 2 is predeccor
        while (x.getpred()):
            print(x.getid())

            #get the precedence of previous one
            #eg:- collect the 2's precedence
            
            x = x.getpred()
        print(x.getid())


g = Graph()
for i in range(1,6):
    g.addvertex(i)
g.addedge(1,2)
g.addedge(2,3)
g.addedge(2,4)
g.addedge(4,5)
g.addedge(1,5)
g.addedge(3,5)
g.addedge(4,3)
g.bfs(g.getvertex(1))
