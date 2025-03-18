#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0) :
        return 2
        #The program returns the value 2
    else :
        if (n == 1) :
            return 1
            #The program returns the value 1
        else :
            a, b = 2, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
                
            #State of the program after the  for loop has been executed: `n` is greater than or equal to 2, `a` is the (n-1)th Fibonacci number, `b` is the nth Fibonacci number.
            return b
            #The program returns the nth Fibonacci number 'b', where 'b' is defined as the nth Fibonacci number and 'n' is greater than or equal to 2.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns different values based on its input: it returns 2 if `n` is 0, 1 if `n` is 1, and the nth Fibonacci number if `n` is 2 or greater.

