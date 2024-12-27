n, m = map(int, raw_input().split())
grid = [ raw_input().strip() for r in range(n) ]

col_dirs = [ [ 0 for c in range(m) ] for r in range(n) ]
for c in range(m):
    count = -1
    for r in range(n):
        if grid[r][c] == '*':
            count += 1
            col_dirs[r][c] += count
    count = -1
    for r in range(n - 1, -1, -1):
        if grid[r][c] == '*':
            count += 1
            col_dirs[r][c] += count

row_dirs = [ [ 0 for c in range(m) ] for r in range(n) ]
for r in range(n):
    count = -1
    for c in range(m):
        if grid[r][c] == '*':
            count += 1
            row_dirs[r][c] += count
    count = -1
    for c in range(m - 1, -1, -1):
        if grid[r][c] == '*':
            count += 1
            row_dirs[r][c] += count

#print(grid)
#print(col_dirs)
#print(row_dirs)

total = 0
for r in range(n):
    for c in range(m):
        total += row_dirs[r][c] * col_dirs[r][c]
print(total)
