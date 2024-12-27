#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^5, and s is a list of strings where each string S_i is either 'AC', 'WA', 'TLE', or 'RE'.
def func_1():
    n = int(input())
    s = [input() for _ in range(n)]
    ac = 0
    wa = 0
    tle = 0
    re = 0
    for i in s:
        if i == 'AC':
            ac += 1
        elif i == 'WA':
            wa += 1
        elif i == 'TLE':
            tle += 1
        elif i == 'RE':
            re += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 10^5\), `s` is a list of `n` strings where each string is either 'AC', 'WA', 'TLE', or 'RE', `ac` is the total count of 'AC' in the list `s`, `wa` is the total count of 'WA' in the list `s`, `tle` is the total count of 'TLE' in the list `s`, `re` is the total count of 'RE' in the list `s`.
    func_2('AC x', ac)
    func_2('WA x', wa)
    func_2('TLE x', tle)
    func_2('RE x', re)
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a list `s` of length `n` containing strings that are either 'AC', 'WA', 'TLE', or 'RE'. It counts the occurrences of each outcome ('AC', 'WA', 'TLE', 'RE') and calls the function `func_2` four times to print these counts in the format "Outcome x Count". The function does not return any value. Potential edge cases include the input `n` being less than 1 or greater than \(10^5\), and the list `s` containing only one of the specified outcomes or an empty list. However, the provided code does not handle these edge cases explicitly.

#State of the program right berfore the function call: args is a variable-length argument list containing strings, and kwargs is a dictionary that can contain 'sep', 'file', 'end', and 'flush' keys with specific types and purposes as described in the docstring of the function.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` is a variable-length argument list containing strings, `at_start` is `False`, `file` has written the concatenation of `str(x)` for each `x` in `args` separated by `sep`, unless `at_start` was `True` initially, in which case no leading `sep` is written.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` is a variable-length argument list containing strings, `at_start` is `False`, `file` has written the concatenation of `str(x)` for each `x` in `args` separated by `sep` followed by `\n`, unless `at_start` was `True` initially, in which case no leading `sep` is written, and the file buffer is flushed.
#Overall this is what the function does:The function `func_2` accepts a variable-length argument list `args` containing strings and a dictionary `kwargs` that can optionally contain 'sep', 'file', 'end', and 'flush' keys. It prints the contents of `args` to a specified output stream (`file`), using the provided separator (`sep`), end character (`end`), and flushes the output buffer if requested (`flush`). If `file` is not specified, it defaults to `sys.stdout`. The function ensures that the output is properly formatted based on the provided arguments. Potential edge cases include when `args` is empty, `sep` is not provided, `file` is not provided, `end` is not provided, and `flush` is not provided. If `args` is empty, nothing is printed. If `sep` is not provided, the default separator is a single space. If `file` is not provided, the output is directed to `sys.stdout`. If `end` is not provided, the default end character is a newline. If `flush` is not provided, the output buffer is not flushed.

