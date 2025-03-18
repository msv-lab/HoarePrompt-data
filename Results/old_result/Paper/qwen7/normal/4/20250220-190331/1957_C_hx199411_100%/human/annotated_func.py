#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 0 ≤ k ≤ n. The coordinates (r_i, c_i) for each of the k moves you made are pairs of integers such that 0 ≤ r_i, c_i < n, and no two rooks (either yours or the computer's) share the same row or column after each of your k moves and their mirrored moves.
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
        
    #State: t is 0, n is an input integer, k is 0, num is the total sum calculated based on the conditions inside the loop, m is n - num, and either m is 0, in which case dp is a list of length 1 filled with 1, or m is not 0, in which case dp is a list of length m + 1 filled with 0s, with dp[1] = 1, dp[2] = 3, and dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10^9 + 7) for i from 3 to m.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers t, n, and k, followed by k pairs of integers (r_i, c_i). It calculates the number of moves where the row index equals the column index (num) and computes m as n - num. Based on the value of m, it either prints 1 or constructs and prints a dynamic programming array dp to compute a specific value modulo \(10^9 + 7\).

