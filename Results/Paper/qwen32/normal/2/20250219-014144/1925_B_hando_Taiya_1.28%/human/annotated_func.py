#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³, and for each test case, x and n are integers such that 1 ≤ x ≤ 10⁸ and 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: the largest valid divisor or quotient `i` or `x // i` that satisfies the conditions `n <= x // i` or `n > x // i` and `n <= i`.
    print(ans)
    #This is printed: ans (where ans is the largest valid divisor or quotient i or x // i that satisfies n <= i and either n <= x // i or n > x // i)
#Overall this is what the function does:The function reads multiple test cases, each consisting of two integers `x` and `n`. For each test case, it determines the largest divisor or quotient of `x` that satisfies the condition `n` is less than or equal to the divisor or quotient. The result for each test case is printed.

