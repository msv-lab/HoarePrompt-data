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
                
            #State of the program after the  for loop has been executed: `a` is the (n-1)th term of the sequence starting with 2 and 1, `b` is the nth term of the sequence starting with 2 and 1, `n` is a non-negative integer greater than 1.
            return b
            #The program returns the nth term 'b' of the sequence starting with 2 and 1, where 'a' is the (n-1)th term and 'n' is a non-negative integer greater than 1.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns 2 if `n` is 0, returns 1 if `n` is 1, and for `n` greater than 1, it returns the nth term of a Fibonacci-like sequence starting with 2 and 1. The sequence is defined such that each term is the sum of the two preceding terms.

