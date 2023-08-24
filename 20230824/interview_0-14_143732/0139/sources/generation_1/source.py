def is_acyclic(n, m, edges):
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
    
    for u in range(1, n+1):
        visited = [False] * (n+1)
        stack = [u]
        while stack:
            node = stack.pop()
            if visited[node]:
                return True
            visited[node] = True
            stack.extend(graph[node])
    
    return False

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

if is_acyclic(n, m, edges):
    print("YES")
else:
    print("NO")