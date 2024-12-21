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
                
            #State of the program after the  for loop has been executed: `n` is a non-negative integer and not equal to 0, and `n` is not equal to 1; `a` is the \((n+1)\)-th term of the Fibonacci sequence starting from 2 and 1; `b` is the \(n\)-th term of the same Fibonacci sequence; `i` is `n`.
            return b
            #`The program returns b, which is the n-th term of the Fibonacci sequence starting from 2 and 1`
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and returns either 2, 1, or the n-th term of a specific Fibonacci sequence starting from 2 and 1. Specifically:
- If `n` is 0, the function returns 2.
- If `n` is 1, the function returns 1.
- For any other non-negative integer `n`, the function computes the n-th term of the Fibonacci sequence where the sequence starts with 2 and 1, and returns this value.

The function correctly handles the base cases (`n = 0` and `n = 1`) and uses a loop to compute the Fibonacci sequence for larger values of `n`. After the loop completes, the function returns the correct n-th term of the specified Fibonacci sequence.

