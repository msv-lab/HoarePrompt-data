#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: Output State: All inputs `n` and `k` from each iteration of the loop have been processed, and the corresponding outputs have been printed. The variable `t` has been decremented until it reaches 0, indicating that all iterations of the loop have completed.
    #
    #In more detail, after all iterations of the loop have finished:
    #- The variable `t` will be 0.
    #- For each iteration, either the condition `4 * n - 2 == k` was met, in which case `k // 2 + 1` was printed, or the condition was not met, in which case `ceil(k / 2)` was printed.
    #- The variables `n` and `k` from each iteration are no longer relevant as the loop has completed, but their values during the last iteration are the most recent ones used in the loop.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads two integers `n` and `k`. If `4 * n - 2` equals `k`, it prints `k // 2 + 1`; otherwise, it prints `ceil(k / 2)`. After processing all test cases, the function outputs the results for each case.

