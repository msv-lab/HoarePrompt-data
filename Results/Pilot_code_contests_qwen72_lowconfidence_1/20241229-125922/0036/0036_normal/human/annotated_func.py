#State of the program right berfore the function call: N is an integer where 1 ≤ N ≤ 10^5, M is an integer where 0 ≤ M ≤ N-1, and a is a list of M unique integers where 1 ≤ a[i] ≤ N-1 and a[i] < a[i+1] for all valid i.
def func():
    n, m = map(int, raw_input().split(' '))
    dp = [(0) for i in range(0, n + 1)]
    dp[0] = 1
    for i in range(0, m):
        a = int(raw_input())
        
        dp[a] = -1
        
    #State of the program after the  for loop has been executed: `N` is an integer where 1 ≤ N ≤ 10^5, `M` is an integer where 0 ≤ M ≤ N-1, `n` is an input integer, `m` is an input integer, `a` is a list of M unique integers where 1 ≤ a[i] ≤ N-1 and a[i] < a[i+1] for all valid i, `dp` is a list of `n + 1` zeros with `dp[0]` being 1 and `dp[a[i]]` being -1 for each a[i] in the list `a`, `i` is `m - 1`.
    for step in range(1, n + 1):
        if dp[step] < 0:
            continue
        
        ans = 0
        
        for prev in [1, 2]:
            if step - prev >= 0 and dp[step - prev] >= 0:
                ans += dp[step - prev]
        
        dp[step] = ans
        
    #State of the program after the  for loop has been executed: `N` is an integer where 1 ≤ N ≤ 10^5, `M` is an integer where 0 ≤ M ≤ N-1, `n` is an input integer, `m` is an input integer, `a` is a list of M unique integers where 1 ≤ a[i] ≤ N-1 and a[i] < a[i+1] for all valid i, `dp` is a list of `n + 1` integers where `dp[0]` is 1, `dp[a[i]]` is -1 for each a[i] in the list `a`, and for each `step` from 1 to `n`, `dp[step]` is the sum of `dp[step - 1]` and `dp[step - 2]` if both are non-negative and within bounds; otherwise, `dp[step]` is 0, `i` is `m - 1`.
    print(dp[n] % 1000000007)
#Overall this is what the function does:The function `func` reads two integers `N` and `M` from the input, followed by `M` unique integers `a[i]` (1 ≤ a[i] ≤ N-1) which are strictly increasing. It initializes a list `dp` of size `N + 1` with all elements set to 0, except `dp[0]` which is set to 1. For each `a[i]` read from the input, it sets `dp[a[i]]` to -1. Then, it iterates through each step from 1 to `N`, and for each step, it calculates the number of ways to reach that step by summing the values of `dp[step - 1]` and `dp[step - 2]` if they are non-negative. If `dp[step]` is -1, it skips the calculation for that step. Finally, it prints the value of `dp[N]` modulo 1000000007. The function does not return any value. Potential edge cases include when `M` is 0 (no obstacles), and when `N` is 1 (only one step). The function handles these cases correctly by ensuring that `dp[0]` is always 1 and by skipping steps marked as obstacles.

