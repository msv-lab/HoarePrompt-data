#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^5, and for each i in range(n), S_i is one of the strings 'AC', 'WA', 'TLE', or 'RE'.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 10^5\), `s` is a list of `n` strings where each string is one of 'AC', 'WA', 'TLE', or 'RE', and `ac`, `wa`, `tle`, and `re` are updated as follows:
    #- `ac` is the count of 'AC' in `s`.
    #- `wa` is the count of 'WA' in `s`.
    #- `tle` is the count of 'TLE' in `s`.
    #- `re` is 1 if 'RE' appears at least once in `s`, otherwise, it is 0.
    func_2('AC x', ac)
    func_2('WA x', wa)
    func_2('TLE x', tle)
    func_2('RE x', re)
#Overall this is what the function does:The function `func_1` processes a list `S` of length `n` (where \(1 \leq n \leq 10^5\)), where each element in the list is one of the strings 'AC', 'WA', 'TLE', or 'RE'. It counts the occurrences of each string type and then calls the function `func_2` with specific messages and corresponding counts. After processing, the function updates four variables: `ac` (count of 'AC'), `wa` (count of 'WA'), `tle` (count of 'TLE'), and `re` (1 if 'RE' appears at least once, otherwise 0). The function does not return any value.

#State of the program right berfore the function call: args is a variable number of strings representing the verdicts for each test case, and file is a file object (defaulting to sys.stdout) where the output will be written to.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` is a variable number of strings, `sep` is a space, `file` is `sys.stdout`, all strings in `args` are concatenated with `sep` in between, `at_start` is `False`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` is a variable number of strings, `sep` is a space, `file` is `sys.stdout`, `at_start` is `False`, `kwargs` does not contain the key `'end'`, and the output buffer of `sys.stdout` has been flushed if the keyword argument `flush` is `True`. Otherwise, the state remains unchanged.
#Overall this is what the function does:The function `func_2` accepts a variable number of string arguments (`args`) and an optional keyword argument `file` (defaulting to `sys.stdout`). It writes these strings to the specified file, separated by a space (`sep`), and adds a newline character (`end`) at the end. If the `flush` keyword argument is set to `True`, it flushes the output buffer of `sys.stdout`. The final state of the program after the function executes is that all strings in `args` are concatenated with a space in between, written to `file`, and followed by a newline character unless explicitly overridden. If `flush` is `True`, the output buffer is flushed.

