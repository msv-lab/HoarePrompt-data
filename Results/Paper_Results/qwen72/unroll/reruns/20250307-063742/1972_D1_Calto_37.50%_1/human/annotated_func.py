#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: a is the greatest common divisor (GCD) of the initial values of a and b, and b is 0.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of a and b, where b is 0.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b` and returns the greatest common divisor (GCD) of the initial values of `a` and `b`. After the function concludes, the variable `a` holds the GCD of the initial values of `a` and `b`, and `b` is 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: `n` and `m` remain the same, `cnt` is updated to `n` plus the sum of integer divisions of `n - i * (i - 1)` by `i * i` for `i` from 1 to `m-1`, plus the number of iterations where `i > 1`.
    if (cnt == 0) :
        return 1
        #The program returns 1.
    #State: `n` and `m` remain the same, `cnt` is updated to `n` plus the sum of integer divisions of `n - i * (i - 1)` by `i * i` for `i` from 1 to `m-1`, plus the number of iterations where `i > 1`. `cnt` is not equal to 0.
    return cnt
    #The program returns the updated value of `cnt`, which is `n` plus the sum of integer divisions of `n - i * (i - 1)` by `i * i` for `i` from 1 to `m-1`, plus the number of iterations where `i > 1`.
#Overall this is what the function does:The function `func_2` accepts two positive integers `n` and `m` (1 <= n, m <= 2 * 10^6). It calculates a value `cnt` based on a loop that iterates from 1 to `m-1`. For each iteration, it updates `cnt` by adding the integer division of `n - i * (i - 1)` by `i * i` and an additional 1 if `i > 1`. After the loop, if `cnt` is 0, the function returns 1. Otherwise, it returns the final value of `cnt`. The function does not modify the input parameters `n` and `m`.

