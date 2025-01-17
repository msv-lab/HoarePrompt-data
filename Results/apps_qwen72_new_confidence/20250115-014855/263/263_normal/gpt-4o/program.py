n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Finding the location of the empty cell
empty_i, empty_j = -1, -1
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            empty_i, empty_j = i, j
            break
    if empty_i != -1:
        break

# Special case when n == 1
if n == 1:
    print(1)
    exit()

# Calculating the target sum (sum of any complete row or column)
target_sum = 0
for i in range(n):
    if i != empty_i:
        target_sum = sum(grid[i])
        break

# Calculating the sum of the row and column of the empty cell
row_sum = sum(grid[empty_i])
col_sum = sum(grid[i][empty_j] for i in range(n))

# Determining the value to fill in the empty cell
empty_value = target_sum - row_sum

# Validation check
if empty_value <= 0 or empty_value != target_sum - col_sum:
    print(-1)
    exit()

grid[empty_i][empty_j] = empty_value

# Checking all rows
for i in range(n):
    if sum(grid[i]) != target_sum:
        print(-1)
        exit()

# Checking all columns
for j in range(n):
    if sum(grid[i][j] for i in range(n)) != target_sum:
        print(-1)
        exit()

# Checking the main diagonal
if sum(grid[i][i] for i in range(n)) != target_sum:
    print(-1)
    exit()

# Checking the secondary diagonal
if sum(grid[i][n - i - 1] for i in range(n)) != target_sum:
    print(-1)
    exit()

# If all checks passed, print the value to fill the empty cell
print(empty_value)
