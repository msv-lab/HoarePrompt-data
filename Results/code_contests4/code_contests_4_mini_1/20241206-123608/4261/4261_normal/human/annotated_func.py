#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 1000, n is an integer such that 1 ≤ n ≤ 30, k is an integer such that 2 ≤ k ≤ 100, and a is a list of n non-negative integers where each element a_i satisfies 0 ≤ a_i ≤ 10^16.
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
        
    #State of the program after the  for loop has been executed: `i` is -1, `r` is the largest integer such that the last value of `i` was a multiple of `k` raised to the power of `r`, `req` contains all distinct values of `j` calculated during all iterations, and `j` includes all integers obtained during the loop iterations added to `req`.
    func_2('YES')
#Overall this is what the function does:The function `func_1` processes an integer list to check certain divisibility conditions involving a base `k`. It determines whether any calculated values from the input list, when reduced iteratively, have been seen before. If a duplicate is found, it calls `func_2` with 'NO' and exits; otherwise, after all iterations, it calls `func_2` with 'YES'. The function does not return any specific value.

#State of the program right berfore the function call: T is a positive integer (1 ≤ T ≤ 1000), n is a positive integer (1 ≤ n ≤ 30), k is an integer (2 ≤ k ≤ 100), and a is an array of n non-negative integers (0 ≤ a_i ≤ 10^{16}) for each test case.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `T` is a positive integer, `n` is a positive integer, `k` is an integer, `a` is an array of `n` non-negative integers, `sep` is ' ', `file` contains the string representations of all elements in `args` separated by spaces, `at_start` is False, and `args` contains all elements processed.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`T` is a positive integer, `n` is a positive integer, `k` is an integer, `a` is an array of `n` non-negative integers, `sep` is ' ', `file` has been modified by writing either `kwargs['end']` or `'\n'`, `at_start` is False, and `args` contains all elements processed. If the flush operation has been performed on `file`, then the corresponding changes are reflected in `file`.
#Overall this is what the function does:The function accepts multiple arguments (args) and keyword arguments (kwargs), and it prints the string representations of the elements in args to a specified output stream (file), separated by a specified separator (sep). It manages the formatting by handling leading separators and appending an end character (or a newline by default) after printing. The function does not return any value; instead, it performs output operations directly to the specified file. Additionally, if the flush option is enabled, it flushes the output stream. The functionality does not process the parameters T, n, k, or array a directly; these appear to be part of the context rather than influencing the current function directly.

