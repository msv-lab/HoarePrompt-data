#State of the program right berfore the function call: Each test case consists of three integers n, m, and k, where 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9), representing the number of sale days, the maximum amount of tickets purchasable each day, and the number of tickets to be bought, respectively. The second line of each test case contains n integers a_1, a_2, ..., a_n, where 1 ≤ a_i ≤ 10^9, representing the price per ticket for each of the upcoming n days. The total number of test cases, t, satisfies 1 ≤ t ≤ 10^4, and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is an input integer, `n`, `m`, `k`, `a_1, a_2, ..., a_n` are the values from the last iteration's input, and the loop has printed the cost for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of the number of sale days (`n`), the maximum number of tickets that can be purchased each day (`m`), and the total number of tickets to be bought (`k`). For each test case, it also receives a list of `n` integers representing the price per ticket for each day. The function calculates and prints the minimum cost to buy `k` tickets, considering the constraints provided.

