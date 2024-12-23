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
                
            #State of the program after the  for loop has been executed: `n` is greater than 5, `a` is the 6th Fibonacci number starting from index 2, `b` is the 7th Fibonacci number starting from index 2
            return b
            #The program returns the 7th Fibonacci number starting from index 2
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and returns either 2, 1, or the 7th Fibonacci number starting from index 2 based on the value of `n`. Specifically:
- If `n` is 0, the function returns 2.
- If `n` is 1, the function returns 1.
- For any other value of `n`, the function computes the Fibonacci sequence up to the `n+1`-th term and returns the 7th Fibonacci number in the sequence (starting from index 2).

This covers all possible inputs for `n` and ensures that the function behaves as specified in the return postconditions.

