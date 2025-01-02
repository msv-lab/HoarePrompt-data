#State of the program right berfore the function call: N is an integer such that 1 <= N <= 10^5, M is an integer such that 0 <= M <= N-1, and a_1, a_2, ..., a_M are integers such that 1 <= a_1 < a_2 < ... < a_M <= N-1.
def func():
    n, m = map(int, raw_input().split(' '))
    dp = [(0) for i in range(0, n + 1)]
    dp[0] = 1
    for i in range(0, m):
        a = int(raw_input())
        
        dp[a] = -1
        
    #State of the program after the  for loop has been executed: `N` is an integer such that \(1 \leq N \leq 10^5\), `M` is an integer such that \(0 \leq M \leq N-1\), `n` is the first integer input, `m` is the second integer input (must be less than or equal to the number of inputs given), `dp` is a list of length `n + 1` with `dp[0] = 1` and `dp[a] = -1` for each `a` that was input by the user, `i` is `m`, `a` is the last integer input by the user.
    for step in range(1, n + 1):
        if dp[step] < 0:
            continue
        
        ans = 0
        
        for prev in [1, 2]:
            if step - prev >= 0 and dp[step - prev] >= 0:
                ans += dp[step - prev]
        
        dp[step] = ans
        
    #State of the program after the  for loop has been executed: `N` is an integer such that \(1 \leq N \leq 10^5\), `M` is an integer such that \(0 \leq M \leq N-1\), `n` is a positive integer within the range \([1, N]\), `dp` is a list of length `n + 1` with `dp[0] = 1` and `dp[a] = -1` for each `a` that was input by the user, `i = M`, `a` is the last integer input by the user, `ans` is the sum of `dp[step - prev]` for all valid `prev` in `[1, 2]` where `step - prev >= 0` and `dp[step - prev] >= 0`, `dp[step]` is `ans` for all valid `step` values where `dp[step] < 0` is not true, `dp[n + 1]` is the final value of `ans` after executing the loop.
    print(dp[n] % 1000000007)
#Overall this is what the function does:The function processes a set of integers `a_1, a_2, ..., a_M` where each `a_i` is an integer between 1 and `N-1` and calculates a dynamic programming array `dp` based on these inputs. Initially, `dp[0]` is set to 1 and `dp[a_i]` is set to -1 for each `a_i`. For each position `step` from 1 to `n`, the function calculates the value of `dp[step]` as the sum of `dp[step - prev]` for `prev` in `[1, 2]` where `step - prev >= 0` and `dp[step - prev] >= 0`. Finally, the function prints the value of `dp[n]` modulo \(10^9 + 7\). The function handles edge cases where `n` or `m` might be zero and ensures that all possible transitions are considered during the calculation.

