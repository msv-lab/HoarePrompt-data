#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3. Each test case consists of two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: Output State: The loop will continue to execute as many times as specified by the user through the input. After all iterations, `t` is a positive integer such that \(1 \leq t \leq 10^3\), and for each iteration, there are corresponding values of `n` and `k` provided by the user, where \(1 \leq n \leq 100\) and \(0 \leq k \leq \frac{n \times (n - 1)}{2}\). The final output state will include all these inputs and their respective processed results from the loop.
    #
    #In simpler terms, after the loop finishes all its iterations, `t` will still be within the range of 1 to 1000, and for each iteration, there will be a pair of integers `n` and `k` that were input by the user, along with the result of the loop's processing for those pairs.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \(n\) and \(k\). It reads the number of test cases \(t\) (where \(1 \leq t \leq 1000\)) and then iterates over each test case. For each test case, it checks if \(1 \leq n \leq 100\) and \(0 \leq k \leq \frac{n \times (n - 1)}{2}\). If the conditions are met, it prints \(n\) if \(n - k \leq 1\), otherwise it prints 1. If the conditions are not met, it does not process the test case and moves to the next one. After processing all test cases, it outputs the results for each valid test case.

