#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: `a` is the greatest common divisor (GCD) of the initial values of `a` and `b`, and `b` is 0.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of `a` and `b`, where `b` is 0.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b` and returns the greatest common divisor (GCD) of the initial values of `a` and `b`. After the function concludes, `a` holds the GCD of the initial `a` and `b`, and `b` is 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: `n` and `m` are positive integers such that 1 <= n, m <= 2 * 10^6, `i` is `m`, `cnt` is `sum(math.ceil((n - (j * j - j)) / (j * j)) + ((n - (j * j - j)) % (j * j) == 0) for j in range(1, m + 1)) - 1`, `x` is `n - (m * m - m)`, `y` is `m * m`.
    return cnt
    #The program returns the value of `cnt`, which is calculated as the sum of `math.ceil((n - (j * j - j)) / (j * j)) + ((n - (j * j - j)) % (j * j) == 0)` for each `j` in the range from 1 to `m` (inclusive), minus 1.
#Overall this is what the function does:The function `func_2` accepts two positive integers `n` and `m` (where 1 <= n, m <= 2 * 10^6) and returns an integer `cnt`. The value of `cnt` is the sum of `math.ceil((n - (j * j - j)) / (j * j)) + ((n - (j * j - j)) % (j * j) == 0)` for each `j` from 1 to `m` (inclusive), minus 1. The function does not modify the input parameters `n` and `m`. After the function concludes, the final state includes the return value `cnt` and the input parameters `n` and `m` remain unchanged.

