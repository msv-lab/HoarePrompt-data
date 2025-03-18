#State of the program right berfore the function call: The input consists of two integers n and m (1 ≤ n, m ≤ 2000) representing the resolution of the monitor, followed by n lines of m characters each, where each character is either '.' (representing a black pixel) or 'w' (representing a white pixel). It is guaranteed that at least one pixel is a white pixel.
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
        
    #State of the program after the  for loop has been executed: `n` is assigned, `m` is assigned, `pixels` is a list of `n` strings with `m` characters, `white_pixels` contains all tuples `(x, y)` for each position where `pixels[i][j]` is 'w', `min_x` is the minimum x-coordinate of all white pixels, `min_y` is the minimum y-coordinate of all white pixels, `max_x` is the maximum x-coordinate of all white pixels, `max_y` is the maximum y-coordinate of all white pixels.
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
            
        #State of the program after the  for loop has been executed: `pixels` contains symbols where:
        #- Each pixel boundary defined by `min_x`, `max_x`, `min_y`, and `max_y` has been updated to '+' if they were originally '.'.
        #- Pixels corresponding to 'w' remain unchanged.
        #- All other pixels have been converted to '.'.
        #- If `n` is 0, `pixels` is an empty list.
        #- If `m` is 0, `pixels` would consist of empty strings for each row, reflecting dimensions, while no changes occur to content since there are no iterations possible.
        for row in pixels:
            print(''.join(row))
            
        #State of the program after the  for loop has been executed: `pixels` is a list of `n` non-empty rows, where each row is a string formed by concatenating its elements, `n` is greater than 0, and `m` is greater than 0. If `n` is 0, `pixels` is an empty list. If `m` is 0, `pixels` consists of empty strings for each row, reflecting dimensions.
    #State of the program after the if-else block has been executed: *`n` and `m` are assigned values, `pixels` is a list of `n` strings with `m` characters, and `white_pixels` contains all tuples `(x, y)` for each position where `pixels[i][j]` is 'w'. If the `frame_size` is greater than the maximum of `n` and `m`, the function returns -1. Otherwise, `pixels` remains a list of `n` non-empty rows, where each row is a string formed by concatenating its elements, with `n` greater than 0 and `m` greater than 0, reflecting the dimensional properties, or may be an empty list if `n` is 0, or consist of empty strings for each row if `m` is 0.
#Overall this is what the function does:The function accepts two integers `n` and `m`, representing the dimensions of a monitor grid, and a grid of pixels where each pixel is either a black ('.') or white ('w') pixel. It identifies the bounding box of the white pixels in the grid. If the size of this bounding box exceeds the dimensions of the grid (either `n` or `m`), the function prints -1. Otherwise, it modifies the border of the bounding box of white pixels by replacing black pixels on the border with '+' and prints the modified grid. If there are no changes to be made due to the size constraint, it simply prints the original grid. The function does not handle the case where the dimensions `n` or `m` are 0, as this would lead to invalid input based on the provided constraints (1 ≤ n, m ≤ 2000).

