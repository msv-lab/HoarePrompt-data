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
                
            #State of the program after the  for loop has been executed: `n` must be greater than or equal to 2, `a` is the (n-1)-th Fibonacci number, `b` is the (n)-th Fibonacci number.
            return b
            #The program returns the (n)-th Fibonacci number
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and returns either 2, 1, or the (n)-th Fibonacci number based on the value of `n`. Specifically:
- If `n` is 0, the function returns 2.
- If `n` is 1, the function returns 1.
- For any other non-negative integer `n`, the function calculates the (n)-th Fibonacci number using a loop and returns it.
Potential edge cases include:
- If `n` is less than 0, which is not handled by the code, the function would raise a `TypeError` when attempting to iterate in the loop. However, since `n` is specified to be a non-negative integer, this case is implicitly covered.
- The function correctly handles the base cases where `n` is 0 or 1, returning 2 and 1 respectively.
- For any `n` greater than 1, the function correctly computes the (n)-th Fibonacci number by iteratively updating two variables, `a` and `b`, until the desired Fibonacci number is reached.

