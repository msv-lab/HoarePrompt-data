#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n and k are integers satisfying 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: Output State: After the loop executes all its iterations, `t` is a positive integer such that \(1 \leq t \leq 10^3\). For each test case, `n` is the integer input received on the line where `n` and `k` are defined, and `k` is the integer input received on the same line as `n`. The loop processes each test case independently, so the final values of `n` and `k` will be the last set of inputs provided within the range of `t` test cases.
    #
    #This means that the final values of `n` and `k` will be those obtained from the last test case processed by the loop, given the constraints on `t`, `n`, and `k`.
#Overall this is what the function does:The function processes up to 1000 test cases, each consisting of two integers \(n\) and \(k\), where \(1 \leq n \leq 100\) and \(0 \leq k \leq \frac{n(n-1)}{2}\). For each test case, it prints either \(n\) if \(n - k \leq 1\), or 1 otherwise. After processing all test cases, it outputs the results for each case.

