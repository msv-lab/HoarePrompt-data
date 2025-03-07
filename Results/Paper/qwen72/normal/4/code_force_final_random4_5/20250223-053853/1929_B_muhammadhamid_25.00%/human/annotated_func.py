#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n and k are integers for each test case such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The loop has completed all iterations, and for each test case, the output is either 1, the ceiling of k divided by 2, or k divided by 2 plus 1, depending on the values of n and k. The variables t, n, and k retain their initial values or are reassigned for each test case as specified by the input.
#Overall this is what the function does:The function reads an integer `t` (1 <= t <= 1000) indicating the number of test cases. For each test case, it reads two integers `n` and `k` (2 <= n <= 10^8 and 1 <= k <= 4n - 2). Depending on the values of `n` and `k`, it prints either 1, the ceiling of `k` divided by 2, or `k` divided by 2 plus 1. After processing all test cases, the function completes and the variables `t`, `n`, and `k` are no longer in scope.

