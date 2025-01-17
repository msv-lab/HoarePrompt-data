def find_mst_and_matching(n, c, weights):
    from heapq import heappop, heappush
    import sys
    
    # Prim's algorithm to find MST
    def prim():
        visited = [False] * n
        min_edge = [(sys.maxsize, -1)] * n
        min_edge[0] = (0, 0)
        min_heap = [(0, 0)]
        mst_edges = []
        
        while min_heap:
            cost, u = heappop(min_heap)
            
            if visited[u]:
                continue
            
            visited[u] = True
            mst_edges.append((min_edge[u][1], u))
            
            for v in range(n):
                if weights[u][v] > 0 and not visited[v] and weights[u][v] < min_edge[v][0]:
                    min_edge[v] = (weights[u][v], u)
                    heappush(min_heap, (weights[u][v], v))
        
        return mst_edges[1:]  # exclude the first dummy edge
    
    mst_edges = prim()
    mst_weight = sum(weights[u][v] for u, v in mst_edges)
    
    # Convert edges to adjacency list
    adj_list = [[] for _ in range(n)]
    for u, v in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Find maximum matching in the tree using a simple DFS based approach
    def dfs(v, match, visited):
        for u in adj_list[v]:
            if not visited[u]:
                visited[u] = True
                if match[u] == -1 or dfs(match[u], match, visited):
                    match[u] = v
                    return True
        return False
    
    match = [-1] * n
    result = 0
    for v in range(n):
        visited = [False] * n
        if dfs(v, match, visited):
            result += 1
    
    max_matching = result // 2  # each edge counted twice
    total_cost = mst_weight + max_matching * c
    
    return total_cost

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
c = int(data[1])
weights = []
index = 2
for i in range(n):
    weights.append(list(map(int, data[index:index+n])))
    index += n

# Solve the problem
result = find_mst_and_matching(n, c, weights)
print(result)