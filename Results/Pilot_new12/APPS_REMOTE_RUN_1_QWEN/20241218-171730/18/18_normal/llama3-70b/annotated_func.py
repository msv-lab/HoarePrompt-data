#State of the program right berfore the function call: n, k, and t are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    print(min(t, k) if t <= n else k - (t - n) % k)
#Overall this is what the function does:The function reads three integers `n`, `k`, and `t` from standard input, where `1 ≤ n ≤ 10^9`, `1 ≤ k ≤ n`, and `1 ≤ t < n + k`. It then calculates and prints one of two possible values based on the relationship between `t` and `n`:

1. If `t` is less than or equal to `n`, it prints the minimum of `t` and `k`.
2. If `t` is greater than `n`, it prints `k - (t - n) % k`.

The function does not return any value. Potential edge cases include when `t` is exactly equal to `n` or when `(t - n) % k` results in zero. In these cases, the function ensures the printed value is within the expected range.

