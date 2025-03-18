#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 0 ≤ k ≤ n. The moves are represented as pairs (r_i, c_i) where 1 ≤ r_i, c_i ≤ n, and no two rooks attack each other either directly or through the mirrored moves made by the computer.
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
        
    #State: Output State: The output state will depend on the inputs provided within each iteration of the loop. Since the problem does not specify any particular input values for `n`, `k`, `c`, and `r`, we can consider a general case where these values vary.
    #
    #The loop processes each value of `t` (which starts as an input integer between 1 and \(10^4\)) until it reaches zero. For each value of `t`, it reads two integers `n` and `k`, followed by `k` pairs of integers `c` and `r`. Based on these inputs, it calculates `num` and then determines `m` as `n - num`. Depending on the value of `m`, it either prints `0`, `1`, or computes a dynamic programming solution to print a result modulo \(10^9 + 7\).
    #
    #Since the exact inputs are not specified, the final output state cannot be precisely determined without knowing the specific values of `n`, `k`, `c`, and `r` for each iteration. However, the process will always follow the described steps for each value of `t`.
    #
    #Output State: The output will consist of multiple lines, each corresponding to a value of `t` processed by the loop. Each line will either print `0`, `1`, or a result computed using dynamic programming based on the input values `n`, `k`, `c`, and `r`.
#Overall this is what the function does:The function processes a series of test cases, where for each case, it accepts integers t, n, and k, along with a list of moves represented as pairs (r_i, c_i). It calculates the number of valid moves (where no two rooks attack each other either directly or through mirrored moves) and then determines the output based on the remaining positions. If no positions are left, it prints 0; if one position is left, it prints 1; otherwise, it uses dynamic programming to compute and print the number of ways to place rooks on the remaining positions modulo \(10^9 + 7\).

