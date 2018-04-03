class TreeNode:
    def __init__(self,item):
        self.left = None
        self.right = None
        self.item = item
    def __repr__(self):
        return self.item
    def __add__(self,nodes = None):
        assert isinstance(nodes, tuple)
        self.left = nodes[0]
        self.right = nodes[1]
    def preorder(self):
        print(self.item)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.item)
        if self.right is not None:
                self.right.inorder()
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()    
        print(self.item)
