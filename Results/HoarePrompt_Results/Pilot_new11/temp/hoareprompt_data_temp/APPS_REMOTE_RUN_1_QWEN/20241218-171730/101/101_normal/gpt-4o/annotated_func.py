#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2000, and screen is a list of n strings, each string is of length m consisting of characters "." and "w", where "w" represents a white pixel and "." represents a black pixel. At least one pixel in the screen is white.
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
        
    #State of the program after the  for loop has been executed: `screen` is a list of `n` strings, each string is of length `m` and consists of characters ".", "w". `top` is the smallest row index of any 'w' in the entire `screen`, `bottom` is the largest row index of any 'w' in the entire `screen`, `left` is the smallest column index of any 'w' in the entire `screen`, `right` is the largest column index of any 'w' in the entire `screen`.
    if (top is None or bottom is None or left is None or right is None) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `screen` is a list of `n` strings, each string is of length `m` and consists of characters ".", "w". `top` is the smallest row index of any 'w' in the entire `screen`, `bottom` is the largest row index of any 'w' in the entire `screen`, `left` is the smallest column index of any 'w' in the entire `screen`, `right` is the largest column index of any 'w' in the entire `screen`. The condition (top is not None and bottom is not None and left is not None and right is not None) is true
    frame_height = bottom - top + 1
    frame_width = right - left + 1
    if (frame_height < 2 or frame_width < 2) :
        return -1
        #-1
    #State of the program after the if block has been executed: `screen` is a list of `n` strings, each string is of length `m` and consists of characters ".", "w"; `top` is the smallest row index of any 'w' in the entire `screen`; `bottom` is the largest row index of any 'w' in the entire `screen`; `left` is the smallest column index of any 'w' in the entire `screen`; `right` is the largest column index of any 'w' in the entire `screen`; `frame_height` is `bottom - top + 1`; `frame_width` is `right - left + 1`. `frame_height` is greater than or equal to 2 and `frame_width` is greater than or equal to 2
    result = [list(row) for row in screen]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if i == top or i == bottom or j == left or j == right:
                if result[i][j] == '.':
                    result[i][j] = '+'
        
    #State of the program after the  for loop has been executed: `screen` is a list of `n` strings, each string is of length `m` and consists of characters ".", "w"; `top` is the smallest row index of any 'w' in the entire `screen`; `bottom` is the largest row index of any 'w' in the entire `screen`; `left` is the smallest column index of any 'w' in the entire `screen`; `right` is the largest column index of any 'w' in the entire `screen`; `frame_height` is `bottom - top + 1`; `frame_width` is `right - left + 1`; `frame_height` is greater than or equal to 2; `frame_width` is greater than or equal to 2; `result` is a list of `n` lists, each list is a copy of the corresponding string in `screen` with all border cells (rows `top` and `bottom`, columns `left` and `right`) updated to '+' if they were originally '.'.
    return result
    #`result` is a list of `n` lists, each list is a copy of the corresponding string in `screen` with all border cells (rows `top` and `bottom`, columns `left` and `right`) updated to '+' if they were originally '.'
#Overall this is what the function does:The function `func_1` accepts three parameters: `n`, `m`, and `screen`. `n` and `m` are positive integers such that 1 ≤ n, m ≤ 2000, and `screen` is a list of `n` strings, each string is of length `m` consisting of characters "." and "w", where "w" represents a white pixel and "." represents a black pixel. At least one pixel in the screen is white.

The function performs the following actions:
1. It finds the topmost, bottommost, leftmost, and rightmost indices of any 'w' in the `screen`.
2. If no white pixels are found (`top` or `bottom` or `left` or `right` remains `None`), it returns -1.
3. It calculates the frame height and width based on the found indices.
4. If the frame height or width is less than 2, it returns -1.
5. It creates a copy of the original `screen` called `result`.
6. It updates the border cells (rows `top` and `bottom`, columns `left` and `right`) in `result` to '+' if they were originally '.'.

The function can return one of three states:
- Case_1: The function returns -1 if no white pixels are found or if the frame dimensions are less than 2.
- Case_2: The function returns -1 under the same conditions as Case_1.
- Case_3: The function returns a list of `n` lists, each list is a copy of the corresponding string in `screen` with all border cells (rows `top` and `bottom`, columns `left` and `right`) updated to '+' if they were originally '.'.

The final state of the program after the function concludes will be:
- If the function returns -1, the program will have returned -1.
- If the function returns a modified `result`, the `result` will be a list of `n` lists, each list is a copy of the corresponding string in `screen` with all border cells (rows `top` and `bottom`, columns `left` and `right`) updated to '+' if they were originally '.'.

