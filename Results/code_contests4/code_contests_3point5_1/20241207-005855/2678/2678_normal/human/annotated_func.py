#State of the program right berfore the function call: grid is a 2D list of characters representing a grid of squares with at least one black square. Each character in the grid is either '#' for a black square or '.' for a white square.**
def func_1(grid):
    H, W = len(grid), len(grid[0])
    q = []
    dist = [0] * H
    for i in range(H):
        dist[i] = []
        
    #State of the program after the  for loop has been executed: grid` is a 2D list of characters representing a grid of squares with at least one black square, `H` is greater than 0, `W`, `q`, and `dist` remain unchanged, and each index of `dist` contains an empty list
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                q.append([i, j])
                grid[i][j] = 0
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, `grid` is a 2D list of characters representing a grid of squares with all black squares replaced with 0. All black square coordinates are stored in `q`. `H` is greater than 0, `W` is greater than 0, `dist` remains unchanged with each index containing an empty list. `j` is equal to `W`, `i` is `H-1`, for the loop to execute again `i` must be less than `H+1`.
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
        
    #State of the program after the loop has been executed: After all iterations of the loop have finished, `grid` will be updated with the values representing the shortest path distances from the starting point. `q` will be empty. `H` and `W` will remain unchanged. `dist` will remain the same. `j` will be equal to `W`, `i` will be equal to `H`. `maxx` will hold the maximum shortest path distance value.
    return maxx
    #The program returns the maximum shortest path distance value stored in variable 'maxx' after all iterations of the loop have finished.
#Overall this is what the function does:The function func_1 accepts a 2D list of characters representing a grid with at least one black square. It replaces all black squares with 0, calculates the shortest path distances from the starting point, and returns the maximum shortest path distance value stored in variable 'maxx' after all iterations of the loop have finished.

