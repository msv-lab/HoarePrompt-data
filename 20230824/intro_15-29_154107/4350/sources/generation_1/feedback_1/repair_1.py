def draw_star(n, m, grid):
    stars = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*' and \
               i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] == '*' and \
               i-1 >= 0 and j+1 < m and grid[i-1][j+1] == '*' and \
               i+1 < n and j-1 >= 0 and grid[i+1][j-1] == '*' and \
               i+1 < n and j+1 < m and grid[i+1][j+1] == '*':
                stars.append((i+1, j+1, 1))
                size = 2
                while i-size >= 0 and i+size < n and j-size >= 0 and j+size < m and \
                      grid[i-size][j-size] == '*' and grid[i-size][j+size] == '*' and \
                      grid[i+size][j-size] == '*' and grid[i+size][j+size] == '*':
                    stars.append((i+1, j+1, size))
                    size += 1
            
                return stars
    
    return -1

n, m = map(int, input().split())
grid = [input() for _ in range(n)]

stars = draw_star(n, m, grid)

if stars == -1:
    print(-1)
else:
    print(len(stars))
    for star in stars:
        print(*star)