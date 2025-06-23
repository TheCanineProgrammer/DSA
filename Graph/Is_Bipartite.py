# A code to check if the given graph is Bipartite or not
from collections import deque

def is_bipartite(graph):
    color = {}

    for node in graph:
        if node not in color:
            queue = deque([node])
            color[node] = 0

            while queue:
                u = queue.popleft()

                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
    return True

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

if is_bipartite(graph):
    print("Yes")
else:
    print("No")