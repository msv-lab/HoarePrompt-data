for _ in range(int(input())):
    n = int(input())
    # Initialize adjacency list and degree list
    adj = [set() for _ in range(n)]
    deg = [0] * n
    
    # Read the edges and build the tree
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1; v -= 1  # Convert to 0-based index
        adj[u].add(v)
        adj[v].add(u)
        deg[u] += 1
        deg[v] += 1
    
    # Identify initial leaves
    leaves = list(filter(lambda x: deg[x] <= 1, [i for i in range(n)]))
    
    cnt = n  # Count of remaining vertices
    rad = 0  # Radius of the tree
    
    # Process layers of leaves
    while cnt > 2:
        cnt -= len(leaves)  # Remove current leaves
        rad += 1  # Increase radius
        nls = []  # New leaves
        for u in leaves:
            v = min(adj[u])  # Get the only neighbor of the leaf
            adj[v].remove(u)  # Remove the leaf from its neighbor's adjacency list
            deg[v] -= 1  # Decrease the degree of the neighbor
            if deg[v] == 1:  # If it becomes a leaf, add to new leaves
                nls.append(v)
        leaves = nls  # Update leaves to new leaves
    
    # Output the result based on the remaining vertices
    if cnt == 1:
        # If one vertex remains, perform operations from the center
        print(rad + 1)
        for i in range(rad + 1):
            print(leaves[0] + 1, i)
    else:
        # If two vertices remain, alternate operations
        if rad % 2:
            print(rad + 1)
            for i in range(1, rad + 2, 2):
                print(leaves[0] + 1, i)
                print(leaves[1] + 1, i)
        else:
            print(rad + 2)
            for i in range(rad + 2):
                print(leaves[0] + 1, i)