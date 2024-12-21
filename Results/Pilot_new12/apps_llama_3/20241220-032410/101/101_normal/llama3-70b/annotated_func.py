#State of the program right berfore the function call: The input to the function is a list of strings, where the first string contains two positive integers n and m (1 ≤ n, m ≤ 2000) separated by a space, representing the resolution of the monitor. The next n strings contain exactly m characters each, where each character is either '.' (period, ASCII code 46) representing a black pixel or 'w' (lowercase English letter w) representing a white pixel.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 2000), `m` is a positive integer (1 ≤ m ≤ 2000), `pixels` is a 2D list containing `n` sublists where each sublist is a list of `m` characters ('.' or 'w'), `white_pixels` is a list of coordinates (i, j) where `pixels[i][j]` is 'w', if `white_pixels` is not empty then `min_x` is the minimum x-coordinate of all 'w' pixels, `min_y` is the minimum y-coordinate of all 'w' pixels, `max_x` is the maximum x-coordinate of all 'w' pixels, `max_y` is the maximum y-coordinate of all 'w' pixels; otherwise, `min_x` is positive infinity, `min_y` is positive infinity, `max_x` is negative infinity, `max_y` is negative infinity.
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
            
        #State of the program after the  for loop has been executed: `n` is a positive integer, `m` is a positive integer, `pixels` is a 2D list where pixels on the border of the frame and originally `'.'` are `'+'` and other non-'w' pixels are `'.'`, `white_pixels` is a list of 'w' pixel coordinates, `min_x`, `min_y`, `max_x`, `max_y` are defined based on `white_pixels`, `frame_size` is less than or equal to the maximum of `n` and `m`.
        for row in pixels:
            print(''.join(row))
            
        #State of the program after the  for loop has been executed: `n` is a positive integer, `m` is a positive integer, `pixels` is a 2D list where pixels on the border of the frame and originally `'.'` are `'+'` and other non-'w' pixels are `'.'`, the string representation of each row in `pixels` has been printed, `white_pixels` is a list of 'w' pixel coordinates, `min_x`, `min_y`, `max_x`, `max_y` are defined based on `white_pixels`, `frame_size` is less than or equal to the maximum of `n` and `m`.
    #State of the program after the if-else block has been executed: `n` is a positive integer (1 ≤ n ≤ 2000), `m` is a positive integer (1 ≤ m ≤ 2000), `pixels` is a 2D list containing `n` sublists where each sublist is a list of `m` characters ('.', 'w', or '+'), `white_pixels` is a list of coordinates (i, j) where `pixels[i][j]` is 'w', if `white_pixels` is not empty then `min_x` is the minimum x-coordinate of all 'w' pixels, `min_y` is the minimum y-coordinate of all 'w' pixels, `max_x` is the maximum x-coordinate of all 'w' pixels, `max_y` is the maximum y-coordinate of all 'w' pixels; otherwise, `min_x` is positive infinity, `min_y` is positive infinity, `max_x` is negative infinity, `max_y` is negative infinity. If `frame_size` is greater than the maximum of `n` and `m`, the value -1 has been printed and returned. Otherwise, the string representation of each row in `pixels` (where pixels on the border of the frame and originally '.' are '+' and other non-'w' pixels are '.') has been printed.
#Overall this is what the function does:The function takes input from the user representing a monitor resolution and pixel data, processes the pixel data to find the minimum and maximum x and y coordinates of the white pixels, and then prints the modified pixel data with a border around the white pixels if the frame size is within the monitor resolution, or prints -1 if the frame size exceeds the monitor resolution. The function does not explicitly return any value but affects the state of the program by printing the modified pixel data or an error message. The input to the function is assumed to be a list of strings where the first string contains two positive integers separated by a space, and the subsequent strings contain pixel data. The function handles edge cases where the frame size is larger than the monitor resolution and where there are no white pixels, resulting in the printing of -1 or an empty frame, respectively. The function also modifies the original pixel data by replacing black pixels on the border of the frame with '+' and leaving other black pixels unchanged.

