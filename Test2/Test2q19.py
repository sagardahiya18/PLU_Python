#19.Perform a Breadth-First Search (BFS) traversal starting from vertex A.

GLOBAL_DICT = {}

class Node:
    def __init__(self, data):
        self.data = data

class Structure:
    def generate(self, data):
        return Node(data)

    def generate_rel(self, node1, node2):
        GLOBAL_DICT[node1] = [node2] 

    def bfs(self, start):
        visited = set()
        queue = [start]
        order = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                if vertex in GLOBAL_DICT:
                    for neighbor in GLOBAL_DICT[vertex]:
                        if neighbor not in visited:
                            queue.append(neighbor)
        return order



s = Structure()
s.generate_rel("A", "B")
s.generate_rel("A", "C")
s.generate_rel("B", "D")
s.generate_rel("C", "D")

print("Graph is:", GLOBAL_DICT)


print("BFS Traversal starting from A:", s.bfs("A"))
