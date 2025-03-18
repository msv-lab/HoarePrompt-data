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
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^3, `x` is an input integer such that 1 ≤ x ≤ 10^8, `n` is an input integer such that 1 ≤ n ≤ x, `ans` is the maximum value between `i` and `x // i` for which either `n` ≤ `x // i` or `n` ≤ `i`, where the loop iterates over `i` from 1 to the integer square root of `x`.
    print(ans)
    #This is printed: ans (where ans is the maximum value between i and x // i for which either n ≤ x // i or n ≤ i, during the loop iteration from 1 to the integer square root of x)
#Overall this is what the function does:The function processes a series of test cases, each containing three values: `t`, `x`, and `n`. It calculates the maximum value between `i` and `x // i` for which either `n` is less than or equal to `x // i` or `n` is less than or equal to `i`, where the loop iterates over `i` from 1 to the integer square root of `x`. The function then prints this maximum value for each test case.

