#State of the program right berfore the function call: grid is a 2D list of characters representing a grid of squares with at least one black square. Each character is either '#' or '.'.
def func_1(grid):
    H, W = len(grid), len(grid[0])
    q = []
    dist = [0] * H
    for i in range(H):
        dist[i] = []
        
    #State of the program after the  for loop has been executed: grid is a 2D list of characters representing a grid of squares with at least one black square, H is greater than 0, W is the length of the first row of the grid, dist is a list of empty lists with length H
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                q.append([i, j])
                grid[i][j] = 0
        
    #State of the program after the  for loop has been executed: grid is a 2D list of characters representing a grid of squares with at least one black square. All black squares ('#') have been replaced with 0. The list q contains the coordinates of all black squares. The variables H, W, dist, i, and j maintain their initial conditions.
    maxx = 0
    while q:
        qq = []
        
        for i, j in q:
            for r, c in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= r < H and 0 <= c < W and grid[r][c] == '.':
                    grid[r][c] = grid[i][j] + 1
                    maxx = max(maxx, grid[r][c])
                    qq.append([r, c])
        
        q = qq
        
    #State of the program after the loop has been executed: After the loop finishes executing, `grid` is updated with the minimum distances from black squares to each empty square. `maxx` contains the maximum distance value stored in `grid`. `H`, `W`, `dist`, `i`, `j`, `r`, `c` maintain their initial conditions. `q` is empty as all empty squares have been processed.
    return maxx
    #The program returns the maximum distance value stored in 'grid' after updating it with the minimum distances from black squares to each empty square
#Overall this is what the function does:The function func_1 accepts a 2D list of characters representing a grid with at least one black square. It replaces black squares with 0 and calculates the minimum distance from each black square to every empty square in the grid. The function then returns the maximum distance value stored in the grid.

