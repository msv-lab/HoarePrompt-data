#State of the program right berfore the function call: **
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
        
    #State of the program after the  for loop has been executed: `n` and `k` are assigned values returned by `get_list()`, `li` is assigned the list returned by `get_list()` with at least 1 element, `req` contains all unique values of `j` encountered during the loop iterations, `r` is assigned the final value of `j`, `i` is 0, `j` is the maximum value that satisfies the loop condition and is not in `req`
    func_2('YES')
#Overall this is what the function does:The function func_1 does not accept any parameters. It iterates over a list of integers, performs certain calculations on each element, and updates variables accordingly. The function has multiple potential return cases based on different conditions, such as maintaining variables unchanged, updating and returning specific variables, performing calculations, and handling loops. The annotations provide insights into various return scenarios, but the actual code execution may not align with all the described cases. Therefore, the functionality includes iterating through the list, updating variables, and handling specific conditions, potentially with different return outcomes than described in the annotations.

#State of the program right berfore the function call: **
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `sep` is assigned the value extracted from `kwargs` or default value ' ', `file` is assigned the value extracted from `kwargs` or default value `sys.stdout`, `at_start` is False, `args` is a list with at least 1 element, `x` represents the last element in the list. If `at_start` is False, then the `sep` value is written to the `file` specified, and `x` is written to the `file`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`sep` is assigned the value extracted from `kwargs` or default value ' ', `file` is assigned the value extracted from `kwargs` or default value `sys.stdout`, `at_start` is False, `args` is a list with at least 1 element, `x` represents the last element in the list. If `at_start` is False and 'flush' key is True, then the `sep` value is written to the `file` specified, and `x` is written to the `file`.
#Overall this is what the function does:The function func_2 does not accept any parameters and iterates over elements in the `args` list, writing them to a specified `file` stream separated by the `sep` value. It then writes the value extracted from `kwargs` with the key 'end' or a newline character by default. If the key 'flush' is True in `kwargs`, the stream is flushed.

