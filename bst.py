import mytree
class BSTnode(mytree.TreeNode):
    def ins(self,item):
        if item<self.item:
            if self.left == None:
                self.left = BSTnode(item)
            else:
                self.left.ins(item)
        else:
            if self.right == None:
                self.right = BSTnode(item)
            else:
                self.right.ins(item)
    def trace(self,target):
        if self.left.item == target :
            self.left = None
        elif self.right.item == target:
            self.right = None
        elif target < self and self.left != None:
            self.left.trace(target)
        elif target > self and self.right != None:
            self.right.trace(target)
    def serch(self,target):
        if self.item == target :
            return self
        elif target < self.item and self.left != None:
            return self.left.search(target)
        elif target > self.item and self.right != None:
            return self.right.search(target)
        return False
    def delete(self,target):
        key = self.serch(target)
        if key is False:
            return False
        if key.merge() == False:
            if self.item == target :
                self.item = None
            else:
                self.trace(target)
        return True
    def merge(self):
        if self.left == None and self.right == None:
            return False
        elif self.left == None :
            self.item = self.right.item
            self.left = self.right.left
            self.right = self.right.right
        elif self.right == None :
            self.item = self.left.item
            self.right = self.left.right
            self.left = self.left.left
        elif self.left.right == None:
            self.item = self.left.item
            self.left =self.left.left
        else:
            temp = self.left
            while temp.right.right != None:
                temp = temp.right
            self.item = temp.right.item
            temp.right = temp.right.left
            
            
        
  
            
