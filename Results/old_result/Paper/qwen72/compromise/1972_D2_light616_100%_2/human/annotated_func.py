#State of the program right berfore the function call: No variables are passed as arguments to the function `func_1`. The function reads `n` and `m` from standard input, where `n` and `m` are positive integers such that 1 ≤ n, m ≤ 2 · 10^6.
def func_1():
    x = 1
    cnt = 0
    n, m = map(int, input().split())
    while x * x <= n:
        y = 1
        
        while (x + y) * x <= n and (x + y) * y <= m:
            if math.gcd(x, y) == 1:
                cnt += min(n // ((x + y) * x), m // ((x + y) * y))
            y += 1
        
        x += 1
        
    #State: `n` and `m` are positive integers such that \(1 \leq n, m \leq 2 \cdot 10^6\), `x` is the smallest integer greater than 1 such that \(x \cdot x > n\), `y` is 1, and `cnt` is the sum of `min(n // ((x + y) * x), m // ((x + y) * y))` for all pairs `(x, y)` where `gcd(x, y) == 1` and \((x + y) * x <= n\) and \((x + y) * y <= m\).
    print(cnt)
    #This is printed: cnt (where cnt is the sum of min(n // ((x + y) * x), m // ((x + y) * y)) for all pairs (x, y) where gcd(x, y) == 1 and (x + y) * x <= n and (x + y) * y <= m)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `m` from standard input, where 1 ≤ n, m ≤ 2 · 10^6. It calculates the number of pairs (x, y) such that 1 ≤ x, y, (x + y) * x ≤ n, (x + y) * y ≤ m, and the greatest common divisor (gcd) of x and y is 1. The function then prints this count. After the function concludes, the values of `n` and `m` remain unchanged, and the count of valid pairs is printed to the standard output.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` must be greater than or equal to 1, `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads a positive integer `t` from the user input, where 1 <= t <= 10^4. The function then calls another function `func_1` exactly `t` times. After the function completes, `t` remains unchanged, and `func_1` has been executed `t` times. The function itself does not return any value.

