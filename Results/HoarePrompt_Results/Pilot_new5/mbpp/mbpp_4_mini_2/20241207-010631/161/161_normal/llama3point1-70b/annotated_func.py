#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0) :
        return 2
        #The program returns the integer value 2
    else :
        if (n == 1) :
            return 1
            #The program returns 1
        else :
            a, b = 2, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
                
            #State of the program after the  for loop has been executed: `n` is greater than or equal to 2, `a` is the (n-1)th value of the sequence defined by the loop, `b` is the nth value of the sequence defined by the loop.
            return b
            #The program returns b, which is the nth value of the sequence defined by the loop, where n is greater than or equal to 2.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns 2 if `n` is 0, 1 if `n` is 1, and the nth Fibonacci number if `n` is greater than or equal to 2.

