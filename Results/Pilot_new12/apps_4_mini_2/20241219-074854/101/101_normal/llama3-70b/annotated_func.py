#State of the program right berfore the function call: The input consists of integers n and m (1 ≤ n, m ≤ 2000), followed by n lines each containing exactly m characters where each character is either '.' (representing a black pixel) or 'w' (representing a white pixel). It is guaranteed that at least one character is 'w'.
def func():
    n, m = map(int, input().split())
    pixels = [list(input()) for _ in range(n)]
    white_pixels = [(i, j) for i in range(n) for j in range(m) if pixels[i][j] ==
    'w']
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float(
    '-inf')
    for (x, y) in white_pixels:
        min_x, min_y = min(min_x, x), min(min_y, y)
        
        max_x, max_y = max(max_x, x), max(max_y, y)
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 2000), `m` is an integer (1 ≤ m ≤ 2000), `pixels` is a list of `n` lists containing input values, `white_pixels` is a list of coordinates representing white pixels; if `white_pixels` is not empty, `min_x` is the minimum x coordinate in `white_pixels`, `min_y` is the minimum y coordinate in `white_pixels`, `max_x` is the maximum x coordinate in `white_pixels`, `max_y` is the maximum y coordinate in `white_pixels`; if `white_pixels` is empty, `min_x` is float('inf'), `min_y` is float('inf'), `max_x` is float('-inf'), `max_y` is float('-inf').
    frame_size = max(max_x - min_x, max_y - min_y) + 1
    if (frame_size > max(n, m)) :
        print(-1)
    else :
        for i in range(n):
            for j in range(m):
                if (i == min_x or i == max_x or j == min_y or j == max_y) and pixels[i][j
                    ] == '.':
                    pixels[i][j] = '+'
                elif pixels[i][j] == 'w':
                    continue
                else:
                    pixels[i][j] = '.'
            
        #State of the program after the  for loop has been executed: `pixels` is updated such that the first and last rows (indexed by `min_x` and `max_x`) and the first and last columns (indexed by `min_y` and `max_y`) contain '+' where conditions were satisfied; `pixels` remains unchanged where it contained 'w' and is set to '.' elsewhere, except for pixels that were blacked out due to conditions; `n` is the original number of rows, `m` is the original number of columns, and if `white_pixels` is not empty, then `frame_size` is within bounds as specified. If `white_pixels` is empty, then `frame_size` remains not computable.
        for row in pixels:
            print(''.join(row))
            
        #State of the program after the  for loop has been executed: `pixels` is a 2D array where each row has been printed; `n` is the original number of rows in `pixels`; `m` is the original number of columns in `pixels`; if `white_pixels` is not empty, then `frame_size` is within bounds; if `pixels` is empty, `n` must be 0 and no output will be printed.
    #State of the program after the if-else block has been executed: *`n` and `m` are integers (1 ≤ n ≤ 2000), `pixels` is a list of `n` lists containing input values, and `white_pixels` is a list of coordinates representing white pixels. If `frame_size` is computed as max(max_x - min_x, max_y - min_y) + 1 and is greater than the maximum of `n` and `m`, the program will proceed accordingly. If `frame_size` is within bounds or if `pixels` is a 2D array that has been printed, the original dimensions of `n` and `m` remain unchanged; if `pixels` is empty, then `n` must be 0 and no output will be printed.
#Overall this is what the function does:The function processes a grid of dimensions n by m, consisting of characters representing pixels (either black represented by '.' or white represented by 'w'). It identifies the coordinates of all white pixels, calculates the minimum and maximum bounds (minimum and maximum x and y coordinates) for these white pixels, and determines a 'frame size' based on these bounds. If the frame size exceeds either dimension of the grid, it prints -1. If the frame size is within bounds, the function updates the grid by marking the edges (first and last rows/columns defined by the minimum and maximum x and y coordinates) with '+' where the conditions for black pixels are met, while retaining existing white pixels. Finally, it prints the modified grid. The function does not return a value, and it assumes that the input grid contains at least one white pixel. Notably, there is a missing check for the scenario when there are no white pixels, which could affect the logic for calculating bounds and printing results; in such a case, the program would not handle the situation appropriately since it relies on the presence of 'w' pixels for proper functionality.

