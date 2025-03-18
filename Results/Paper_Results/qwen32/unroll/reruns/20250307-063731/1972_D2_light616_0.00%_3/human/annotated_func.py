#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_1():
    x = 1
    cnt = 0
    n, m = map(int, input().split())
    while x * x <= n:
        y = 1
        
        while (x + y) * x <= n and (x + y) * y <= m:
            if math.gcd(x, y) == 1:
                cnt += min(n / ((x + y) * x), m // ((x + y) * y))
            y += 1
        
        x += 1
        
    #State: `n` is `input_n`, `m` is `input_m`, `x` is the smallest integer such that `x * x > n`, `cnt` is the total count accumulated based on the conditions specified in the loop.
    print(cnt)
    #This is printed: cnt (where cnt is the total count accumulated based on the conditions specified in the loop)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `m` from the input, calculates a count based on specific conditions involving the greatest common divisor of pairs of integers, and prints the resulting count.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `n` and `m` are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6; `t` is an input integer.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, then calls `func_1` exactly `t` times. The function does not accept parameters `n` and `m` directly, nor does it return the greatest common divisor (GCD) of `n` and `m`. The final state of the program after it concludes is that `func_1` has been executed `t` times.

