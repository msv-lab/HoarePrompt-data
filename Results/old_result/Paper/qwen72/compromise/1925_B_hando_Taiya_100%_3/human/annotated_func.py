#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, x is an integer such that 1 <= x <= 10^8, and n is an integer such that 1 <= n <= x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: `t` remains unchanged, `x` and `n` remain unchanged, `ans` is the largest divisor of `x` that is less than or equal to `x // n` or `n`.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the value of `ans`, which is the largest divisor of `x` that is less than or equal to `min(x // n, n)`.
    #
    #Since the exact values of `x` and `n` are not provided, we can't compute the exact numerical value of `ans`. However, based on the given information, the print statement will output the largest divisor of `x` that meets the specified condition.
    #
    #Output:
#Overall this is what the function does:The function `func_1` does not accept any parameters and does not return any value. It reads two integers `x` and `n` from the user input, where `1 <= x <= 10^8` and `1 <= n <= x`. The function then calculates and prints the largest divisor of `x` that is less than or equal to `min(x // n, n)`. The state of the program after the function concludes is that `x` and `n` remain unchanged, and the value of `ans` is the largest divisor of `x` that meets the specified condition.

