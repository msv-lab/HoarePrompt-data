#State of the program right berfore the function call: n, k, and t are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    print(min(t, k) if t <= n else k - (t - n) % k)
#Overall this is what the function does:The function reads three integers \( n \), \( k \), and \( t \) from standard input, where \( 1 \leq n \leq 10^9 \), \( 1 \leq k \leq n \), and \( 1 \leq t < n + k \). It then calculates and prints the result based on the following logic:
- If \( t \leq n \), it prints the minimum value between \( t \) and \( k \).
- If \( t > n \), it calculates the remainder when \( t - n \) is divided by \( k \) and subtracts this remainder from \( k \), then prints the result.

