# A code to calculate the number of connected components of the given graph

from collections import deque

def find_connected_components_bfs(graph):
    visited = set()
    connected_components = []

    for node in graph:
        if node not in visited:
            current_component = []
            queue = deque([node])
            visited.add(node)

            while queue:
                current_node = queue.popleft()
                current_component.append(current_node)
                for neighbor in graph.get(current_node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            connected_components.append(current_component)
    return connected_components


"""
n: the number of vertices
m: the number of edges
"""

n, m = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print("Number of Connected Components:")
print(len(find_connected_components_bfs(graph)))