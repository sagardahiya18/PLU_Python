# Create the following binary tree:
# ```
# 50
# / \
# 30 70
# ```
# Display the root, left child, and right child.

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BinaryTree:
    def __init__(self,data):
        self.root=Node(data)
        
    def insertNode(self,data):
        new_node=Node(data)
        if self.root is None:
            self.root=new_node
        else:
            current=self.root    
            while True:
                if data<current.data:
                    if current.left is None:
                        current.left=new_node
                        break
                    else:
                        current=current.left
                else:
                    if current.right is None:
                        current.right=new_node
                        break
                    else:
                        current=current.right
                        
    def display(self):
        print("Root: ",self.root.data)
        print("Left Child: ",self.root.left.data)
        print("Right Child: ",self.root.right.data)
        
bt=BinaryTree(50)
bt.insertNode(30)
bt.insertNode(70)
bt.display()