class BinaryTree:
    def __init__(self,rootobj):
        self.key = rootobj
        self.leftchild = None
        self.rightchild = None
    def insertLeft(self,newvalue):
        if self.leftchild == None:
            self.leftchild = BinaryTree(newvalue)
        else:
            t = BinaryTree(newvalue)
            t.leftchild = self.leftchild
            self.leftchild = t
    def insertRight(self,newvalue):
        if self.rightchild == None:
            self.rightchild = BinaryTree(newvalue)
        else:
            t = BinaryTree(newvalue)
            t.rightchild = self.rightchild
            self.rightchild = t
    def getRightChild(self):
        return self.rightchild
    def getLeftChild(self):
        return self.leftchild
    def setRootVal(self,obj):
        self.key = obj
    def getRootVal():
        return self.key
t = BinaryTree()
print(t)
