def is_valid_minesweeper_field(n, m, field):
    def count_bombs_around(x, y):
        bomb_count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == '*':
                    bomb_count += 1
        return bomb_count

    for i in range(n):
        for j in range(m):
            if field[i][j] == '.':
                if count_bombs_around(i, j) != 0:
                    return "NO"
            elif field[i][j] == '*':
                continue
            else:
                expected_bombs = int(field[i][j])
                actual_bombs = count_bombs_around(i, j)
                if expected_bombs != actual_bombs:
                    return "NO"
    return "YES"

# Reading input
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# Checking the validity of the Minesweeper field
result = is_valid_minesweeper_field(n, m, field)
print(result)
