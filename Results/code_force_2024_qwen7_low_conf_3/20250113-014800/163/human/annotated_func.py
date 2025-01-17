#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n ≤ 10^6 and 1 ≤ m ≤ 2⋅10^5. Each line contains two integers l_i and r_i such that 1 ≤ l_i ≤ r_i ≤ n.
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
        
    #State of the program after the  for loop has been executed: `t` is a positive integer such that 1 ≤ `t` ≤ 10^4, `i` is `n`, `aseg` is a list of length `n + 2` where `aseg[i]` is the cumulative sum of increments and decrements up to index `i`, `along` is a list of length `n + 2` where `along[i]` is the maximum right boundary encountered up to index `i`, `dp` is a list of length `n + 2` where `dp[i]` is the maximum value calculated by the loop for each index `i` from `n` to `1`, and the final value of `dp[1]` is printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers \(n\) and \(m\) such that \(1 \leq n \leq 10^6\) and \(1 \leq m \leq 2 \cdot 10^5\). It then reads \(m\) pairs of integers \(l_i\) and \(r_i\) such that \(1 \leq l_i \leq r_i \leq n\). The function constructs a list `aseg` which keeps track of cumulative increments and decrements up to each index, and a list `along` which records the maximum right boundary encountered up to each index. It then calculates a dynamic programming array `dp` to find the maximum value based on certain conditions. Finally, it prints the value stored in `dp[1]`. This process is repeated for each test case.

