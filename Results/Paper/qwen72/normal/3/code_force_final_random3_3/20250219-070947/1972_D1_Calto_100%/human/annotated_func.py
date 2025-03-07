#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: `a` is the greatest common divisor (GCD) of the initial values of `a` and `b`, and `b` is 0.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of `a` and `b`, where `b` is 0.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b` and returns the greatest common divisor (GCD) of the initial values of `a` and `b`. After the function concludes, `a` holds the GCD, and `b` is 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: `n` and `m` are positive integers such that 1 <= n, m <= 2 * 10^6, `i` is `m`, `cnt` is -1 + Σ(math.ceil((n - (i * i - i)) / (i * i)) + ((n - (i * i - i)) % (i * i) == 0)) for i from 1 to m.
    return cnt
    #The program returns the value of `cnt`, which is calculated as -1 plus the sum of (math.ceil((n - (i * i - i)) / (i * i)) + ((n - (i * i - i)) % (i * i) == 0)) for each `i` from 1 to `m`. Here, `n` and `m` are positive integers such that 1 <= n, m <= 2 * 10^6, and `i` is initialized to `m`.
#Overall this is what the function does:The function `func_2` accepts two positive integers `n` and `m` (1 <= n, m <= 2 * 10^6) and returns an integer `cnt`. The value of `cnt` is calculated as the sum of a specific expression for each integer `i` from 1 to `m`, minus 1. Specifically, for each `i`, the expression is `math.ceil((n - (i * i - i)) / (i * i)) + ((n - (i * i - i)) % (i * i) == 0)`. The final state of the program is that `cnt` holds this computed value, while `n` and `m` remain unchanged.

