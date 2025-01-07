#State of the program right berfore the function call: n, k, and t are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    print(min(t, k) if t <= n else k - (t - n) % k)
#Overall this is what the function does:The function reads three integers `n`, `k`, and `t` from user input. It prints `min(t, k)` if `t <= n`; otherwise, it prints `k - (t - n) % k`.

