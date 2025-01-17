def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, q = int(data[index]), int(data[index + 1])
        index += 2
        
        parent = [0] * (n + 1)
        for i in range(2, n + 1):
            parent[i] = int(data[index])
            index += 1
        
        b = [0] * (n + 1)
        for i in range(1, n + 1):
            b[i] = int(data[index])
            index += 1
        
        operations = []
        for _ in range(q):
            t, x, v = int(data[index]), int(data[index + 1]), int(data[index + 2])
            operations.append((t, x, v))
            index += 3
        
        # Build the tree
        children = [[] for _ in range(n + 1)]
        for i in range(2, n + 1):
            children[parent[i]].append(i)
        
        # DFS to get subtree sizes and entry/exit times
        entry = [0] * (n + 1)
        exit = [0] * (n + 1)
        time = 0
        
        def dfs(node):
            nonlocal time
            entry[node] = time
            time += 1
            for child in children[node]:
                dfs(child)
            exit[node] = time
        
        dfs(1)
        
        # Process each prefix of operations
        growth = [0] * (n + 1)
        harvest = [0] * (n + 1)
        
        for t, x, v in operations:
            if t == 1:
                growth[x] += v
            else:
                harvest[x] += v
            
            # Check if the tree can be healthy
            total_growth = [0] * (n + 1)
            total_harvest = [0] * (n + 1)
            
            def dfs_check(node):
                total_growth[node] = growth[node]
                total_harvest[node] = harvest[node]
                for child in children[node]:
                    dfs_check(child)
                    total_growth[node] += total_growth[child]
                    total_harvest[node] += total_harvest[child]
            
            dfs_check(1)
            
            possible = True
            for i in range(1, n + 1):
                if total_growth[i] < b[i] or total_harvest[i] > total_growth[i]:
                    possible = False
                    break
            
            if possible:
                results.append("YES")
            else:
                results.append("NO")
    
    sys.stdout.write("\n".join(results) + "\n")