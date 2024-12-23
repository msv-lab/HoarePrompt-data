#State of the program right berfore the function call: The input consists of a line containing two integers n and m (1 ≤ n, m ≤ 2000), followed by n lines of exactly m characters each. Each character is either a period (ASCII code 46) representing a black pixel or the lowercase letter 'w' representing a white pixel. At least one 'w' is guaranteed to be present in the input.
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
        
    #State of the program after the  for loop has been executed: `white_pixels` is not an empty list, `min_x` is the smallest `x` coordinate of all `'w'` pixels, `min_y` is the smallest `y` coordinate of all `'w'` pixels, `max_x` is the largest `x` coordinate of all `'w'` pixels, `max_y` is the largest `y` coordinate of all `'w'` pixels.
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
            
        #State of the program after the  for loop has been executed: `i` is `n`, `n` is the same as before, `m` is the same as before, `pixels[i][j]` for all `i` and `j` is either `'+', 'w',` or `'. '` where: 
        #- If `i == min_x` or `i == max_x` or `j == min_y` or `j == max_y` and `pixels[i][j] == '.'`, then `pixels[i][j]` is set to `'+'`.
        #- If `pixels[i][j] == 'w'`, then `pixels[i][j]` remains `'w'`.
        #- Otherwise, `pixels[i][j]` remains `'.'`.
        for row in pixels:
            print(''.join(row))
            
        #State of the program after the  for loop has been executed: `pixels` is a non-empty list with at least `n` rows, `i` is `n`, `m` is the same as before, and every row of `pixels` is printed exactly once.
    #State of the program after the if-else block has been executed: *`white_pixels` is not an empty list, `min_x` is the smallest `x` coordinate of all `'w'` pixels, `min_y` is the smallest `y` coordinate of all `'w'` pixels, `max_x` is the largest `x` coordinate of all `'w'` pixels, `max_y` is the largest `y` coordinate of all `'w'` pixels, `frame_size` is `max(max_x - min_x, max_y - min_y) + 1`. If `frame_size` is greater than the maximum of `n` and `m`, then `frame_size` remains unchanged. Otherwise, `pixels` is a non-empty list with at least `n` rows, `i` is `n`, and every row of `pixels` is printed exactly once.
#Overall this is what the function does:The function reads a grid of pixels from standard input, where each line contains exactly `m` characters representing either a period (black pixel) or the letter 'w' (white pixel). It calculates the bounding box of the white pixels and checks if the bounding box can fit within the original grid dimensions. If the bounding box exceeds the grid dimensions, it prints `-1`. Otherwise, it pads the grid with '+' characters along the edges defined by the bounding box and prints the modified grid. The function handles cases where the grid might be too small to contain the bounding box by printing `-1`.

