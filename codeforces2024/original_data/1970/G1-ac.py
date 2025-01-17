def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        c = int(data[index + 2])
        index += 3
        
        # Read the edges
        edges = []
        for _ in range(m):
            u = int(data[index]) - 1
            v = int(data[index + 1]) - 1
            edges.append((u, v))
            index += 2
        
        if n == 2:
            # If there are only two nodes, the only possible split is 1-1
            results.append(2)
            continue
        
        # Since m = n - 1, the graph is a tree
        # We need to find a way to cut one edge to minimize x^2 + y^2 where x + y = n
        
        # Use DFS to find the sizes of subtrees
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def subtree_sizes(root):
            size = [0] * n
            visited = [False] * n
            stack = [root]
            parent = [-1] * n
            visited[root] = True
            
            # Post-order traversal to calculate sizes
            post_order = []
            while stack:
                node = stack.pop()
                post_order.append(node)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        parent[neighbor] = node
                        stack.append(neighbor)
            
            # Calculate subtree sizes
            while post_order:
                node = post_order.pop()
                size[node] = 1  # count itself
                for neighbor in graph[node]:
                    if neighbor != parent[node]:  # only consider children
                        size[node] += size[neighbor]
            
            return size
        
        sizes = subtree_sizes(0)
        
        # Now find the optimal cut
        min_funding = float('inf')
        for u, v in edges:
            if sizes[u] > sizes[v]:
                u, v = v, u
            # u is the child of v in the considered edge
            size_u = sizes[u]
            size_v = n - size_u
            
            funding = size_u**2 + size_v**2
            min_funding = min(min_funding, funding)
        
        results.append(min_funding)
    
    # Output all results
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()