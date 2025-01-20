#State of the program right berfore the function call: n, m, and k are integers such that 1 ≤ n ≤ m ≤ 10^9 and 1 ≤ k ≤ n.
def func():
    n, m, k = map(int, input().split())
    if (k == 1) :
        print(min(m // n, m - (n - 1)))
    else :
        print(min(m // n + 1, m - (n - k)))
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers satisfying 1 ≤ `n` ≤ `m` ≤ 10^9 and 1 ≤ `k` ≤ `n`. If `k` is 1, the output is `min(m // n, m - (n - 1))`. Otherwise, the output is `min(m // n + 1, m - (n - k))`.
#Overall this is what the function does:The function reads three integers \( n \), \( m \), and \( k \) from the standard input, where \( 1 \leq n \leq m \leq 10^9 \) and \( 1 \leq k \leq n \). It then calculates and prints one of two values based on the value of \( k \):

1. If \( k = 1 \), it prints \( \min\left(\frac{m}{n}, m - (n - 1)\right) \).
2. Otherwise, it prints \( \min\left(\left\lfloor \frac{m}{n} \right\rfloor + 1, m - (n - k)\right) \).

The function does not accept any parameters and does not return any value. After executing the function, the program will have printed one of the two calculated values, depending on the value of \( k \). The function handles all valid inputs within the specified constraints.

