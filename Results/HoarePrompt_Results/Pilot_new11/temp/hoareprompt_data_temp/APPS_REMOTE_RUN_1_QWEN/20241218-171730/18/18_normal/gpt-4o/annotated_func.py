#State of the program right berfore the function call: n, k, and t are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k.
def func():
    n, k, t = map(int, input().split())
    if (t <= k) :
        print(t)
    else :
        if (t <= n) :
            print(k)
        else :
            print(n + k - t)
        #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are integers. If `t` is less than or equal to `n`, then `k` is printed. Otherwise, `n + k - t` is printed.
    #State of the program after the if-else block has been executed: *`n`, `k`, and `t` are integers such that 1 ≤ n ≤ 10^9, 1 ≤ k ≤ n, and 1 ≤ t < n + k, and the program prints either the value of `t` or `n + k - t` based on the condition `t <= k`.
#Overall this is what the function does:The function reads three integers \( n \), \( k \), and \( t \) from standard input, where \( 1 \leq n \leq 10^9 \), \( 1 \leq k \leq n \), and \( 1 \leq t < n + k \). It then determines the output based on the following conditions:
1. If \( t \leq k \), it prints \( t \).
2. If \( k < t \leq n \), it prints \( k \).
3. If \( n < t < n + k \), it prints \( n + k - t \).

After the function concludes, the program will have printed one of the values \( t \), \( k \), or \( n + k - t \) depending on the given conditions. The function does not return any value but outputs the result directly.

