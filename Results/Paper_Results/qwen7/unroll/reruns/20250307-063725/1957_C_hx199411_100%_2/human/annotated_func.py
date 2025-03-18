#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 0 ≤ k ≤ n. The coordinates (r_i, c_i) for each move you made are integers such that 1 ≤ r_i, c_i ≤ n. The k moves and the implied computer moves are valid, meaning no two rooks attack each other.
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
        
    #State: Output State: The output state will consist of a series of integers printed based on the input provided within the loop iterations. For each iteration, the program processes two inputs: `n` and `k`, followed by `k` pairs of integers `c` and `r`. It calculates `num` based on the conditions given and then determines `m` as `n - num`. Depending on the value of `m`, it either prints `1` or proceeds to compute a dynamic programming array `dp` to print the result modulo \(10^9 + 7\).
    #
    #The exact output values depend on the specific inputs provided for each iteration, but the general process is as follows:
    #- If `m` is 0 or 1, it prints `1`.
    #- Otherwise, it computes a dynamic programming array `dp` where `dp[i]` represents the number of ways to achieve a certain state with `i` remaining elements, and prints `dp[m]`.
    #
    #Since the initial state of `t` is an integer between 1 and \(10^4\) and the loop runs exactly `t` times, the output will be a sequence of lines, each corresponding to one of these iterations. Each line will contain either `1` or a computed value from the dynamic programming array `dp`.
#Overall this is what the function does:The function processes a series of test cases, where for each case, it reads integers t, n, k, and k pairs of coordinates (r_i, c_i). It calculates the number of non-attacking rook positions based on the given moves and prints the result for each test case. If the remaining non-attacking positions are 0 or 1, it prints 1. Otherwise, it uses dynamic programming to compute the number of ways to achieve the remaining non-attacking positions and prints the result modulo \(10^9 + 7\).

