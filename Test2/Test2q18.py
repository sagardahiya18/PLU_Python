#Check whether there is a direct edge between two given vertices

GLOBAL_DICT={}
class Node:
    def __init__(self,data):
        self.data=data
        
class Structure:
     def generate(self,data):
         new_node=Node(data)
         return new_node
     
     def generate_rel(self,node1,node2):
        GLOBAL_DICT[node1] = [node2]   

     def is_connected(self, v1, v2):
        
        if v1 in GLOBAL_DICT and v2 in GLOBAL_DICT[v1]:
            return True
        return False

s = Structure()

s.generate_rel("A", "B")
s.generate_rel("A", "C")
s.generate_rel("B", "D")
s.generate_rel("C", "D")

print("Graph is:", GLOBAL_DICT)


print("Is A connected to B?", s.is_connected("A", "B"))
print("Is A connected to C?", s.is_connected("A", "C"))
print("Is B connected to D?", s.is_connected("B", "D"))
print("Is C connected to D?", s.is_connected("C", "D"))
