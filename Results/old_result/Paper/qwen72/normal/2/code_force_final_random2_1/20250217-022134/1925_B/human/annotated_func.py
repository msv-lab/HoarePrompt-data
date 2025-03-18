#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^3, x is an integer where 1 ≤ x ≤ 10^8, and n is an integer where 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^3, `x` is the first integer from the input, `n` is the second integer from the input and 1 ≤ n ≤ x, `i` is `isqrt(x) + 1`, and `ans` is the largest divisor of `x` such that either `n` ≤ `x // i` or `n` ≤ `i`. If no such divisor exists, `ans` remains 0.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the value of `ans`, which is the largest divisor of `x` that meets the given conditions.
    #   - If no such divisor exists, `ans` remains 0.
    #
    #Output:
#Overall this is what the function does:The function reads two integers, `x` and `n`, from the input, where `1 ≤ x ≤ 10^8` and `1 ≤ n ≤ x`. It then calculates the largest divisor of `x` such that either `n` is less than or equal to `x // i` or `n` is less than or equal to `i`, where `i` is a divisor of `x`. If no such divisor exists, the function prints `0`. The function does not return any value; it only prints the result.

