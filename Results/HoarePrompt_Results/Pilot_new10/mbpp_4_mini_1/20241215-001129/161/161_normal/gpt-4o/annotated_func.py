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
                
            #State of the program after the  for loop has been executed: `n` is a non-negative integer greater than 0 and not equal to 1, `a` is the (n-1)-th Fibonacci number starting from (2, 1), `b` is the n-th Fibonacci number starting from (2, 1).
            return b
            #The program returns the n-th Fibonacci number 'b' starting from the sequence (2, 1), where n is a non-negative integer greater than 0 and not equal to 1.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns 2 if `n` is 0, 1 if `n` is 1, and the n-th Fibonacci number starting from the sequence (2, 1) for `n` greater than 1. The Fibonacci sequence generated begins with 2 and 1 instead of the typical 0 and 1.

