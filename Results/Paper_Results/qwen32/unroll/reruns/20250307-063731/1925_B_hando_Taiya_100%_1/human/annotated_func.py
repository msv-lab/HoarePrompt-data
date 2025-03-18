#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, and for each of the t test cases, there are two integers x and n such that 1 <= x <= 10^8 and 1 <= n <= x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: `t` is an integer such that 1 <= t <= 10^3; `x` and `n` are integers read from the input such that 1 <= x <= 10^8 and 1 <= n <= x; `ans` is the largest divisor of `x` that is less than or equal to `n` or its corresponding pair divisor `x // i` that is also less than or equal to `n`.
    print(ans)
    #This is printed: ans (where ans is the largest divisor of x that is less than or equal to n or its corresponding pair divisor x // i that is also less than or equal to n)
#Overall this is what the function does:The function `func_1` reads two integers `x` and `n` for each of `t` test cases, where `1 <= n <= x`. It calculates and prints the largest divisor of `x` that is less than or equal to `n` or its corresponding pair divisor `x // i` that is also less than or equal to `n`.

