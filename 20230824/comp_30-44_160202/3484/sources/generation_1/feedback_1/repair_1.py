n, k = map(int, input().split())

if k == 0:
    print("yes")
    for i in range(n):
        row = []
        for j in range(n):
            row.append(j+1)
        print(*row)
    exit()

grid = [None] * n
col_numbers_check = [set() for _ in range(n)]

for i in range(k):
    row = list(map(int, input().split()))
    grid[i] = row
    for j in range(n):
        col_numbers_check[j].add(grid[i][j])

for j in range(n):
    if len(col_numbers_check[j]) < n:
        print("no")
        exit()

row_numbers = set(range(1, n + 1))
col_numbers = [set() for _ in range(n)]

for i in range(k):
    for j in range(n):
        col_numbers[j].add(grid[i][j])
        row_numbers.discard(grid[i][j])

for i in range(k, n-1):
    missing_num = row_numbers.pop()
    for j in range(n):
        if missing_num not in col_numbers[j]:
            grid[i][j] = missing_num
            col_numbers[j].add(missing_num)
            break
    else:
        print("no")
        exit()

for row in grid:
    print(*row)
    