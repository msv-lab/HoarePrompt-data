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
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10³, `x` is a positive integer such that 1 ≤ x ≤ 10⁸, `n` is a positive integer such that 1 ≤ n ≤ x, `ans` is the maximum value between all `i` and `x // i` where `i` is a divisor of `x` and either `i` or `x // i` is less than or equal to `n`.
    print(ans)
    #This is printed: ans (where ans is the maximum value between all i and x // i for divisors i of x such that either i or x // i is less than or equal to n)
#Overall this is what the function does:The function processes a series of test cases, where for each case it reads two positive integers \(x\) and \(n\). It then calculates the maximum value between all divisors \(i\) of \(x\) and their corresponding complementary divisors \(x // i\), but only considering those divisors that are less than or equal to \(n\). Finally, it prints the maximum value found for each test case.

