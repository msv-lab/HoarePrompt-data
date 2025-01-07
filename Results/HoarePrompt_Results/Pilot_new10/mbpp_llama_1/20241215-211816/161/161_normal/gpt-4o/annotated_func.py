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
                
            #State of the program after the  for loop has been executed: `n` is a non-negative integer larger than 1, `a` is the (n-1)th Fibonacci-like number in a sequence starting with 2 and 1, `b` is the nth Fibonacci-like number in a sequence starting with 2 and 1.
            return b
            #The program returns the nth Fibonacci-like number in a sequence starting with 2 and 1, where n is a non-negative integer larger than 1.
#Overall this is what the function does:The function accepts a non-negative integer `n` and returns the nth Fibonacci-like number in a sequence starting with 2 and 1, where `n` equals 0 returns 2, `n` equals 1 returns 1, and for `n` larger than 1, it returns the nth number in the sequence

