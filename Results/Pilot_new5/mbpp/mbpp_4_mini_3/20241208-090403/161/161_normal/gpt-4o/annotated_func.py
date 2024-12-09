#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0) :
        return 2
        #The program returns the integer 2
    else :
        if (n == 1) :
            return 1
            #The program returns 1
        else :
            a, b = 2, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
                
            #State of the program after the  for loop has been executed: `a` is the value of `b` after `n - 1` iterations, `b` is the sum of the last two values of `a` and `b`, and `n` is greater than or equal to 2.
            return b
            #The program returns b, which is the sum of the last two values of a and b, with a being the value of b after n - 1 iterations, and n being greater than or equal to 2.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns 2 if `n` is 0, returns 1 if `n` is 1, and returns the `n`th Fibonacci number for `n >= 2`.

