#State of the program right berfore the function call: grid is a list of strings, where each string represents a row of the grid containing characters '#' (black square) and '.' (white square). The grid has at least one black square, and the dimensions of the grid are such that 1 <= len(grid) <= 1000 and 1 <= len(grid[0]) <= 1000.
def func_1(grid):
    H, W = len(grid), len(grid[0])
    q = []
    dist = [0] * H
    for i in range(H):
        dist[i] = []
        
    #State of the program after the  for loop has been executed: `grid` is a list of strings, `H` is a non-negative integer, `W` is the number of columns in `grid[0]` if `H` > 0, `q` is an empty list, `dist` is a list where each element `dist[i]` is an empty list for `i` in range `H`.
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                q.append([i, j])
                grid[i][j] = 0
        
    #State of the program after the  for loop has been executed: `grid` is a list of strings with all '#' characters replaced by 0, `q` contains the coordinates of all replaced '#' characters in the form of lists `[i, j]` for all rows, `H` is greater than or equal to 0, `W` is the number of columns in `grid[0]` if `H` > 0.
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
        
    #State of the program after the loop has been executed: `grid` is a list of strings with all '#' characters replaced by 0 and updated values in cells that were '.'; `q` is empty, `H` is greater than or equal to 0, `W` is the number of columns in `grid[0]`, `maxx` is the maximum value found in all updated cells of `grid`.
    return maxx
    #The program returns the maximum value found in all updated cells of the grid
#Overall this is what the function does:The function accepts a list of strings representing a grid of characters, where '#' represents a black square and '.' represents a white square. It replaces all '#' characters with 0 and updates the '.' characters to reflect the distance from the nearest '#' character, returning the maximum distance found in the updated cells. If there are no '.' characters adjacent to a '#', those cells remain unchanged. The function assumes that at least one '#' character is present in the grid.

