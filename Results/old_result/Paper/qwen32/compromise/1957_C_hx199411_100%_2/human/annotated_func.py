#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and k is an integer such that 0 ≤ k ≤ n. Each of the next k lines contains two integers r_i and c_i, denoting the i-th move you made, where 1 ≤ r_i, c_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is 0; `n`, `k`, `num`, and `m` are determined by the inputs and calculations within the loop; `dp` is calculated and printed only if `m` is greater than 1.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the size of a grid `n` and the number of moves `k`. It then reads `k` pairs of integers representing moves on the grid. Based on these moves, it calculates and prints a result for each test case. The result is `1` if the remaining unvisited cells on the grid after the moves can be visited in exactly one or zero additional moves, otherwise, it calculates the number of ways to visit the remaining cells using dynamic programming and prints this number modulo \(10^9 + 7\).

