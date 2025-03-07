#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n and k are integers such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: Output State: `t` must be greater than 0 and less than or equal to 10^3, `i` is 3, `n` is the first integer input converted to an integer, `k` is the second integer input converted to an integer.
    #
    #After all iterations of the loop have finished, the variable `i` will be equal to `t` because the loop runs from `0` to `t-1`. Therefore, `i` will be `t`. The values of `n` and `k` will be the inputs provided for the last iteration of the loop, as these values are read inside the loop and do not change across iterations.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). For each test case, it checks if \( k \) is greater than or equal to \( n - 1 \). If true, it prints 1; otherwise, it prints \( n \). The function reads \( t \) test cases from the input, where \( t \) is a positive integer between 1 and 1000. After processing all test cases, it outputs the results for each case.

