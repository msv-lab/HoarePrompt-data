#State of the program right berfore the function call: k, n, a, and b are integers such that 0 <= k <= n, and 1 <= n, a, b <= 10^9.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value of k * b - k * (k - 1) // 2 + (n - k) * a
#Overall this is what the function does:The function calculates and returns a specific value based on the input integers `k`, `n`, `a`, and `b` using the formula `k * b - k * (k - 1) // 2 + (n - k) * a`.

