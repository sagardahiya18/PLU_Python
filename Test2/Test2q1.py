#.Create a linked list containing the values 10, 20, 30, 40, 50 and display all the elements
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_start(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    
    def display(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.ref
    
ll=LinkedList()
ll.insert_start(50)
ll.insert_start(40)
ll.insert_start(30)
ll.insert_start(20)
ll.insert_start(10)
ll.display()   
    
