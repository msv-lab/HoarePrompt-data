#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 3 \cdot 10^5 and 0 ≤ k ≤ n, and each move (r_i, c_i) is a pair of integers where 1 ≤ r_i, c_i ≤ n, and all moves are valid according to the game rules.
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
        
    #State: t = 0, n and k are unchanged for the last test case, num is the final count of moves, m is the remaining moves, and dp contains the computed dynamic programming array for the last test case.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k`, followed by `k` pairs of integers `(r_i, c_i)`. It calculates the number of moves `num` based on the pairs, and then computes the remaining moves `m` as `n - num`. If `m` is 0, it prints 0. If `m` is 1, it prints 1. For `m` greater than 1, it uses dynamic programming to compute and print a result based on the number of remaining moves. After processing all test cases, `t` is 0, and the function does not return any value.

