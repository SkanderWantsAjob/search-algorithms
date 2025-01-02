def dfs(graph, s1):
    pile = [s1]
    visited=[]
    while pile:
        
        node= pile.pop(-1)
        print(node)
        visited.append(node)
        # Accessing the 'graphe' attribute of the 'graph' object
        for neighbor in graph.graphe.get(node, []):  # Safe handling if node has no neighbors
            if neighbor not in visited and neighbor not in pile:

                pile.append(neighbor)
                print(pile)
    return visited


