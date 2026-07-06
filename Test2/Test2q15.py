#Count the total number of nodes present in a binary tree.

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

    def countNodes(self, node):
        if node is None:
            return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)
tree = BinaryTree(10)
tree.insertNode(5)
tree.insertNode(15)
tree.insertNode(3)
tree.insertNode(7)

print("Total number of nodes:",tree.countNodes(tree.root))