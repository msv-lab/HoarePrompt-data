#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n and k are integers for each test case such that 1 <= n <= 3 * 10^5 and 0 <= k <= n, and each of the k moves is represented by two integers r_i and c_i, where 1 <= r_i, c_i <= n, and all moves are valid.
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
        
    #State: The loop has finished executing, `t` is now 0, and `n`, `k`, `c`, `r`, and `num` are the final values computed during the last iteration of the loop. `m` is `n - num`, and if `m` is 0 or 1, the program has printed 1. If `m` is greater than 1, `dp` is a list of length `m + 1` where `dp[1]` is 1, `dp[2]` is 3, and for each `i` from 3 to `m`, `dp[i]` is computed as `(dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10^9 + 7)`, and the program has printed `dp[m]`.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `n` and `k`, followed by `k` pairs of integers `(r_i, c_i)`. It calculates the number of moves where `r_i` equals `c_i` and uses this to compute a value `m`. If `m` is 0 or 1, the function prints 1. If `m` is greater than 1, it computes a dynamic programming array `dp` and prints the value of `dp[m]`. After processing all test cases, the function terminates with `t` set to 0.

