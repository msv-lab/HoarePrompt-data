#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
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
        
    #State: `x` is `x_final` (smallest integer greater than the square root of `n`), `y` is the last value checked in the inner loop for the previous `x`, `cnt` is `cnt_final` (sum of all valid `min(n // ((x + y) * x), m // ((x + y) * y))` for all pairs `(x, y)` where `gcd(x, y) == 1`).
    print(cnt)
    #This is printed: cnt (where cnt is the sum of all valid min(n // ((x + y) * x), m // ((x + y) * y)) for all pairs (x, y) where gcd(x, y) == 1)
#Overall this is what the function does:The function reads two positive integers `n` and `m` from the input, calculates the sum of the minimum values of `n // ((x + y) * x)` and `m // ((x + y) * y)` for all pairs `(x, y)` where `gcd(x, y) == 1` and `x * x <= n` and `(x + y) * x <= n` and `(x + y) * y <= m`, and prints this sum.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an input integer representing the number of test cases, where `t` is `0` (after decrementing by 1 for each iteration); `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` reads a positive integer `t` representing the number of test cases, then processes each of these `t` test cases by calling `func_1()` for each one. It does not accept any parameters and does not explicitly return any value, but it implicitly returns the results of processing each test case through `func_1()`.

