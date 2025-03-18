#State of the program right berfore the function call: k, a, b, and n are integers such that 0 <= k <= min(n, b), 1 <= n, a, b <= 10^9.
def func_1(k, a, b, n):
    ans = 0
    ans += k * b
    ans += (n - k) * a
    return ans <= n * max(a, b)
    #The program returns True
#Overall this is what the function does:The function accepts four integer parameters `k`, `a`, `b`, and `n` with the constraints 0 <= k <= min(n, b) and 1 <= n, a, b <= 10^9. It calculates a value based on these parameters and returns True if the calculated value is less than or equal to `n` times the maximum of `a` and `b`.

