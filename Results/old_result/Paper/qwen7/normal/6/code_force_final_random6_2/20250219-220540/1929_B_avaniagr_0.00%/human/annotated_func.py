#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: Output State: The loop processes each line of input until there are no more lines to read. For each line, `n` and `k` are integers where `n` is between 2 and \(10^8\) inclusive, and `k` is between 1 and \(4n - 2\) inclusive. After processing all lines, the loop terminates, and the final values of `n` and `k` from the last line of input are used in the calculation.
    #
    #The expression `(k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k == 4 * n - 2)` evaluates to either the value of `2 * n` or `k` itself, depending on the relationship between `k` and `4 * n - 3`. Specifically, if `k` is less than `4 * n - 3`, the result is `2 * n`; if `k` is exactly `4 * n - 2`, the result is `k`; otherwise, it is `2 * n`.
    #
    #Thus, the final output state is the result of applying this expression to the last line's `n` and `k` values processed by the loop.
#Overall this is what the function does:The function reads multiple lines of input, each containing two integers \(n\) and \(k\), where \(2 \leq n \leq 10^8\) and \(1 \leq k \leq 4n - 2\). For each line, it calculates and prints a value based on the relationship between \(k\) and \(4n - 3\). Specifically, if \(k < 4n - 3\), it prints \(2n\); if \(k = 4n - 2\), it prints \(k\); otherwise, it prints \(2n\). After processing all input lines, the function completes without returning any explicit value.

