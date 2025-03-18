#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, and for each of the t test cases, x and n are integers such that 1 <= x <= 10^8 and 1 <= n <= x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: `ans` is the largest divisor of `x` that is less than or equal to `n` or its corresponding pair divisor `x // i` that is less than or equal to `n`. The values of `t`, `x`, and `n` remain unchanged.
    print(ans)
    #This is printed: ans (where ans is the largest divisor of x that is less than or equal to n or its corresponding pair divisor x // i that is also less than or equal to n)
#Overall this is what the function does:The function `func_1` reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `n` and prints the largest divisor of `x` that is less than or equal to `n` or its corresponding pair divisor `x // i` that is also less than or equal to `n`. The values of `t`, `x`, and `n` remain unchanged after processing each test case.

