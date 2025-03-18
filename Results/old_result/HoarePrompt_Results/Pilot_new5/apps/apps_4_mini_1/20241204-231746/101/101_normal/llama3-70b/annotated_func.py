#State of the program right berfore the function call: The input consists of two integers n and m (1 ≤ n, m ≤ 2000), followed by n lines each containing exactly m characters, where each character is either '.' (black pixel) or 'w' (white pixel). It is guaranteed that at least one character in the input is 'w'.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 2000, `m` is an integer between 1 and 2000, `pixels` must contain at least one 'w', `white_pixels` must be a list containing the coordinates of all 'w' in `pixels`, `min_x` is the minimum x-coordinate of all 'w', `min_y` is the minimum y-coordinate of all 'w', `max_x` is the maximum x-coordinate of all 'w', `max_y` is the maximum y-coordinate of all 'w'.
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
            
        #State of the program after the  for loop has been executed: `n` is between 1 and 2000, `m` is between 1 and 2000, `pixels` will contain updated values where the border coordinates defined by `min_x`, `max_x`, `min_y`, and `max_y` are set to '+' for all '.' positions on the borders, all 'w' positions remain unchanged, and all other positions are set to '.'; `white_pixels` still contains the coordinates of all 'w' in the original `pixels`, `min_x`, `min_y`, `max_x`, and `max_y` remain unchanged.
        for row in pixels:
            print(''.join(row))
            
        #State of the program after the  for loop has been executed: `n` is between 1 and 2000, `m` is between 1 and 2000, `pixels` contains `n` rows where each row is a string formed by joining the elements of that row in the original `pixels`, and all rows have been printed out.
    #State of the program after the if-else block has been executed: *`n` and `m` are integers between 1 and 2000. If `frame_size` is greater than the maximum of `n` and `m`, then the conditions related to `pixels` and `white_pixels` hold, and `frame_size` is confirmed to be greater than both `n` and `m`. Otherwise, the `pixels` contain `n` rows where each row is a string formed by the elements of that row in the original `pixels`, and all rows have been printed out.
#Overall this is what the function does:The function accepts two integers `n` and `m`, representing the dimensions of a grid, followed by `n` lines of input containing `m` characters each, which can be either '.' (black pixel) or 'w' (white pixel). It identifies the minimum bounding rectangle that contains all 'w' pixels. If the size of this rectangle exceeds either dimension of the grid, it prints `-1`. Otherwise, it updates the border of the rectangle to '+' where there are '.' pixels and then prints the modified grid. The function ensures that at least one 'w' is present in the input, as guaranteed by the problem constraints.

