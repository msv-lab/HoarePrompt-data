#State of the program right berfore the function call: r, g, and b are non-negative integers representing the number of red, green, and blue balloons, respectively, such that 0 ≤ r, g, b ≤ 2·10^9.
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
#Overall this is what the function does:The function accepts no parameters and reads three non-negative integers from input, representing the counts of red, green, and blue balloons. It then performs calculations to determine a value based on the relationships between these counts. The function ultimately calls another function, `func_2`, passing the calculated value, but does not return any value itself. It does not handle cases where the input values are outside the specified range or where inputs are invalid, such as non-integer values.

#State of the program right berfore the function call: r, g, and b are non-negative integers where 0 ≤ r, g, b ≤ 2·10^9.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `r`, `g`, `b` are non-negative integers; `file` contains all elements of `args` written as strings, separated by `sep` if there are multiple elements; `at_start` is False.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`r`, `g`, `b` are non-negative integers; `file` has written the value of `kwargs.pop('end', '\n')`; `at_start` is False. If `kwargs.pop('flush', False)` is True, then the file has been flushed.
#Overall this is what the function does:The function does not accept any explicit parameters and prints the string representations of elements from an unspecified iterable `args` to a specified output stream, `file`. It separates the elements with a specified separator `sep` and ends the output with a specified ending string `end`. If the `flush` keyword argument is set to True, it flushes the output stream. The function relies on the presence of `args` and `kwargs`, which are not defined within the function, suggesting that it is intended to be called with these arguments in a broader context or is part of a larger system, such as a print-like function.

