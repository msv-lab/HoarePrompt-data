#State of the program right berfore the function call: The input consists of two integers n and m representing the dimensions of the monitor, followed by n lines of strings, where each string contains exactly m characters. Characters "." represent black pixels, and "w" represent white pixels. It is guaranteed that at least one pixel is white, and 1 ≤ n, m ≤ 2000.
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
        
    #State of the program after the  for loop has been executed: `n` is the first integer input, `pixels` is a list of `n` lists, each containing `m` characters ('.' or 'w'), `white_pixels` is a list of tuples representing the coordinates `(i, j)` of all 'w' characters in the `pixels` grid and must contain at least one tuple, `min_x` is the smallest `x` value from all tuples in `white_pixels`, `min_y` is the smallest `y` value from all tuples in `white_pixels`, `max_x` is the largest `x` value from all tuples in `white_pixels`, `max_y` is the largest `y` value from all tuples in `white_pixels`.
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
            
        #State of the program after the  for loop has been executed: `n` is greater than 0, `white_pixels` contains at least one tuple, `m` is the length of each list in `pixels`, for all `(i, j)` in `pixels`, `pixels[i][j]` is `'+'` if `(i == min_x or i == max_x or j == min_y or (j == max_y))`, and `'.'` otherwise. If `pixels[i][j]` was `'w'`, it remains `'w'`. If `pixels[i][j]` was `'.'`, it becomes `'w'` if `(i == min_x or i == max_x or j == min_y or (j == max_y))` and `'.'` otherwise.
        for row in pixels:
            print(''.join(row))
            
        #State of the program after the  for loop has been executed: `pixels` is a list of lists, where each inner list represents a row of the pixel matrix, and each element in the inner list is either `'w'` or `'.'`. For each `(i, j)` in `pixels`, if `i == min_x` or `i == max_x` or `j == min_y` or `j == max_y`, then `pixels[i][j]` is `'w'`; otherwise, `pixels[i][j]` is `'.'`. The loop will execute at least as many times as the number of rows in `pixels`.
    #State of the program after the if-else block has been executed: *`n` is the first integer input, `pixels` is a list of `n` lists, each containing `m` characters ('.' or 'w'). `white_pixels` is a list of tuples representing the coordinates `(i, j)` of all 'w' characters in the `pixels` grid and must contain at least one tuple. `min_x` is the smallest `x` value from all tuples in `white_pixels`, `min_y` is the smallest `y` value from all tuples in `white_pixels`, `max_x` is the largest `x` value from all tuples in `white_pixels`, `max_y` is the largest `y` value from all tuples in `white_pixels`, `frame_size` is `max(max_x - min_x, max_y - min_y) + 1`. If `frame_size` is greater than the maximum of `n` and `m`, then `-1` is printed to the console. Otherwise, for each `(i, j)` in `pixels`, if `i == min_x` or `i == max_x` or `j == min_y` or `j == max_y`, then `pixels[i][j]` is `'w'`; otherwise, `pixels[i][j]` is `'.'`.
#Overall this is what the function does:The function processes a grid of pixels represented as a list of strings, where each string contains exactly `m` characters ('.' for black pixels and 'w' for white pixels). It calculates the bounding box of the white pixels and checks if the size of this bounding box can fit within the original dimensions of the grid. If the bounding box cannot fit, it prints `-1`. Otherwise, it modifies the grid by converting the border of the bounding box into '+' characters while keeping the white pixels as 'w' and all other pixels as '.'. Finally, it prints the modified grid row by row.

