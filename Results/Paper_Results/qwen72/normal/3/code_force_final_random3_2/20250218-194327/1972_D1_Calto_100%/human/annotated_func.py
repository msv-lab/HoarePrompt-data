#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: The loop terminates when `b` becomes 0, and `a` holds the greatest common divisor (GCD) of the initial values of `a` and `b`, with `1 <= a <= n` still holding true.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of `a` and `b`, where `1 <= a <= n` is still true.
#Overall this is what the function does:The function `func_1` accepts two parameters `a` and `b`, both of which are positive integers within the ranges `1 <= a <= n` and `1 <= b <= m`. It returns the greatest common divisor (GCD) of the initial values of `a` and `b`. After the function concludes, `a` holds the GCD of the initial values of `a` and `b`, and `b` is 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: `n` and `m` are positive integers such that 1 <= n, m <= 2 * 10^6, `cnt` is the sum of `math.ceil((n - (i * i - i)) / (i * i)) + ((n - (i * i - i)) % (i * i) == 0)` for all `i` from 1 to `m`, `i` is `m`, `x` is `n - (m * m - m)`, `y` is `m * m`.
    return cnt
    #The program returns the sum of `math.ceil((n - (i * i - i)) / (i * i)) + ((n - (i * i - i)) % (i * i) == 0)` for all `i` from 1 to `m`.
#Overall this is what the function does:The function `func_2` accepts two positive integers `n` and `m` (where 1 <= n, m <= 2 * 10^6) and returns an integer `cnt`. The value of `cnt` is the sum of a series of calculations performed for each integer `i` from 1 to `m`. For each `i`, the calculation is the ceiling of the division of `(n - (i * i - i))` by `(i * i)`, plus 1 if the remainder of this division is 0. After the function concludes, `cnt` holds the final result of these calculations, and the input variables `n` and `m` remain unchanged.

