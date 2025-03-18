#State of the program right berfore the function call: Each test case consists of three integers n, m, and k where 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). The test case also includes a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop has executed `t` times, and the variables `n`, `m`, `k`, and the list `a_1, a_2, ..., a_n` remain unchanged.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three integers `n`, `m`, and `k`, and a list of `n` integers. For each test case, it calculates and prints a cost value based on the given constraints and the input values.

