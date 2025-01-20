#State of the program right berfore the function call: n, m, and k are integers such that 1 ≤ n ≤ m ≤ 10^9 and 1 ≤ k ≤ n.
def func():
    n, m, k = map(int, input().split())
    if (k == 1) :
        print(min(m // n, m - (n - 1)))
    else :
        print(min(m // n + 1, m - (n - k)))
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers. If `k` equals 1, the printed value is `min(m // n, m - (n - 1))`. If `k` does not equal 1, the printed value is `min(m // n + 1, m - (n - k))`.
#Overall this is what the function does:The function takes no parameters and reads three integers \( n \), \( m \), and \( k \) from the standard input, where \( 1 \leq n \leq m \leq 10^9 \) and \( 1 \leq k \leq n \). It then prints one of two values based on the value of \( k \):

- If \( k = 1 \), it prints the minimum value between \( \frac{m}{n} \) (integer division) and \( m - (n - 1) \).
- If \( k \neq 1 \), it prints the minimum value between \( \frac{m}{n} + 1 \) (integer division) and \( m - (n - k) \).

The function does not return any value; instead, it prints the computed result to the standard output. There are no edge cases mentioned in the provided code, but it handles the general case correctly according to the given conditions.

