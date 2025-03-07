#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and k is an integer such that 0 ≤ k ≤ n. Each of the next k lines contains two integers r_i and c_i, denoting the i-th move you made, where 1 ≤ r_i, c_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5.
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
            print(1)
        elif m == 1:
            print(1)
        else:
            dp = [(0) for i in range(m + 1)]
            dp[1] = 1
            dp[2] = 3
            for i in range(3, m + 1):
                dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10 ** 9 + 7)
            print(dp[m])
        
    #State: `t` is 0, `n` is the last input integer such that 1 ≤ n ≤ 3 · 10^5, `k` is the last input integer such that 0 ≤ k ≤ n, `num` is the sum of 1s and 2s based on the conditions encountered in each of the `k` iterations for the last test case, and `m` is `n - num`. If `m` is 0 or 1, no further changes occur. If `m` is greater than 1, the `dp` array is fully populated from `dp[1]` to `dp[m]` with each element calculated using the formula `dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10^9 + 7)`.
#Overall this is what the function does:The function processes multiple test cases, each involving a grid of size `n` and a series of `k` moves. For each move, it calculates a score based on whether the move is on the diagonal (`r_i == c_i`) or not. It then determines a value `m` which is the difference between `n` and the accumulated score. Depending on the value of `m`, it either outputs `1` if `m` is `0` or `1`, or computes a result using dynamic programming and outputs that result if `m` is greater than `1`.

