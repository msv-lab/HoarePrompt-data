n, m = map(int, input().split())

grid = []
for _ in range(n):
    row = input()
    grid.append(row)

count = 0
for i in range(n-1):
    for j in range(m-1):
        face = grid[i][j] + grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1]
        if face == "face":
            count += 1

print(count)