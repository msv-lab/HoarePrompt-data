#State of the program right berfore the function call: N and M are integers such that 1 <= N <= 10^5 and 0 <= M <= N-1, and a_1, a_2, ..., a_M are integers such that 1 <= a_1 < a_2 < ... < a_M <= N-1.
def func():
    n, m = map(int, raw_input().split(' '))
    dp = [(0) for i in range(0, n + 1)]
    dp[0] = 1
    for i in range(0, m):
        a = int(raw_input())
        
        dp[a] = -1
        
    #State of the program after the  for loop has been executed: `dp` is a list of length `n + 1` with the first element equal to 1, all other elements equal to 0 except for the elements at indices `a1`, `a2`, ..., `am-1`, which are `-1`; `n` is the first integer input; `m` is the second integer input and must be at least 1; `i` is `m - 1`; `a1`, `a2`, ..., `am-1` are integers input during the loop iterations.
    for step in range(1, n + 1):
        if dp[step] < 0:
            continue
        
        ans = 0
        
        for prev in [1, 2]:
            if step - prev >= 0 and dp[step - prev] >= 0:
                ans += dp[step - prev]
        
        dp[step] = ans
        
    #State of the program after the  for loop has been executed: `dp` is a list of length `n + 1` where `dp[0]` is 1, and for all `i` such that `1 ≤ i ≤ n` and `i` is not equal to any `ai (1 ≤ i ≤ m - 1)`, `dp[i]` is the sum of `dp[i - 1]` and `dp[i - 2]`, and for all `i` such that `1 ≤ i ≤ n` and `i` is equal to any `ai (1 ≤ i ≤ m - 1)`, `dp[i]` remains -1, `n` is the first integer input, `m` is the second integer input and is at least 1, `i` is `m - 1`, and `a1`, `a2`, ..., `am-1` are integers input during the loop iterations.
    print(dp[n] % 1000000007)
#Overall this is what the function does:The function reads two integers \(N\) and \(M\) from standard input, followed by \(M\) integers representing a strictly increasing sequence \(a_1, a_2, \ldots, a_M\). It then constructs a dynamic programming array \(dp\) of length \(N+1\), where \(dp[0] = 1\) and \(dp[i] = -1\) for each \(i\) in the sequence \(a_1, a_2, \ldots, a_M\). For all other indices \(i\), \(dp[i]\) is computed as the sum of \(dp[i-1]\) and \(dp[i-2]\), modulo \(1000000007\). After constructing the array, the function prints \(dp[N] \mod 1000000007\).

This function effectively calculates a modified Fibonacci sequence with specific indices set to \(-1\) based on the given sequence \(a_1, a_2, \ldots, a_M\), and then returns the value at index \(N\).

