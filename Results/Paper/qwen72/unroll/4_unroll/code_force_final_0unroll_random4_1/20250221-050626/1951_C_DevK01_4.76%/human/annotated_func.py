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
        
    #State: The loop iterates `t` times, and after each iteration, the values of `n`, `m`, `k`, and `M` are updated based on the input for that iteration. After all iterations, the values of `n`, `m`, `k`, and `M` will be the values from the last iteration, and the list `N` will be the last computed sublist of `M` used in the cost calculation. The variable `cost` will hold the final computed cost for the last iteration. The sum of `n` over all test cases does not exceed 3 · 10^5.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads three integers `n`, `m`, and `k`, and a list `M` of `n` integers representing ticket prices. It calculates the minimum total cost to buy exactly `k` tickets over `n` days, considering the daily purchase limit `m`. After processing all test cases, it prints the calculated minimum cost for each test case. The final state of the program includes the values of `n`, `m`, `k`, and `M` from the last test case, and the list `N` which is the last computed sublist of `M` used in the cost calculation for the last test case.

