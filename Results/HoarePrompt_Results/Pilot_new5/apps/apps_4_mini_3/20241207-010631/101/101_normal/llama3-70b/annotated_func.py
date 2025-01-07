#State of the program right berfore the function call: The function doesn't take any input arguments. The monitor resolution is represented as a pair of integers n and m (1 ≤ n, m ≤ 2000), followed by n lines of m characters each, where each character is either a '.' (representing a black pixel) or 'w' (representing a white pixel). It is guaranteed that at least one pixel of the monitor is white.
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
        
    #State of the program after the  for loop has been executed: `min_x` is the minimum x-coordinate among all elements in `white_pixels`, `min_y` is the minimum y-coordinate among all elements in `white_pixels`, `max_x` is the maximum x-coordinate among all elements in `white_pixels`, `max_y` is the maximum y-coordinate among all elements in `white_pixels`, `white_pixels` must contain at least 0 elements. If `white_pixels` is empty, `min_x` and `min_y` remain as float('inf'), while `max_x` and `max_y` remain as float('-inf').
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
            
        #State of the program after the  for loop has been executed: `min_x`, `min_y`, `max_x`, `max_y` are the minimum and maximum coordinates among all elements in `white_pixels`; `frame_size` is `max(max_x - min_x, max_y - min_y) + 1`, which is less than or equal to `max(n, m)`; `pixels` is updated such that all positions on the edges defined by `min_x`, `max_x`, `min_y`, `max_y` are marked with '+' if they were originally '.', while the positions with 'w' remain unchanged, and all other positions are set to '.'; `i` is equal to `n - 1` after the last iteration, and `j` ranges from `0` to `m - 1` during the final processing of the last row.
        for row in pixels:
            print(''.join(row))
            
        #State of the program after the  for loop has been executed: `min_x`, `min_y`, `max_x`, `max_y` are valid coordinates from `white_pixels`, `frame_size` is less than or equal to `max(n, m)`, `pixels` has been entirely printed row by row as strings, `i` is equal to `n`, and `j` is not applicable as the loop has completed all iterations.
    #State of the program after the if-else block has been executed: *`min_x`, `min_y`, `max_x`, `max_y` are the minimum and maximum x and y coordinates among all elements in `white_pixels`, respectively, and `frame_size` is defined as `max(max_x - min_x, max_y - min_y) + 1`. If `frame_size` is greater than `max(n, m)`, the output is -1. Otherwise, `frame_size` is less than or equal to `max(n, m)`, and the pixels have been entirely printed row by row as strings, with `i` equal to `n` and `j` not applicable as the loop has completed all iterations.
#Overall this is what the function does:The function accepts no parameters and processes a grid of pixels (black and white) with dimensions specified by the user input. It identifies the coordinates of all white pixels and calculates a frame size that encompasses all white pixels. If the frame size exceeds the monitor's dimensions, it outputs -1. Otherwise, it modifies the grid to replace the edges of the frame with '+' signs (if they were black) and prints the modified grid. The function guarantees at least one white pixel is present, so there will always be valid coordinates for the frame calculations.

