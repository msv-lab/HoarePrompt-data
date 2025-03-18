#State of the program right berfore the function call: n, k, and t are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    print(min(t, k) if t <= n else k - (t - n) % k)
#Overall this is what the function does:The function reads three integers, `n`, `k`, and `t`, where the constraints are 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k. It calculates a result based on the value of `t` in relation to `n` and `k`. If `t` is less than or equal to `n`, it returns the minimum of `t` and `k`. If `t` is greater than `n`, it computes `k - (t - n) % k`, which determines a cyclical offset based on how far `t` exceeds `n`. The function prints this result and does not return any values. Potential edge cases include scenarios where `t` is exactly `n`, less than `n`, or significantly greater than `n`, which inform how the function resolves inputs to outputs. Moreover, the function does not handle invalid inputs or exceptions, which could lead to issues in production scenarios.

