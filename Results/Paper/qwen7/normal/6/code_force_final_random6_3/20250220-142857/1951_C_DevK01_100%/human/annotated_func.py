#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n.
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
        
    #State: Output State: `t` is equal to 0, `L` is an empty list, `M` is an empty list, `n` is 0, `m` is any non-negative integer (determined by the last iteration's input), `k` is any non-negative integer (determined by the last iteration's input), `q` is 0, `N` is an empty list, and `cost` is 0.
    #
    #This output state indicates that after all iterations of the loop have been executed, `t` has reached 0, meaning all test cases have been processed. All other variables are reset or empty as they were either initialized to empty lists or zero at the start of each iteration and are not modified outside the loop body.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers t, n, m, k, and a list a of n integers. For each test case, it calculates a cost based on specific conditions involving n, m, and k, and prints the calculated cost. After processing all test cases, the function outputs the total cost for all cases.

