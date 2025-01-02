#State of the program right berfore the function call: N and M are integers such that 1 <= N <= 10^5 and 0 <= M <= N-1, and a_1, a_2, ..., a_M are integers such that 1 <= a_1 < a_2 < ... < a_M <= N-1.
def func():
    n, m = map(int, raw_input().split(' '))
    dp = [(0) for i in range(0, n + 1)]
    dp[0] = 1
    for i in range(0, m):
        a = int(raw_input())
        
        dp[a] = -1
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range \([1, 10^5]\), `m` is an integer within the range \([0, n-1]\), `dp` is a list of length `n + 1` with `dp[0]` equal to `1` and all other elements equal to `0` if `m == 0`; otherwise, `dp` is a list where `dp[a]` is `-1` for each `a` that was input during the loop, and all other elements remain `0`.
    for step in range(1, n + 1):
        if dp[step] < 0:
            continue
        
        ans = 0
        
        for prev in [1, 2]:
            if step - prev >= 0 and dp[step - prev] >= 0:
                ans += dp[step - prev]
        
        dp[step] = ans
        
    #State of the program after the  for loop has been executed: `prev` is 1 or 2, `step` is `n + k` (where `k` is a non-negative integer), `ans` is `1`, `dp` is a list of length `n + 1` with `dp[0]` equal to `1` and all other elements equal to `0`, and `dp[n + k]` is `1`.
    print(dp[n] % 1000000007)
#Overall this is what the function does:The function processes an integer `N` and another integer `M`, along with a sequence of integers `a_1, a_2, ..., a_M` such that `1 <= a_1 < a_2 < ... < a_M <= N-1`. It initializes a dynamic programming (DP) array `dp` of length `N+1` with `dp[0]` set to `1` and all other elements initialized to `0`. For each `a_i` in the sequence, it sets `dp[a_i]` to `-1`. Then, it updates the DP array to compute the number of ways to reach each index `i` from `0` to `N` using steps of size `1` or `2`, avoiding the indices marked as `-1`. Finally, it prints the value of `dp[N]` modulo `1000000007`.

