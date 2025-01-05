#State of the program right berfore the function call: **
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function reads three integers `n`, `b`, and `c` from user input, calculates a value `x` based on the division of the maximum by the minimum of `b` and `c`, and then prints the result of a mathematical expression involving `n`, `b`, `c`, `x`. The function does not accept any parameters and does not return any output.

