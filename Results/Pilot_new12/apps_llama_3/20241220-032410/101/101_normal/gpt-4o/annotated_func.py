#State of the program right berfore the function call: n and m are positive integers, and screen is a 2D list of strings of length m, where each string consists of characters "." and "w", representing the state of the monitor pixels, with at least one "w" present in the screen.
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
        
    #State of the program after the  for loop has been executed: `n` and `m` are positive integers, `screen` is a 2D list of strings of length `m`, `top` is the minimum row index where 'w' is found or `None`, `bottom` is the maximum row index where 'w' is found or `None`, `left` is the minimum column index where 'w' is found or `None`, `right` is the maximum column index where 'w' is found or `None`.
    if (top is None or bottom is None or left is None or right is None) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `n` and `m` are positive integers, `screen` is a 2D list of strings of length `m`, `top` is the minimum row index where 'w' is found, `bottom` is the maximum row index where 'w' is found, `left` is the minimum column index where 'w' is found, and `right` is the maximum column index where 'w' is found, and all of `top`, `bottom`, `left`, and `right` are not `None`.
    frame_height = bottom - top + 1
    frame_width = right - left + 1
    if (frame_height < 2 or frame_width < 2) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `n` and `m` are positive integers, `screen` is a 2D list of strings of length `m`, `top` is the minimum row index where 'w' is found, `bottom` is the maximum row index where 'w' is found, `left` is the minimum column index where 'w' is found, `right` is the maximum column index where 'w' is found, `frame_height` equals `bottom - top + 1`, `frame_width` equals `right - left + 1`, and all of `top`, `bottom`, `left`, and `right` are not `None`. The `frame_height` is greater than or equal to 2 and the `frame_width` is greater than or equal to 2.
    result = [list(row) for row in screen]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if i == top or i == bottom or j == left or j == right:
                if result[i][j] == '.':
                    result[i][j] = '+'
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `m` is a positive integer, `screen` is a 2D list of strings of length `m`, `top` is set, `bottom` is set and greater than or equal to `top + 1`, `left` is set, `right` is set and greater than or equal to `left + 1`, `frame_height` equals `bottom - top + 1` and is greater than or equal to 2, `frame_width` equals `right - left + 1` and is greater than or equal to 2, and `result` is a 2D list where all border elements that were initially dots are replaced with pluses, and the rest of the elements are the same as `screen`.
    return result
    #The program returns a 2D list `result` where all border elements that were initially dots are replaced with pluses, and the rest of the elements are the same as the initial `screen`, with a frame of height `bottom - top + 1` and width `right - left + 1`, where `bottom` is greater than or equal to `top + 1` and `right` is greater than or equal to `left + 1`.
#Overall this is what the function does:The function accepts two positive integers `n` and `m`, and a 2D list `screen` of strings of length `m`, where each string consists of characters "." and "w". It returns either -1 or a modified 2D list. The function finds the minimum and maximum row and column indices where 'w' is found in the `screen`. If any of these indices are not found or if the frame height or width (defined by the difference between the maximum and minimum indices plus one) is less than 2, the function returns -1. Otherwise, it creates a copy of the `screen` and replaces the border elements (i.e., the top, bottom, left, and right edges of the frame) that are initially dots with pluses, leaving the rest of the elements unchanged. The function then returns this modified 2D list. The function handles edge cases where the input `screen` does not contain any 'w' characters or where the frame height or width is less than 2, in which case it returns -1.

