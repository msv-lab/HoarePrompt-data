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
                
            #State of the program after the  for loop has been executed: `n` is a positive integer and `n` is not equal to 1, `a` is the `(n-1)`th number in the Fibonacci-like sequence starting with 2 and 1, `b` is the `n`th number in the Fibonacci-like sequence starting with 2 and 1.
            return b
            #The program returns the nth number in a Fibonacci-like sequence that starts with 2 and 1.
#Overall this is what the function does:The function accepts a non-negative integer `n` as input and returns a value based on the following conditions: if `n` is 0, it returns 2; if `n` is 1, it returns 1; for any other positive integer `n`, it calculates and returns the `n`th number in a Fibonacci-like sequence that starts with 2 and 1, where each subsequent number is the sum of the two preceding ones. This covers all potential cases, including edge cases where `n` is 0 or 1, and ensures that the function behaves consistently for all non-negative integers.

