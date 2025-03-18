#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, each test case consists of two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: Output State: `t` is an integer between 1 and 1000 inclusive, `i` is 999 (since the loop runs from 0 to `t-1`), `n` is an input integer, `k` is an input integer. The value of `t` remains unchanged throughout the loop executions, and `i` increments by 1 in each iteration until it reaches `t-1`. After all iterations, `n` and `k` will have the values from the last input provided during the loop's execution, but their specific values depend on the inputs given during each iteration.
#Overall this is what the function does:The function processes up to 1000 test cases, where each test case consists of two integers \( n \) and \( k \). For each test case, it checks if \( k \) is greater than or equal to \( n - 1 \). If true, it prints 1; otherwise, it prints \( n \). After processing all test cases, it outputs the results for each test case.

