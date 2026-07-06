#Insert a new node containing 25 after the node containing 20

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_mid(self,data,prev):
        new_node=Node(data)
        new_node.ref=prev.ref
        prev.ref=new_node
    
    def display(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.ref
            
ll=LinkedList()
ll.head=Node(10)
second=Node(20) 

third=Node(30)
fourth=Node(40)
fifth=Node(50)

ll.head.ref=second
second.ref=third
third.ref=fourth
fourth.ref=fifth

ll.insert_mid(25,second)
ll.display()