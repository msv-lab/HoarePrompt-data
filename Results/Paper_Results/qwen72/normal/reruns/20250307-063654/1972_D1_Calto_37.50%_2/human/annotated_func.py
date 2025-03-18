#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: `a` is the greatest common divisor (GCD) of the initial values of `a` and `b`, and `b` is 0; `a` and `b` are still positive integers such that 1 <= `a` <= `n` and 0 <= `b` <= `m`.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of `a` and `b`, where `a` is a positive integer such that 1 <= `a` <= `n` and `b` is 0. Since the GCD of any positive integer `a` and 0 is `a` itself, the program returns `a`.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b` with constraints 1 <= `a` <= `n` and 1 <= `b` <= `m`. It returns the greatest common divisor (GCD) of the initial values of `a` and `b`. After the function concludes, `a` holds the GCD of the initial `a` and `b`, and `b` is 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: `n` and `m` are positive integers such that 1 <= n, m <= 2 * 10^6, `cnt` is `n` + (m - 1) + sum((n - (i * i - i)) // (i * i) for i in range(1, m - 1)), `i` is `m - 1`, `m` is greater than or equal to `m`, `x` is `n` - ((m - 1) * (m - 2)), `y` is (m - 1) * (m - 1).
    if (cnt == 0) :
        return 1
        #The program returns 1.
    #State: `n` and `m` are positive integers such that 1 <= n, m <= 2 * 10^6, `cnt` is `n` + (m - 1) + sum((n - (i * i - i)) // (i * i) for i in range(1, m - 1)), `i` is `m - 1`, `m` is greater than or equal to `m`, `x` is `n` - ((m - 1) * (m - 2)), `y` is (m - 1) * (m - 1), and `cnt` is not equal to 0.
    return cnt
    #The program returns the value of `cnt`, which is calculated as `n` + (m - 1) + sum((n - (i * i - i)) // (i * i) for i in range(1, m - 1)), where `n` and `m` are positive integers such that 1 <= n, m <= 2 * 10^6, and `cnt` is not equal to 0.
#Overall this is what the function does:The function `func_2` accepts two positive integers `n` and `m` (1 <= n, m <= 2 * 10^6). It calculates a value `cnt` based on a series of integer divisions and additions. If `cnt` is 0, the function returns 1. Otherwise, it returns the value of `cnt`, which is the sum of `n`, `m - 1`, and a series of integer divisions derived from a formula involving `n` and `m`.

