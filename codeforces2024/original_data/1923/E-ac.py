for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    
    # Adjust colors to be zero-indexed
    for i in range(n):
        c[i] -= 1
    
    # Initialize adjacency list for the tree
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        v, u = map(int, input().split())
        tree[v - 1].append(u - 1)
        tree[u - 1].append(v - 1)
    
    # Arrays to keep track of path counts
    mas = [0] * n
    ans = 0
    kol = [0] * n
    
    # Stack for DFS, starting with node 0
    stack = [[0, 1]]
    paren = [-1] * n  # To track parent nodes and avoid revisiting
    
    while stack:
        el, pos = stack.pop()
        
        if pos == 1:
            # First visit to the node
            kol[el] = mas[c[el]]  # Store current path count for this color
            mas[c[el]] = 0  # Reset path count for this color
            stack.append([el, 2])  # Mark node for post-visit processing
            
            # Explore children
            for x in tree[el]:
                if x != paren[el]:  # Avoid revisiting the parent
                    stack.append([el, 3])  # Mark for path count update
                    stack.append([x, 1])  # Visit child node
                    paren[x] = el  # Set parent of child node
        
        elif pos == 3:
            # After visiting a child, update path count
            ans += mas[c[el]]  # Add paths ending at this node's color
            mas[c[el]] = 0  # Reset path count for this color
        
        else:
            # Post-visit processing
            mas[c[el]] = kol[el] + 1  # Restore path count and include this node
    
    # Output the total number of beautiful paths
    print(ans + sum(kol))
