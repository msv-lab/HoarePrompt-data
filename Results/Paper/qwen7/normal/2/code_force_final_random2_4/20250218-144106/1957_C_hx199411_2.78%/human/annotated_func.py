#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 0 ≤ k ≤ n. The coordinates (r_i, c_i) for each of the k moves you made are integers such that 1 ≤ r_i, c_i ≤ n, and no two rooks (either yours or the computer's) share the same row or column after each of your k moves and their mirrored moves.
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
            print(0)
        elif m == 1:
            print(1)
        else:
            dp = [(0) for i in range(m + 1)]
            dp[1] = 1
            dp[2] = 3
            for i in range(3, m + 1):
                dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10 ** 9 + 7)
            print(dp[m])
        
    #State: t is False, n is an input integer, k is an input integer, num is an integer between 0 and 2*k, m is either 0 or a positive integer less than or equal to 10000, c and r are input integers, dp is a list of m + 1 elements where each element is an integer, starting from 0 up to dp[m], with dp[1] being 1, dp[2] being 3, and each subsequent dp[i] for i from 3 to m calculated as (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % 1000000007.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers t, n, k, and k pairs of coordinates (r_i, c_i). It calculates the number of rooks placed on the main diagonal and computes a dynamic programming array dp based on this count. Finally, it prints the value of dp[m], where m is derived from the initial values of n and the count of rooks on the main diagonal.

