#Find and display all the leaf nodes of a binary tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
        
    def insertNode(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def displayLeafNodes(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.data, end=" ")
        else:
            self.displayLeafNodes(node.left)
            self.displayLeafNodes(node.right)


tree = BinaryTree(10)
tree.insertNode(5)
tree.insertNode(15)
tree.insertNode(3)
tree.insertNode(7)

print("Leaf nodes are:", end=" ")
tree.displayLeafNodes(tree.root)
