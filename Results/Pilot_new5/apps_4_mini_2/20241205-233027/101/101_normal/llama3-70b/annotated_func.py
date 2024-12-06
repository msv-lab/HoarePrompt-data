#State of the program right berfore the function call: The input consists of two integers n and m (1 ≤ n, m ≤ 2000), followed by n lines of m characters each, where each character is either '.' (indicating a black pixel) or 'w' (indicating a white pixel). There is at least one 'w' character in the input.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 2000, `m` is an integer between 1 and 2000, `pixels` is a list containing `n` entries of input strings, `white_pixels` contains all tuples of coordinates for each pixel equal to 'w', `min_x` is the minimum x-coordinate among all white pixels, `min_y` is the minimum y-coordinate among all white pixels, `max_x` is the maximum x-coordinate among all white pixels, `max_y` is the maximum y-coordinate among all white pixels.
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
            
        #State of the program after the  for loop has been executed: `n` is an integer between 1 and 2000, `m` is an integer between 1 and 2000, `pixels` contains modified pixel values such that border pixels that were originally '.' are now '+', all 'w' pixels remain unchanged, and any other pixels are set to '.'; `white_pixels` contains all coordinates of 'w' pixels; `min_x`, `min_y`, `max_x`, and `max_y` are the defined borders based on 'w' pixels.
        for row in pixels:
            print(''.join(row))
            
        #State of the program after the  for loop has been executed: `n` is between 1 and 2000, `m` is between 1 and 2000, `pixels` is a two-dimensional array with `n` rows, `row` is each row in `pixels` printed as a string, and the output is the string representation of all rows concatenated and printed to the console.
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 2000, `m` is an integer between 1 and 2000, `pixels` is a list containing `n` entries of input strings, `white_pixels` contains all tuples of coordinates for each pixel equal to 'w', `min_x` is the minimum x-coordinate among all white pixels, `min_y` is the minimum y-coordinate among all white pixels, `max_x` is the maximum x-coordinate among all white pixels, `max_y` is the maximum y-coordinate among all white pixels, and `frame_size` is equal to `max(max_x - min_x, max_y - min_y) + 1`. If `frame_size` is greater than the maximum of `n` and `m`, -1 has been printed. Otherwise, the string representation of all rows in `pixels` is concatenated and printed to the console.
#Overall this is what the function does:The function accepts two integers `n` and `m`, and then reads `n` lines of pixel data consisting of characters '.' and 'w'. It identifies the minimum and maximum coordinates of the 'w' pixels, calculates the frame size, and checks if it exceeds the dimensions of the pixel grid. If the frame size is larger than the maximum of `n` and `m`, it prints -1. Otherwise, it modifies the border pixels that are '.' to '+', keeps the 'w' pixels unchanged, and converts all other pixels to '.'. Finally, it prints the modified pixel grid. The function does not return a value; it only prints the result.

