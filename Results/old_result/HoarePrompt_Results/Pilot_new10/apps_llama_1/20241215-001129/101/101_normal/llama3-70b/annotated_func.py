#State of the program right berfore the function call: the input consists of a pair of integers n and m (1 ≤ n, m ≤ 2000) representing the resolution of the monitor, followed by n lines of m characters each, where "." represents a black pixel and "w" represents a white pixel, and at least one pixel of the monitor is white.
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
        
    #State of the program after the  for loop has been executed: `n` and `m` are integers with `1 ≤ n, m ≤ 2000`, `pixels` is a 2D list of size `n x m` where each element is either "." or "w", `white_pixels` is a list of coordinates of 'w' valued pixels in `pixels`, `min_x` is the smallest x-coordinate in `white_pixels` if it is not empty, otherwise `float('inf')`, `min_y` is the smallest y-coordinate in `white_pixels` if it is not empty, otherwise `float('inf')`, `max_x` is the largest x-coordinate in `white_pixels` if it is not empty, otherwise `float('-inf')`, `max_y` is the largest y-coordinate in `white_pixels` if it is not empty, otherwise `float('-inf')`.
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
            
        #State of the program after the  for loop has been executed: `n` and `m` are integers with `1 ≤ n, m ≤ 2000`, `pixels` is a 2D list of size `n x m` where if a cell is on the border defined by the original `min_x`, `max_x`, `min_y`, and `max_y` and its original value is `'.'`, then its value is `'+'`, otherwise if its original value is `'w'`, it remains `'w'`, and all other cells are `'.'`, `white_pixels` is a list of coordinates of 'w' valued pixels in `pixels`, `min_x` and `max_x` are the smallest and largest x-coordinates in `white_pixels`, `min_y` and `max_y` are the smallest and largest y-coordinates in `white_pixels`, `frame_size` equals `max(max_x - min_x, max_y - min_y) + 1` and is less than or equal to the maximum of `n` and `m`.
        for row in pixels:
            print(''.join(row))
            
        #State of the program after the  for loop has been executed: `n` and `m` are integers with `1 ≤ n, m ≤ 2000`, `pixels` is a 2D list of size `n x m`, `white_pixels` is a list of coordinates of 'w' valued pixels in the original `pixels`, `min_x` and `max_x` are the smallest and largest x-coordinates in `white_pixels`, `min_y` and `max_y` are the smallest and largest y-coordinates in `white_pixels`, `frame_size` equals `max(max_x - min_x, max_y - min_y) + 1` and is less than or equal to the maximum of `n` and `m`, and the string representation of each row in `pixels` has been printed to the console.
    #State of the program after the if-else block has been executed: `n` and `m` are integers with `1 ≤ n, m ≤ 2000`, `pixels` is a 2D list of size `n x m` where each element is either "." or "w", `white_pixels` is a list of coordinates of 'w' valued pixels in `pixels`, `min_x` is the smallest x-coordinate in `white_pixels` if it is not empty, otherwise `float('inf')`, `min_y` is the smallest y-coordinate in `white_pixels` if it is not empty, otherwise `float('inf')`, `max_x` is the largest x-coordinate in `white_pixels` if it is not empty, otherwise `float('-inf')`, `max_y` is the largest y-coordinate in `white_pixels` if it is not empty, otherwise `float('-inf')`, `frame_size` is equal to `max(max_x - min_x, max_y - min_y) + 1`. If `frame_size` is greater than the maximum of `n` and `m`, then the value `-1` has been printed. Otherwise, the string representation of each row in `pixels` has been printed to the console.
#Overall this is what the function does:The function reads monitor resolution and pixel data, identifies the bounding box of white pixels, and if the box size is within the monitor's dimensions, it prints the modified pixel data with a frame around the white pixels; otherwise, it prints -1.

