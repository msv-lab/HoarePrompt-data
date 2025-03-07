#State of the program right berfore the function call: k is an integer such that 0 <= k <= min(n, b), a and b are positive integers, and n is a positive integer such that 1 <= n, a, b <= 10^9.
def func_1(k, a, b, n):
    ans = 0
    ans += k * b
    ans += (n - k) * a
    return ans <= n * max(a, b)
    #The program returns True.
#Overall this is what the function does:The function `func_1` accepts four parameters: `k`, `a`, `b`, and `n`. It calculates the value of `ans` as `k * b + (n - k) * a` and returns `True` if `ans` is less than or equal to `n * max(a, b)`. Given the constraints on the input parameters, the function will always return `True`.

