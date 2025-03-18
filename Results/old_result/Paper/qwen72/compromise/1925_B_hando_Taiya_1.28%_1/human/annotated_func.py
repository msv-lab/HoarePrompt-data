#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, x is an integer such that 1 <= x <= 10^8, and n is an integer such that 1 <= n <= x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: `t` remains unchanged, `x` and `n` remain unchanged, `ans` is the largest divisor of `x` that is less than or equal to `n` or the largest quotient of `x` divided by a divisor that is less than or equal to `n`.
    print(ans)
    #This is printed: ans (where ans is the largest divisor of x that is less than or equal to n or the largest quotient of x divided by a divisor that is less than or equal to n)
#Overall this is what the function does:The function `func_1` reads two integers `x` and `n` from the user input, where `1 <= x <= 10^8` and `1 <= n <= x`. It then calculates and prints the largest divisor of `x` that is less than or equal to `n` or the largest quotient of `x` divided by a divisor that is less than or equal to `n`. The function does not return any value. The state of `t` is not affected by this function, and `x` and `n` remain unchanged after the function concludes.

