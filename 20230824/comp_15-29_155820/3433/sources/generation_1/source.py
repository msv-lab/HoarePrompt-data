from collections import deque

def is_valid(x, y, R, C):
    return x >= 0 and x < R and y >= 0 and y < C

def bfs(grid, fire, R, C, j_x, j_y):
    visited = [[False for _ in range(C)] for _ in range(R)]
    queue = deque()
    queue.append((j_x, j_y, 0))
    visited[j_x][j_y] = True

    while queue:
        x, y, minutes = queue.popleft()

        if x == 0 or x == R-1 or y == 0 or y == C-1:
            return minutes
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = x + dx
            new_y = y + dy

            if is_valid(new_x, new_y, R, C) and not visited[new_x][new_y] and grid[new_x][new_y] == '.':
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, minutes + 1))
    
    return -1

def escape_maze(R, C, maze):
    grid = [[] for _ in range(R)]
    j_x, j_y = -1, -1
    fire = []
    for i in range(R):
        for j in range(C):
            grid[i].append(maze[i][j])
            if maze[i][j] == 'J':
                j_x, j_y = i, j
            elif maze[i][j] == 'F':
                fire.append((i, j))
    
    minutes = bfs(grid, fire, R, C, j_x, j_y)
    return "IMPOSSIBLE" if minutes == -1 else minutes

R, C = map(int, input().split())
maze = []
for _ in range(R):
    maze.append(input())

print(escape_maze(R, C, maze))