def is_cyclic_util(graph, node, visited, path):
    visited[node] = True
    path[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if is_cyclic_util(graph, neighbor, visited, path):
                return True
        elif path[neighbor]:
            return True

    path[node] = False
    return False

def is_acyclic(n, m, edges):
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * (n+1)
    path = [False] * (n+1)

    for u in range(1, n+1):
        if not visited[u]:
            if is_cyclic_util(graph, u, visited, path):
                return False

    return True