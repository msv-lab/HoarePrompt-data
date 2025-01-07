#State of the program right berfore the function call: n, m, r, and k are integers such that 1 ≤ n, m ≤ 10^5, 1 ≤ r ≤ min(n, m), and 1 ≤ k ≤ min(n * m, 10^5).
def func():
    n, m, r, k = map(int, input().split())
    ans = min(k, (n - r + 1) * (m - r + 1))
    print(ans / ((n - r + 1) * (m - r + 1)))
#Overall this is what the function does:The function reads four integers \(n\), \(m\), \(r\), and \(k\) from input, ensuring they meet the specified constraints. It calculates the minimum of \(k\) and \((n - r + 1) \times (m - r + 1)\), and prints the ratio of this minimum to \((n - r + 1) \times (m - r + 1)\).

