#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, and n is a positive integer such that 2 <= n <= 10^4.
def func_1(a, b, c, d):
    print('?', a, b, c, d)
    #This is printed: ? a b c d
    return input()
    #The program returns an input value provided by the user
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters \(a\), \(b\), \(c\), and \(d\), all less than \(n\), where \(n\) is a positive integer between 2 and 10,000. It prints these parameters and then waits for the user to provide an input, which it subsequently returns.

