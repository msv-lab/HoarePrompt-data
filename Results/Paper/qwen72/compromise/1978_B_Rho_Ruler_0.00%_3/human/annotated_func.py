#State of the program right berfore the function call: k, a, b, and n are non-negative integers such that 0 <= k <= min(n, b), 1 <= n, a, b <= 10^9.
def func_1(k, a, b, n):
    ans = 0
    ans += k * b
    ans += (n - k) * a
    return ans <= n * max(a, b)
    #The program returns True.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `k`, `a`, `b`, and `n`, where `0 <= k <= min(n, b)` and `1 <= n, a, b <= 10^9`. It calculates a value `ans` which is the sum of `k * b` and `(n - k) * a`. The function then returns a boolean indicating whether `ans` is less than or equal to `n * max(a, b)`. Given the constraints and the calculation, the function always returns `True`.

