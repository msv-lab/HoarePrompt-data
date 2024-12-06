#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0) :
        return 2
        #The program returns the integer 2
    else :
        if (n == 1) :
            return 1
            #The program returns the integer 1
        else :
            a, b = 2, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
                
            #State of the program after the  for loop has been executed: `n` is a positive integer greater than 1, `a` is the Fibonacci number F(n), `b` is the Fibonacci number F(n + 1).
            return b
            #The program returns the Fibonacci number F(n + 1), where n is a positive integer greater than 1 and a is the Fibonacci number F(n)
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns 2 if `n` is 0, returns 1 if `n` is 1, and returns the Fibonacci number F(n + 1) for any positive integer `n` greater than 1. If `n` is negative, the behavior of the function is not defined as it only handles non-negative integers; however, since `n` is stated to be a non-negative integer, this edge case is implicitly handled.

