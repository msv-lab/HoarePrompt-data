#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n consisting of "-" and "+" characters.
def func_1():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n):
        cnt += 1 if s[i] == '+' else -1
        
        if cnt < 0:
            cnt = 0
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `cnt` is the final count after processing the string `s` according to the given conditions, `i` is `n-1` and `s` is the original string. If the loop does not execute at all (i.e., `n` is 0), then `cnt` remains 0.
    func_2(cnt)
#Overall this is what the function does:The function processes a string `s` of length `n`, where `n` is a positive integer between 1 and 100, and `s` consists of "-" and "+" characters. It counts the number of "+" characters minus the number of "-" characters up to a point where the count becomes negative, at which point it resets the count to zero. After processing the entire string, it calls another function `func_2` with the final count as its argument. If the string is empty (`n` is 0), the initial count remains 0.

#State of the program right berfore the function call: This function does not contribute to solving the given problem. The provided function `func_2` is a utility function for printing values to a stream and does not relate to the operations described in the problem statement.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: Output State: `at_start` is `False`, `kwargs` no longer contains 'sep' and 'file' keys, `sep` is `b' '`, `file` is `sys.stdout`, `args` must have at least one element, and `sys.stdout` content is the concatenated string representations of all elements in `args` separated by `b' '`.
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`at_start` is `False`, `kwargs` no longer contains 'sep', 'file', and 'end' keys, `sep` is `b' '`, `file` is `sys.stdout`, `args` must have at least one element, `sys.stdout` content is the original concatenated string representations of all elements in `args` separated by `b' '` followed by `b'\n'`, and `sys.stdout` buffer is flushed if `kwargs.pop('flush', False)` is explicitly set to `True`. Otherwise, the buffer remains unchanged.
#Overall this is what the function does:The function `func_2` does not accept any parameters and does not return any value. Its primary action is to print the elements of the `args` tuple, separated by a space (`b' '`), to the standard output (`sys.stdout`). After the loop, it writes the `end` value (defaulting to `b'\n'`) and flushes the buffer if specified. However, the function is not designed to handle or process any keyword arguments other than `'sep'`, `'file'`, `'end'`, and `'flush'`. If these keyword arguments are present in the `kwargs` dictionary, they are ignored.

