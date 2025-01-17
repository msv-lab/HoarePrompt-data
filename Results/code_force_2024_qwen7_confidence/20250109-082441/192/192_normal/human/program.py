from collections import defaultdict, deque

def dfs(node, parent, depth, adj, parent_table, depth_table):
    stack = [(node, parent)]
    while stack:
        node, parent = stack.pop()
        parent_table[node] = parent
        depth_table[node] = depth[node]
        for neighbor in adj[node]:
            if neighbor != parent:
                depth[neighbor] = depth[node] + 1
                stack.append((neighbor, node))

def preprocess_lca(n, adj):
    LOG = 17  # Since n <= 100000, log2(100000) is around 17
    parent_table = [-1] * (n + 1)
    depth_table = [0] * (n + 1)
    depth = [0] * (n + 1)
    
    # Start DFS from node 1 (assuming 1 is the root)
    dfs(1, -1, depth, adj, parent_table, depth_table)
    
    # Binary lifting table
    up = [[-1] * LOG for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        up[i][0] = parent_table[i]
    
    for j in range(1, LOG):
        for i in range(1, n + 1):
            if up[i][j - 1] != -1:
                up[i][j] = up[up[i][j - 1]][j - 1]
    
    return up, depth_table

def lca(u, v, up, depth):
    if depth[u] < depth[v]:
        u, v = v, u
    
    LOG = len(up[0])
    
    # Bring u and v to the same depth
    for i in range(LOG - 1, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            u = up[u][i]
    
    if u == v:
        return u
    
    for i in range(LOG - 1, -1, -1):
        if up[u][i] != up[v][i]:
            u = up[u][i]
            v = up[v][i]
    
    return up[u][0]

def path_frequency(u, v, lca, values, parent_table):
    freq = defaultdict(int)
    
    # Traverse from u to lca
    while u != lca:
        freq[values[u]] += 1
        u = parent_table[u]
    
    # Traverse from v to lca
    while v != lca:
        freq[values[v]] += 1
        v = parent_table[v]
    
    # Include the LCA node itself
    freq[values[lca]] += 1
    
    return freq

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    
    values = [0] * (n + 1)
    for i in range(1, n + 1):
        values[i] = int(data[index])
        index += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        adj[u].append(v)
        adj[v].append(u)
    
    q = int(data[index])
    index += 1
    
    queries = []
    for _ in range(q):
        u1 = int(data[index])
        v1 = int(data[index + 1])
        u2 = int(data[index + 2])
        v2 = int(data[index + 3])
        k = int(data[index + 4])
        index += 5
        queries.append((u1, v1, u2, v2, k))
    
    # Preprocess LCA
    up, depth_table = preprocess_lca(n, adj)
    
    # Prepare parent table for path frequency calculation
    parent_table = [-1] * (n + 1)
    for i in range(1, n + 1):
        parent_table[i] = up[i][0]
    
    results = []
    
    for u1, v1, u2, v2, k in queries:
        lca1 = lca(u1, v1, up, depth_table)
        lca2 = lca(u2, v2, up, depth_table)
        
        freq1 = path_frequency(u1, v1, lca1, values, parent_table)
        freq2 = path_frequency(u2, v2, lca2, values, parent_table)
        
        mismatched_values = []
        
        all_values = set(freq1.keys()).union(set(freq2.keys()))
        
        for value in all_values:
            if freq1[value] != freq2[value]:
                mismatched_values.append(value)
        
        result = mismatched_values[:min(len(mismatched_values), k)]
        results.append(f"{len(result)} " + " ".join(map(str, result)))
    
    sys.stdout.write("\n".join(results) + "\n")