#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³. For each test case, x and n are integers such that 1 ≤ x ≤ 10⁸ and 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10³; `x` and `n` are integers read from the input such that 1 ≤ x ≤ 10⁸ and 1 ≤ n ≤ x; `ans` is the largest value of `i` or `x // i` that satisfies the conditions for all divisors `i` of `x` up to `isqrt(x)`.
    print(ans)
    #This is printed: ans (where ans is the largest value of i or x // i for all divisors i of x up to isqrt(x))
#Overall this is what the function does:The function reads multiple test cases, each consisting of two integers `x` and `n`, and prints the largest divisor of `x` that is less than or equal to `n` or the corresponding quotient `x // i` that is less than or equal to `n`.

