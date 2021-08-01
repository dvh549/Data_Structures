class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def set_left(self, value):
        self.left = Node(value)
        
    def set_right(self, value):
        self.right = Node(value)
        
    def is_leaf(self):
        if self.left == None and self.right == None:
            return True
        return False
        
class BinaryTree:
    def __init__(self):
        self.root = None
     
    def get_root(self):
        if self.root == None:
            print("Root not set yet.")
        else:
            print(self.root.value)
            return self.root
        
    def set_root(self, value):
        self.root = Node(value)
        
    def is_empty(self):
        if self.root == None:
            print("Tree is empty.")
        else:
            print("Tree is not empty.")
            
    def count_nodes(self, node):
        if node == None:
            return 0
        if node.is_leaf():
            return 1
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
        
    def no_of_nodes(self):
        if self.root == None:
            return 0
        return self.count_nodes(self.root)
        
    def count_height(self, node):
        if node == None:
            return 0
        if node.is_leaf():
            return 1
        return 1 + max(self.count_height(node.left), self.count_height(node.right))
        
    def height_of_tree(self):
        if self.root == None:
            return 0
        return self.count_height(self.root)
        
bt = BinaryTree()
bt.get_root()
bt.set_root(2)
bt.get_root()
bt.is_empty()
root = bt.get_root()
root.set_left(3)
root.set_right(4)
print(bt.no_of_nodes())
root_left = root.left
root.left.set_left(5)
print(bt.height_of_tree())
