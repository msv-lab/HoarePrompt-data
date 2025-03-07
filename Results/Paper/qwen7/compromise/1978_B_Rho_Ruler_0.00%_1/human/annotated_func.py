#State of the program right berfore the function call: t is a positive integer, and each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9.
def func_1(k, a, b, n):
    ans = 0
    ans += k * b
    ans += (n - k) * a
    return ans <= n * max(a, b)
    #The program returns a boolean value indicating whether the expression `k * b + (n - k) * a` is less than or equal to `n * max(a, b)` holds true, given that `t` is a positive integer and `ans` is already defined as `k * b + (n - k) * a`.
#Overall this is what the function does:The function accepts four parameters: `k`, `a`, `b`, and `n`. It calculates the value of `ans` as `k * b + (n - k) * a` and returns `True` if `ans` is less than or equal to `n * max(a, b)`, otherwise it returns `False`.

