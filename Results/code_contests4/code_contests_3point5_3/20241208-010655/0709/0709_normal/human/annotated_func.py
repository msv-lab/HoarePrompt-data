#State of the program right berfore the function call: r, g, and b are non-negative integers such that 0 ≤ r, g, b ≤ 2·10^9.**
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
#Overall this is what the function does:The function `func_1` reads three non-negative integers `r`, `g`, and `b` from input, sorts them, and performs a series of calculations based on these values. It then calls another function `func_2` with the calculated value `t`. The function `func_1` does not accept any parameters and does not have a return value.

#State of the program right berfore the function call: r, g, and b are non-negative integers such that 0 ≤ r, g, b ≤ 2·10^9.**
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `r`, `g`, and `b` are non-negative integers such that 0 ≤ r, g, b ≤ 2·10^9. `at_start` is False. All elements in the list `args` have been written to the file as strings separated by the value of `sep`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`r`, `g`, and `b` are non-negative integers such that 0 ≤ r, g, b ≤ 2·10^9. `at_start` is False. All elements in the list `args` have been written to the file as strings separated by the value of `sep`. The 'flush' operation has been performed.
#Overall this is what the function does:The function func_2 does not accept any parameters. It iterates over the elements in the list `args`, converts them to strings, and writes them to the output file separated by the value of `sep`. It then writes the value specified by the keyword argument 'end' to the file. If the keyword argument 'flush' is True, it flushes the stream. The function does not calculate or return the maximum possible number of different colors that can be obtained by mixing red, green, and blue colors.

