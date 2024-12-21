#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0) :
        return 2
        #The program returns the integer 2
    else :
        if (n == 1) :
            return 1
            #The program returns the integer 1
        else :
            a, b = 2, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
                
            #State of the program after the  for loop has been executed: `a` is `b` value at the end of all iterations, `b` is the $(n-1)$-th number in the sequence following `b` starts at 1 and the second number is 2.
            return b
            #The program returns the $(n-1)$-th number in the sequence following that starts at 1 and 2, where `b` is the $(n-1)$-th number in that sequence.
#Overall this is what the function does:The function accepts a non-negative integer parameter `n`. It returns 2 if `n` is 0, returns 1 if `n` is 1, and for values of `n` greater than 1, it returns the (n-1)-th Fibonacci number, where the sequence starts with 1 (the 0th Fibonacci number) and 2 (the 1st Fibonacci number). The function does not handle negative integers, which could potentially lead to misuse if such values are passed.

