from collections import deque

def solve(n, m, q, grid, queries):
    # Step 1: Precompute Manhattan distances to volcanos
    dist_to_volcano = [[float('inf')] * m for _ in range(n)]
    volcano_positions = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 'v']
    
    queue = deque(volcano_positions)
    for x, y in volcano_positions:
        dist_to_volcano[x][y] = 0
    
    # BFS for multi-source shortest path
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and dist_to_volcano[nx][ny] == float('inf'):
                dist_to_volcano[nx][ny] = dist_to_volcano[x][y] + 1
                queue.append((nx, ny))
    
    # Step 2: Extract island boundary
    boundary = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if grid[ni][nj] == '.':
                        boundary.add((ni, nj))
    
    # Step 3: Process queries
    results = []
    for x, y in queries:
        if (x - 1, y - 1) in boundary:
            results.append(dist_to_volcano[x - 1][y - 1])
        else:
            results.append(0)  # Invalid round trip
    
    return results

# Input handling and output
n, m, q = map(int, input().split())
grid = [input().strip() for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(q)]
results = solve(n, m, q, grid, queries)
print("\n".join(map(str, results)))
