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
        
    #State: `t` is an integer where 1 <= t <= 10^3, `x` is an integer where x >= 1, `n` is an integer where 1 <= n <= x, `i` is `isqrt(x) + 1`, and `ans` is the largest divisor of `x` such that `n` <= `x // i` or `n` <= `i`. If no such divisor exists, `ans` remains 0.
    print(ans)
    #This is printed: ans (where ans is the largest divisor of x such that n <= x // i or n <= i, or 0 if no such divisor exists)
#Overall this is what the function does:The function reads two integers, `x` and `n`, from the user input. It then calculates the largest divisor of `x` such that `n` is less than or equal to either `x // i` or `i`, where `i` is a divisor of `x`. If no such divisor exists, the function prints 0. The function does not return any value; it only prints the result.

