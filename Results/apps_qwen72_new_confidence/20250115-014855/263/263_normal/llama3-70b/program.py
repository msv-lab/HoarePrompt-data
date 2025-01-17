n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            x, y = i, j
            break

row_sum = sum(grid[x])
col_sum = sum(grid[i][y] for i in range(n))
diag1_sum = sum(grid[i][i] for i in range(n))
diag2_sum = sum(grid[i][n-i-1] for i in range(n))

target_sum = max(row_sum, col_sum, diag1_sum, diag2_sum)

if target_sum == row_sum:
    print(target_sum - row_sum + 1)
elif target_sum == col_sum:
    print(target_sum - col_sum + 1)
elif target_sum == diag1_sum:
    print(target_sum - diag1_sum + 1)
elif target_sum == diag2_sum:
    print(target_sum - diag2_sum + 1)
else:
    print(-1)
