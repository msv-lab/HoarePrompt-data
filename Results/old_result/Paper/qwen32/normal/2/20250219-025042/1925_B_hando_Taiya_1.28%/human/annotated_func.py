#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, x and n are integers such that 1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: the largest integer `i` or `x // i` that is a divisor of `x` and satisfies the given conditions for `n`.
    print(ans)
    #This is printed: ans (where ans is the largest integer i or x // i that is a divisor of x and satisfies the given conditions for n)
#Overall this is what the function does:For each test case consisting of two integers `x` and `n`, the function determines and prints the largest integer `i` or `x // i` that is a divisor of `x` and satisfies the condition that `n` is less than or equal to either `i` or `x // i`.

