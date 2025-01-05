#State of the program right berfore the function call: n is an integer such that 5 <= n <= 100.**
def func_1(n, a):
    r = 1
    s = 1
    p = n
    g = 1
    for i in range(a):
        r = r * p
        
        p -= 1
        
        s = s * g
        
        g += 1
        
    #State of the program after the  for loop has been executed: Output State: n is an integer such that 5 <= n <= 100, r is the factorial of n, s is n!, p is 0, g is n+1.
    return r / s
    #The program returns 1, as r is the factorial of n and s is n!, so r/s is equal to n!/n! which simplifies to 1
#Overall this is what the function does:The function func_1 accepts two parameters, n and a, where n is an integer satisfying 5 <= n <= 100. The function calculates the factorial of n and returns 1 by dividing the factorial of n by n!.

