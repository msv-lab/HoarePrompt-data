#State of the program right berfore the function call: k, a, b, and n are non-negative integers such that 1 <= n, a, b <= 10^9 and 0 <= k <= min(n, b).
def func_1(k, a, b, n):
    ans = 0
    ans += k * b
    ans += (n - k) * a
    return ans <= n * max(a, b)
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts four parameters `k`, `a`, `b`, and `n`, all of which are non-negative integers within the constraints 1 <= n, a, b <= 10^9 and 0 <= k <= min(n, b). It calculates a value `ans` which is the sum of `k * b` and `(n - k) * a`. The function then returns a boolean value indicating whether `ans` is less than or equal to `n * max(a, b)`. Given the constraints and the calculation, the function will always return `True`.

