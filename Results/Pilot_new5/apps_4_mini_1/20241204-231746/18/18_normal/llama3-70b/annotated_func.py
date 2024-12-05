#State of the program right berfore the function call: n, k, and t are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    print(min(t, k) if t <= n else k - (t - n) % k)
#Overall this is what the function does:The function accepts three integers `n`, `k`, and `t` and computes an output based on the value of `t`. If `t` is less than or equal to `n`, it returns the minimum of `t` and `k`. If `t` is greater than `n`, it returns `k - (t - n) % k`, effectively calculating a value based on the overflow of `t` beyond `n`. This function does not return any value; instead, it directly prints the result to the output.

