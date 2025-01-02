from depth_first_search import DFS

class Graph:
    def __init__(self):
        self.graphe = {}

    def add_edge(self, node, neighbor):
        if node not in self.graphe:
            self.graphe[node] = []
        self.graphe[node].append(neighbor)

# Create the graph
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'E')
g.add_edge('E', 'F')

# Undirected edges (optional, depending on the graph type)
g.add_edge('B', 'A')
g.add_edge('C', 'A')
g.add_edge('D', 'B')
g.add_edge('E', 'B')
g.add_edge('E', 'C')
g.add_edge('F', 'E')

# Test the dfs function
result = DFS.dfs(g, 'A')
print("DFS Traversal:", result)
