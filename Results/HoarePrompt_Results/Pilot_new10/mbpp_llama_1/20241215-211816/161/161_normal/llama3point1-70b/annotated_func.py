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
                
            #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is the (n-1)th Fibonacci number, `b` is the nth Fibonacci number
            return b
            #The program returns the nth Fibonacci number
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns a value based on a modified Fibonacci-like sequence where the 0th term is 2, the 1st term is 1, and each subsequent term is the sum of the two preceding ones, thus returning 2 for `n = 0`, 1 for `n = 1`, and the `n`th term of this sequence for `n > 1`.

