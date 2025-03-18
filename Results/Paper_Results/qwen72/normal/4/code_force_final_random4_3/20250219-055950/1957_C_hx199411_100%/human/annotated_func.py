#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case where 1 ≤ n ≤ 3 \cdot 10^5 and 0 ≤ k ≤ n, and each of the k moves is represented by two integers r_i and c_i, which are valid positions on the n \times n chessboard.
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
        
    #State: `t` is 0, `n` is an input integer where 1 ≤ n ≤ 3 · 10^5, `k` is an input integer where 1 ≤ k ≤ n, `num` is the total number of `c` and `r` values read, where `num` is incremented by 1 if `c` equals `r` and by 2 if `c` does not equal `r` for each iteration of the loop. `m` is `n - num` for each test case. If `m` is 0 or 1, the function prints 1. If `m` is at least 3, `dp` is a list of length `m + 1` where each element is 0 except `dp[1]` is 1, `dp[2]` is 3, and for each `j` from 3 to `m`, `dp[j]` is `(dp[j - 1] + (j - 1) * dp[j - 2] * 2) % (10^9 + 7)`. The function prints `dp[m]` for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` (1 ≤ t ≤ 10^4) indicating the number of test cases. For each test case, it reads two integers `n` (1 ≤ n ≤ 3 \cdot 10^5) and `k` (0 ≤ k ≤ n), followed by `k` pairs of integers `(r_i, c_i)` representing moves on an `n \times n` chessboard. It calculates a value `num` based on the moves: `num` is incremented by 1 if `r_i` equals `c_i`, and by 2 otherwise. The function then computes `m` as `n - num`. If `m` is 0 or 1, it prints 1. Otherwise, it calculates a dynamic programming array `dp` of length `m + 1` where `dp[1]` is 1, `dp[2]` is 3, and for each `i` from 3 to `m`, `dp[i]` is `(dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10^9 + 7)`. Finally, it prints `dp[m]` for each test case.

