#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 2000, and screen is a list of strings, each string consisting of exactly m characters where each character is either '.' (indicating a black pixel) or 'w' (indicating a white pixel).
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
        
    #State of the program after the  for loop has been executed: `n` and `m` are integers such that 1 ≤ `n` ≤ 2000 and 1 ≤ `m` ≤ 2000; `screen` is a list of strings; `top`, `bottom`, `left`, and `right` will represent the bounding box of all 'w' characters in the `screen` if any are present, where `top` is the minimum row index, `bottom` is the maximum row index, `left` is the minimum column index, and `right` is the maximum column index. If no 'w' characters are found, `top` and `bottom` will remain None, and `left` and `right` will remain out of bounds.
    if (top is None or bottom is None or left is None or right is None) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: *`n` and `m` are integers such that 1 ≤ `n` ≤ 2000 and 1 ≤ `m` ≤ 2000; `screen` is a list of strings; `top`, `bottom`, `left`, and `right` are all integers representing the bounding box of all 'w' characters in the `screen`, and none of these values are None. In this case, `top` is the minimum row index of the 'w' characters, `bottom` is the maximum row index, `left` is the minimum column index, and `right` is the maximum column index.
    frame_height = bottom - top + 1
    frame_width = right - left + 1
    if (frame_height < 2 or frame_width < 2) :
        return -1
        #The program returns -1, indicating that the current value of `frame_height` is less than 2 or the current value of `frame_width` is less than 2.
    #State of the program after the if block has been executed: *`n` and `m` are integers such that 1 ≤ `n` ≤ 2000 and 1 ≤ `m` ≤ 2000; `screen` is a list of strings; `top`, `bottom`, `left`, and `right` remain unchanged; `frame_height` is greater than or equal to 2; `frame_width` is greater than or equal to 2.
    result = [list(row) for row in screen]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if i == top or i == bottom or j == left or j == right:
                if result[i][j] == '.':
                    result[i][j] = '+'
        
    #State of the program after the  for loop has been executed: `n` and `m` are integers between 1 and 2000, `screen` is a list of strings, and `result` is a modified list of lists of characters. All entries in `result` that correspond to the indices where `i` is equal to `top` or `bottom`, or `j` is equal to `left` or `right`, which were originally '.', are now updated to '+'. The `top`, `bottom`, `left`, and `right` indices remain unchanged within their specified bounds, and any original entries in `result` not affected by this update remain unchanged.
    return result
    #The program returns the modified list 'result' where entries corresponding to the indices defined by 'top', 'bottom', 'left', and 'right' are updated to '+' if they were originally '.'
#Overall this is what the function does:Functionality: The function accepts two integers `n` and `m` (where \(1 \leq n, m \leq 2000\)) and a list of strings `screen`, with each string containing exactly `m` characters that are either '.' (black pixel) or 'w' (white pixel). The function identifies the bounding box of all 'w' characters in the `screen`. If no 'w' characters are found or if the constructed bounding box has a width or height less than 2, the function returns -1. If 'w' characters are present and the bounding box dimensions are valid, the function produces a modified list `result`, where the border of the bounding box (top, bottom, left, right) is updated from '.' to '+'. Variables `top`, `bottom`, `left`, and `right` represent the bounding box's limits and are determined based on the locations of 'w' pixels. If the bounding box is valid, the function returns the modified `result`; otherwise, it returns -1. The function does not account for edge cases if `screen` contains non-standard characters (characters other than '.' or 'w').

