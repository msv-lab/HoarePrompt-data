#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 0 ≤ k ≤ n; for each test case, r_i and c_i are integers such that 1 ≤ r_i, c_i ≤ n and the k moves and the implied computer moves are valid; the sum of n over all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: `t` is `0`, `n` is the last input integer, `k` is the last input integer, `num` is the total sum of 1 added when `c` equals `r` and 2 added when `c` does not equal `r` for all iterations, `i` is `k - 1`, `c` and `r` are integers from the last input, and `m` is `n - num`. The variable `dp` is a list of length `m + 1` where each element is calculated according to the formula \((dp[i - 1] + (i - 1) * dp[i - 2] * 2) \% (10^9 + 7)\), starting with `dp[1] = 1` and `dp[2] = 3`, and finally, the output is `dp[m]`.
    #
    #This means that after all iterations of the loop have finished, `t` will be `0` since it starts at the initial value of `int(input())` and is decremented by `1` in each iteration until it reaches `0`. The final values of `n` and `k` will be those provided in the last input. The variable `num` will hold the cumulative count based on the conditions specified in the loop. The variable `m` will be the result of `n - num`. The list `dp` will contain the computed values following the given recurrence relation, and the final printed output will be `dp[m]`, which is the last computed value in the list `dp`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer t (number of test cases), two integers n and k (where n is the size of the board and k is the number of moves), and k pairs of integers (r, c) representing moves on the board. For each test case, it calculates the number of valid moves (where r equals c adds 1 to the count, otherwise adds 2) and computes a dynamic programming solution to determine the number of ways to achieve a specific configuration on the board. The function prints the result for each test case, which is the number of ways to achieve the configuration modulo \(10^9 + 7\). If no valid moves are left, it prints 1.

