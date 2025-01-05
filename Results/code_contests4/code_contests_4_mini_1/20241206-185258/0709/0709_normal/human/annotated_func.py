#State of the program right berfore the function call: r, g, and b are non-negative integers representing the number of red, green, and blue balloons respectively, with the constraint 0 ≤ r, g, b ≤ 2·10^9.
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
#Overall this is what the function does:The function accepts three non-negative integers `r`, `g`, and `b`, representing the number of red, green, and blue balloons respectively. It calculates a value `t` based on the number of red balloons and the number of green and blue balloons after adjusting for the number of red balloons. The function may call another function `func_2` with the computed value `t`. However, it does not return a value directly. The function also does not handle cases where the input is invalid or does not adhere to the specified constraints.

#State of the program right berfore the function call: r, g, and b are non-negative integers representing the number of red, green, and blue balloons respectively, with the constraint 0 ≤ r, g, b ≤ 2·10^9.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `r`, `g`, `b` are non-negative integers, `sep` is a space character, `file` is sys.stdout, `at_start` is False, `x` is written to `file` as a string for each element in `args`, and if `args` is empty, `at_start` remains True.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`r`, `g`, `b` are non-negative integers, `sep` is a space character, `file` is sys.stdout, `at_start` is False; if `kwargs.pop('flush', False)` is True, then `file.flush()` is executed. The value of `kwargs.pop('end', '\n')` is written to `file`, and `at_start` remains True if `args` is empty.
#Overall this is what the function does:The function accepts no parameters and prints values to a specified output stream. It does not evaluate the total number of balloons or return any message regarding the state of the balloons. It simply writes the provided arguments to the output with a specified separator and an optional ending character. If no arguments are provided, nothing is printed.

