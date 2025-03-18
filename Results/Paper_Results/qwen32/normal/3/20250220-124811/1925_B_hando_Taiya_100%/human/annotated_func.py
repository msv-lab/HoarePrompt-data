#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, and for each test case, x and n are integers such that 1 <= x <= 10^8 and 1 <= n <= x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: `ans` is the maximum value found during the iterations that satisfies either `n <= x // i` or `n <= i` for `i` in the range from 1 to `isqrt(x)`.
    print(ans)
    #This is printed: ans (where ans is the maximum value of i in the range from 1 to isqrt(x) that satisfies either n <= x // i or n <= i)
#Overall this is what the function does:The function `func_1` reads two integers `x` and `n` for each of `t` test cases, where `1 <= n <= x`. It calculates and prints the maximum value `i` within the range from 1 to the integer square root of `x` such that either `n` is less than or equal to `x // i` or `n` is less than or equal to `i`.

