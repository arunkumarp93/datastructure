"""
Adajency list implementation

 two class need to created on has to keep the vertex(Node) id and connections details(vertex)
 another class need to create the vertexlist and sum of vertex(graph)
"""

class Vertex:
    """
     Vertex class hold key in self.id(individual vertex)
     store the connections in self.connectedTo with weight

     remaining methods getconnections(return all the connections),getid and getweight(return weight )
    """
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    def addneighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    def getconnections(self):
        self.connectedTo.keys()
    def getid(self):
        return self.id
    def getweight(self,nbr):
        return self.connectedTo[nbr]
      
class Graph:
    """
    Vertexlist hold all the vertex in Dictionary(self.vertexlist)
    also count the vertex and store (self.numvertices)

    addvertex increase the numvertices count ,add new vertex then add the key and
    vertex to vertexlist dictionary

    function addEdge connect two vertex if any vertex is unavailable add it to
    vertexlist
    """
    def __init__(self):
        self.vertlist = {}
        self.numlist = 0
    def addvertex(self,key):
        self.numlist = self.numlist + 1
        newvertex = Vertex(key)
        self.vertlist[key] = newvertex
        return newvertex
    def getvertex(self,n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.vertlist

    def addedge(self,f,t,cost=0):
        if f not in self.vertlist:
            nv = self.addvertex(f)
        elif t not in self.vertlist:
            nv = self.addvertex(t)
        else:
            self.vertlist[f].addneighbor(self.vertlist[t],cost)
    def getvertices(self):
        return self.vertlist.keys()
    def __iter__(self):
        return iter(self.vertlist.values())
g = Graph()
for i in range(5):
    g.addvertex(i)
