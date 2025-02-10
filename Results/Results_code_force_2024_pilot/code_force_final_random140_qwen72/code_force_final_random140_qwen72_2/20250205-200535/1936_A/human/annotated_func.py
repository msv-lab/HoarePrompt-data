#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, and n is an integer where 2 <= n <= 10^4.
def func_1(a, b, c, d):
    print('?', a, b, c, d)
    #This is printed: ? [a] [b] [c] [d] (where [a], [b], [c], and [d] are non-negative integers such that 0 <= [a], [b], [c], [d] < n, and n is an integer where 2 <= n <= 10^4)
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `a`, `b`, `c`, and `d`, all of which are less than `n` (where 2 <= n <= 10^4). It prints a query string with these parameters and then returns the user's input as a string. The function does not modify the input parameters.

