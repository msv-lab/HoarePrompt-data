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
            cost += m * sum(N) + m * m * ((n - 1) * (n - 2) // 2) + n * m * mu
        
        print(cost)
        
        continue
        
    #State: Output State: After the loop executes all iterations, `t` will be equal to the total number of iterations the loop ran, which is the final value of `t` provided as input. For each iteration, `n` will be the length of the list `N`, which contains the first `q` elements of `M` after sorting. `m` will be the minimum value between the second and third elements of `L`. `k` will be the third element of `L`. `q` will be the ceiling value of `k / m`. `N` will be a list containing the first `q` elements of `M` after sorting. `cost` will be calculated based on the conditions given: if `n * m == k`, then `cost` will be `m * sum(N) + m * m * ((n - 1) * n // 2)`. Otherwise, `cost` will be `mu * w + m * sum(N) + m * m * ((n - 1) * (n - 2) // 2) + n * m * mu`, where `mu` is `k - (n - 1) * m` and `w` is the last element of `N` before it is popped. The program will print the `cost` for each iteration and continue to the next one until all iterations are completed.
#Overall this is what the function does:The function processes multiple test cases defined by the number of test cases `t`, and for each test case, it calculates a cost based on the values of `n`, `m`, `k`, and a sorted list `M`. It sorts the list `M`, determines the number of elements `q` to consider, and then calculates the cost according to specific conditions. The function prints the calculated cost for each test case and continues to the next one until all test cases are processed.

