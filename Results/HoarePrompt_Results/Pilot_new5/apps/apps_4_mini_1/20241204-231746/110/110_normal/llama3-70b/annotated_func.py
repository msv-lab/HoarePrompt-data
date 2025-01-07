#State of the program right berfore the function call: n, m, r, and k are integers such that 1 ≤ n, m ≤ 10^5, 1 ≤ r ≤ min(n, m), and 1 ≤ k ≤ min(n·m, 10^5).
def func():
    n, m, r, k = map(int, input().split())
    ans = min(k, (n - r + 1) * (m - r + 1))
    print(ans / ((n - r + 1) * (m - r + 1)))
#Overall this is what the function does:The function accepts four integers `n`, `m`, `r`, and `k` based on user input and calculates the minimum of `k` and the area defined by `(n - r + 1) * (m - r + 1)`. It then returns the ratio of this minimum value to the area `(n - r + 1) * (m - r + 1)`. The function does not handle potential division by zero if `n - r + 1` or `m - r + 1` is zero.

