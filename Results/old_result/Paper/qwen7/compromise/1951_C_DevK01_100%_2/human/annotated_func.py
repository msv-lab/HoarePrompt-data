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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, and for each iteration of the loop, `t` items are processed. After all iterations, the value of `t` remains unchanged, and each `cost` calculated for each iteration is printed. The other variables (`L`, `M`, `n`, `m`, `k`, `q`, `N`, `w`, `mu`) are reset for each iteration and do not affect the final state of `t`.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads integers \( n \), \( m \), and \( k \) along with a list of \( n \) integers \( a \). It calculates a cost based on certain conditions involving \( n \), \( m \), and \( k \), and prints the cost for each test case. After processing all test cases, it outputs the calculated costs for each case.

