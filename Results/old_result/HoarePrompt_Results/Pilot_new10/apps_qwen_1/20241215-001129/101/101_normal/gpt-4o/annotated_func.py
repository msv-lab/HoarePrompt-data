#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2000, and screen is a list of n strings, where each string contains exactly m characters. The characters in the strings are either "." (representing black pixels) or "w" (representing white pixels), and at least one pixel in the monitor is white.
def func_1(n, m, screen):
    top = bottom = left = right = None
    for i in range(n):
        for j in range(m):
            if screen[i][j] == 'w':
                if top is None:
                    top = bottom = i
                    left = right = j
                else:
                    if i < top:
                        top = i
                    if i > bottom:
                        bottom = i
                    if j < left:
                        left = j
                    if j > right:
                        right = j
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that \(1 \leq n \leq 2000\), `m` is a positive integer such that \(1 \leq m \leq 2000\), `screen` is a list of `n` strings where each string contains exactly `m` characters, and the characters are either "." or "w". `top` is the smallest row index where 'w' is found, `bottom` is the largest row index where 'w' is found, `left` is the smallest column index where 'w' is found, `right` is the largest column index where 'w' is found.
    if (top is None or bottom is None or left is None or right is None) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `n` is a positive integer such that \(1 \leq n \leq 2000\), `m` is a positive integer such that \(1 \leq m \leq 2000\), `screen` is a list of `n` strings where each string contains exactly `m` characters, and the characters are either "." or "w", `top` is the smallest row index where 'w' is found, `bottom` is the largest row index where 'w' is found, `left` is the smallest column index where 'w' is found, `right` is the largest column index where 'w', and none of `top`, `bottom`, `left`, or `right` is None
    frame_height = bottom - top + 1
    frame_width = right - left + 1
    if (frame_height < 2 or frame_width < 2) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `n` is a positive integer such that \(1 \leq n \leq 2000\), `m` is a positive integer such that \(1 \leq m \leq 2000\), `screen` is a list of `n` strings where each string contains exactly `m` characters, and the characters are either "." or "w", `top` is the smallest row index where 'w' is found, `bottom` is the largest row index where 'w' is found, `left` is the smallest column index where 'w' is found, `right` is the largest column index where 'w', `frame_height` is `bottom - top + 1`, `frame_width` is `right - left + 1`, and `frame_height` is greater than or equal to 2, `frame_width` is greater than or equal to 2
    result = [list(row) for row in screen]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if i == top or i == bottom or j == left or j == right:
                if result[i][j] == '.':
                    result[i][j] = '+'
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that \(1 \leq n \leq 2000\), `m` is a positive integer such that \(1 \leq m \leq 2000\), `screen` remains unchanged except for the boundary elements which are now `'+'`, `top` is the smallest row index where `'w'` is found, `bottom` is the largest row index where `'w'` is found, `left` is the smallest column index where `'w'` is found, `right` is the largest column index where `'w'`, `frame_height` is `bottom - top + 1` and is greater than or equal to 2, `frame_width` is `right - left + 1` and is greater than or equal to 2, `result` is a list of lists where each inner list is a copy of the corresponding row in the `screen` list with the boundary elements set to `'+'` if they were originally `'.'`.
    return result
    #The program returns a list of lists 'result' where each inner list is a copy of the corresponding row in the 'screen' list with the boundary elements set to '+' if they were originally '.'
#Overall this is what the function does:The function `func_1` accepts three parameters: `n`, `m`, and `screen`. `n` and `m` are positive integers such that \(1 \leq n, m \leq 2000\), and `screen` is a list of `n` strings, where each string contains exactly `m` characters. The characters in the strings are either "." (representing black pixels) or "w" (representing white pixels). The function finds the smallest and largest row and column indices where "w" is found and sets the boundary elements (top, bottom, left, and right sides) of the white region to "+" if they were originally ".". If no white pixels are found or if the resulting frame dimensions are less than 2x2, the function returns -1. Otherwise, it returns the modified `screen` list with the boundary elements set to "+" if they were originally ".".

