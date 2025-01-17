def func_1(grid, r, c, visited, i1, j1, i2, j2):
    if i2 < 0 or i2 >= r or j2 < 0 or (j2 >= c):
        return False
    if grid[i2][j2] == '*' or visited[i2][j2]:
        return False
    connected_pixels = 0
    for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        (ni, nj) = (i2 + di, j2 + dj)
        if 0 <= ni < r and 0 <= nj < c and (grid[ni][nj] == '*'):
            connected_pixels += 1
    if connected_pixels < 2:
        return False
    return True

def func_2(grid, r, c, initial_position, final_position):
    visited = [[False] * c for _ in range(r)]
    q = deque()
    q.append(initial_position)
    visited[initial_position[0]][initial_position[1]] = True
    parent = {}
    while q:
        current_position = q.popleft()
        if current_position == final_position:
            break
        (i, j) = current_position
        for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            (ni, nj) = (i + di, j + dj)
            if func_1(grid, r, c, visited, i, j, ni, nj):
                visited[ni][nj] = True
                q.append((ni, nj))
                parent[ni, nj] = (i, j)
    if final_position not in parent:
        return None
    moves = []
    current_position = final_position
    while current_position != initial_position:
        parent_position = parent[current_position]
        moves.append((parent_position[0] + 1, parent_position[1] + 1, current_position[0] + 1, current_position[1] + 1))
        current_position = parent_position
    moves.reverse()
    return moves

def func_3():
    (r, c) = map(int, input().split())
    initial_grid = [input() for _ in range(r)]
    input()
    final_grid = [input() for _ in range(r)]
    initial_position = None
    final_position = None
    for i in range(r):
        for j in range(c):
            if initial_grid[i][j] == '*':
                initial_position = (i, j)
            if final_grid[i][j] == '*':
                final_position = (i, j)
    moves = func_2(initial_grid, r, c, initial_position, final_position)
    if moves:
        print('YES')
        print(len(moves))
        for move in moves:
            print(*move)
    else:
        print('NO')
if __name__ == '__main__':
    func_3()