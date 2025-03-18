#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 3 × 10^5 and 0 ≤ k ≤ n, and each of the k moves is represented by a pair of integers (r_i, c_i) where 1 ≤ r_i, c_i ≤ n, and all moves are valid.
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
        
    #State: The loop has completed all iterations, and the final output state is that `t` is 0, and the values of `n`, `k`, `num`, `m`, and `dp` are no longer relevant as they are reinitialized in each iteration of the loop.
#Overall this is what the function does:The function `func` reads multiple test cases from the input. For each test case, it processes integers `n` and `k`, and a list of `k` moves, where each move is a pair of integers `(r_i, c_i)`. It calculates a value based on the number of moves where `r_i` equals `c_i` and the number of moves where `r_i` does not equal `c_i`. The function then computes a result using dynamic programming and prints the result for each test case. After processing all test cases, the function terminates with `t` set to 0, and the values of `n`, `k`, `num`, `m`, and `dp` being reinitialized for each test case.

