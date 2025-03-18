from collections import deque, defaultdict
 
def find_winner(n, edges, start):
    # Build the tree using an adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # Find the leaves
    leaves = [node for node in tree if len(tree[node]) == 1]
    
    # Function to find the distance from the start node to a target node using BFS
    def bfs(start, target):
        queue = deque([(start, 0)])  # (current_node, current_distance)
        visited = set([start])
        
        while queue:
            current, dist = queue.popleft()
            if current == target:
                return dist
            
            for neighbor in tree[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return -1  # Should never reach here if the tree is valid and connected
    
    # Compute the distances from the start node to both leaves
    dist1 = bfs(start, leaves[0])
    dist2 = bfs(start, leaves[1])
    
    # Determine the winner based on the distances
    if dist1 % 2 == 0 or dist2 % 2 == 0:
        return "Ron"
    else:
        return "Hermione"
 
# Read input
n, t = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]
starts = list(map(int, input().split()))
 
# There is only one game (t=1), so we handle just one starting position
start = starts[0]
print(find_winner(n, edges, start))