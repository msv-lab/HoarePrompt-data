from collections import deque

def is_valid(x, y, R, C):
    return x >= 0 and x < R and y >= 0 and y < C

def bfs(grid, R, C, j_x, j_y):
    visited = [[False for _ in range(C)] for _ in range(R)]
    queue = deque()
    queue.append((j_x, j_y, 0))
    visited[j_x][j_y] = True

    # Check if Joe is already at an exit square
    if j_x == 0 or j_x == R-1 or j_y == 0 or j_y == C-1:
        return 0

    while queue:
        x, y, minutes = queue.popleft()

        # Check if Joe is adjacent to an exit square
        if x == 0 or x == R-1 or y == 0 or y == C-1:
            return minutes + 1
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = x + dx
            new_y = y + dy

            if is_valid(new_x, new_y, R, C) and not visited[new_x][new_y] and grid[new_x][new_y] == '.':
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, minutes + 1))
    
    return -1

def escape_maze(R, C, maze):
    grid = []
    j_x, j_y = -1, -1
    for i in range(R):
        row = list(maze[i])  # Create a new list for each row
        grid.append(row)
        if 'J' in row:
            j_x, j_y = i, row.index('J')
    
    minutes = bfs(grid, R, C, j_x, j_y)
    return "IMPOSSIBLE" if minutes == -1 else minutes

R, C = map(int, input().split())
maze = []
for _ in range(R):
    maze.append(input())

print(escape_maze(R, C, maze))