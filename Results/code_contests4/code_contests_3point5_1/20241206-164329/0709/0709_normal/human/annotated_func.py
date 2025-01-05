#State of the program right berfore the function call: r, g, and b are non-negative integers.**
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
#Overall this is what the function does:The function `func_1` internally processes three non-negative integers `r`, `g`, and `b`. It sorts these integers and performs a series of calculations on them to determine a final value `t`. The function then calls another function `func_2` with the calculated value `t`. However, the annotations do not provide a clear insight into the exact purpose or outcome of these calculations. It seems to involve manipulation of the input values `r`, `g`, and `b` to generate the final value `t`, but the exact logic and purpose of this transformation remain ambiguous due to the lack of detailed explanation in the annotations.

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
        
    #State of the program after the  for loop has been executed: `at_start` is False, `args` is an empty iterable, `x` is None
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`at_start` is False, `args` is an empty iterable, `x` is None. If kwargs.pop('flush', False) returns True, the program modifies the state of the variables. Otherwise, there is no change in the state of the variables.
#Overall this is what the function does:The function `func_2` operates on three non-negative integers `r`, `g`, and `b` such that 0 ≤ r, g, b ≤ 2·10^9. It does not accept any parameters and performs some operations or calculations with these integers. The function then prints the results to a stream or `sys.stdout` by default. The function handles the formatting of the output by using the provided `sep`, `file`, `end`, and `flush` keyword arguments. The state of the program after execution involves the modification of variables based on these arguments.

