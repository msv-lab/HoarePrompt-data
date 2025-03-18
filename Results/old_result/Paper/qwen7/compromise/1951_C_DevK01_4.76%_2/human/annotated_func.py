#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(n⋅m, 10^9); a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n.
def func():
    t = int(input())
    for _ in range(t):
        L = list(map(int, input().split()))
        
        M = list(map(int, input().split()))
        
        n, m, k = L[0], L[1], L[2]
        
        m = min(m, k)
        
        M.sort()
        
        q = int(math.ceil(k / m))
        
        N = M[:q]
        
        n = len(N)
        
        if n * m == k:
            cost = m * sum(N) + m * m * ((n - 1) * n // 2)
        else:
            w = N.pop()
            mu = k - (n - 1) * m
            cost = mu * w
            n = len(N)
            cost += m * sum(N) + m * m * ((n - 1) * (n - 2) // 2) + n * m * mu
        
        print(cost)
        
        continue
        
    #State: Output State: t is an integer between 1 and 10^4; n, m, and k are undefined; the loop has executed t times, and for each iteration, a cost has been calculated based on the input values of L and M, and printed. The specific values of n, m, and k after all iterations depend on the input provided during each iteration of the loop.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads the values of `n`, `m`, and `k` along with a list `M` of `n` integers. It then calculates a cost based on these values and prints the result. The final state of the program after processing all test cases includes the output of the calculated costs for each test case.

