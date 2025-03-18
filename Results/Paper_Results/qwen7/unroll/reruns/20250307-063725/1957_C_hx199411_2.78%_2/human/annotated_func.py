#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 0 ≤ k ≤ n. The moves are represented as pairs (r_i, c_i) for 1 ≤ i ≤ k, where 1 ≤ r_i, c_i ≤ n, and these moves are valid according to the problem statement.
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
        
    #State: Output State: The output state will be a series of integers printed based on the input values provided within each iteration of the loop.
    #
    #Explanation: Each iteration of the while loop processes a set of inputs (`n`, `k`, and subsequent pairs of integers `c` and `r`). Based on these inputs, it calculates a value `m` which is then used to compute and print a result using dynamic programming. The final output is a sequence of printed integers, each corresponding to the computed value of `dp[m]` for each input set processed by the loop. The exact values printed depend on the specific inputs provided during each iteration.
#Overall this is what the function does:The function processes a series of test cases, each containing integers \( t \), \( n \), \( k \), and pairs of integers \( (r_i, c_i) \). For each test case, it calculates a value \( m \) based on the number of equal pairs \( (r_i, c_i) \) and prints a sequence of integers derived using dynamic programming. The final output consists of a series of integers, each corresponding to the computed value of \( dp[m] \) for each test case.

