#State of the program right berfore the function call: n and m are integers representing the dimensions of the monitor resolution where 1 ≤ n, m ≤ 2000, and screen is a list of strings with length n, where each string has a length of m containing characters either '.' (representing a black pixel) or 'w' (representing a white pixel).
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
        
    #State of the program after the  for loop has been executed: `n` is an integer ≥ 1, `m` is an integer ≥ 1, `screen` is a list of strings of length `n`, `top` is the minimum row index of 'w' encountered (or None if 'w' was not found), `bottom` is the maximum row index of 'w' encountered (or None if 'w' was not found), `left` is the minimum column index of 'w' encountered (or None if 'w' was not found), `right` is the maximum column index of 'w' encountered (or None if 'w' was not found).
    if (top is None or bottom is None or left is None or right is None) :
        return -1
        #The program returns -1, indicating that 'w' was not found in at least one of the specified row or column indices since top, bottom, left, or right is None.
    #State of the program after the if block has been executed: *`n` is an integer ≥ 1, `m` is an integer ≥ 1, `screen` is a list of strings of length `n`, `top`, `bottom`, `left`, and `right` are all integers corresponding to the indices of 'w' encountered, with `top` being the minimum row index, `bottom` being the maximum row index, `left` being the minimum column index, and `right` being the maximum column index encountered.
    frame_height = bottom - top + 1
    frame_width = right - left + 1
    if (frame_height < 2 or frame_width < 2) :
        return -1
        #The program returns -1, indicating an invalid or insufficient frame size based on the conditions that frame_height is less than 2 or frame_width is less than 2.
    #State of the program after the if block has been executed: *`n` is an integer ≥ 1, `m` is an integer ≥ 1, `screen` is a list of strings of length `n`, `top`, `bottom`, `left`, `right` are all integers, `frame_height` is equal to `bottom - top + 1`, and `frame_width` is equal to `right - left + 1`. Both `frame_height` and `frame_width` are greater than or equal to 2.
    result = [list(row) for row in screen]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if i == top or i == bottom or j == left or j == right:
                if result[i][j] == '.':
                    result[i][j] = '+'
        
    #State of the program after the  for loop has been executed: `n` is an integer ≥ 1, `m` is an integer ≥ 1, `screen` is a list of strings of length `n`, `top` is an integer, `bottom` is an integer where `bottom ≥ top`, `left` is an integer, `right` is an integer where `right ≥ left`, `frame_height` is equal to `bottom - top + 1`, `frame_width` is equal to `right - left + 1`, and `result` is a list of lists of characters from `screen`, where all positions on the boundaries defined by `top`, `bottom`, `left`, and `right` that originally contained '.' are set to '+'. All other positions in `result` remain unchanged. The loop executes until `i` is greater than `bottom` and all boundary cells within the specified ranges have been processed.
    return result
    #The program returns a list of lists of characters from 'screen', where all positions on the boundaries defined by 'top', 'bottom', 'left', and 'right' that originally contained '.' are set to '+', and all other positions remain unchanged.
#Overall this is what the function does:The function accepts two integer parameters `n` and `m`, and a list of strings `screen`, which represents a monitor resolution containing characters either '.' or 'w'. It returns -1 if 'w' is not found in the screen or if the resulting frame's height or width is less than 2. If 'w' is found, it returns a modified list, where all boundary positions composed of '.' within the identified rectangle defined by the outermost 'w' characters are replaced with '+', while all other positions remain unchanged.

