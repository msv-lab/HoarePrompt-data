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
        
    #State: `n`, `m`, `x` is the smallest integer greater than the square root of `n`, `y` is the last value it had in the inner loop, `cnt` is the total count calculated.
    print(cnt)
    #This is printed: cnt (where cnt is the total count calculated in the program)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `m` from the input, calculates a count `cnt` based on certain conditions involving the greatest common divisor (GCD) of pairs of integers `x` and `y`, and prints the final value of `cnt`.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t is the same integer value provided by the user, which is a positive integer such that 1 <= t <= 10^4.
#Overall this is what the function does:The function `func_2` reads a positive integer `t` from the user input, then calls `func_1` exactly `t` times. The function itself does not return any value.

