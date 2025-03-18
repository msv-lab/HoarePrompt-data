#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 0 ≤ k ≤ n; for each test case, r_i and c_i are integers such that 1 ≤ r_i, c_i ≤ n and the k moves and the implied computer moves are valid.
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
        
    #State: All iterations of the loop have completed, and the final value of `m` is either 0 or \( n - (num + 2 \times k - 2) \). If `m` is 0, then `i` is 0. Otherwise, `i` is equal to `m`. The variable `t` is `False`, indicating that the loop has finished.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers t, n, k, and pairs of integers (r, c). For each test case, it calculates the number of valid moves and computes a result based on the remaining positions after these moves. If no valid positions remain, it prints 1. Otherwise, it uses dynamic programming to compute and print a specific value related to the remaining positions.

