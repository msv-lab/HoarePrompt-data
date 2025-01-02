#State of the program right berfore the function call: field is a string consisting of '*' and '.', and i is an integer such that 0 <= i < len(field).
def func_1(field, i):
    for slice_len in xrange(1, len(field) + 1):
        res = field[i::slice_len]
        
        if len(res) == 5 and set(res) == {'*'}:
            return slice_len
        
    #State of the program after the  for loop has been executed: `field` is a string consisting of '*' and '.', `i` is undefined, `slice_len` is either `len(field) + 1` or less than `len(field)`, `res` is a slice of `field` starting from an undefined index `i` with a step of `slice_len`. If there exists any slice of `field` starting from any index with a step of `slice_len` such that the length of the slice is 5 and all elements in the slice are '*', the function returns the corresponding `slice_len`. Otherwise, the function returns `None`.
    return 0
    #The program returns None
#Overall this is what the function does:The function `func_1` accepts a string `field` consisting of '*' and '.' characters and an integer `i` such that \(0 \leq i < \text{len}(field)\). It aims to find a slice length (`slice_len`) that meets specific conditions. Specifically:

- It iterates through possible slice lengths from 1 to the length of `field`.
- For each slice length, it extracts a substring `res` from `field` starting at index `i` with the current slice length.
- If `res` has a length of 5 and consists entirely of '*', it returns the current slice length.
- If no such slice is found, the function returns `None`.

The potential edge cases include:
- If `field` is empty or `i` is out of bounds, the function will still follow the same logic but will not find a valid `res` substring, leading to a return value of `None`.
- If the first condition (`len(res) == 5 and set(res) == {'*'}`) is met, the function will immediately return the slice length, which means the subsequent conditions (`slice_len_current + 1` and `slice_len_current + 2`) will not be checked.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and field is a string consisting of '*' and '.' representing the scheme of the level, where '*' denotes a platform and '.' denotes a pit.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 100\), `field` is the input string provided by the user, and `win` is `True` if there exists an index `i` where `field[i] != '.'` and either \(i + 4 \times \text{slice\_len} + \text{slice\_len} \geq n\) or `field[i + 5 \times \text{slice\_len}] == '*'`, otherwise `win` remains `False`.
    if win :
        print('yes')
    else :
        print('no')
    #State of the program after the if-else block has been executed: `n` is an integer such that \(1 \leq n \leq 100\), `field` is the input string provided by the user, and `win` is `True` if there exists an index `i` where `field[i] != '.'` and either \(i + 4 \times \text{slice\_len} + \text{slice\_len} \geq n\) or `field[i + 5 \times \text{slice\_len}] == '*'`, otherwise `win` remains `False`. If `win` is `True`, the condition is maintained. If `win` is `False`, it remains `False`.
#Overall this is what the function does:The function processes an integer `n` such that \(1 \leq n \leq 100\) and a string `field` consisting of '*' and '.', determining whether there exists an index `i` where `field[i] != '.'` and either \(i + 5 \times \text{slice\_len} \geq n\) or `field[i + 5 \times \text{slice\_len}] == '*'`. The function then prints 'yes' if a winning condition is found (i.e., `win` is `True`), and 'no' otherwise. Potential edge cases include scenarios where no valid index `i` is found within the specified constraints, which results in `win` remaining `False` by default. The function does not modify the input parameters `n` and `field`.

