class BinaryTree:
    """
    Binary tree class

    """
    def __init__ (self, data):
        #root node
        self.data = data
        self.left = None
        #left child
        self.right = None
        #right child

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def insert_left(self, value):
        temp = BinaryTree(value)
        if self.left is not None:
           temp.left  = self.left
        self.left =  temp

    def inset_right(self, value):
        temp = BinaryTree(value)
        if self.right is not None:
           temp.right = self.right
        self.right =  temp

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.data)

    def pre_order(self):
        print(self.data)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.data)
        if self.right:
            self.right.in_order()
