#State of the program right berfore the function call: field is a string consisting of '*' and '.', and i is an integer such that 0 <= i < len(field).
def func_1(field, i):
    for slice_len in xrange(1, len(field) + 1):
        res = field[i::slice_len]
        
        if len(res) == 5 and set(res) == {'*'}:
            return slice_len
        
    #State of the program after the  for loop has been executed: `field` is a non-empty string, `res` is the final substring of `field` starting from index `i` and sliced with the last `slice_len` value. If the length of `res` is 5 and the set of characters in `res` is equal to {'*'}, the function returns the last `slice_len` value. Otherwise, the function returns None.
    return 0
    #The program returns None
#Overall this is what the function does:The function `func_1` accepts a string `field` consisting of '*' and '.' and an integer `i` such that \(0 \leq i < \text{len}(field)\). It iterates over possible slice lengths from 1 to the length of `field`. For each slice length, it creates a substring `res` starting from index `i` and slices `field` with the current slice length. If the length of `res` is exactly 5 and all characters in `res` are '*', the function returns the current slice length. If no such substring is found, the function returns 0.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and field is a string of length n consisting of characters '*' and '.', representing the segments of the level where '*' is a platform and '.' is a pit.
def func_2():
    n = int(raw_input())
    field = raw_input()
    win = False
    for i in xrange(n):
        if field[i] != '.':
            slice_len = func_1(field, i)
            if slice_len:
                j = i + 4 * slice_len
                if j + slice_len >= n or field[j + slice_len] == '*':
                    win = True
                    break
        
    #State of the program after the  for loop has been executed: `i` is 100 (or the last index `n-1`), `n` is a positive integer, `field` is a string of length `n` consisting of characters `'*'` and `'.'`, `win` is `True` if any `field[i]` is not `'.'` and satisfies the conditions within the loop, otherwise `win` remains `False`, `j` is `i + 4 * slice_len` where `slice_len` is the return value of `func_1(field, i)` if `field[i] != '.'`. If `j + slice_len >= n` or `field[j + slice_len] == '*'`, the nearest enclosing loop or switch statement is broken out of.
    if win :
        print('yes')
    else :
        print('no')
    #State of the program after the if-else block has been executed: *`i` is 100, `n` is a positive integer, `field` is a string of length `n` consisting of characters `'*'` and `'.'`. If `win` is `True` (at least one `field[i]` is not `'.'` and satisfies the conditions within the loop), then the nearest enclosing loop or switch statement is broken out of if either `j + slice_len >= n` or `field[j + slice_len] == '*'`, the output is 'yes'. If `win` is `False`, `j` is `i + 4 * slice_len` where `slice_len` is the return value of `func_1(field, i)` if `field[i] == '.'`, and if `j + slice_len >= n` or `field[j + slice_len] == '*'`, the nearest enclosing loop or switch statement is broken out of; the console prints 'no'.
#Overall this is what the function does:The function `func_2` accepts an integer `n` and a string `field` which is a sequence of `'*'` and `'.'`. It checks if there exists a segment in `field` that can be safely traversed without falling into a pit (`'.'`). Specifically, it looks for a segment starting at an index where the character is not a pit (`'.'`), and checks if a subsequent segment of length `4 * slice_len` is either outside the bounds of the string or is itself a platform (`'*'`). If such a segment is found, the function sets `win` to `True`. After checking all possible segments, the function prints `'yes'` if `win` is `True`, indicating that a safe path exists, and `'no'` otherwise. Potential edge cases include when `n` is less than 1 or when the entire `field` consists of pits only. The function also assumes that `func_1` returns the length of the segment to be checked, and this functionality is not explicitly defined in the provided code.

