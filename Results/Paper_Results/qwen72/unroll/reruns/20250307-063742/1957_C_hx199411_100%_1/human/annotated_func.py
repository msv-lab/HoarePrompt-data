#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 3 \cdot 10^5 and 0 ≤ k ≤ n, and each of the k moves (r_i, c_i) is a pair of integers such that 1 ≤ r_i, c_i ≤ n and no two moves share the same row or column.
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
        
    #State: t = 0, n and k retain their last input values, num is the sum of 1 or 2 based on the last set of moves, m is calculated as n - num, and dp[m] is the final value printed for the last test case.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k`, followed by `k` pairs of integers `(r_i, c_i)`. It calculates a value `num` based on the pairs, where `num` is incremented by 1 if `r_i` equals `c_i`, and by 2 otherwise. It then computes `m` as `n - num`. If `m` is 0 or 1, the function prints 1. Otherwise, it computes a dynamic programming array `dp` where `dp[i]` is the number of ways to arrange `i` elements under certain conditions, and prints `dp[m]`. After processing all test cases, `t` is 0, and the function has printed the result for each test case.

