#State of the program right berfore the function call: n and m are integers such that 1 <= n <= 2000 and 1 <= m <= 2000, and screen is a 2D list of strings where each string has length m and consists of characters '.' and 'w', representing the state of the monitor pixels.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 2000, `m` is an integer such that 1 <= `m` <= 2000, `screen` is a 2D list of strings where each string has length `m` and consists of characters '.' and 'w', `i` is `n-1`, `j` is `m-1`, and `top`, `bottom`, `left`, and `right` represent the bounding box of all 'w' characters in `screen`, or are `None` if no 'w' characters are found.
    if (top is None or bottom is None or left is None or right is None) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `n` is an integer such that 1 <= `n` <= 2000, `m` is an integer such that 1 <= `m` <= 2000, `screen` is a 2D list of strings where each string has length `m` and consists of characters '.' and 'w', `i` is `n-1`, `j` is `m-1`, and `top`, `bottom`, `left`, and `right` are not `None`, representing the bounding box of all 'w' characters in `screen`.
    frame_height = bottom - top + 1
    frame_width = right - left + 1
    if (frame_height < 2 or frame_width < 2) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `n` is an integer such that 1 <= `n` <= 2000, `m` is an integer such that 1 <= `m` <= 2000, `screen` is a 2D list of strings where each string has length `m` and consists of characters '.' and 'w', `i` is `n-1`, `j` is `m-1`, `top`, `bottom`, `left`, and `right` are not `None`, representing the bounding box of all 'w' characters in `screen`, `frame_height` is `bottom - top + 1`, and `frame_width` is `right - left + 1`. The `frame_height` is greater than or equal to 2 and the `frame_width` is greater than or equal to 2.
    result = [list(row) for row in screen]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if i == top or i == bottom or j == left or j == right:
                if result[i][j] == '.':
                    result[i][j] = '+'
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 2000, `m` is an integer such that 1 <= `m` <= 2000, `screen` is a 2D list of strings where each string has length `m` and consists of characters '.' and 'w', `result` is a modified 2D list where all '.' characters on the borders defined by `top`, `bottom`, `left`, and `right` have been replaced with '+', `top`, `bottom`, `left`, and `right` are not `None` and represent the bounding box of all 'w' characters in `screen`, `frame_height` is `bottom - top + 1` and is greater than or equal to 2, and `frame_width` is `right - left + 1` and is greater than or equal to 2.
    return result
    #The program returns the modified 2D list 'result' where all '.' characters on the borders defined by 'top', 'bottom', 'left', and 'right' have been replaced with '+'. The 'result' is based on the 'screen' which is a 2D list of strings with length 'm' and consists of characters '.' and 'w'. The 'top', 'bottom', 'left', and 'right' are the bounding box of all 'w' characters in 'screen', with 'frame_height' being 'bottom - top + 1' and 'frame_width' being 'right - left + 1', both of which are greater than or equal to 2.
#Overall this is what the function does:The function accepts parameters `n`, `m`, and `screen`, where `n` and `m` are integers representing the dimensions of the 2D list `screen`, and `screen` is a 2D list of strings with length `m` and consists of characters '.' and 'w'. The function returns either -1 or the modified 2D list where '.' characters on the borders of the bounding box of all 'w' characters in `screen` have been replaced with '+'. The function first checks if there are any 'w' characters in the `screen`. If not, or if the bounding box of the 'w' characters has a height or width less than 2, it returns -1. If the 'w' characters form a valid bounding box with a height and width of at least 2, it creates a copy of the `screen`, replaces the '.' characters on the borders of the bounding box with '+', and returns this modified 2D list. The function handles edge cases where the 'w' characters may be located at the edges of the `screen`, and it correctly calculates the bounding box and modifies the borders accordingly.

