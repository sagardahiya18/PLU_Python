#Count and display the total number of nodes in the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.ref
        

    def count_nodes(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.ref
        return count

# Example usage
ll = LinkedList()
ll.insert_start(50)
ll.insert_start(40)
ll.insert_start(30)
ll.insert_start(20)
ll.insert_start(10)

ll.display()
print("Total number of nodes:", ll.count_nodes())
