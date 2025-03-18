#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: `a` is the GCD of the original `a` and `b`; `b` is 0.
    return a
    #The program returns the GCD of the original `a` and `b`. Since `b` is 0, the GCD is the value of `a`.
#Overall this is what the function does:The function accepts two positive integer parameters `a` and `b` and returns their greatest common divisor (GCD).

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: `n` and `m` are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6; `cnt` is the sum of `math.ceil((n - (i * i - i)) / (i * i)) + ((n - (i * i - i)) % (i * i) == 0)` for all `i` from 1 to `m`; `x` is `n - (m * m - m)`; `y` is `m * m`.
    return cnt
    #The program returns `cnt`, which is the sum of `math.ceil((n - (i * i - i)) / (i * i)) + ((n - (i * i - i)) % (i * i) == 0)` for all `i` from 1 to `m`
#Overall this is what the function does:The function `func_2` takes two positive integer parameters, `n` and `m`, and returns the sum of `math.ceil((n - (i * i - i)) / (i * i)) + ((n - (i * i - i)) % (i * i) == 0)` for all `i` from 1 to `m`.

