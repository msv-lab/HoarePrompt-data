def dfs(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True

    rec_stack[node] = False
    return False

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = [False] * (n + 1)
rec_stack = [False] * (n + 1)
has_cycle = False

for node in range(1, n + 1):
    if not visited[node]:
        if dfs(node, graph, visited, rec_stack):
            has_cycle = True
            break

if has_cycle:
    print("NO")
else:
    print("YES")
