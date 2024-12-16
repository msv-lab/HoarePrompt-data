#State of the program right berfore the function call: The input consists of two space-separated integers n and m representing the dimensions of the monitor, followed by n lines each containing m characters. The characters are either '.' (black pixel) or 'w' (white pixel), with at least one 'w' present in the input.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of rows, `m` is an integer representing the number of columns, `pixels` is a list of `n` lists, where each inner list contains a string of characters, `white_pixels` is a list of tuples (i, j) where `pixels[i][j]` is 'w', `min_x` is the smallest `x` coordinate of all white pixels, `min_y` is the smallest `y` coordinate of all white pixels, `max_x` is the largest `x` coordinate of all white pixels, `max_y` is the largest `y` coordinate of all white pixels.
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
            
        #State of the program after the  for loop has been executed: `n` is a positive integer, `m` is a positive integer, `pixels` is an `n x m` 2D list, `min_x` is the smallest `x` coordinate of all white pixels, `min_y` is the smallest `y` coordinate of all white pixels, `max_x` is the largest `x` coordinate of all white pixels, `max_y` is the largest `y` coordinate of all white pixels, `frame_size` is \(\max(\max(\text{max\_x}) - \min(\text{min\_x}), \max(\text{max\_y}) - \min(\text{min\_y})) + 1\), and `frame_size` is less than or equal to the maximum of `n` and `m`.
        #
        #For every `i` in the range `[0, n-1]` and every `j` in the range `[0, m-1]`:
        #- If `j` is such that `(i == min_x or i == max_x or j == min_y or j == max_y)` and `pixels[i][j] == '.'`, then `pixels[i][j]` is changed to `'+'.`
        #- If `pixels[i][j]` is `'w'`, it remains `'w'`.
        #- Otherwise, `pixels[i][j]` is changed to `'.'`.
        #
        #After the loop executes, all boundary pixels (where `i` is `min_x` or `max_x` or `j` is `min_y` or `max_y`) are set to `'+'`, and all other pixels are either `'.'` or `'w'`.
        for row in pixels:
            print(''.join(row))
            
        #State of the program after the  for loop has been executed: `n` is a positive integer; `m` is a positive integer; `pixels` is an `n x m` 2D list with at least one row; `min_x` is the smallest `x` coordinate of all white pixels; `min_y` is the smallest `y` coordinate of all white pixels; `max_x` is the largest `x` coordinate of all white pixels; `max_y` is the largest `y` coordinate of all white pixels; `frame_size` is \(\max(\max(\text{max\_x}) - \min(\text{min\_x}), \max(\text{max\_y}) - \min(\text{min\_y})) + 1\) and is less than or equal to the maximum of `n` and `m`; after executing the loop, all boundary pixels (where `i` is `min_x` or `max_x` or `j` is `min_y` or `max_y`) are set to `'+'`, and all other pixels are either `'.'` or `'w'`.
    #State of the program after the if-else block has been executed: `n` is an integer representing the number of rows, `m` is an integer representing the number of columns, `pixels` is a list of `n` lists, where each inner list contains a string of characters, `white_pixels` is a list of tuples (i, j) where `pixels[i][j]` is 'w', `min_x` is the smallest `x` coordinate of all white pixels, `min_y` is the smallest `y` coordinate of all white pixels, `max_x` is the largest `x` coordinate of all white pixels, `max_y` is the largest `y` coordinate of all white pixels, `frame_size` is \(\max(\max(\text{max\_x}) - \min(\text{min\_x}), \max(\text{max\_y}) - \min(\text{min\_y})) + 1\). If `frame_size` is greater than the maximum of `n` and `m`, the function prints `-1`. Otherwise, after executing the loop, all boundary pixels (where `i` is `min_x` or `max_x` or `j` is `min_y` or `max_y`) are set to `'+'`, and all other pixels are either `'.'` or `'w'`.
#Overall this is what the function does:The function reads the dimensions of a monitor and its pixel representation from standard input, identifies the bounding box of white pixels, and then modifies the pixel representation to set the boundary pixels to '+' and internal pixels to '.', unless the required frame size exceeds the dimensions of the monitor in which case it prints -1.

