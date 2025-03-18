#State of the program right berfore the function call: k, n, a, and b are non-negative integers such that 0 <= k <= min(n, b), 1 <= n, a, b <= 10^9.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value of the expression `k * b - k * (k - 1) // 2 + (n - k) * a`, where `k` is a non-negative integer between 0 and the minimum of `n` and `b`, `n` is a non-negative integer between 1 and 10^9, `a` is a non-negative integer between 1 and 10^9, and `b` is a non-negative integer between 1 and 10^9.
#Overall this is what the function does:The function `func_1` accepts four non-negative integers `k`, `n`, `a`, and `b` with the constraints `0 <= k <= min(n, b)` and `1 <= n, a, b <= 10^9`. It returns a single integer value, which is the result of the expression `k * b - k * (k - 1) // 2 + (n - k) * a`. This value represents a combination of linear and quadratic terms involving `k`, `n`, `a`, and `b`. The function does not modify any of its input parameters.

