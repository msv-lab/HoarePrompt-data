#State of the program right berfore the function call: T is an integer between 1 and 1000, n is an integer between 1 and 30, k is an integer between 2 and 100, and a is a list of n integers where each integer is between 0 and 10^16.
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
        
    #State of the program after the  for loop has been executed: `i` is -1, `r` is the last computed value of `j`, `req` contains all unique values of `j` computed during the iterations.
    func_2('YES')
#Overall this is what the function does:The function accepts two integers `n` and `k`, and a list of integers `li` containing `n` elements. It processes each integer in `li` to compute a series of values based on the divisibility of the integer by powers of `k`, tracking unique results. If a duplicate value is found during the computation, the function calls `func_2` with 'NO' and terminates; otherwise, it calls `func_2` with 'YES' after processing all integers. The function does not return any specific value.

#State of the program right berfore the function call: T is a positive integer (1 ≤ T ≤ 1000) representing the number of test cases. For each test case, n is an integer (1 ≤ n ≤ 30) and k is an integer (2 ≤ k ≤ 100). The second line of each test case contains n integers a_i (0 ≤ a_i ≤ 10^16) representing the target array.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `T` is a positive integer (1 ≤ `T` ≤ 1000), `args` contains at least `n` elements, `at_start` is False, `sep` is written to the file between each element of `args` after the first element, the values of all elements in `args` are written to the file as strings.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`T` is a positive integer (1 ≤ `T` ≤ 1000), `args` contains at least `n` elements, `at_start` is False, `sep` is written to the file between each element of `args` after the first element, a value (either from `kwargs` or a newline) is written to the file. If the `flush` argument from `kwargs` is True, the file's internal buffer is flushed to ensure all data is written to the file.
#Overall this is what the function does:The function accepts a variable number of arguments and keyword arguments, writes the string representations of the arguments to a specified output stream separated by a defined separator (defaulting to a space), and appends an end character (defaulting to a newline) after the last argument. The function also has an option to flush the output stream if specified. However, the function does not handle the test cases or input constraints mentioned in the initial comments, as it lacks parameters for `T`, `n`, `k`, and the target array, making the comments misleading.

