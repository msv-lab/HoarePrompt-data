#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0) :
        return 2
        #The program returns the value 2
    else :
        if (n == 1) :
            return 1
            #The program returns 1, where n is a non-negative integer greater than 0 and its current value is equal to 1.
        else :
            a, b = 2, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
                
            #State of the program after the  for loop has been executed: `n` is greater than 1, `a` is the (n-1)-th Fibonacci number, `b` is the n-th Fibonacci number.
            return b
            #The program returns the n-th Fibonacci number which is represented by variable 'b'
#Overall this is what the function does:The function accepts a non-negative integer `n`. It returns 2 if `n` is 0, returns 1 if `n` is 1, and calculates the n-th Fibonacci number for `n` greater than 1, represented by the variable `b`. The function does not account for negative integers, as it assumes `n` is non-negative, and correctly handles the Fibonacci series for valid non-negative integers. Therefore, for valid inputs, it either returns a predefined value or computes the desired Fibonacci number.

