#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 2000, screen is a list of n strings, each string consists of exactly m characters where each character is either '.' or 'w', and there is at least one 'w' character in the screen.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 2000\), `m` is an integer such that \(1 \leq m \leq 2000\), `screen` is a list of `n` strings, each string consists of exactly `m` characters where each character is either `'.'` or `'w'`, and there is at least one `'w'` character in the `screen`. After the loop completes, `top` is the smallest index of any row containing a `'w'`, `bottom` is the largest index of any row containing a `'w'`, `left` is the smallest column index of any `'w'`, and `right` is the largest column index of any `'w'`. The variables `n`, `m`, and the content of `screen` remain constant throughout the loop. The loop iterates through all `n` rows and `m` columns, ensuring that `i` will be `n` and `j` will be `m` after the loop ends.
    if (top is None or bottom is None or left is None or right is None) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: `n` is an integer such that \(1 \leq n \leq 2000\), `m` is an integer such that \(1 \leq m \leq 2000\), `screen` is a list of `n` strings, each string consists of exactly `m` characters where each character is either `'.'` or `'w'`, and there is at least one `'w'` character in the `screen`. After the loop completes, `top` is the smallest index of any row containing a `'w'`, `bottom` is the largest index of any row containing a `'w'`, `left` is the smallest column index of any `'w'`, and `right` is the largest column index of any `'w'`. The variables `n`, `m`, and the content of `screen` remain constant throughout the loop. The loop iterates through all `n` rows and `m` columns, ensuring that `i` will be `n` and `j` will be `m` after the loop ends. Additionally, `top` is not `None`, `bottom` is not `None`, `left` is not `None`, and `right` is not `None`.
    frame_height = bottom - top + 1

frame_width = right - left + 1
    if (frame_height < 2 or frame_width < 2) :
        return -1
        #The program returns -1
    #State of the program after the if block has been executed: n is an integer such that \(1 \leq n \leq 2000\), m is an integer such that \(1 \leq m \leq 2000\), screen is a list of n strings, each string consists of exactly m characters where each character is either '.' or 'w', and there is at least one 'w' character in the screen, top is the smallest index of any row containing a 'w', bottom is the largest index of any row containing a 'w', left is the smallest column index of any 'w', right is the largest column index of any 'w', frame_height is (bottom - top + 1), frame_width is (right - left + 1), and both frame_height and frame_width are greater than or equal to 2
    result = [list(row) for row in screen]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if i == top or i == bottom or j == left or j == right:
                if result[i][j] == '.':
                    result[i][j] = '+'
        
    #State of the program after the  for loop has been executed: After the loop has finished executing, the variables `n`, `m`, `screen`, `top`, `bottom`, `left`, `right`, `frame_height`, and `frame_width` remain unchanged. The variable `i` has the value `bottom + 1`. All elements in `result` at positions `[i][j]` where `i` is `top` or `bottom` or `j` is `left` or `right` will be updated to '+' if they were initially '.', and all other elements in `result` remain unchanged.
    return result
    #The program returns `result`, which is a 2D list where all elements at positions `[i][j]` where `i` is `top` or `bottom` or `j` is `left` or `right` have been updated to '+' if they were initially '.', and all other elements remain unchanged.
#Overall this is what the function does:The function `func_1` takes three parameters: `n`, `m`, and `screen`. `n` and `m` are integers such that \(1 \leq n, m \leq 2000\), and `screen` is a list of `n` strings, each string consisting of exactly `m` characters where each character is either `'.'` or `'w'`, with at least one `'w'` character in the `screen`.

The function determines the bounding box of all `'w'` characters in the `screen` and then modifies the `screen` to create a frame around this bounding box by changing certain `'.'` characters to `'+'`.

1.

