#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(n⋅m, 10^9). a is a list of n integers where 1 ≤ a_i ≤ 10^9 for each i in range n. The sum of n over all test cases does not exceed 3⋅10^5.
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
        
    #State: After executing the loop for `t` iterations, the variable `cost` will hold the calculated cost for each iteration based on the given logic. The values of `n`, `m`, `k`, and `a` will remain unchanged from their initial states, and `t` will be the number of iterations executed.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers t, n, m, k, and a list a of n integers. For each test case, it calculates a cost based on specific conditions involving n, m, and k, and prints the calculated cost. The function does not return any value explicitly but prints the cost for each test case.

