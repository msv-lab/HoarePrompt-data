#State of the program right berfore the function call: m is a positive integer (1 ≤ m ≤ 10^9), a and b are positive integers (1 ≤ a, b ≤ 10^5).
def func():
    m, a, b = map(int, input().split())
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(m + 1):
        if i + a <= m:
            dp[i + a] += dp[i]
        
        if i - b >= 0:
            dp[i] += dp[i - b]
        
    #State of the program after the  for loop has been executed: `m`, `a`, and `b` are positive integers. The list `dp` will have its zeroth index as 1, and indexes from `1` to `m` will be updated based on the operations performed in the loop. Specifically, `dp[i + a]` will accumulate the values of `dp[i]` for all valid `i`, and `dp[i]` will accumulate values from `dp[i - b]` for all valid `i`. After the loop completes, `dp` will represent the number of ways to reach each index from 0 to `m` based on the steps defined by `a` and `b`.
    print(sum(dp))
#Overall this is what the function does:The function accepts three positive integers `m`, `a`, and `b` from user input, where `1 ≤ m ≤ 10^9` and `1 ≤ a, b ≤ 10^5`. It calculates the number of ways to reach each index from `0` to `m` based on steps defined by `a` (forward step) and `b` (backward step). The function returns the total number of ways to reach index `m` after processing the dynamic programming list `dp`. However, the exact output is not stored or returned; instead, it is printed directly. Note that for larger values of `m`, memory consumption will be significant due to the size of the `dp` list.

