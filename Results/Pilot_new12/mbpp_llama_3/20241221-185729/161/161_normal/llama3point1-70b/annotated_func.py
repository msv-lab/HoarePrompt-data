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
                
            #State of the program after the  for loop has been executed: `n` is a positive integer greater than 1, `a` is the (n-1)th number in the Fibonacci sequence starting with 2 and 1, `b` is the nth number in the Fibonacci sequence starting with 2 and 1.
            return b
            #The program returns the nth number in the Fibonacci sequence starting with 2 and 1, where n is a positive integer greater than 1.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns a value based on the value of `n`. If `n` is 0, the function returns 2. If `n` is 1, the function returns 1. For any other positive integer `n` greater than 1, the function returns the nth number in the Fibonacci sequence starting with 2 and 1. The function covers all non-negative integer cases for `n` and does not modify the input variable `n`. The final state of the program after it concludes is that it returns a specific integer value determined by the input `n`, without altering the original input.

