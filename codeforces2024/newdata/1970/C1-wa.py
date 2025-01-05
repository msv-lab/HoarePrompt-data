from collections import deque

def solve():
    # Read input
    n, t = map(int, input().split())  # number of nodes (n), number of rounds (t)
    
    # Initialize adjacency list for the tree
    adj = [[] for _ in range(n + 1)]
    
    # Reading the edges of the tree
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Read the initial stone position (we only have one query, so t = 1)
    start_node = int(input())
    
    # Find the two leaf nodes (they have exactly one neighbor)
    leaf_nodes = []
    for i in range(1, n + 1):
        if len(adj[i]) == 1:  # This is a leaf node
            leaf_nodes.append(i)
    
    # Function to calculate the shortest distance from the start node to the nearest leaf
    def bfs(start):
        # Distance array
        dist = [-1] * (n + 1)
        queue = deque([start])
        dist[start] = 0
        
        while queue:
            node = queue.popleft()
            
            for neighbor in adj[node]:
                if dist[neighbor] == -1:  # Not visited
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)
        
        # Find the minimum distance to any leaf node
        min_distance = float('inf')
        for leaf in leaf_nodes:
            if dist[leaf] != -1:
                min_distance = min(min_distance, dist[leaf])
        
        return min_distance
    
    # Get the minimum distance to the nearest leaf from the start node
    min_dist_to_leaf = bfs(start_node)
    
    # Determine the winner based on the distance
    if min_dist_to_leaf % 2 == 1:
        print("Ron")  # Odd distance, Ron wins
    else:
        print("Hermione")  # Even distance, Hermione wins

# Call the function to solve the problem
solve()
