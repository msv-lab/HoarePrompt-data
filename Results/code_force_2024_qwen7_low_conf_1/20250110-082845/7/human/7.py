def bfs(tree, start_node):
    from collections import deque
    queue = deque([start_node])
    distances = {start_node: 0}
    while queue:
        node = queue.popleft()
        current_distance = distances[node]
        for neighbor in tree[node]:
            if neighbor not in distances:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)
    return distances

def solve_tree_compass(n, edges):
    # Build the tree from edges
    tree = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # Start from an arbitrary node, here node 1
    distances = bfs(tree, 1)
    
    # Determine operations
    operations = []
    max_distance = max(distances.values())
    for d in range(max_distance + 1):
        nodes_at_d = [node for node, dist in distances.items() if dist == d]
        if nodes_at_d:
            operations.append((nodes_at_d[0], d))
    
    return len(operations), operations

# Example usage
n = 4
edges = [(1, 2), (1, 3), (1, 4)]
num_operations, operations = solve_tree_compass(n, edges)
print(num_operations)
for v, d in operations:
    print(v, d)