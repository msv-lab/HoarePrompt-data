from collections import defaultdict, deque

def dfs(graph, start, colors, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor] and colors[neighbor] == 1:
                stack.append(neighbor)

def is_chain(graph, colors):
    black_vertices = [i for i, color in enumerate(colors) if color == 1]
    
    if len(black_vertices) <= 1:
        return "Yes"
    
    # Find the farthest black vertex from the first black vertex
    visited = [False] * len(colors)
    dfs(graph, black_vertices[0], colors, visited)
    farthest_vertex = max((i for i in range(len(colors)) if visited[i]), key=lambda x: colors[x])
    
    # Reset visited array and perform DFS from the farthest vertex
    visited = [False] * len(colors)
    dfs(graph, farthest_vertex, colors, visited)
    
    # Check if all black vertices are visited exactly once
    for i in black_vertices:
        if not visited[i]:
            return "No"
    
    return "Yes"

def solve(n, q, colors, edges, queries):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    results = []
    for query in queries:
        # Toggle the color of the queried vertex
        colors[query-1] ^= 1
        # Check if the black vertices form a chain
        result = is_chain(graph, colors)
        results.append(result)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

index = 0
results = []

t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    q = int(data[index + 1])
    index += 2
    
    colors = list(map(int, data[index:index + n]))
    index += n
    
    edges = []
    for _ in range(n - 1):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        edges.append((x, y))
    
    queries = []
    for _ in range(q):
        u = int(data[index])
        index += 1
        queries.append(u)
    
    results.extend(solve(n, q, colors, edges, queries))

# Print results
print("\n".join(results))