#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n ≤ 10^6 and 1 ≤ m ≤ 2⋅10^5. Each line of the next m lines contains two integers l_i and r_i such that 1 ≤ l_i ≤ r_i ≤ n.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is 0, `dp[1]` is the maximum value obtained by the dynamic programming process defined by the loop, `aseg[i + 1]` is the cumulative sum of the original values in the list `aseg` from index 0 to `n-1`, `along[i]` is the maximum value `along` has ever reached up to index `i`, all other variables retain their unchanged final values after the loop completes.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it processes integers `n` and `m` where \(1 \leq n \leq 10^6\) and \(1 \leq m \leq 2 \cdot 10^5\), and `m` pairs of integers \(l_i\) and \(r_i\) where \(1 \leq l_i \leq r_i \leq n\). It then performs a series of operations to compute a dynamic programming solution to find the maximum value of a certain subarray configuration. Specifically, it calculates a cumulative sum array `aseg` and a maximum reach array `along`. After these computations, it determines the maximum value `dp[1]` based on the values in `aseg` and `along`. Finally, the function prints the result `dp[1]` for each test case.

