# A code to calculate the length of the shortest cycle in the given graph

from collections import deque

def shortest_cycle_length(graph):
    min_cycle_length = float('inf')
    nodes = list(graph.keys())

    for start_node in nodes:
        distances = {node: -1 for node in nodes}
        parent = {node: None for node in nodes}
        queue = deque([(start_node, None, 0)]) # (node, parent_node, distance)
        distances[start_node] = 0

        while queue:
            current_node, current_parent, current_distance = queue.popleft()

            for neighbor in graph.get(current_node, []):
                if neighbor == current_parent:
                    continue  # Avoid going back immediately

                if distances[neighbor] != -1:  # Visited neighbor, potential cycle
                    # Cycle detected: current_node -> neighbor -> path_back_to_start_node -> start_node
                    # Length = distance(start_node, current_node) + distance(start_node, neighbor) + 1 (for edge current_node-neighbor)
                    cycle_length = current_distance + distances[neighbor] + 1
                    min_cycle_length = min(min_cycle_length, cycle_length)
                else:  # Unvisited neighbor
                    distances[neighbor] = current_distance + 1
                    parent[neighbor] = current_node
                    queue.append((neighbor, current_node, current_distance + 1))

    return min_cycle_length if min_cycle_length != float('inf') else -1

n, m = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(shortest_cycle_length(graph))