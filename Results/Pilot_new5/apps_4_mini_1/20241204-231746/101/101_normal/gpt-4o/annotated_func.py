#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 2000, and screen is a list of strings of length m, where each string contains exactly m characters consisting of '.' for black pixels and 'w' for white pixels, with at least one 'w' present in the screen.
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
        
    #State of the program after the  for loop has been executed: `top` is the minimum row index of 'w' characters, `bottom` is the maximum row index of 'w' characters, `left` is the minimum column index of 'w' characters, `right` is the maximum column index of 'w' characters; `n` is the number of rows, `m` is the number of columns.
    if (top is None or bottom is None or left is None or right is None) :
        return -1
        #The program returns -1, indicating that there is no valid index for the 'w' characters due to at least one of the indices (top, bottom, left, right) being None.
    #State of the program after the if block has been executed: *`top` is the minimum row index of 'w' characters, `bottom` is the maximum row index of 'w' characters, `left` is the minimum column index of 'w' characters, `right` is the maximum column index of 'w' characters; `n` is the number of rows, `m` is the number of columns. None of the values of `top`, `bottom`, `left`, or `right` are None.
    frame_height = bottom - top + 1
    frame_width = right - left + 1
    if (frame_height < 2 or frame_width < 2) :
        return -1
        #The program returns -1 because frame_height is less than 2 or frame_width is less than 2.
    #State of the program after the if block has been executed: *`top` is the minimum row index of 'w' characters, `bottom` is the maximum row index of 'w' characters, `left` is the minimum column index of 'w' characters, `right` is the maximum column index of 'w' characters, `n` is the number of rows, `m` is the number of columns, `frame_height` is equal to `bottom - top + 1`, `frame_width` is equal to `right - left + 1`, and both `frame_height` and `frame_width` are greater than or equal to 2.
    result = [list(row) for row in screen]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if i == top or i == bottom or j == left or j == right:
                if result[i][j] == '.':
                    result[i][j] = '+'
        
    #State of the program after the  for loop has been executed: `top` is less than or equal to `bottom`, `bottom` is less than `n`, `left` is less than or equal to `right`, `right` is less than `m`, and all elements `result[i][j]` on the boundary defined by `top`, `bottom`, `left`, and `right` have been updated to '+' if they were originally '.'.
    return result
    #The program returns the updated 'result' matrix where the boundary defined by 'top', 'bottom', 'left', and 'right' has been modified with '+' in place of '.'
#Overall this is what the function does:The function accepts two integer parameters, `n` (number of rows) and `m` (number of columns), along with a list of strings `screen` representing a grid of pixels. It identifies the smallest rectangle that contains all 'w' (white pixel) characters in the grid. If no 'w' characters are found or if the rectangle formed has a height or width less than 2, it returns -1. Otherwise, it modifies the boundaries of this rectangle to replace '.' (black pixels) with '+' and returns the updated grid. The function ensures that `screen` has at least one 'w' character, as guaranteed by the input conditions.

