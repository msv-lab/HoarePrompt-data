from collections import defaultdict

def find_expected_length(n, roads):
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    return dfs(1, 0, graph, visited) / n

def dfs(city, length, graph, visited):
    visited.add(city)
    num_neighbours = len(graph[city]) - (city != 1)
    if num_neighbours == 0:
        return length
    
    expected_length = 0
    for neighbour in graph[city]:
        if neighbour not in visited:
            expected_length += dfs(neighbour, length + 1, graph, visited)
    
    return expected_length / num_neighbours

n = int(input())
roads = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    roads.append((u, v))

expected_length = find_expected_length(n, roads)
print("{:.15f}".format(expected_length))