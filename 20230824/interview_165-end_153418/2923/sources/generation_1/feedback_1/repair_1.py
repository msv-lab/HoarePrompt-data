INF = float('inf')
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(r, c, visited, soldiers):
    queue = [(r, c)]
    visited[r][c] = True
    count = 0

    while queue:
        x, y = queue.pop(0)
        count += 1
        if grid[x][y] == 'B':
            return count
        elif grid[x][y].isdigit() and int(grid[x][y]) > soldiers:
            soldiers = int(grid[x][y])
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                if grid[nx][ny] == 'A' or grid[nx][ny] == 'B' or (grid[nx][ny].isdigit() and int(grid[nx][ny]) <= soldiers):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return INF

w, h = map(int, input().split())

grid = []
for _ in range(h):
    row = input()
    grid.append(list(row))

ans = INF

for i in range(h):
    for j in range(w):
        if grid[i][j] == 'A':
            visited = [[False] * w for _ in range(h)]
            soldiers_needed = bfs(i, j, visited, 0)
            if soldiers_needed < INF:
                ans = min(ans, soldiers_needed)

if ans == INF:
    print(-1)
else:
    print(ans)