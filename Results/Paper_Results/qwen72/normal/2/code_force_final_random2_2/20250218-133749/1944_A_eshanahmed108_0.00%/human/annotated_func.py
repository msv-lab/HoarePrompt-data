#State of the program right berfore the function call: t is a positive integer where 1 ≤ t ≤ 10^3, and for each test case, n and k are integers such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: `t` is a positive integer where \(1 \leq t \leq 10^3\), and for each test case, `n` and `k` are integers such that \(1 \leq n \leq 100\) and \(0 \leq k \leq n \cdot (n - 1) / 2\). The loop has executed `t` times, and for each iteration, the output was either `n` if `n - k <= 1` or `1` otherwise.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by two integers `n` and `k`. It reads the number of test cases `t` (where 1 ≤ t ≤ 10^3) and for each test case, it reads `n` (1 ≤ n ≤ 100) and `k` (0 ≤ k ≤ n * (n - 1) / 2). For each test case, the function prints `n` if `n - k` is less than or equal to 1; otherwise, it prints 1. After processing all test cases, the function completes, and the final state is that the specified number of test cases have been processed and the appropriate outputs have been printed for each.

