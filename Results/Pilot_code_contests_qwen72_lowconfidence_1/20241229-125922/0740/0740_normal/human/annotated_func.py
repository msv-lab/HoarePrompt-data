#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 10^5, and x is a list of k integers where each integer is in the range 1 to n inclusive.
def func_1():
    n, k = readlist()
    x = readlist()
    counter = [(-1, -1)] * (n + 1)
    for (i, xi) in enumerate(x):
        if counter[xi][0] == -1:
            counter[xi] = i, -1
        else:
            counter[xi] = counter[xi][0], i
        
    #State of the program after the  for loop has been executed: `n` and `k` are the first and second integers from the input list respectively, both within the range 1 to 10^5, `x` is a list of integers read from the input, `counter` is a list of length `n + 1` where each element at index `xi` (for each `xi` in `x`) is a tuple `(first_occurrence, last_occurrence)`. Here, `first_occurrence` is the index of the first occurrence of `xi` in `x`, and `last_occurrence` is the index of the last occurrence of `xi` in `x`. If `xi` does not appear in `x`, the corresponding element in `counter` remains `(-1, -1)`.
    res = 0
    for i in range(1, n + 1):
        if counter[i][0] == -1:
            res += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer within the range 1 to \(10^5\), `k` is a positive integer within the range 1 to \(10^5\), `x` is a list of integers, `counter` is a list of length `n + 1` where each element at index `xi` (for each `xi` in `x`) is a tuple `(first_occurrence, last_occurrence)`, `res` is the number of integers from 1 to `n` that do not appear in the list `x`.
    for i in range(1, n):
        if counter[i][0] != -1:
            if counter[i][1] != -1:
                if counter[i + 1][0] == -1 or counter[i + 1][0] > counter[i][1]:
                    res += 1
            elif counter[i + 1][0] == -1 or counter[i + 1][0] > counter[i][0]:
                res += 1
        else:
            res += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer within the range 1 to \(10^5\), `k` is a positive integer within the range 1 to \(10^5\), `x` is a list of integers, `counter` is a list of length `n + 1` where each element at index `xi` (for each `xi` in `x`) is a tuple `(first_occurrence, last_occurrence)`, `res` is the number of integers from 1 to `n` that do not appear in the list `x` and also do not form a consecutive sequence with any integer that appears in the list `x`.
    for i in range(1, n):
        if counter[i + 1][0] != -1:
            if counter[i + 1][1] != -1:
                if counter[i][0] == -1 or counter[i][0] > counter[i + 1][1]:
                    res += 1
            elif counter[i][0] == -1 or counter[i][0] > counter[i + 1][0]:
                res += 1
        else:
            res += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer within the range 1 to \(10^5\), `k` is a positive integer within the range 1 to \(10^5\), `x` is a list of integers, `counter` is a list of length `n + 1` where each element at index `xi` (for each `xi` in `x`) is a tuple `(first_occurrence, last_occurrence)`, `res` is the number of integers from 1 to `n` that do not appear in the list `x` and also do not form a consecutive sequence with any integer that appears in the list `x`. After the loop finishes executing, `res` contains the count of integers from 1 to `n` that satisfy the above condition, and `i` is `n - 1`.
    func_2(res)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` and a list `x` of `k` integers, where each integer in `x` is between 1 and `n` inclusive. It then processes the list `x` to determine the number of integers from 1 to `n` that do not appear in `x` and also do not form a consecutive sequence with any integer that appears in `x`. The result, stored in `res`, is passed to another function `func_2`. The function does not return any value. Edge cases include when `x` is empty or when all integers from 1 to `n` are present in `x`. In these cases, `res` will be 0. Additionally, the function assumes that the input values are within the specified range and that `readlist` is a valid function for reading input lists.

#State of the program right berfore the function call: args is a tuple of any values, and kwargs is a dictionary that may contain the keys 'sep', 'file', 'end', and 'flush'. 'sep' is a bytes object used to separate the arguments, 'file' is a file-like object to which the output is written, 'end' is a bytes object appended after the last argument, and 'flush' is a boolean indicating whether to forcibly flush the stream.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` is a tuple of any values, `kwargs` is a dictionary that may contain the keys 'end', 'flush', and 'sep', `sep` is a bytes object used to separate the arguments, now equal to the value of 'sep' from `kwargs` if it existed, otherwise `b' '`, `file` is a file-like object to which the output is written, now equal to the value of 'file' from `kwargs` if it existed, otherwise `sys.stdout`, `at_start` is False, `file` contains the string representations of all elements in `args` separated by `sep`. If `args` is empty, `file` remains unchanged, and `at_start` remains True.
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` is a tuple of any values, `kwargs` is a dictionary that may contain the keys 'flush' and 'sep', `sep` is a bytes object used to separate the arguments, now equal to the value of 'sep' from `kwargs` if it existed, otherwise `b' '`, `file` is a file-like object to which the output is written, now equal to the value of 'file' from `kwargs` if it existed, otherwise `sys.stdout`, `at_start` is False, `file` contains the string representations of all elements in `args` separated by `sep` followed by the value of 'end' from `kwargs` if it existed, otherwise `b'\n'`. If `kwargs['flush']` was True, the buffer of `file` has been flushed.
#Overall this is what the function does:The function `func_2` prints the values of its arguments to a specified file-like object, defaulting to `sys.stdout` if no file is specified. It separates the arguments using a byte string separator (`sep`), defaults to a space (`b' '`), and appends a byte string terminator (`end`), defaults to a newline (`b'\n'`). If the `flush` keyword argument is set to `True`, the output stream is forcibly flushed. The function modifies the `kwargs` dictionary by removing the used keys ('sep', 'file', 'end', 'flush'). If `args` is empty, nothing is printed, and `file` remains unchanged. The function does not return any value.

