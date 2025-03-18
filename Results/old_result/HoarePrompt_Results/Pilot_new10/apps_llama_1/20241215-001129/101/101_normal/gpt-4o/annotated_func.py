#State of the program right berfore the function call: n and m are positive integers, and screen is a list of strings of length m, where each string consists of only "." and "w" characters.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `m` is a positive integer, `screen` is a list of strings of length `m`, `i` is `n-1`, `j` is `m-1`, and `top`, `bottom`, `left`, and `right` are either the minimum and maximum row and column indices of all 'w' characters in `screen` or `None` if no 'w' characters are found.
    if (top is None or bottom is None or left is None or right is None) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `n` is a positive integer, `m` is a positive integer, `screen` is a list of strings of length `m`, `i` is `n-1`, `j` is `m-1`, and `top`, `bottom`, `left`, and `right` are the minimum and maximum row and column indices of all 'w' characters in `screen`, and none of `top`, `bottom`, `left`, or `right` are `None`.
    frame_height = bottom - top + 1
    frame_width = right - left + 1
    if (frame_height < 2 or frame_width < 2) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `n` is a positive integer, `m` is a positive integer, `screen` is a list of strings of length `m`, `i` is `n-1`, `j` is `m-1`, `top`, `bottom`, `left`, and `right` are the minimum and maximum row and column indices of all 'w' characters in `screen`, `frame_height` is `bottom - top + 1`, `frame_width` is `right - left + 1`, and both `frame_height` and `frame_width` are greater than or equal to 2
    result = [list(row) for row in screen]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if i == top or i == bottom or j == left or j == right:
                if result[i][j] == '.':
                    result[i][j] = '+'
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `m` is a positive integer, `screen` is a list of strings of length `m`, `top`, `bottom`, `left`, and `right` are the minimum and maximum row and column indices of all 'w' characters in `screen`, `frame_height` is `bottom - top + 1`, `frame_width` is `right - left + 1`, `i` is `bottom`, `j` is `right`, and `result` is a 2D list of characters where each inner list is a modified copy of the corresponding row in `screen` with all '.' characters at the border positions (at `top`, `bottom`, `left`, or `right`) replaced with '+'.
    return result
    #The program returns a 2D list of characters `result` where each inner list is a modified copy of the corresponding row in `screen` with all '.' characters at the border positions (at `top`, `bottom`, `left`, or `right`) replaced with '+'. The `result` has a height of `frame_height` which is `bottom - top + 1` and a width of `frame_width` which is `right - left + 1`.
#Overall this is what the function does:The function accepts two positive integers `n` and `m`, and a list of strings `screen`, where each string consists of only "." and "w" characters. It finds the bounding box of all 'w' characters in `screen`. If no 'w' characters are found, or if the height or width of this bounding box is less than 2, it returns -1. Otherwise, it creates a copy of `screen`, replaces all "." characters at the border positions of the bounding box with "+", and returns this modified copy.

