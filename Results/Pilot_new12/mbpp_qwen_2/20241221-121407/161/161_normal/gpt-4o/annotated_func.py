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
                
            #State of the program after the  for loop has been executed: `n` is a non-negative integer and \( n \neq 0 \) and \( n \neq 1 \); `a` is the \( n \)-th Fibonacci number; `b` is the \( (n+1) \)-th Fibonacci number.
            return b
            #The program returns the (n+1)-th Fibonacci number
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` as a parameter and returns either 2, 1, or the \((n+1)\)-th Fibonacci number based on the value of `n`. Specifically:
- If `n` is 0, the function returns 2.
- If `n` is 1, the function returns 1.
- For any other non-negative integer `n`, the function computes the \((n+1)\)-th Fibonacci number using a loop and returns it.

