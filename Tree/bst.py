"""Helper function to apply binary tree"""
class TreeNode:
    def __init__(self,key,value,left=None,right=None,parent=None):
        self.key = key
        self.payload = value
        self.left = left
        self.right = right
        self.parent = parent
    def hasleftchild(self):
        return self.left
    def hasrightchild(self):
        return self.right
    def isleft(self):
        return self.parent and self.parent.left == self
    def isright(self):
        return self.parent and self.parent.right == self
    def isroot(self):
        return not self.parent
    def hasanychild(self):
        return self.left or self.right
    def hasbothchild(self):
        return self.left and self.right
    def isleaf(self):
        return not (self.left or self.right)
    def replacenode(self,key,value,left,right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        if self.hasleftchild():
            self.left.parent = self
        if self.hasrightchild():
            self.right.parent = self
"""Implement the binary search tree"""
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def length(self):
        return self.size

    """
    insert the value based on parent node key value
    """
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1
    def _put(self,key,value,currentnode):
        if key < currentnode.key:
            if currentnode.hasleftchild():
               self._put(key,value,currentnode.left)
            else:
                currentnode.left = TreeNode(key,value,parent=currentnode)
        else:
            if currentnode.hasrightchild():
                self._put(key,value,currentnode.right)
            else:
                currentnode.right = TreeNode(key,value,parent=currentnode)

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currentnode):
        if key == currentnode.key:
            return currentnode
        elif key < currentnode.key:
            self._get(key,currentnode.left)
        elif key > currentnode.key:
            self._get(key,currentnode.right)
        else:
            return None
    """
    If node is root remove the root else use helper function
    remove to remove the node
    """
    def delete(self,key):
        if self.size > 1 :
            removenode = self._get(self,key)
            if removenode:
                self.remove(removenode)
                self.size = self.size - 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.key == key:
            self.root = None
            self.size = self.size -1
        else:
            raise KeyError("Error,Key not in tree")
    """
    Remove the element
    """
    def remove(self,currentnode):
        # remove is leaf no child
        if currentnode.isleaf():
            if currentnode == currentnode.parent.left:
                currentnode.parent.left = None
            else:
                currentnode.parent.right = None
        #both child remove using the helper function
        elif currentnode.hasbothchildren():
            succ = currentnode.findsuccessor()
            succ.spliceout()
            currentnode.key = succ.key
            currentnode.payload = succ.payload
        else:
            #only on child left either right
            if currentnode.hasleftchild():
                if currentnode.isleftchild():
                    currentnode.left.parent = currentnode.parent
                    currentnode.parent.left = currentnode.left
                elif currentnode.isrightchild():
                    currentnode.right.parent = currentnode.parent
                    currentnode.parent.right = currentnode.right
                else:
                    currentnode.replacenode(currentnode.left.key,
                                          currentnode.left.payload,
                                           currentnode.left.left,
                                           currentnode.right.right)
            else:
                if currentnode.isleftchild():
                    currentnode.right.parent = currentnode.parent
                    currentnode.parent.left = currentnode.right
                elif currentnode.isrightchild():
                    currentnode.right.parent = currentnode.parent
                    currentnode.parent.right = currentnode.right
                else:
                    currentnode.replacenode(currentnode.right.key,
                                         currentnode.right.payload,
                                         currentnode.right.left,
                                         currentnode.right.right,)

    """
    find the minimum value
    """
    def findsuccessor(self):
        succ = None
        if self.hasrightchild():
            succ =self.right.findmin()
        else:
            if self.parent:
                if self.islefthild():
                    succ = self.parent
                else:
                    self.parent.right= None
                    succ = self.parent.findsuccessor()
                    self.parent.right = self
        return succ
    def findmin(self):
        current = self
        while current.hasleftchild():
           current = current.leftchild
        return current

    """
    remove the child
    """
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
               self.parent.leftChild = None
            else:
               self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                  self.parent.leftChild = self.leftChild
                else:
                  self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    """
    Delete item
    """
    def __delitem__(self,k):
        self.delete(k)
    """
    print the given key item
    """
    def __getitem__(self,k):
        self.get(k)

    """
    Set item like dictionary
    """
    def __setitem__(self,k,v):
        self.put(k,v)


mytree=BinarySearchTree()
mytree[2] = "first"
mytree[3] = "second"

print(mytree[2])
