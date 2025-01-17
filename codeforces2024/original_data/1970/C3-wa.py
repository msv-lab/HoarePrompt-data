from collections import defaultdict
n, t = map(int, input().split())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
startNode = list(map(int, input().split()))
def iterative_dfs(start, graph, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
visited = set()
for node in startNode:
    if node not in visited:
        iterative_dfs(node, graph, visited)
for node in startNode:
    print("Ron" if node in visited else "Hermione")