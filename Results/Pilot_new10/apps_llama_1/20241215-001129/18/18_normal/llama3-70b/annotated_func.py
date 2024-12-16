#State of the program right berfore the function call: n, k, and t are integers such that 1 <= n <= 10^9, 1 <= k <= n, and 1 <= t < n + k.
def func():
    n, k, t = map(int, input().split())
    print(min(t, k) if t <= n else k - (t - n) % k)
#Overall this is what the function does:The function accepts three integer parameters `n`, `k`, and `t` and prints the minimum of `t` and `k` if `t` is less than or equal to `n`, or `k - (t - n) % k` if `t` is greater than `n`, where `n`, `k`, and `t` are integers such that `1 <= n <= 10^9`, `1 <= k <= n`, and `1 <= t < n + k`.

