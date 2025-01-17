def can_gather_ants(n, edges):
    from collections import defaultdict, deque
    
    # Create adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Function to simulate ant movement
    def simulate_movement(start):
        visited = set()
        queue = deque([(start, 0)])  # (house, number of ants)
        while queue:
            house, ants = queue.popleft()
            if house in visited:
                continue
            visited.add(house)
            for neighbor in graph[house]:
                if (neighbor, ants) not in visited:
                    queue.append((neighbor, ants))
        return len(visited) == n
    
    # Check if all ants can gather at any house
    for house in range(1, n+1):
        if simulate_movement(house):
            return True
    return False

# Input reading
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]

# Output the result
print("YES" if can_gather_ants(n, edges) else "NO")