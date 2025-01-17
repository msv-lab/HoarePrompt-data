from collections import defaultdict, deque

def dfs(node, parent, depth, adj, euler, first, last, depth_list):
    euler.append(node)
    first[node] = len(euler) - 1
    depth_list[node] = depth
    for neighbor in adj[node]:
        if neighbor != parent:
            dfs(neighbor, node, depth + 1, adj, euler, first, last, depth_list)
            euler.append(node)
    last[node] = len(euler) - 1

def build_lca(n, adj):
    euler = []
    first = [-1] * (n + 1)
    last = [-1] * (n + 1)
    depth_list = [-1] * (n + 1)
    dfs(1, -1, 0, adj, euler, first, last, depth_list)
    
    m = len(euler)
    log = [0] * (m + 1)
    for i in range(2, m + 1):
        log[i] = log[i // 2] + 1
    
    st = [[0] * (log[m] + 1) for _ in range(m)]
    for i in range(m):
        st[i][0] = euler[i]
    
    j = 1
    while (1 << j) <= m:
        i = 0
        while (i + (1 << j) - 1) < m:
            if depth_list[st[i][j - 1]] < depth_list[st[i + (1 << (j - 1))][j - 1]]:
                st[i][j] = st[i][j - 1]
            else:
                st[i][j] = st[i + (1 << (j - 1))][j - 1]
            i += 1
        j += 1
    
    return first, last, depth_list, st, log

def lca(u, v, first, depth_list, st, log):
    left = first[u]
    right = first[v]
    if left > right:
        left, right = right, left
    j = log[right - left + 1]
    if depth_list[st[left][j]] < depth_list[st[right - (1 << j) + 1][j]]:
        return st[left][j]
    else:
        return st[right - (1 << j) + 1][j]

def path_values(u, v, lca_node, values, first, last):
    path = set()
    for node in [u, v]:
        while node != lca_node:
            path.add(values[node])
            node = parent[node]
    path.add(values[lca_node])
    return path

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
    
    adj = defaultdict(list)
    for _ in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        adj[u].append(v)
        adj[v].append(u)
    
    first, last, depth_list, st, log = build_lca(n, adj)
    
    q = int(data[index])
    index += 1
    
    results = []
    for _ in range(q):
        u1 = int(data[index])
        v1 = int(data[index + 1])
        u2 = int(data[index + 2])
        v2 = int(data[index + 3])
        k = int(data[index + 4])
        index += 5
        
        lca1 = lca(u1, v1, first, depth_list, st, log)
        lca2 = lca(u2, v2, first, depth_list, st, log)
        
        path1_values = path_values(u1, v1, lca1, values, first, last)
        path2_values = path_values(u2, v2, lca2, values, first, last)
        
        diff_values = path1_values.symmetric_difference(path2_values)
        
        result = list(diff_values)[:min(len(diff_values), k)]
        results.append(f"{len(result)} " + " ".join(map(str, result)))
    
    sys.stdout.write("\n".join(results) + "\n")