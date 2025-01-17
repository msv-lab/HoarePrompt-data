from collections import deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    q = int(data[index + 2])
    index += 3
    
    grid = []
    for _ in range(n):
        grid.append(data[index])
        index += 1
    
    queries = []
    for _ in range(q):
        x = int(data[index]) - 1
        y = int(data[index + 1]) - 1
        queries.append((x, y))
        index += 2
    
    # Directions for moving in the grid
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Step 1: Find all volcano positions
    volcanoes = []
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'v':
                volcanoes.append((r, c))
    
    # Step 2: Calculate distance to nearest volcano for each cell
    distance_to_volcano = [[float('inf')] * m for _ in range(n)]
    queue = deque(volcanoes)
    
    for r, c in volcanoes:
        distance_to_volcano[r][c] = 0
    
    while queue:
        r, c = queue.popleft()
        current_distance = distance_to_volcano[r][c]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#' and distance_to_volcano[nr][nc] == float('inf'):
                distance_to_volcano[nr][nc] = current_distance + 1
                queue.append((nr, nc))
    
    # Step 3: Find the boundary of the island
    island_boundary = set()
    for r in range(n):
        for c in range(m):
            if grid[r][c] == '#':
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '.':
                        island_boundary.add((nr, nc))
    
    # Step 4: For each query, calculate the maximum safety
    results = []
    for x, y in queries:
        # We need to find the maximum safety of a round trip starting from (x, y)
        # The safety is determined by the minimum distance to a volcano from the path
        # that encircles the island.
        
        # Since the problem guarantees that the ocean and volcano cells form a single
        # connected component, we can assume that any ocean cell can potentially be
        # part of a valid round trip.
        
        # The maximum safety is the minimum distance to a volcano from the island boundary
        max_safety = min(distance_to_volcano[r][c] for r, c in island_boundary)
        
        results.append(max_safety)
    
    # Output the results for each query
    for result in results:
        print(result)