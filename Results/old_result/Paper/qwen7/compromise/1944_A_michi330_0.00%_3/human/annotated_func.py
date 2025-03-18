#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n and k are integers such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: Output State: The output state will consist of `t` lines, where each line contains either "1" or "n - 1". Specifically, for each iteration of the loop, if `k` is greater than or equal to `n - 1`, the output will be "1", otherwise it will be "n - 1". Since the exact values of `n` and `k` are not specified, the output can vary based on user input during each iteration.
#Overall this is what the function does:The function processes a series of test cases defined by the number of tests `t`. For each test case, it reads two integers `n` and `k`. Based on the value of `k` relative to `n-1`, it outputs either "1" or "n-1". The final state of the program consists of `t` lines of output, each containing either "1" or "n-1" depending on the condition met by `k` for each test case.

