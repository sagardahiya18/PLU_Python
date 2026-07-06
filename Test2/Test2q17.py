# 17.Create an undirected graph with the following edges:
# * A – B
# * A – C
# * B – D
# * C – D
# Display the adjacency list of the graph.

GLOBAL_DICT={}
class Node:
    def __init__(self,data):
        self.data=data
        
class Structure:
     def generate(self,data):
         new_node=Node(data)
         return new_node
     
     def generate_rel(self,node1,node2):
        GLOBAL_DICT[node1]=[node2]
        
s = Structure()
# node1 = s.generate("A")
# node2 = s.generate("B")
# node3 = s.generate("C")

s.generate_rel("A", "B")
s.generate_rel("A", "c")
s.generate_rel("B", "D")
s.generate_rel("C", "D")

print(GLOBAL_DICT)
