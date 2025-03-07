#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, each test case consists of two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: Output State: The loop will execute exactly `t` times, where `t` is a positive integer such that \(1 \leq t \leq 10^3\). After all iterations, for each iteration, `n` is the first integer input, `k` is the second integer input, and the condition `n - k <= 1` is checked. If the condition is true, `n` is printed; otherwise, `1` is printed.
    #
    #This means that after all the iterations, the final output will be a series of numbers, either `n` or `1`, depending on whether `n - k <= 1` was true for each pair of inputs `(n, k)`.
#Overall this is what the function does:The function processes up to 1000 test cases, each consisting of two integers \( n \) and \( k \). For each test case, it checks if \( n - k \leq 1 \). If true, it prints \( n \); otherwise, it prints \( 1 \). The function does not return any value but produces a series of outputs, either the original \( n \) or \( 1 \), based on the condition.

