
# 20.Perform a Depth-First Search (DFS) traversal starting from vertex A

GLOBAL_DICT = {}

class Node:
    def __init__(self, data):
        self.data = data

class Structure:
    def generate(self, data):
        return Node(data)

    def generate_rel(self, node1, node2):
        GLOBAL_DICT[node1] = [node2]   

    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                if vertex in GLOBAL_DICT:
                    for neighbor in reversed(GLOBAL_DICT[vertex]):
                        if neighbor not in visited:
                            stack.append(neighbor)
        return order



s = Structure()
s.generate_rel("A", "B")
s.generate_rel("A", "C")
s.generate_rel("B", "D")
s.generate_rel("C", "D")

print("Graph is:", GLOBAL_DICT)


print("DFS Traversal starting from A:", s.dfs("A"))
