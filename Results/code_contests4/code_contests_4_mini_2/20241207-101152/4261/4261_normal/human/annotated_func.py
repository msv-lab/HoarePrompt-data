#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 1000, n is an integer such that 1 ≤ n ≤ 30, k is an integer such that 2 ≤ k ≤ 100, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i ≤ 10^16.
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
        
    #State of the program after the  for loop has been executed: `i` is -1, `r` is the last computed value of `j`, `j` is the last computed value before exiting the loop, `req` contains all unique values of `j` computed during the iterations.
    func_2('YES')
#Overall this is what the function does:The function accepts two integers `n` and `k`, and a list `li` of `n` integers. It processes each integer in `li`, calculating a value `j` based on the divisibility by powers of `k` and tracks unique values of `j`. If a duplicate value is found, it calls `func_2` with 'NO' and exits; otherwise, after processing all integers, it calls `func_2` with 'YES'. The function does not return any value, always resulting in a return of None.

#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 1000, n is an integer such that 1 ≤ n ≤ 30, k is an integer such that 2 ≤ k ≤ 100, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i ≤ 10^{16}.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `T` is an integer such that 1 ≤ `T` ≤ 1000, `n` is an integer such that 1 ≤ `n` ≤ 30, `k` is an integer such that 2 ≤ `k` ≤ 100, `a` is a list of `n` integers where each integer `a_i` satisfies 0 ≤ `a_i` ≤ 10^{16}, `at_start` is False, `args` has been fully iterated over, and all elements of `args` have been written to the file, with `sep` written between the elements except before the first one.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`T` is an integer such that 1 ≤ `T` ≤ 1000, `n` is an integer such that 1 ≤ `n` ≤ 30, `k` is an integer such that 2 ≤ `k` ≤ 100, `a` is a list of `n` integers where each integer `a_i` satisfies 0 ≤ `a_i` ≤ 10^{16}, `at_start` is False, `args` has been fully iterated over, and all elements of `args` have been written to the file with `sep` written between the elements except before the first one; the file ends with the value of `kwargs.pop('end', '\n')`. If `kwargs.pop('flush', False)` is True, the file buffer is flushed, ensuring that all data written to the file is pushed out to the underlying storage.
#Overall this is what the function does:The function accepts variable arguments and keyword arguments for printing. It writes the elements of `args` to a specified output stream (`file`), separating them with a specified separator (`sep`). After writing all elements, it appends an ending character (default is a newline) and optionally flushes the output buffer if the `flush` keyword argument is set to True. It does not use the parameters `T`, `n`, `k`, and `a` in its logic, making those parameters irrelevant to its functionality.

