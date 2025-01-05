#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 30), k is an integer (2 ≤ k ≤ 100), and li is a list of n non-negative integers (0 ≤ a_i ≤ 10^16).
def func_1():
    n, k = get_list()
    li = get_list()
    req = set()
    for i in li:
        r = 0
        
        while i > 0:
            j = 0
            while i % k ** (j + 1) == 0:
                j += 1
            i //= k ** j
            j += r
            if j in req:
                func_2('NO')
                return
            req.add(j)
            r = j
            i -= 1
        
    #State of the program after the  for loop has been executed: `req` contains all unique values of `j` computed during the loop iterations, `r` is equal to the last computed value of `j`, `i` is less than the original value of `i` for all elements of `li`, and all values in `req` are non-negative integers derived from the computations based on the elements of `li`. If `li` was empty, `req` remains empty, and `r` and `j` are unchanged.
    func_2('YES')
#Overall this is what the function does:The function accepts a positive integer `n`, an integer `k`, and a list `li` of `n` non-negative integers. It processes each element in `li` to compute a set of unique values derived from their divisibility by powers of `k`. If any computed value already exists in the set, it calls `func_2` with 'NO' and exits; otherwise, after processing all elements, it calls `func_2` with 'YES'. The function does not return any value.

#State of the program right berfore the function call: args is a variable-length argument list containing values of any type, and kwargs is a dictionary of optional keyword arguments that may include 'sep', 'file', 'end', and 'flush'.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` is a variable-length argument list containing values of any type, `x` is the last value in `args`, `at_start` is False, `file` now contains the string representations of all values in `args` separated by `sep`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` is a variable-length argument list containing values of any type, `x` is the last value in `args`, `at_start` is False, `file` contains the string representations of all values in `args` separated by `sep`, the value of `kwargs` has been updated due to the pop operation, and if the previous value associated with the key 'flush' was removed and is now True, the flush operation has been executed on `file`.
#Overall this is what the function does:The function accepts a variable-length argument list `args` containing values of any type and a dictionary `kwargs` for optional keyword arguments. It prints the string representations of the values in `args` to a specified `file` stream, separated by a specified `sep` string, and ends with a specified `end` string. If the `flush` keyword argument is set to True, it flushes the output stream. The function does not return any value.

