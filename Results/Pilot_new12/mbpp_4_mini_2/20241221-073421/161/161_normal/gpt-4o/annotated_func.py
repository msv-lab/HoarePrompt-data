#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0) :
        return 2
        #The program returns the constant value 2.
    else :
        if (n == 1) :
            return 1
            #The program returns 1
        else :
            a, b = 2, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
                
            #State of the program after the  for loop has been executed: `a` is the (n-1)th Fibonacci-like number, `b` is the nth Fibonacci-like number with base cases a_1=2, b_1=1 for n ≥ 2.
            return b
            #The program returns the nth Fibonacci-like number 'b', where base cases are a_1=2, b_1=1 for n ≥ 2.
#Overall this is what the function does:The function accepts a non-negative integer `n` and behaves as follows: it returns 2 if `n` is 0, returns 1 if `n` is 1, and for `n ≥ 2`, it calculates and returns the `n`-th term of a Fibonacci-like sequence where the base cases are defined as `a_1=2` and `b_1=1`. The sequence follows the rule that each subsequent number is the sum of the two preceding numbers. The function efficiently computes the result using iterative calculations. There are no checks for negative values of `n`, but since the problem states `n` is a non-negative integer, that case does not need to be covered.

