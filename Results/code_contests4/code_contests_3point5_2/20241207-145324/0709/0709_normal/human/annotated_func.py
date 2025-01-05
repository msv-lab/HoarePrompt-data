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
#Overall this is what the function does:The function `func_1` reads three non-negative integers `r`, `g`, and `b` from input, sorts them, and performs calculations based on these values. However, the function calls another function `func_2` with a calculated parameter `t` as an argument. The function `func_1` does not explicitly return any value.

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
        
    #State of the program after the  for loop has been executed: at_start is False, file has been written with the string representation of all elements in args
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *at_start is False. The file has been written with the string representation of all elements in args. If the 'end' key is present in kwargs and the value is True, then it is popped. Otherwise, no changes occur.
#Overall this is what the function does:The function `func_2` does not accept any parameters and operates without any input values. It iterates over the elements in `args`, writes their string representations to the output file defined by `kwargs`, and separates them by the specified separator. If provided, it writes the specified end value at the end. If the `flush` key is set to True in `kwargs`, it flushes the output file. The function does not return any specific value.

