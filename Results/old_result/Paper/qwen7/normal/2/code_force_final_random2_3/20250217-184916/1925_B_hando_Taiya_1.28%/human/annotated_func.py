#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x and n are positive integers such that 1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: Output State: `i` is `isqrt(x) + 1`, `x` is an input integer such that \(1 \leq x \leq 10^8\), and `ans` is the maximum value found during the loop, which is the largest integer `i` such that `x` is divisible by `i` and either `n` is less than or equal to `x // i` or `n` is greater than `i`.
    #
    #In simpler terms, `ans` will hold the greatest divisor of `x` that is less than or equal to `sqrt(x)` and also satisfies the condition related to `n`.
    print(ans)
    #This is printed: ans (where ans is the largest divisor of x that is less than or equal to sqrt(x) and satisfies the condition n <= x//i or n > i)
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers \(x\) and \(n\). For each test case, it finds the largest divisor of \(x\) that is less than or equal to \(\sqrt{x}\) and satisfies one of two conditions: \(n \leq \frac{x}{i}\) or \(n > i\). The function then prints the largest such divisor for each test case.

