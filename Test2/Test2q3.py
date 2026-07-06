#.Delete the node containing 30 from the linked list and display the updated list

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def delete_mid(self,prev):
        del_node=prev.ref
        prev.ref=del_node.ref
        del_node.ref=None
    
    def traverse(self):
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

ll.delete_mid(second)
ll.traverse()
