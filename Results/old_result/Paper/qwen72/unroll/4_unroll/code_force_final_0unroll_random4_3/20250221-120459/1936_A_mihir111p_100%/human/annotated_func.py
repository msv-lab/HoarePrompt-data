#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, and n is an integer where 2 <= n <= 10^4.
def func_1(a, b, c, d):
    print('?', a, b, c, d)
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, and n is an integer where 2 <= n <= 10^4)
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `a`, `b`, `c`, and `d`, each less than `n` where `2 <= n <= 10^4`. It prints a query string in the format `? [a] [b] [c] [d]` and then returns the user's input as a string. After the function concludes, the user's input is available as the return value, and the original parameters `a`, `b`, `c`, and `d` remain unchanged.

