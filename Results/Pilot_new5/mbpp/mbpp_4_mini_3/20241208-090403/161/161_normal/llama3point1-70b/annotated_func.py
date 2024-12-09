#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0) :
        return 2
        #The program returns the value 2.
    else :
        if (n == 1) :
            return 1
            #The program returns the value 1
        else :
            a, b = 2, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
                
            #State of the program after the  for loop has been executed: `n` is greater than 1, `a` is the Fibonacci number at position `n-1`, `b` is the Fibonacci number at position `n`.
            return b
            #The program returns the Fibonacci number at position n, which is represented by variable 'b'
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns 2 if `n` is 0, returns 1 if `n` is 1, and returns the Fibonacci number at position `n` for any other non-negative integer `n` greater than 1.

