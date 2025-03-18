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
        
    #State: `t` is an integer such that 1 <= t <= 10^3, `x` is an integer such that 1 <= x <= 10^8, `n` is an integer such that 1 <= n <= x, and `i` is the largest integer such that `i` <= `isqrt(x)`. `ans` is the maximum value of all divisors `i` of `x` for which `n` <= `x // i` or `n` <= `i`.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the maximum divisor `i` of `x` that satisfies either \(n \leq \frac{x}{i}\) or \(n \leq i\).
    #
    #Since the exact values of `x` and `n` are not provided, we can't compute the exact numerical value of `ans`. However, based on the given conditions, the print statement will output the maximum divisor `i` of `x` that meets the specified criteria.
    #
    #Output:
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads two integers, `x` and `n`, from the user input, where `1 <= x <= 10^8` and `1 <= n <= x`. The function then calculates and prints the maximum divisor `i` of `x` such that either `n <= x // i` or `n <= i`. The final state of the program includes the printed value of `ans`, which is the maximum divisor of `x` that meets the specified criteria.

