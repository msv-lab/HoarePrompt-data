#State of the program right berfore the function call: n, m, r, k are integers such that 1 ≤ n, m ≤ 10^5, 1 ≤ r ≤ min(n, m), and 1 ≤ k ≤ min(n * m, 10^5).
def func():
    n, m, r, k = map(int, input().split())
    ans = min(k, (n - r + 1) * (m - r + 1))
    print(ans / ((n - r + 1) * (m - r + 1)))
#Overall this is what the function does:The function reads four integers \( n \), \( m \), \( r \), and \( k \) from the standard input, where \( 1 \leq n, m \leq 10^5 \), \( 1 \leq r \leq \min(n, m) \), and \( 1 \leq k \leq \min(n \times m, 10^5) \). It then calculates the minimum value between \( k \) and \( (n - r + 1) \times (m - r + 1) \), stores this value in the variable `ans`, and prints the ratio of `ans` to \( (n - r + 1) \times (m - r + 1) \). The function does not return any value explicitly but prints the result to the standard output. Potential edge cases include when \( n \) or \( m \) is equal to \( r \) or when \( k \) equals \( (n - r + 1) \times (m - r + 1) \).

