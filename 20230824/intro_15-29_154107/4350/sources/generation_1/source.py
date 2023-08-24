def draw_star(n, m, grid):
    stars = []
    for i in range(1, n-1):
        for j in range(1, m-1):
            if grid[i][j] == '*' and grid[i-1][j] == '*' and grid[i+1][j] == '*' and grid[i][j-1] == '*' and grid[i][j+1] == '*':
                stars.append((i+1, j+1, 1))
                size = 2
                while i-size >= 0 and i+size < n and j-size >= 0 and j+size < m and \
                      grid[i-size][j] == '*' and grid[i+size][j] == '*' and \
                      grid[i][j-size] == '*' and grid[i][j+size] == '*':
                    stars.append((i+1, j+1, size))
                    size += 1
                
                return stars
    
    return None

n, m = map(int, input().split())
grid = [input() for _ in range(n)]

stars = draw_star(n, m, grid)

if stars is None:
    print(-1)
else:
    print(len(stars))
    for star in stars:
        print(*star)