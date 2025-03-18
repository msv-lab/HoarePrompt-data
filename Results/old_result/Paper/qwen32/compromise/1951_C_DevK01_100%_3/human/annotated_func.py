#State of the program right berfore the function call: Each test case consists of three integers n, m, and k (1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, 1 ≤ k ≤ min(nm, 10^9)) representing the number of sale days, the maximum number of tickets that can be purchased each day, and the total number of tickets to be bought, respectively. The second line of each test case contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the price per ticket for each of the upcoming n days. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is unchanged; `a` is unchanged; `m` is unchanged; `n`, `k`, and `M` are redefined in each iteration and do not persist after the loop.
#Overall this is what the function does:The function calculates and prints the minimum cost required to purchase a specified total number of tickets (`k`) over a given number of days (`n`), with a daily limit on the number of tickets that can be bought (`m`). The cost is determined based on the prices of tickets for each day, provided in a list. The function processes multiple test cases, each defined by its own set of `n`, `m`, `k`, and ticket prices.

