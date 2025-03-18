#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 ≤ a, b, c, d < n, and n is a positive integer (2 ≤ n ≤ 10^4).
def func_1(a, b, c, d):
    print('?', a, b, c, d)
    #This is printed: '? a b c d' (where a, b, c, and d are non-negative integers such that 0 ≤ a, b, c, d < n, and n is a positive integer (2 ≤ n ≤ 10^4))
    return input()
    #The program returns an input value from the user, as the return statement is calling for user input but no specific value is provided in the initial state.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `a`, `b`, `c`, and `d`. It prints these values and then waits for the user to input a value, which it returns.

