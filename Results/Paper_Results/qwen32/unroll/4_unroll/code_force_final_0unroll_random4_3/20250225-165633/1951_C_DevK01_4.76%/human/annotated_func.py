#State of the program right berfore the function call: Each test case contains three integers n, m, and k (1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, 1 ≤ k ≤ min(nm, 10^9)) representing the number of sale days, the maximum amount of tickets purchasable each day, and the number of tickets to be bought at the end, respectively. The second line of each test case contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the price per ticket for each of the upcoming n days. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: the sequence of costs printed for each of the t test cases.
#Overall this is what the function does:The function reads multiple test cases, each consisting of the number of sale days (`n`), the maximum number of tickets that can be purchased each day (`m`), the total number of tickets to be bought (`k`), and the price per ticket for each day. It calculates and prints the minimum total cost to buy `k` tickets, considering the constraints on the number of tickets that can be purchased each day.

