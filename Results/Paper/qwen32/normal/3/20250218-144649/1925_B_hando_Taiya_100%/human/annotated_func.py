#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. Each test case consists of two integers x and n such that 1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: `ans` is the maximum value of `i` or `x // i` such that `n <= i` or `n <= x // i` for all divisors `i` of `x` up to `isqrt(x)`.
    print(ans)
    #This is printed: ans (where ans is the maximum value of either i or x // i such that n <= i or n <= x // i for all divisors i of x up to isqrt(x))
#Overall this is what the function does:The function reads multiple test cases, each consisting of two integers `x` and `n`. For each test case, it calculates and prints the maximum value of either `i` or `x // i` such that `n` is less than or equal to `i` or `n` is less than or equal to `x // i` for all divisors `i` of `x` up to the integer square root of `x`.

