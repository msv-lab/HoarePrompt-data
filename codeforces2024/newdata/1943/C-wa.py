def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        
        # Initialize adjacency list and degree count
        adj = [set() for _ in range(n)]
        deg = [0] * n
        
        # Read edges and build the tree
        for _ in range(n - 1):
            u, v = int(data[index]), int(data[index + 1])
            index += 2
            u -= 1
            v -= 1
            adj[u].add(v)
            adj[v].add(u)
            deg[u] += 1
            deg[v] += 1
        
        # Find initial leaves
        leaves = [i for i in range(n) if deg[i] == 1]
        
        cnt = n
        rad = 0
        
        # Iteratively remove leaves
        while cnt > 2:
            cnt -= len(leaves)
            rad += 1
            new_leaves = []
            for u in leaves:
                # Each leaf has exactly one neighbor
                v = next(iter(adj[u]))
                adj[v].remove(u)
                deg[v] -= 1
                if deg[v] == 1:
                    new_leaves.append(v)
            leaves = new_leaves
        
        # Determine the operations based on remaining vertices
        if cnt == 1:
            results.append(f"{rad + 1}")
            for i in range(rad + 1):
                results.append(f"{leaves[0] + 1} {i}")
        else:
            if rad % 2 == 1:
                results.append(f"{rad + 1}")
                for i in range(1, rad + 2, 2):
                    results.append(f"{leaves[0] + 1} {i}")
                    results.append(f"{leaves[1] + 1} {i}")
            else:
                results.append(f"{rad + 2}")
                for i in range(rad + 2):
                    results.append(f"{leaves[0] + 1} {i}")
    
    # Print all results
    sys.stdout.write("\n".join(results) + "\n")