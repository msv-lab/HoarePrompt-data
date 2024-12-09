#State of the program right berfore the function call: n, k, and t are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    print(min(t, k) if t <= n else k - (t - n) % k)
#Overall this is what the function does:The function accepts three integers, `n`, `k`, and `t`, which represent various constraints. It computes and prints the minimum of `t` and `k` if `t` is less than or equal to `n`. If `t` exceeds `n`, it computes the value `k - (t - n) % k`, which appears to determine a certain position relative to `k` based on the excess of `t` over `n`. The function effectively handles inputs within the specified constraints but does not explicitly return any value; it only prints the result.

