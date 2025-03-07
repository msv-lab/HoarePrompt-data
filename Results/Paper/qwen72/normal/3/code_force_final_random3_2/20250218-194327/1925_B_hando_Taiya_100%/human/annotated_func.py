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
        
    #State: `t` is an integer such that 1 <= t <= 10^3, `x` is an integer provided by the input and must be at least 1, `n` is an integer provided by the input and 1 <= n <= x, `i` is the largest integer such that `i * i <= x`. If `x` is divisible by any integer `i` in the range 1 to `isqrt(x) + 1`, and if `n` <= `x // i` or `n` <= `i`, then `ans` is the maximum value of `i` or `x // i` that satisfies these conditions. Otherwise, `ans` remains 0.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the value of `ans`.
    #   - If the conditions are met, `ans` will be the maximum value of `i` or \(\frac{x}{i}\) that satisfies the conditions.
    #   - If the conditions are not met, `ans` will be 0.
    #
    #Based on the initial state and the conditions, the output will be:
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads two integers `x` and `n` from the input, where `1 <= x <= 10^8` and `1 <= n <= x`. It then calculates the maximum integer `i` such that `x` is divisible by `i` and `n` is less than or equal to either `i` or `x // i`. The function prints this maximum value if it exists; otherwise, it prints 0. The function does not return any value.

