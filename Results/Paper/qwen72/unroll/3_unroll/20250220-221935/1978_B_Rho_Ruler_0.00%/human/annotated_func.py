#State of the program right berfore the function call: k, a, b, and n are non-negative integers such that 0 <= k <= min(n, b) and 1 <= n, a, b <= 10^9.
def func_1(k, a, b, n):
    ans = 0
    ans += k * b
    ans += (n - k) * a
    return ans <= n * max(a, b)
    #The program returns True if `ans` is less than or equal to `n * max(a, b)`, where `ans` is calculated as `k * b + (n - k) * a`.
#Overall this is what the function does:The function `func_1` accepts four non-negative integers `k`, `a`, `b`, and `n` with the constraints 0 <= k <= min(n, b) and 1 <= n, a, b <= 10^9. It calculates the value `ans` as `k * b + (n - k) * a` and returns `True` if `ans` is less than or equal to `n * max(a, b)`. Otherwise, it returns `False`.

