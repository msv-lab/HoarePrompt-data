#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 2000, and screen is a list of strings of length m containing only characters 'w' and '.' where at least one character is 'w'.
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
        
    #State of the program after the  for loop has been executed: `top` is the minimum row index containing 'w', `bottom` is the maximum row index containing 'w', `left` is the minimum column index containing 'w', `right` is the maximum column index containing 'w', `n` is an integer such that 1 ≤ `n` ≤ 2000, `m` is an integer such that 1 ≤ `m` ≤ 2000, `screen` is a list of strings containing at least one 'w'. If 'w' is present in the screen, `top`, `bottom`, `left`, and `right` will not be None; otherwise, if no 'w' is present, they remain None.
    if (top is None or bottom is None or left is None or right is None) :
        return -1
        #The program returns -1 due to the presence of None in the variables top, bottom, left, or right, indicating an undefined state.
    #State of the program after the if block has been executed: *`top` is the minimum row index containing 'w', `bottom` is the maximum row index containing 'w', `left` is the minimum column index containing 'w', `right` is the maximum column index containing 'w', `n` is an integer such that 1 ≤ `n` ≤ 2000, `m` is an integer such that 1 ≤ `m` ≤ 2000, `screen` is a list of strings containing at least one 'w'. None of `top`, `bottom`, `left`, or `right` are None.
    frame_height = bottom - top + 1
    frame_width = right - left + 1
    if (frame_height < 2 or frame_width < 2) :
        return -1
        #The program returns -1 due to the condition that the current value of frame_height is less than 2 or the current value of frame_width is less than 2.
    #State of the program after the if block has been executed: *`top` is the minimum row index containing 'w', `bottom` is the maximum row index containing 'w', `left` is the minimum column index containing 'w', `right` is the maximum column index containing 'w', `n` is an integer such that 1 ≤ `n` ≤ 2000, `m` is an integer such that 1 ≤ `m` ≤ 2000, `screen` is a list of strings containing at least one 'w', `frame_height` is equal to `bottom - top + 1`, `frame_width` is equal to `right - left + 1`, `frame_height` is greater than or equal to 2, and `frame_width` is greater than or equal to 2.
    result = [list(row) for row in screen]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if i == top or i == bottom or j == left or j == right:
                if result[i][j] == '.':
                    result[i][j] = '+'
        
    #State of the program after the  for loop has been executed: `top` is the minimum row index containing 'w', `bottom` is the maximum row index containing 'w', `left` is the minimum column index containing 'w', `right` is the maximum column index containing 'w', `result` contains '+' at the border positions defined by `top`, `bottom`, `left`, and `right` where originally there were '.', the positions inside the rectangle defined by these boundaries remain unaffected.
    return result
    #The program returns the modified 'result' which contains '+' at the border positions defined by 'top', 'bottom', 'left', and 'right', where originally there were '.'
#Overall this is what the function does:The function accepts two integers `n` and `m`, and a list of strings `screen`. It calculates the minimum and maximum indices of 'w' characters in the `screen`. If no 'w' characters are found or if the resulting rectangle formed by these indices is less than 2 in height or width, it returns -1. Otherwise, it returns a modified version of `screen`, replacing the border positions of the rectangle defined by the 'w' characters with '+' while leaving the interior unchanged.

