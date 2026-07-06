#Perform an Inorder Traversal on a binary tree.
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

    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)


tree = BinaryTree(10)
tree.insertNode(5)
tree.insertNode(15)
tree.insertNode(3)
tree.insertNode(7)

print("Inorder Traversal (Left → Root → Right):")
tree.inorder(tree.root)