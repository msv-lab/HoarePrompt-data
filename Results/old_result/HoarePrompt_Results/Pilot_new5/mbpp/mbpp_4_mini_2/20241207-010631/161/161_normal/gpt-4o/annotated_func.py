#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0) :
        return 2
        #The program returns the integer 2
    else :
        if (n == 1) :
            return 1
            #The program returns 1, which is the current value of n
        else :
            a, b = 2, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
                
            #State of the program after the  for loop has been executed: `n` is a non-negative integer greater than 1, `a` is the (n-1)-th Fibonacci number starting from 1, `b` is the n-th Fibonacci number starting from 1.
            return b
            #The program returns b, which is the n-th Fibonacci number starting from 1, where n is a non-negative integer greater than 1.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns 2 if `n` is 0, returns 1 if `n` is 1, and returns the n-th Fibonacci number starting from 1 for all other values of `n` greater than 1. It does not handle negative integers and assumes the input is always a non-negative integer.

