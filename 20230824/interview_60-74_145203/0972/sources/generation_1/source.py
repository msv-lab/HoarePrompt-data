n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(input())

# Check if there is a black cell in each row
for i in range(n):
    if 'B' not in grid[i]:
        print("NO")
        exit()

# Check if there is a black cell in each column
for j in range(m):
    for i in range(n):
        if grid[i][j] == 'B':
            break
    else:
        print("NO")
        exit()

# Check if there are any cells that need more than one direction change
for i in range(1, n-1):
    for j in range(1, m-1):
        if grid[i][j] == 'B':
            if not (grid[i-1][j] == 'B' or grid[i+1][j] == 'B' or grid[i][j-1] == 'B' or grid[i][j+1] == 'B'):
                print("NO")
                exit()

print("YES")