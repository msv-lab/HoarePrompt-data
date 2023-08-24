def count_gold(map):
    max_gold = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "P":
                x, y = i, j
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    dfs(map, x, y, visited, max_gold)
    return max_gold

def dfs(map, x, y, visited, max_gold):
    if map[x][y] == "G":
        max_gold += 1
    visited.add((x, y))
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny] != "#" and (nx, ny) not in visited:
            dfs(map, nx, ny, visited, max_gold)