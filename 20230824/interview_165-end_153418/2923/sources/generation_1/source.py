def min_soldiers(w, h, grid):
    INF = float('inf')
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(r, c, visited, soldiers):
        queue = [(r, c)]
        visited[r][c] = True
        count = 0

        while queue:
            x, y = queue.pop(0)
            if grid[x][y] == 'B':
                return count
            elif grid[x][y].isdigit() and int(grid[x][y]) > soldiers:
                soldiers = int(grid[x][y])
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                    if grid[nx][ny] == 'A' or grid[nx][ny] == 'B' or int(grid[nx][ny]) <= soldiers:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            count += 1
        return INF

    ans = INF
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'A':
                for dx, dy in dirs:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < h and 0 <= ny < w:
                        if grid[nx][ny] == 'B':
                            ans = min(ans, 0)
                            break
                        elif grid[nx][ny] == 'A':
                            break
                        elif grid[nx][ny].isdigit():
                            visited = [[False] * w for _ in range(h)]
                            soldiers = int(grid[nx][ny])
                            soldiers_needed = bfs(nx, ny, visited, soldiers)
                            if soldiers_needed < INF:
                                ans = min(ans, soldiers_needed)
                                break

    if ans == INF:
        return -1
    else:
        return ans

w, h = map(int, input().split())
grid = [input() for _ in range(h)]
print(min_soldiers(w, h, grid))