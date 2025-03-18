#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^4, n and k are integers for each test case where 1 <= n <= 3 * 10^5 and 0 <= k <= n, and each move (r_i, c_i) is a pair of integers where 1 <= r_i, c_i <= n, and all moves are valid.
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
        
    #State: `t` is 0, `n` and `k` are the input values for the last test case, `num` is the total number of times the loop has incremented `num` based on the conditions `c == r` (increment by 1) or `c != r` (increment by 2) for the last test case, `m` is `n - num` for the last test case, and `dp` is a list of length `m + 1` with all elements initialized to 0. If `m` is 0, `dp` remains as a list of length 1 with all elements initialized to 0. If `m` is 1, `dp` is a list of length 2 with `dp[1]` set to 1. If `m` is at least 3, `dp[1]` is 1, `dp[2]` is 3, and `dp[i]` for `i` from 3 to `m` is updated to `(dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10
#Overall this is what the function does:The function processes multiple test cases, each defined by the size of a board `n`, the number of moves `k`, and a list of valid moves `(r_i, c_i)`. For each test case, it calculates a value based on the moves and prints the result. The final state of the program is that `t` is 0, `n` and `k` are the input values for the last test case, `num` is the total number of times the loop has incremented `num` based on the conditions `c == r` (increment by 1) or `c != r` (increment by 2) for the last test case, and `m` is `n - num` for the last test case. If `m` is 0 or 1, the function prints 1. If `m` is at least 3, the function computes and prints a value from a dynamic programming array `dp` where `dp[m]` is calculated based on a specific recurrence relation.

