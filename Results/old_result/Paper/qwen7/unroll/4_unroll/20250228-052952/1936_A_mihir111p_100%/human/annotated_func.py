#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 ≤ a, b, c, d < n, and n is a positive integer (2 ≤ n ≤ 10^4).
def func_1(a, b, c, d):
    print('?', a, b, c, d)
    #This is printed: ? a b c d (where a, b, c, and d are non-negative integers in the range 0 to n-1)
    return input()
    #The program returns an input value provided by the user
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `a`, `b`, `c`, and `d`, each less than `n` (where `2 ≤ n ≤ 10^4`). It prints these parameters and then waits for user input, returning that input value.

