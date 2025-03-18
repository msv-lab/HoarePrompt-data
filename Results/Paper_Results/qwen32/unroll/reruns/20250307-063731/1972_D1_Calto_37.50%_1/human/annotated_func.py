#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: a is the greatest common divisor of the original a and b, and b is 0.
    return a
    #The program returns a, which is the greatest common divisor of the original a and b, and b is 0.
#Overall this is what the function does:The function accepts two positive integer parameters `a` and `b` and returns their greatest common divisor.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: `cnt` is `n + m - 2`.
    if (cnt == 0) :
        return 1
        #The program returns 1
    #State: `cnt` is `n + m - 2`, and `cnt` is not equal to 0
    return cnt
    #The program returns the value of `cnt` which is `n + m - 2` and is not equal to 0.
#Overall this is what the function does:The function `func_2` takes two positive integer parameters `n` and `m`. It performs a series of calculations and returns either 1 if the computed value `cnt` is 0, or the value of `cnt` itself if it is not 0. The value of `cnt` is ultimately `n + m - 2` unless it evaluates to 0, in which case the function returns 1.

