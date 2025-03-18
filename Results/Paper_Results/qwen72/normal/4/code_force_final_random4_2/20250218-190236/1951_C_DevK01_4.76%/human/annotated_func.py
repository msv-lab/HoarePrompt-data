#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9), representing the number of sale days, the maximum amount of tickets purchasable each day, and the number of tickets to be bought, respectively. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, representing the price per ticket for each of the upcoming n days. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop has executed `t` times, where `t` is the initial integer input by the user. For each iteration, `L` and `M` are lists of integers provided by the user input, `n` is the number of sale days, `m` is the minimum of the maximum tickets purchasable each day and the number of tickets to be bought, `k` is the number of tickets to be bought, `q` is the ceiling of `k / m`, and `N` is a list of the first `q` elements of the sorted `M`. If `n * m == k`, the cost is calculated as `m * sum(N) + m * m * ((n - 1) * n // 2)`. Otherwise, the last element `w` is removed from `N`, `mu` is calculated as `k - (n - 1) * m`, and the cost is updated to `mu * w + m * sum(N) + m * m * ((n - 1) * (n - 2) // 2) + n * m * mu`. The `cost` for each test case is printed, and the loop continues to the next iteration until all `t` iterations are completed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two lines of input: the first line contains three integers `n`, `m`, and `k`, representing the number of sale days, the maximum number of tickets purchasable each day, and the total number of tickets to be bought, respectively. The second line contains a list of `n` integers `a`, representing the price per ticket for each of the `n` days. The function calculates the minimum total cost required to buy `k` tickets over the `n` sale days, considering the constraint that no more than `m` tickets can be bought on any single day. It prints the calculated minimum cost for each test case. After all test cases are processed, the function concludes.

