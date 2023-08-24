import sys

def count_spanning_unicyclic_subgraphs(V, E, edges):
    MOD = 10**9+7
    adj = [[] for _ in range(V+1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    def dfs(v, parent, visited, cycles):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                cycles[0] += 1
                dfs(u, v, visited, cycles)
            elif u != parent:
                cycles[0] += 1
    
    def count_cycles(v, parent, visited, cycles):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                cycles[0] += 1
                dfs(u, v, visited, cycles)
                count_cycles(u, v, visited, cycles)
    
    cycles = [0]
    visited = [False] * (V+1)
    for v in range(1, V+1):
        if not visited[v]:
            cycles[0] += 1
            dfs(v, 0, visited, cycles)
            count_cycles(v, 0, visited, cycles)
    
    return pow(2, cycles[0]-1, MOD)

# Read input
V, E = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(E)]

result = count_spanning_unicyclic_subgraphs(V, E, edges)

# Print output
print(int(result))