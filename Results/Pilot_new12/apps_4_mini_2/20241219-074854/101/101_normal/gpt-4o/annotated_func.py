#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2000, and screen is a list of strings where each string has a length of m and consists of characters either '.' or 'w', ensuring at least one 'w' is present in the list.
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
        
    #State of the program after the  for loop has been executed: `top` is the minimum row index of 'w', `bottom` is the maximum row index of 'w', `left` is the minimum column index of 'w', `right` is the maximum column index of 'w', `n` and `m` are positive integers with at least one 'w' present in `screen`.
    if (top is None or bottom is None or left is None or right is None) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: *`top` is the minimum row index of 'w', `bottom` is the maximum row index of 'w', `left` is the minimum column index of 'w', `right` is the maximum column index of 'w', and none of the variables `top`, `bottom`, `left`, or `right` are None. Additionally, `n` and `m` are positive integers with at least one 'w' present in `screen`.
    frame_height = bottom - top + 1
    frame_width = right - left + 1
    if (frame_height < 2 or frame_width < 2) :
        return -1
        #The program returns -1, indicating that either the frame height is less than 2 or the frame width is less than 2.
    #State of the program after the if block has been executed: *`top` is the minimum row index of 'w', `bottom` is the maximum row index of 'w', `left` is the minimum column index of 'w', `right` is the maximum column index of 'w', `frame_height` is equal to `bottom - top + 1`, `frame_width` is equal to `right - left + 1`, `frame_height` is greater than or equal to 2 and `frame_width` is greater than or equal to 2.
    result = [list(row) for row in screen]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if i == top or i == bottom or j == left or j == right:
                if result[i][j] == '.':
                    result[i][j] = '+'
        
    #State of the program after the  for loop has been executed: `result` has the frame defined by indices from `top` to `bottom` and from `left` to `right` updated with '+', specifically at the border positions represented by `top`, `bottom`, `left`, and `right`; `frame_height` is the original value, equal to `bottom - top + 1`, and `frame_width` is the original value, equal to `right - left + 1`.
    return result
    #The program returns the frame defined by indices from 'top' to 'bottom' and from 'left' to 'right', which is updated with '+' at the border positions represented by 'top', 'bottom', 'left', and 'right'
#Overall this is what the function does:The function accepts two positive integers, `n` and `m`, and a list of strings, `screen`, where each string consists of characters `'.'` and `'w'`, ensuring that at least one `'w'` is present in the list. It analyzes the positions of `'w'` characters in the `screen` to determine the bounding rectangle defined by the minimum and maximum row and column indices of these characters. If the height or width of this rectangle (frame) is less than 2, the function returns `-1`. Otherwise, it returns a modified version of `screen` where the borders of the rectangle are marked with `'+'`, specifically at the indices corresponding to the found bounding rectangle. The returned frame includes all characters within the rectangle but updates only the border positions to have `'+'` instead of `'.'`. Note that the function does not validate that `n` and `m` are greater than or equal to 1, and it assumes the presence of at least one `'w'`.

