#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(n⋅m, 10^9). a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n.
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
        
    #State: Output State: The final state will depend on the inputs provided within each iteration of the loop. For each iteration, `t` integers are read for `L` and `t` integers are read for `M`. The variable `cost` is calculated based on the values of `n`, `m`, `k`, and the sorted list `M`. The exact value of `cost` varies with each input, but it represents the total cost calculated according to the given logic. After all iterations, the final `cost` values from each iteration are printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, m, and k, along with a list of n integers. For each test case, it calculates a cost based on the values of n, m, and k, and the sorted list of integers. The cost is determined by partitioning the list into segments and applying specific mathematical operations. After processing all test cases, it prints the calculated cost for each case.

