#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and k is an integer such that 0 ≤ k ≤ n. Each of the next k lines contains two integers r_i and c_i, denoting the i-th move you made, where 1 ≤ r_i, c_i ≤ n. It is guaranteed that the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: t is 0, n is the last value read from the input, k is the last value read from the input, num is the sum of 1s and 2s based on whether c == r or not across all k iterations, m is n - num, and dp is a list of length m + 1 with values calculated by the recurrence relation if m > 1.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid size `n` and a number of moves `k`. For each test case, it calculates a result based on the moves made, where each move is represented by a pair of integers `(r_i, c_i)`. The result is printed for each test case, which is either `1` if the remaining cells to be filled are `0` or `1`, or a value computed using a dynamic programming approach if there are more cells to be filled.

