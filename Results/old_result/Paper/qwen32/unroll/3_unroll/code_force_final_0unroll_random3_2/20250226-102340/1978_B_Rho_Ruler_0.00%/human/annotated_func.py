#State of the program right berfore the function call: k is an integer such that 0 <= k <= min(n, b), a and b are integers such that 1 <= a, b <= 10^9, and n is an integer such that 1 <= n <= 10^9.
def func_1(k, a, b, n):
    ans = 0
    ans += k * b
    ans += (n - k) * a
    return ans <= n * max(a, b)
    #The program returns True
#Overall this is what the function does:The function `func_1` takes four parameters: `k`, `a`, `b`, and `n`. It calculates a value based on these parameters and returns `True` if this calculated value is less than or equal to `n` times the maximum of `a` and `b`.

