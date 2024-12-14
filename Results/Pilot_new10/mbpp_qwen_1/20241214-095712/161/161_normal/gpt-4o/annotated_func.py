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
                
            #State of the program after the  for loop has been executed: `n` must be greater than or equal to 2, `a` is the nth Fibonacci number where the first Fibonacci number is 1 and the second is 2, `b` is the (n-1)th Fibonacci number where the first Fibonacci number is 1 and the second is 2.
            return b
            #`b`, which is the (n-1)th Fibonacci number where the first Fibonacci number is 1 and the second is 2
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and returns 2 if `n` is 0, 1 if `n` is 1, and the (n-1)th Fibonacci number (where the first Fibonacci number is 1 and the second is 2) for any other non-negative integer `n`.

