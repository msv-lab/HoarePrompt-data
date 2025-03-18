#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: a is the greatest common divisor (GCD) of the initial values of a and b, and b is 0.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of a and b, where b is 0.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b` and returns the greatest common divisor (GCD) of the initial values of `a` and `b`. After the function concludes, the value of `b` is 0, and `a` holds the GCD of the initial inputs.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: `cnt` is the sum of `x // y` for each `i` from 1 to `m-1`, plus the number of iterations where `i > 1`.
    if (cnt == 0) :
        return 1
        #The program returns 1.
    #State: *`cnt` is the sum of `x // y` for each `i` from 1 to `m-1`, plus the number of iterations where `i > 1`, and `cnt` is not equal to 0
    return cnt
    #The program returns the value of `cnt`, which is the sum of `x // y` for each `i` from 1 to `m-1`, plus the number of iterations where `i > 1`, and `cnt` is not equal to 0.
#Overall this is what the function does:The function `func_2` accepts two positive integers `n` and `m` (1 <= n, m <= 2 * 10^6). It calculates a value `cnt` which is the sum of `x // y` for each `i` from 1 to `m-1`, where `x = n - (i * i - i)` and `y = i * i`, plus the number of iterations where `i > 1`. If `cnt` is 0, the function returns 1. Otherwise, it returns the value of `cnt`.

