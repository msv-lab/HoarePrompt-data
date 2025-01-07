#State of the program right berfore the function call: n, k, and t are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    print(min(t, k) if t <= n else k - (t - n) % k)
#Overall this is what the function does:The function accepts three integers, `n`, `k`, and `t`, provided via standard input. It computes and prints either `min(t, k)` if `t` is less than or equal to `n`, or `k - (t - n) % k` if `t` is greater than `n`. This logic effectively allows for two scenarios: when `t` is within the bounds of `n`, it returns the minimum of `t` and `k`; otherwise, it calculates a value based on the periodic behavior defined by `k` for the excess of `t` over `n`. The function does not return any values, as it only prints the result.

