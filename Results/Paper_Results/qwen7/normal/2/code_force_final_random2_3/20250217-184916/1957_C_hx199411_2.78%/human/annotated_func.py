#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 0 ≤ k ≤ n. The moves are represented as pairs of integers (r_i, c_i) for i-th move you made, where 1 ≤ r_i, c_i ≤ n. No two rooks share the same row or column before each move, and the k moves and the implied computer moves are valid. The sum of n over all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: After the loop executes all iterations, `t` will be 0 because the loop continues as long as `t` is non-zero, decrementing `t` by 1 in each iteration until it reaches 0. At this point, no further iterations will occur. The values of `n`, `k`, `num`, `i`, `c`, and `r` will depend on the inputs provided during each iteration of the loop. Specifically, `num` will be the cumulative sum of 2 for each pair where `c` does not equal `r`, plus 1 for each pair where `c` equals `r`. The variable `m` will be `n - num`. If `m` is 0, `m` will remain 0; if `m` is 1, `m` will remain 1; otherwise, `dp` will be a list of length `m + 1` where each element is computed using the recurrence relation \((dp[i - 1] + (i - 1) * dp[i - 2] * 2) \mod (10^9 + 7)\), starting with `dp[1] = 1` and `dp[2] = 3`.
    #
    #The final output will be determined by the value of `m`:
    #- If `m` is 0, the output will be `0`.
    #- If `m` is 1, the output will be `1`.
    #- Otherwise, the output will be the value of `dp[m]` modulo \(10^9 + 7\).
#Overall this is what the function does:The function processes multiple test cases, where each case involves an integer t (1 ≤ t ≤ 10^4), followed by t pairs of integers (n, k) (1 ≤ n ≤ 3⋅10^5, 0 ≤ k ≤ n). It then receives k moves, each represented as a pair of integers (r_i, c_i) (1 ≤ r_i, c_i ≤ n). For each test case, it calculates the number of valid moves (where the row and column indices are either both equal or not equal) and determines the remaining count of valid positions. Based on this count, it computes a specific value using dynamic programming and returns this value modulo \(10^9 + 7\). If the remaining count is 0, it returns 0; if 1, it returns 1; otherwise, it returns the computed value.

