#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ \min(nm, 10^9). a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n.
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
        
    #State: Output State: After the loop executes all iterations, `t` will be 0, indicating that there are no more inputs to process. The variables `L`, `M`, `n`, `m`, `k`, `q`, `N`, and `cost` will be undefined or reset to their initial states for the last input, but since `t` is now 0, these variables will not be used further. The loop has completed all its iterations, and the program is ready to terminate.
    #
    #In natural language: After all iterations of the loop have finished, `t` will be 0, meaning no more inputs are left to process. All other variables (`L`, `M`, `n`, `m`, `k`, `q`, `N`, and `cost`) will either be undefined or will hold the final values from the last input processed before `t` became 0. The program will now terminate as there are no more inputs to handle.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads integers `n`, `m`, and `k` along with a list `M` of `n` integers. It then calculates a cost based on specific conditions involving `n`, `m`, and `k`. The cost is determined by sorting `M`, selecting a subset of elements, and performing arithmetic operations. After processing all test cases, the function prints the calculated cost for each case and terminates.

