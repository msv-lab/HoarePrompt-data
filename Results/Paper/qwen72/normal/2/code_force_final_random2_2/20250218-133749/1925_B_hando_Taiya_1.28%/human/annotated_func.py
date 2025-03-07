#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^3, x is an integer where 1 <= x <= 10^8, and n is an integer where 1 <= n <= x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: `t` remains an integer where 1 <= t <= 10^3, `x` remains the first integer from the input, `n` remains the second integer from the input, `i` is `isqrt(x) + 1`, and `ans` is the maximum divisor of `x` that is less than or equal to `n` or the maximum quotient of `x` divided by a divisor that is less than or equal to `n`.
    print(ans)
    #This is printed: ans (where ans is the maximum divisor of x that is less than or equal to n or the maximum quotient of x divided by a divisor that is less than or equal to n)
#Overall this is what the function does:The function reads two integers, `x` and `n`, from the input. It then calculates and prints the maximum divisor of `x` that is less than or equal to `n` or the maximum quotient of `x` divided by a divisor that is less than or equal to `n`. The function does not return any value. After the function concludes, `x` and `n` remain unchanged, and the program state includes the printed result.

