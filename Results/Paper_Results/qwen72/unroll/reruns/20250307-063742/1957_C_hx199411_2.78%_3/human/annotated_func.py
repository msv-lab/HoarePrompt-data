#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 3 · 10^5 and 0 ≤ k ≤ n, and each move (r_i, c_i) is a pair of integers such that 1 ≤ r_i, c_i ≤ n and no two moves share the same row or column. The sum of n over all test cases does not exceed 3 · 10^5.
def func():
    t = int(input())
    while t:
        t -= 1
        
        n, k = list(map(int, input().split(' ')))
        
        num = 0
        
        for i in range(k):
            c, r = list(map(int, input().split(' ')))
            if c == r:
                num += 1
            else:
                num += 2
        
        m = n - num
        
        if m == 0:
            print(0)
        elif m == 1:
            print(1)
        else:
            dp = [(0) for i in range(m + 1)]
            dp[1] = 1
            dp[2] = 3
            for i in range(3, m + 1):
                dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10 ** 9 + 7)
            print(dp[m])
        
    #State: t is 0, n and k retain their last input values, num is the final calculated value for the last test case, m is the final calculated value for the last test case, and dp is the final dynamic programming array for the last test case.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k`, and a series of `k` moves `(r_i, c_i)`. The function calculates the number of ways to place non-attacking rooks on an `n x n` grid, given the moves, and prints the result for each test case. After processing all test cases, `t` is 0, and the last values of `n`, `k`, `num`, `m`, and the dynamic programming array `dp` are retained, but they are not used outside the function.

