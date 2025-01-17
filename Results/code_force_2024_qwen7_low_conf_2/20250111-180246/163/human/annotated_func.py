#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n ≤ 10^6 and 1 ≤ m ≤ 2·10^5. Each l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n. The sum of n across all test cases does not exceed 10^6, and the sum of m across all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        aseg = [0] * (n + 2)
        
        along = [-1] * (n + 2)
        
        for i in range(m):
            l, r = map(int, input().split())
            aseg[l] += 1
            aseg[r + 1] -= 1
            along[l] = max(r + 1, along[l])
        
        dp = [0] * (n + 2)
        
        for i in range(n):
            aseg[i + 1] += aseg[i]
            along[i] = max(along[i], along[i - 1])
        
        for i in range(n, 0, -1):
            if along[i] < 0:
                dp[i] = dp[i + 1]
            else:
                dp[i] = max(dp[i + 1], aseg[i] + dp[along[i]])
        
        print(dp[1])
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is a positive integer, `m` is a non-negative integer, `aseg` is a list of length `n + 2` where all elements are integers, `along` is a list of length `n + 2` where all elements are integers, `dp` is a list of length `n + 2` where all elements are integers, `dp[1]` contains the maximum value that can be obtained starting from index 1 and moving backwards through the `dp` array based on the operations performed by the loop, all other elements of `dp` are updated according to the loop logic, `aseg[0]` is its original value, for each `j` from 1 to `n + 1`, `aseg[j]` is the cumulative sum up to `j - 1`, `along[0]` is its original value, for each `k` from 1 to `n - 1`, `along[k]` is the maximum of `along[k]` and `along[k - 1]`, `along[n]` is the maximum value among all elements in `along`, `l` and `r` are any valid integers.
#Overall this is what the function does:The function processes multiple test cases, each containing integers `n` and `m`, and arrays of integers `l_i` and `r_i`. For each test case, it constructs a dynamic programming (DP) solution to find the maximum value that can be obtained starting from index 1 and moving backwards through the DP array based on the specified operations. Specifically, for each interval `[l_i, r_i]`, it updates two auxiliary arrays: `aseg` (which keeps track of prefix sums) and `along` (which stores the maximum possible end index for each start index). After processing all intervals, it calculates the DP values such that `dp[i]` represents the maximum value obtainable starting from index `i`. The function ultimately prints the result of `dp[1]` for each test case. Potential edge cases include when `l_i` equals `r_i` (in which case no update is made to `aseg`), and when there are no valid intervals (in which case `dp[1]` would be zero).

