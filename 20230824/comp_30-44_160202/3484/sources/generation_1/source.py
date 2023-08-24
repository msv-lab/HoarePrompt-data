n, k = map(int, input().split())

# create the initial grid with the filled rows
grid = []
for i in range(k):
    row = list(map(int, input().split()))
    grid.append(row)

# check if each column and row already contains all integers from 1 to n
for i in range(k):
    if len(set(grid[i])) < n:
        print("no")
        break
else:
    row_numbers = set(range(1, n + 1))
    col_numbers = [set() for _ in range(n)]
    for i in range(k):
        for j in range(n):
            col_numbers[j].add(grid[i][j])

    for i in range(k, n):
        row_numbers -= set(grid[i])
        for j in range(n):
            col_numbers[j].add(grid[i][j])

    for i in range(k, n):
        missing_num = row_numbers.pop()
        for j in range(n):
            if missing_num not in col_numbers[j]:
                grid[i][j] = missing_num
                col_numbers[j].add(missing_num)
                break
        else:
            print("no")
            break
    else:
        for row in grid:
            print(*row)
