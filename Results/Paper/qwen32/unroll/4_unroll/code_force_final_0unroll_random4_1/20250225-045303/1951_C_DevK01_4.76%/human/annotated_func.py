#State of the program right berfore the function call: Each test case consists of three integers n, m, and k where 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). Additionally, there is a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 representing the price per ticket for each of the n days. The total number of days n across all test cases does not exceed 3 · 10^5.
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
        
    #State: t is the same as the input integer; n, m, k, M, and N are reset for each iteration and do not persist.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three integers `n`, `m`, and `k`, and a list of `n` integers representing ticket prices. For each test case, it calculates and prints the minimum cost to buy up to `k` tickets, given that `m` is the total amount of money available per ticket purchase and tickets can be bought in batches of up to `m` tickets per day.

