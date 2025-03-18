#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and k is an integer such that 0 ≤ k ≤ n. Each of the next k lines contains two integers r_i and c_i, denoting the i-th move you made, where 1 ≤ r_i ≤ n and 1 ≤ c_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: - For the first test case, the output is `1`.
    #- For the second test case, the output is `1`.
    #
    #Given the above example, the output state after all iterations is:
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each involving a grid of size `n` and a series of `k` moves specified by row and column indices. For each test case, it calculates and prints the number of ways to place non-attacking rooks on the grid after accounting for the moves, modulo \(10^9 + 7\).

