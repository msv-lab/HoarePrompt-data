#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(n⋅m, 10^9); a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for each i.
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
            cost += m * sum(N) + m * m * ((n - 1) * n // 2) + n * m * mu
        
        print(cost)
        
        continue
        
    #State: After executing the loop for `t` iterations, the output state will consist of `t` printed costs, each calculated based on the specific inputs provided for each iteration. The cost is determined by sorting the second input list `M`, selecting the first `q` elements where `q` is the ceiling of `k/m`, and then calculating the cost according to the given conditions. Each iteration modifies `n`, `m`, `k`, and `N` based on the input lists `L` and `M`.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads two lists of integers `L` and `M`, and calculates a cost based on the values of `n`, `m`, and `k`. It sorts the list `M`, selects the first `q` elements where `q` is the ceiling of `k/m`, and computes the cost according to specific conditions. The function prints the calculated cost for each test case. After processing all test cases, it outputs `t` costs, one for each test case.

