#State of the program right berfore the function call: r, g, and b are non-negative integers representing the number of red, green, and blue balloons respectively, where 0 ≤ r, g, b ≤ 2·10^9.
def func_1():
    r, g, b = sorted(map(int, input().split()))
    t = r
    g -= r
    b -= r
    t += g // 3
    b -= g - g % 3
    g = g % 3
    t += (g == 1 and b > 1) + (g == 2 and b > 0)
    func_2(t)
#Overall this is what the function does:The function accepts three non-negative integer parameters representing quantities of red, green, and blue balloons, respectively. It calculates a value `t` based on the number of balloons that can be formed from the available colors, taking into account the minimum of the three counts and how many full sets of three can be made from the green balloons. The function then calls another function `func_2` with this calculated value `t`. The function does not return any value.

#State of the program right berfore the function call: r, g, and b are non-negative integers representing the number of red, green, and blue balloons respectively, where 0 ≤ r, g, b ≤ 2·10^9.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `r`, `g`, `b` are non-negative integers; `sep` is ' '; `file` has written the string representations of all elements in `args` separated by `sep`; `at_start` is False; `args` is a non-empty iterable; and all elements of `args` have been written to the output.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`r`, `g`, `b` are non-negative integers; `sep` is ' '; `file` has written the string representations of all elements in `args` separated by `sep`; `at_start` is False; `args` is a non-empty iterable; all elements of `args` have been written to the output; the string represented by `kwargs.pop('end', '\n')` has been written to `file`. If `kwargs.pop('flush', False)` is True, the file has been flushed.
#Overall this is what the function does:The function accepts three parameters `r`, `g`, and `b`, which are non-negative integers representing the counts of red, green, and blue balloons respectively. It prints the string representations of all elements in the iterable `args`, separated by a specified separator `sep`, and followed by a specified ending string from `kwargs`. If specified, it also flushes the output stream. However, the function does not utilize the parameters `r`, `g`, and `b` in its operation, thus they are irrelevant within this context.

