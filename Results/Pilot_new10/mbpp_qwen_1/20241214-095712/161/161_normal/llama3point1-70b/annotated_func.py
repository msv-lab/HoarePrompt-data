#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0) :
        return 2
        #The program returns 2
    else :
        if (n == 1) :
            return 1
            #The program returns 1
        else :
            a, b = 2, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
                
            #State of the program after the  for loop has been executed: `a` is the (n+1)-th Fibonacci number, `b` is the (n+2)-th Fibonacci number, `n` must be a non-negative integer greater than or equal to 2.
            return b
            #The program returns b, which is the (n+2)-th Fibonacci number
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and returns 2 if `n` is 0, 1 if `n` is 1, and the (n+2)-th Fibonacci number if `n` is greater than or equal to 2.

