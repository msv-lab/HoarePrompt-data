#State of the program right berfore the function call: n, m, r, and k are integers such that 1 ≤ n, m ≤ 100000, 1 ≤ r ≤ min(n, m), and 1 ≤ k ≤ min(n·m, 100000).
def func():
    n, m, r, k = map(int, input().split())
    ans = min(k, (n - r + 1) * (m - r + 1))
    print(ans / ((n - r + 1) * (m - r + 1)))
#Overall this is what the function does:The function accepts four integers `n`, `m`, `r`, and `k` from user input, which must fall within specific ranges. It computes the value `ans` as the minimum between `k` and the area equivalent to a rectangle formed in a grid defined by the dimensions `(n - r + 1)` and `(m - r + 1)`. The function then outputs the result of dividing `ans` by the area `(n - r + 1) * (m - r + 1)`. If the area is zero (which can occur if `r` is equal to `n` or `m`), dividing by zero will result in an error. Therefore, the function should ideally handle cases where `n` or `m` is equal to `r` to avoid undefined behavior. The function primarily produces a floating-point output based on the computed values.

