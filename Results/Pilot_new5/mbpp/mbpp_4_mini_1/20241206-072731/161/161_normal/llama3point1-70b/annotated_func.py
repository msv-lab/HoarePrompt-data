#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0) :
        return 2
        #The program returns the integer value 2
    else :
        if (n == 1) :
            return 1
            #The program returns the value 1
        else :
            a, b = 2, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
                
            #State of the program after the  for loop has been executed: `a` is the (n-1)th Fibonacci number, `b` is the nth Fibonacci number, `n` is a non-negative integer greater than 0 and not equal to 1.
            return b
            #The program returns the nth Fibonacci number, where 'b' is the nth Fibonacci number and 'n' is a non-negative integer greater than 0 and not equal to 1.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns 2 if `n` is 0, 1 if `n` is 1, and the nth Fibonacci number for all other positive values of `n` greater than 1.

